import os
import glob
import json
import requests

# Live HAPI FHIR Public Server URL Endpoint
TARGET_URL = "https://fhir.org"

# Set a unique prefix so your app dashboard queries only pull your specific data
UNIQUE_PREFIX = "MB15_"

# Gather generated records
files = glob.glob(os.path.join(".", "output", "fhir", "*.json"))

print(f"Filtering and uploading custom namespaced cohort to {TARGET_URL}...\n")
headers = {"Content-Type": "application/fhir+json; charset=utf-8"}
uploaded_count = 0

for file_path in files:
    filename = os.path.basename(file_path)
    
    # Ignore background architecture master data catalogs
    if "hospital" in filename or "practitioner" in filename:
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            bundle = json.load(f)
        except Exception:
            continue
            
    # Verification Gate: Ensure the patient actively triggered your stroke metrics
    has_neuro_metrics = False
    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})
        if resource.get("resourceType") == "Observation":
            codes = resource.get("code", {}).get("coding", [])
            if any(c.get("code") == "97711-6" for c in codes):
                has_neuro_metrics = True
                break
                
    # Skip standard healthy profiles who never experienced a stroke
    if not has_neuro_metrics:
        continue

    # Namespace Isolation: Inject prefix into the Patient Resource fields
    for entry in bundle.get("entry", []):
        resource = entry.get("resource", {})
        if resource.get("resourceType") == "Patient":
            for name in resource.get("name", []):
                original_family = name.get("family", "")
                name["family"] = f"{UNIQUE_PREFIX}{original_family}"
                print(f"Isolated: Prepending identifier to family name -> {name['family']}")

    # Execute HTTP POST Transaction to the cloud endpoint
    try:
        response = requests.post(TARGET_URL, json=bundle, headers=headers)
        if response.status_code in [200, 201]:
            uploaded_count += 1
            print(f"✔ Success: {filename} uploaded successfully. (Status {response.status_code})")
        else:
            print(f"❌ Server Error uploading {filename}: Status {response.status_code}")
    except Exception as e:
        print(f"💥 Network Error connecting to sandbox: {e}")

print(f"\nIngestion Sync Complete. Uploaded {uploaded_count} custom namespaced stroke profiles.")
