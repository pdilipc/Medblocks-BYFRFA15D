# Stroke Neurorehabilitation & Neurotech Ecosystem Module

This directory contains the custom Synthea™ Generic Module Framework (GMF) configuration file (`holistic_stroke_neurorehabilitation_and_neurotech_ecosystem.json`) designed to simulate a holistic, longitudinal patient journey for ischemic stroke survivors. 

Unlike standard acute-care modules, this file models post-acute workflows, continuous remote patient monitoring (RPM), clinical triage decision logic, and advanced neurotechnology interventions (**Dozee**, **recoveriX**, and **SynPhne**) leading to a unified neuroplastic outcome endpoint.

---

## 🗺️ Visual Architecture Summary

Below is the conceptual and structural layout of the patient workflow as rendered by the Synthea Module Builder:

```text
 [ Acute Stroke Onset ] 
           │
           ▼
 [ Emergency Department Care ] ──► (Thrombolytic Therapy)
           │
           ▼
 [ Inpatient Rehab Facility Admission ]
           │
           ▼
 [ Dozee RPM Mat Setup ] ──► Tracks Continuous Heart Rate & Sleep Efficiency
           │
           ▼
 [ Baseline Inclusion Assessment ] ──► (Fugl-Meyer Upper Extremity Evaluation)
           │
      ┌────┴──────────────────────────────┐ (Clinical Triage Fork)
      │ 45% Probability                   │ 55% Probability
      ▼                                   ▼
 [ recoveriX BCI-FES Track ]         [ SynPhne EEG-EMG Track ]
      │                                   │
      ├─► Procedure: BCI Therapy          ├─► Procedure: Neuromuscular Re-education
      └─► Metric: Imagery Accuracy (87%)  └─► Metric: ARAT Coordination Score (34)
      │                                   │
      └────┬──────────────────────────────┘
           │
           ▼
 [ 4-6 Week Therapy Delay ] ──► Simulates ongoing rehabilitation duration
           │
           ▼
 [ Unified Neuroplastic Outcome ] ──► Re-assesses Final FMA-UE Score (51)
           │
           ▼
 [ Discharge & Condition Resolution ] ──► Terminal State
```

---

## 📋 Detailed Clinical Pathway Breakdown

### 1. The Acute Emergency Phase
* **Acute_Stroke_Onset & Emergency_Encounter**: The patient experiences an acute ischemic stroke (coded as SNOMED-CT `42343007`) and is immediately admitted to an Emergency Department.
* **Acute_Thrombolytic_Intervention**: The clinical team administers urgent clot-busting medication (Thrombolytic therapy, SNOMED-CT `230958000`) to restore cerebral blood flow before discharging them from acute care.

### 2. Post-Acute Admission & Safety Telemetry
* **Inpatient_Rehab_Admission**: The patient is transferred out of the emergency ward and enters an inpatient rehabilitation facility (SNOMED-CT `305368008`) to begin recovery.
* **Dozee_RPM_Setup**: Upon arrival, a **Dozee contactless monitoring mattress mat** (SNOMED-CT `469007003`) is deployed beneath their bedding.
* **Continuous Vitals & Sleep Architecture Tracking**: The simulator generates immediate baseline telemetry for the patient's resting Heart Rate (`76 bpm`) and **Sleep Efficiency (`81%`)** via LOINC codes. Tracking sleep architecture is clinically vital here, as high-quality sleep cycles are a known prerequisite for neuroplastic healing.

### 3. The Clinical Triage Decision
* **Baseline_Inclusion_Assessment**: Before any specialized therapy begins, a clinician scores the patient's paretic upper limb using the gold-standard **Fugl-Meyer Assessment Upper Extremity (FMA-UE)** (LOINC `97711-6`).
* **The Triage Branching Gate**: The engine uses a probability distribution to triage the patient based on clinical inclusion criteria:
  * **Track A (45% probability)**: Routed to **recoveriX** if they present with severe impairment/flaccid paralysis and require passive, involuntary neural priming.
  * **Track B (55% probability)**: Routed to **SynPhne** if they possess minimal retained voluntary motor function and qualify for active, task-oriented biofeedback.

### 4. Specialized Device Therapies
* **The recoveriX Path (`Route_To_RecoveriX_Track`)**: The patient completes a multi-session Brain-Computer Interface (BCI) regimen. The simulator generates an **EEG Motor Imagery Classification Accuracy score of `87%`** (LOINC `95728-2`), validating that the patient's brain waves are successfully engaging the feedforward loop to trigger the electrical stimulation.
* **The SynPhne Path (`Route_To_SynPhne_Track`)**: The patient undergoes active neuromuscular re-education using the dual EEG/EMG sensor array. The simulator captures an **Action Research Arm Test (ARAT) score of `34`** (LOINC `95729-0`), measuring fine-motor coordination and proving the patient is actively inhibiting harmful muscle co-contraction compensation patterns.

### 5. Recovery Consolidation & Discharge
* **Therapy_Timeline_Delay**: The patient remains in the rehabilitation cycle for a realistic timeframe of **4 to 6 weeks**, allowing the neurological therapies to take continuous physical effect.
* **Unified_Neuroplastic_Outcome**: Regardless of whether the patient took the recoveriX or SynPhne track, they both arrive at this shared outcome milestone. Their **FMA-UE score is reassessed and shows a definitive improvement to `51`**, demonstrating documented neuroplastic recovery across the cohort.
* **Resolve_Stroke_Condition & Terminal**: The inpatient rehab encounter ends, the acute stroke condition is flagged as managed/resolved in the patient's longitudinal record, and the simulation loop concludes cleanly.

---

## 🛠️ Data Standards & Terminology Mapping

To ensure your downstream data analytics models or FHIR registries can easily evaluate and compare therapeutic efficacy, this module utilizes standard clinical codes across all states:


| State Class | Platform Concept | Coding System | Code Identifier |
| :--- | :--- | :--- | :--- |
| **Condition** | Ischemic Stroke Onset | SNOMED-CT | `42343007` |
| **Device** | Dozee Mattress Deployed | SNOMED-CT | `469007003` |
| **Observation** | Dozee Sleep Efficiency | LOINC | `93832-3` |
| **Procedure** | recoveriX BCI Therapy | SNOMED-CT | `225285002` |
| **Observation** | recoveriX Imagery Accuracy | LOINC | `95728-2` |
| **Procedure** | SynPhne Task Re-education | SNOMED-CT | `225285002` |
| **Observation** | SynPhne ARAT Total Score | LOINC | `95729-0` |
| **Observation** | Unified Fugl-Meyer Outcome | LOINC | `97711-6` |

---

## 🚀 How to Generate This Dataset Locally

1. Place the `holistic_stroke_neurorehabilitation_and_neurotech_ecosystem.json` module file into your local Synthea codebase directory:
   ```bash
   cp holistic_stroke_neurorehabilitation_and_neurotech_ecosystem.json ./src/main/resources/modules/
   ```
2. Build and compile the local test suite using Gradle:
   ```bash
   ./gradlew build check test
   ```
3. Generate a population cohort of 1,000 synthetic patient records containing this integrated technology footprint:
   ```bash
   ./run_synthea -p 1000 -m "holistic_stroke_neurorehabilitation_and_neurotech_ecosystem"
   ```
4. Find your generated FHIR bundles output cleanly as JSON files inside:
   ```text
   ./output/fhir/
   ```
