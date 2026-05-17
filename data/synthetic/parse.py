import os
import json
import glob

# Path to your generated FHIR records
output_path = os.path.join(".", "output", "fhir", "*.json")
files = glob.glob(output_path)

print(f"Scanning {len(files)} files for Fugl-Meyer Scores (LOINC: 97711-6)...\n")
print(f"{'Patient Name':<30} | {'Baseline Score':<15} | {'Final Score':<15}")
print("-" * 68)

cohort_count = 0

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            bundle = json.load(f)
        except Exception:
            continue
        
        # Extract patient name
        patient_name = "Unknown"
        fma_scores = []
        
        for entry in bundle.get("entry", []):
            resource = entry.get("resource", {})
            
            # Find Patient Name
            if resource.get("resourceType") == "Patient":
                name_list = resource.get("name", [])
                if name_list:
                    given = " ".join(name_list[0].get("given", []))
                    family = name_list[0].get("family", "")
                    patient_name = f"{given} {family}"
            
            # Find Fugl-Meyer Observations
            if resource.get("resourceType") == "Observation":
                codes = resource.get("code", {}).get("coding", [])
                for c in codes:
                    if c.get("code") == "97711-6":
                        val = resource.get("valueQuantity", {}).get("value")
                        if val is not None:
                            fma_scores.append(val)

        # If they went through the neuro module, they'll have at least one score
        if fma_scores:
            cohort_count += 1
            # Sort them so baseline (earlier/lower usually) comes first, or print what we have
            baseline = fma_scores[0]
            final = fma_scores[1] if len(fma_scores) > 1 else "N/A (Dropped Out)"
            print(f"{patient_name:<30} | {baseline:<15} | {final:<15}")

print("-" * 68)
print(f"Total patients who actively entered your Neurotech Cohort: {cohort_count} out of {len(files)}")
