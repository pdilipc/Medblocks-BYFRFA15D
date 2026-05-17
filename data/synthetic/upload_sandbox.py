import os
import glob
import json
import requests

TARGET_URL = "https://hapi.fhir.org/baseR4"
UNIQUE_PREFIX = "MB15_"
REQUIRE_NEURO_METRICS = False
TIMEOUT_SECONDS = 60

files = glob.glob(os.path.join(".", "output", "fhir", "*.json"))

print(f"Validating and uploading FHIR bundles to {TARGET_URL}...\n")

headers = {
    "Content-Type": "application/fhir+json; charset=utf-8",
    "Accept": "application/fhir+json"
}

uploaded_count = 0
skipped_count = 0
failed_count = 0

for file_path in files:
    filename = os.path.basename(file_path)

    if "hospital" in filename.lower() or "practitioner" in filename.lower():
        print(f"Skipping reference/master file: {filename}")
        skipped_count += 1
        continue

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            bundle = json.load(f)
    except Exception as e:
        print(f"Skipping {filename}: invalid JSON ({e})")
        skipped_count += 1
        continue

    if bundle.get("resourceType") != "Bundle":
        print(f"Skipping {filename}: not a FHIR Bundle")
        skipped_count += 1
        continue

    bundle_type = bundle.get("type")
    if bundle_type not in ["transaction", "batch"]:
        print(f"Skipping {filename}: Bundle.type is '{bundle_type}', not transaction/batch")
        skipped_count += 1
        continue

    entries = bundle.get("entry", [])
    if not entries:
        print(f"Skipping {filename}: empty bundle")
        skipped_count += 1
        continue

    missing_request = False
    for entry in entries:
        if "request" not in entry:
            missing_request = True
            break

    if missing_request:
        print(f"Skipping {filename}: bundle entries missing request blocks")
        skipped_count += 1
        continue

    has_neuro_metrics = False
    for entry in entries:
        resource = entry.get("resource", {})
        if resource.get("resourceType") == "Observation":
            codes = resource.get("code", {}).get("coding", [])
            if any(c.get("code") == "97711-6" for c in codes):
                has_neuro_metrics = True
                break

    if REQUIRE_NEURO_METRICS and not has_neuro_metrics:
        print(f"Skipping {filename}: no neurorehabilitation observation code 97711-6 found")
        skipped_count += 1
        continue

    patient_found = False
    for entry in entries:
        resource = entry.get("resource", {})
        if resource.get("resourceType") == "Patient":
            patient_found = True
            for name in resource.get("name", []):
                original_family = name.get("family", "")
                if original_family and not original_family.startswith(UNIQUE_PREFIX):
                    name["family"] = f"{UNIQUE_PREFIX}{original_family}"
                    print(f"{filename}: patient family renamed to {name['family']}")

    if not patient_found:
        print(f"Warning: {filename} contains no Patient resource")

    try:
        response = requests.post(
            TARGET_URL,
            headers=headers,
            json=bundle,
            timeout=TIMEOUT_SECONDS
        )

        if response.status_code in [200, 201]:
            uploaded_count += 1
            print(f"SUCCESS: {filename} uploaded (HTTP {response.status_code})")
        else:
            failed_count += 1
            print(f"FAILED: {filename} (HTTP {response.status_code})")
            try:
                print(response.json())
            except Exception:
                print(response.text[:1000])

    except requests.RequestException as e:
        failed_count += 1
        print(f"NETWORK ERROR: {filename}: {e}")

print("\nUpload complete.")
print(f"Uploaded: {uploaded_count}")
print(f"Skipped: {skipped_count}")
print(f"Failed: {failed_count}")