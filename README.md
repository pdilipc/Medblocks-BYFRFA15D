# Medblocks - Build Your First Real FHIR App in 15 Days - Submission


# Verada Neurorehab Readiness

Verada Neurorehab Readiness is a FHIR-based application for remote neurorehabilitation workflows. It combines home physiological monitoring, rehabilitation planning, and structured clinical documentation to help clinicians assess daily readiness for therapy, personalize sessions, and write outcomes back into the patient record.

This repository is designed as a practical specialty-care interoperability app rather than a generic patient viewer. It focuses on a real neurorehabilitation workflow in which physiological context collected before the day begins can support safer, more personalized therapy decisions for stroke and other neurological motor deficit pathways.

## Overview

In many rehabilitation pathways, patients generate useful data at home before treatment begins, but that information is often disconnected from the day’s clinical workflow. This app brings together patient context, physiological observations, rehabilitation plans, and post-session outcomes in a focused interface that supports clinical decision-making and structured record updates.

The primary use case is a home-based or hybrid neurorehabilitation pathway in which a clinician reviews overnight or recent physiological data, checks the active rehabilitation plan, decides whether to proceed, modify, or defer therapy, and records the session outcome in interoperable FHIR format.

## Features

- Patient lookup and selection with core demographic and rehabilitation context.
- Daily readiness dashboard showing recent physiological observations and relevant clinical context.
- Session planning workflow to support proceed, modify, or defer decisions with clinician rationale.
- Post-session documentation for structured recording of therapy delivered and patient response.
- Bidirectional FHIR workflow that reads from a FHIR server and writes structured updates back into the record.
- Compact architecture designed for rapid prototyping and future expansion into broader neurorehabilitation workflows.
- Specialty focus on neurorehabilitation rather than generic data visualization.

## Use Case

A patient receiving neurorehabilitation at home is passively monitored overnight or before the day’s therapy session. Before treatment begins, the clinician opens the app, reviews recent observations alongside the patient’s clinical and rehabilitation context, and decides whether to proceed with the session, modify intensity, or defer for review.

After the session, the clinician records the treatment delivered and the patient’s response in structured FHIR format. This creates a clear longitudinal record of readiness, intervention, and outcome that can support continuity across providers and settings.

## Architecture

The application is designed as a lightweight clinical workflow layer on top of a FHIR server. It consumes patient, monitoring, and care-planning resources to create a therapist-facing readiness view, then persists structured treatment and follow-up data after the session.

At a high level, the architecture includes four logical layers:

1. **FHIR data layer**  
   A FHIR server stores and serves patient, device, observation, condition, plan, and session documentation resources.

2. **Integration layer**  
   Remote monitoring sources and rehabilitation systems contribute relevant physiological and therapy data that can be normalized into FHIR-compatible structures.

3. **Application layer**  
   The app presents a focused clinician workflow for reviewing readiness, planning the session, and documenting outcomes.

4. **Clinical intelligence layer**  
   In the challenge version, this is intentionally lightweight and supports simple decision framing rather than complex predictive modeling. Over time, the same workflow could support richer longitudinal and adaptive intelligence.

A deeper architecture description is available in [`docs/architecture.md`](docs/architecture.md).

### Suggested high-level flow

```text
Remote Monitoring Device / RPM Source
                |
                v
        FHIR-normalized Observations
                |
                v
           FHIR Server
                |
    --------------------------------
    |              |               |
    v              v               v
 Patient      CarePlan /      Condition /
 Context      ServiceRequest   Clinical Context
    \              |               /
     \             |              /
      \            |             /
       v           v            v
      Verada Neurorehab Readiness App
                |
                v
   Session Decision + Documentation
                |
                v
      Write-back to FHIR Server
```

## FHIR Resources

This project uses a compact set of FHIR resources to support the workflow:

- `Patient`  
  Used for identity, demographics, and patient context.

- `Encounter`  
  Represents the rehabilitation touchpoint or clinical session context.

- `Device`  
  Identifies the remote monitoring or rehabilitation device contributing data.

- `Observation`  
  Represents home physiological data, symptom check-ins, tolerance, fatigue, adherence, and outcome measures.

- `Condition`  
  Captures diagnosis and active clinical problems relevant to therapy planning.

- `AllergyIntolerance` and `MedicationStatement`  
  Optional resources for additional safety and treatment context.

- `CarePlan`  
  Represents the rehabilitation pathway, goals, and planned interventions.

- `ServiceRequest`  
  Represents the prescribed rehabilitation service or therapy order.

- `Procedure`  
  Documents the therapy actually delivered during the session.

- `QuestionnaireResponse`  
  Captures structured patient- or clinician-reported check-ins such as fatigue, tolerance, or readiness-related prompts.

A more detailed resource breakdown is available in [`docs/fhir-resources.md`](docs/fhir-resources.md).

### Example workflow mapping

| Workflow step | Primary FHIR resources |
|---|---|
| Patient selection | `Patient`, `Encounter` |
| Review baseline and active context | `Condition`, `CarePlan`, `ServiceRequest` |
| Review recent physiological state | `Device`, `Observation` |
| Record today’s decision | `Encounter`, `Observation`, `QuestionnaireResponse` |
| Record therapy delivered | `Procedure`, `Encounter` |
| Write back outcomes and follow-up | `Observation`, `Communication`, optionally updated `CarePlan` |

## Getting Started

### Prerequisites

- A development or sandbox FHIR server.
- Sample or synthetic FHIR data with resources such as `Patient`, `Observation`, `Condition`, and `CarePlan`.
- A local frontend development environment.
- Optional mock integrations for remote physiological data if live device feeds are not available.

### Initial setup

1. Clone this repository.
2. Configure the FHIR server base URL in your environment settings.
3. Load or connect sample FHIR resources needed for the demo workflow.
4. Start the local development environment.
5. Validate that the app can read patient context and write back session data.

### Minimum demo scope

For a short build cycle, keep the implementation limited to four screens:

1. Patient selection.
2. Daily readiness dashboard.
3. Session planning.
4. Post-session documentation.

That scope is enough to demonstrate a complete FHIR workflow without overbuilding the platform. A focused, working app is likely to be more persuasive than a broad prototype with shallow implementation.

## Roadmap

### Phase 1
- Implement patient selection and summary context.
- Retrieve core FHIR resources from the target server.
- Display recent physiological observations in a clinician-friendly readiness view.
- Capture a simple daily decision: proceed, modify, or defer.

### Phase 2
- Add post-session documentation with `Procedure`, `Observation`, and `QuestionnaireResponse`.
- Support structured write-back into the FHIR server.
- Add lightweight trend views for recent observations and session history.

### Phase 3
- Add richer baseline and longitudinal context.
- Support multiple rehabilitation devices and monitoring inputs through a more flexible integration layer.
- Expand into a broader neurorehabilitation orchestration workflow across settings.

### Future direction
- Introduce more advanced clinical intelligence for personalization and recovery support.
- Support broader interoperability with NHS and international workflows.
- Extend from challenge prototype to production-grade neurorehabilitation infrastructure.

## Docs

- [Architecture](docs/architecture.md)
- [FHIR Resources](docs/fhir-resources.md)
- [Workflow](docs/workflow.md)

## Why this repository exists

This repository exists to demonstrate how FHIR can support a clinically meaningful neurorehabilitation workflow using remote physiological monitoring and structured therapy documentation. It is intentionally scoped as a practical app that connects monitoring, decision support, care delivery, and interoperable write-back in a specialty pathway.

## Repository Structure

```text
.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   └── fhir-resources.md
├── src/
├── public/
├── examples/
│   └── sample-fhir-data/
├── .env.example
├── package.json
└── LICENSE
```

## Notes

This repository is intentionally scoped as a focused FHIR app for neurorehabilitation readiness and session documentation. It is designed to demonstrate a real clinical workflow clearly, while still leaving room for future expansion into deeper longitudinal intelligence and production-grade interoperability.

This repository is intentionally scoped as a focused FHIR app for neurorehabilitation readiness and session documentation. It is designed to demonstrate a real clinical workflow clearly, while still leaving room for future expansion into deeper longitudinal intelligence and production-grade interoperability.



# Medblocks - Build Your First Real FHIR App in 15 Days - Submission

# Verada Neurorehab Readiness

Verada Neurorehab Readiness is a FHIR-based application for remote neurorehabilitation workflows. It combines home physiological monitoring, advanced clinical triage, and structured clinical documentation to help clinicians assess daily readiness for therapy, personalize sessions, and write outcomes back into the patient record.

This repository is designed as a practical specialty-care interoperability app rather than a generic patient viewer. It focuses on a real neurorehabilitation workflow in which physiological context collected before the day begins can support safer, more personalized therapy decisions for stroke and other neurological motor deficit pathways.

## 🚀 Synthea Generation Engine

To power development, testing, and validation, this project natively targets a custom, clinical-grade patient dataset generated via the **Synthea™ Generic Module Framework (GMF)**. 

The application logic explicitly consumes longitudinal patient records mapped across an end-to-end stroke neurotech ecosystem, processing data generated by three real-world medical platforms:
1. **Dozee** (Contactless Ballistocardiography RPM Mat for sleep and vitals telemetry)
2. **recoveriX** (Closed-loop EEG Brain-Computer Interface + Functional Electrical Stimulation)
3. **SynPhne** (Synergistic Physio-Neuro Wearable for dual EEG/EMG neuromuscular task training)

---

## Overview

In many rehabilitation pathways, patients generate useful data at home before treatment begins, but that information is often disconnected from the day’s clinical workflow. This app brings together patient context, physiological observations, rehabilitation plans, and post-session outcomes in a focused interface that supports clinical decision-making and structured record updates.

The primary use case is a home-based or hybrid neurorehabilitation pathway in which a clinician reviews overnight or recent physiological data, checks the active rehabilitation plan, decides whether to proceed, modify, or defer therapy, and records the session outcome in interoperable FHIR format.

---

## Features

- **Patient Lookup & Demographics**: Complete profile selection embedded with historic ischemic stroke context.
- **Dozee Vitals & Readiness Dashboard**: Visual displays tracking resting heart rate and sleep efficiency trends captured via contactless ballistocardiography.
- **Clinical Inclusion Triage**: Decision architecture that segments patients based on baseline paretic-limb functional metrics.
- **Neurotech Procedural Logging**: Workflows customized to document either passive recoveriX BCI stimulation loops or active SynPhne neuromuscular biofeedback sessions.
- **Bidirectional FHIR Write-Back**: Real-time state persistence saving outcomes (FMA-UE and ARAT metrics) directly back onto the destination FHIR server.
- **Compact Prototype Footprint**: Four clean clinical views (Lookup, Readiness, Planning, Outcomes) designed for high-density information delivery.

---

## Use Case & Clinical Workflow

A patient receiving neurorehabilitation at home is passively monitored overnight using a **Dozee sensor mat**. Before treatment begins, the clinician opens the app and checks the baseline **Fugl-Meyer Assessment (FMA-UE)** score:
* **Severe Deficits (<20)**: Clinician confirms inclusion criteria for **recoveriX BCI-FES** therapy to involuntarily prime feedforward paths.
* **Minimal Retained Motor Function (20-40)**: Clinician routes the patient to active **SynPhne EEG/EMG task training** to inhibit maladaptive compensation.

Following a 4-to-6 week session block, final outcome gains are assessed using unified tracking scores and pushed downstream to update the longitudinal EHR.

---

## Architecture

The application is designed as a lightweight clinical workflow layer on top of a FHIR server. It consumes patient, monitoring, and care-planning resources to create a therapist-facing readiness view, then persists structured treatment and follow-up data after the session.

### Technical Data Flow

```text
       Dozee RPM Mattress Mat            recoveriX / SynPhne Tech
                 │                                   │
                 ▼                                   ▼
   Overnight Vitals / Sleep (LOINC)    Functional Outcomes (LOINC/SNOMED)
                 │                                   │
                 └─────────────────┬─────────────────┘
                                   │
                                   ▼
                            FHIR Server Bundle
                                   │
  ┌────────────────────────────────┼────────────────────────────────┐
  ▼                                ▼                                ▼
Patient Context             CarePlan Object                 Clinical Condition
(`Patient` Resource)     (`ServiceRequest` / `CarePlan`)   (`Condition` - Stroke)
  │                                │                                │
  └────────────────────────────────┼────────────────────────────────┘
                                   │
                                   ▼
                    Verada Neurorehab Readiness App
                                   │
                                   ▼
                 Session Triage Triage Decision Matrix
                     (recoveriX BCI vs. SynPhne)
                                   │
                                   ▼
                    Write-back to FHIR Server (`Procedure`)
```

---

## 🗂️ FHIR Resource Mapping & Standards Registry

The application data architecture strictly binds to standard clinical terminologies populated by the underlying **Synthea simulation engine**:


| Workflow Stage | FHIR Resource | Coding System | Code Identifier | Platform Concept |
| :--- | :--- | :--- | :--- | :--- |
| **Cohort Setup** | `Condition` | SNOMED-CT | `42343007` | Ischemic stroke diagnosis |
| **Device Onboarding** | `Device` | SNOMED-CT | `469007003` | Dozee mattress deployment |
| **Vitals Baseline** | `Observation` | LOINC | `93832-3` | Dozee continuous sleep efficiency |
| **Clinical Triage** | `Observation` | LOINC | `97711-6` | Baseline Fugl-Meyer Score (FMA-UE) |
| **Intervention A** | `Procedure` | SNOMED-CT | `225285002` | recoveriX neurorehabilitation session |
| **Metric A** | `Observation` | LOINC | `95728-2` | Motor imagery classification accuracy |
| **Intervention B** | `Procedure` | SNOMED-CT | `225285002` | SynPhne physical neuro-reeducation |
| **Metric B** | `Observation` | LOINC | `95729-0` | Action Research Arm Test (ARAT) score |
| **Outcome Milestone** | `Observation` | LOINC | `97711-6` | Post-therapy final FMA-UE reassessment |

---

## Getting Started

### Prerequisites

- A development or sandbox FHIR server (e.g., HAPI FHIR, Azure API for FHIR).
- Our custom **Synthea Neurotech Cohort Engine** to generate test datasets.
- A local frontend development environment (Node.js/npm).

### Initial Data Setup & Execution

1. Clone this repository.
2. Navigate to your local Synthea instance directory and copy our custom module file:
   ```bash
   cp templates/stroke_neurotech.json [YOUR_SYNTHEA_PATH]/src/main/resources/modules/
   ```
3. Generate 1,000 highly specified synthetic neurotech patient records:
   ```bash
   ./run_synthea -p 1000 -m "stroke_neurotech"
   ```
4. Upload the generated JSON bundles found in `./output/fhir/` directly to your sandbox FHIR server using a POST request or bulk load script.
5. Configure your app's environment connection variables to query your server endpoint, and execute:
   ```bash
   npm run dev
   ```

---

## Roadmap

### Phase 1 (Completed)
* Engineered custom **Synthea Stroke Neurotech Module** layout mapping baseline Dozee telemetry and triage pathways.
* Configured local sandbox environment to parse initial `Patient` and `Condition` resource structures.

### Phase 2 (Active Development)
* Building out the **Daily Readiness UI component** mapping real LOINC identifiers for sleep and baseline upper-limb tracking metrics.
* Implementing branching layout views for specialized session planning screens (recoveriX vs. SynPhne logging controls).
* Wiring the write-back engine to capture and persist post-session outcomes directly into the destination FHIR registry.

### Phase 3
* Incorporating dynamic, randomized mathematical deviation logic inside the data generation pipeline to analyze outlier patient recovery profiles.
