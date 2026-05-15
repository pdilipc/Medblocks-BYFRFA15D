# Medblocks - Build Your First Real FHIR App in 15 Days - Submission


# Verada Neurorehab Readiness

Verada Neurorehab Readiness is a FHIR-based application for remote neurorehabilitation workflows. It combines home physiological monitoring, rehabilitation planning, and structured clinical documentation to help clinicians assess daily readiness for therapy, personalize sessions, and write outcomes back into the patient record. [web:36][cite:16][cite:17]

This project is designed as a practical healthcare interoperability app rather than a generic patient viewer. It focuses on a real neurorehabilitation workflow in which physiological context collected before the day begins can support safer and more personalized therapy decisions for conditions such as stroke and other neurological motor deficits. [cite:18][cite:19][cite:23]

## Overview

In many rehabilitation pathways, patients generate useful data at home before treatment begins, but that information is often disconnected from the day’s clinical workflow. This app brings together patient context, physiological observations, rehabilitation plans, and post-session outcomes in a focused interface that supports clinical decision-making and structured record updates. [cite:23][cite:24][web:1]

The primary use case is a home-based or hybrid neurorehabilitation pathway in which a clinician reviews overnight or recent physiological data, checks the active rehabilitation plan, decides whether to proceed, modify, or defer therapy, and records the session outcome in interoperable FHIR format. [cite:23][cite:24][web:1]

## Features

- Patient lookup and selection with core demographic and rehabilitation context. [web:30]
- Daily readiness dashboard showing recent physiological observations and relevant clinical context. [cite:23][web:1]
- Session planning workflow to support proceed, modify, or defer decisions with clinician rationale. [cite:24]
- Post-session documentation for structured recording of therapy delivered and patient response. [cite:16][web:1]
- Bidirectional FHIR workflow that reads from a FHIR server and writes structured updates back into the record. [cite:16][web:36]
- Specialty focus on neurorehabilitation rather than generic data visualization. [cite:19][cite:20]

## Architecture

The application is designed as a lightweight clinical workflow layer on top of a FHIR server. It consumes patient, monitoring, and care-planning resources to create a therapist-facing readiness view, then persists structured treatment and follow-up data after the session. [web:36][web:43][cite:17]

At a high level, the architecture includes four logical layers:

1. **FHIR data layer**  
   A FHIR server stores and serves patient, device, observation, condition, plan, and session documentation resources. [web:1][web:43]

2. **Integration layer**  
   Remote monitoring sources and rehabilitation systems contribute relevant physiological and therapy data that can be normalized into FHIR-compatible structures. [cite:17][cite:23]

3. **Application layer**  
   The app presents a focused clinician workflow for reviewing readiness, planning the session, and documenting outcomes. [cite:24][web:36]

4. **Clinical intelligence layer**  
   In the challenge version, this is intentionally lightweight and supports simple decision framing rather than complex predictive modeling. Over time, the same workflow could support richer longitudinal and adaptive intelligence. [cite:18][cite:23]

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
  Used for identity, demographics, and patient context. [web:30]

- `Encounter`  
  Represents the rehabilitation touchpoint or clinical session context. [web:43]

- `Device`  
  Identifies the remote monitoring or rehabilitation device contributing data. [web:1]

- `Observation`  
  Represents home physiological data, symptom check-ins, tolerance, fatigue, adherence, and outcome measures. [web:1][cite:23]

- `Condition`  
  Captures diagnosis and active clinical problems relevant to therapy planning. [web:4][cite:24]

- `AllergyIntolerance` and `MedicationStatement`  
  Optional resources for additional safety and treatment context. [web:4]

- `CarePlan`  
  Represents the rehabilitation pathway, goals, and planned interventions. [web:4][cite:16]

- `ServiceRequest`  
  Represents the prescribed rehabilitation service or therapy order. [web:4]

- `Procedure`  
  Documents the therapy actually delivered during the session. [web:1][web:4]

- `QuestionnaireResponse`  
  Captures structured patient- or clinician-reported check-ins such as fatigue, tolerance, or readiness-related prompts. [web:1]

### Example workflow mapping

| Workflow step | Primary FHIR resources |
|---|---|
| Patient selection | `Patient`, `Encounter` [web:30][web:43] |
| Review baseline and active context | `Condition`, `CarePlan`, `ServiceRequest` [web:4][cite:16] |
| Review recent physiological state | `Device`, `Observation` [web:1][cite:23] |
| Record today’s decision | `Encounter`, `Observation`, `QuestionnaireResponse` [web:1][cite:24] |
| Record therapy delivered | `Procedure`, `Encounter` [web:1][web:4] |
| Write back outcomes and follow-up | `Observation`, `Communication`, optionally updated `CarePlan` [web:1][cite:16] |

## Use Case

A patient receiving neurorehabilitation at home is passively monitored overnight or before the day’s therapy session. Before treatment begins, the clinician opens the app, reviews recent observations alongside the patient’s clinical and rehabilitation context, and decides whether to proceed with the session, modify intensity, or defer for review. [cite:23][cite:24]

After the session, the clinician records the treatment delivered and the patient’s response in structured FHIR format. This creates a clear longitudinal record of readiness, intervention, and outcome that can support continuity across providers and settings. [cite:16][cite:18][web:1]

## Getting Started

### Prerequisites

- A FHIR server for development or testing. [web:36][web:43]
- Synthetic or test patient data with core resources such as `Patient`, `Observation`, `Condition`, and `CarePlan`. [web:83]
- A frontend framework or app shell for building the clinical interface.
- Access to a sandbox or mock integration for remote physiological data if live device data is not available.

### Initial setup

1. Clone this repository.
2. Configure environment variables for the target FHIR server base URL.
3. Load or connect sample FHIR resources needed for the demo workflow.
4. Start the local development environment.
5. Validate that the app can read patient context and write back session data. [web:36][web:43]

### Minimum demo scope

For a short build cycle, keep the implementation limited to four screens:

1. Patient selection.
2. Daily readiness dashboard.
3. Session planning.
4. Post-session documentation. [web:36][web:40]

That scope is enough to demonstrate a complete FHIR workflow without overbuilding the platform. A focused, working app is likely to be more persuasive than a broad prototype with shallow implementation. [web:40][web:46]

## Roadmap

### Phase 1
- Implement patient selection and summary context.
- Retrieve core FHIR resources from the target server.
- Display recent physiological observations in a clinician-friendly readiness view.
- Capture a simple daily decision: proceed, modify, or defer. [web:36][cite:23]

### Phase 2
- Add post-session documentation with `Procedure`, `Observation`, and `QuestionnaireResponse`.
- Support structured write-back into the FHIR server.
- Add lightweight trend views for recent observations and session history. [web:1][cite:24]

### Phase 3
- Add richer baseline and longitudinal context.
- Support multiple rehabilitation devices and monitoring inputs through a more flexible integration layer.
- Expand into a broader neurorehabilitation orchestration workflow across settings. [cite:17][cite:18]

### Future direction
- Introduce more advanced clinical intelligence for personalization and recovery support.
- Support broader interoperability with NHS and international workflows.
- Extend from challenge prototype to production-grade neurorehabilitation infrastructure. [cite:20][cite:21]

## Why this repository exists

This repository exists to demonstrate how FHIR can support a clinically meaningful neurorehabilitation workflow using remote physiological monitoring and structured therapy documentation. It is intentionally scoped as a practical app that connects monitoring, decision support, care delivery, and interoperable write-back in a specialty pathway. [cite:16][cite:17][web:36]

## Repository structure

A suggested repository structure:

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









# Architecture

Verada Neurorehab Readiness is designed as a lightweight workflow application layered on top of a FHIR server. Its purpose is to combine patient context, remote physiological monitoring, rehabilitation planning, and post-session documentation in one clinician-facing workflow. [web:43][cite:17][cite:23]

The architecture is intentionally compact for rapid implementation. It prioritizes clear interoperability and a working end-to-end clinical use case over heavy infrastructure or advanced analytics in the first version. [web:36][web:40]

## Design Goals

- Keep the workflow clinically meaningful and easy to demonstrate. [web:36]
- Read real FHIR resources from a server and write structured outputs back. [web:43][web:95]
- Support home or hybrid neurorehabilitation pathways using physiological observations as pre-session context. [cite:23][cite:24]
- Remain extensible for broader Verada orchestration and intelligence layers in future versions. [cite:17][cite:18]

## High-Level Components

### 1. FHIR Server

The FHIR server acts as the system of record for patient context, device-linked observations, conditions, rehabilitation plans, and session outcomes. It provides the interoperable resource layer that the app reads from and writes to. [web:1][web:43]

### 2. Monitoring and Device Inputs

Remote monitoring systems contribute physiological data such as heart rate, respiration, sleep-related measures, movement trends, or other relevant pre-session signals. These data are normalized into FHIR-compatible structures, primarily through `Device` and `Observation` resources. [web:1][cite:23]

### 3. Application Layer

The application presents a therapist-facing interface with patient lookup, daily readiness review, session planning, and post-session documentation. It translates FHIR resources into a clear workflow that supports real care delivery decisions. [cite:24][web:36]

### 4. Documentation and Write-back

After the therapy session, the app records what happened using structured resources such as `Procedure`, `Observation`, `QuestionnaireResponse`, and encounter-linked updates. This creates continuity in the record and supports future longitudinal interpretation. [web:1][web:4][cite:16]

## Data Flow

```text
Remote Monitoring Source / Rehab Device
                |
                v
       FHIR-normalized Device Data
                |
                v
            FHIR Server
                |
     ---------------------------
     |            |            |
     v            v            v
  Patient      Conditions    Care Plans
  Context      + History     + Requests
     \            |            /
      \           |           /
       \          |          /
        v         v         v
      Verada Neurorehab Readiness
                |
                v
      Session Decision + Outcome
                |
                v
            FHIR Write-back
```

## Application Boundaries

The first version should not attempt to implement a full clinical intelligence engine or a full EPR replacement. Its purpose is to show that physiological context, rehabilitation planning, and structured documentation can be connected in a focused FHIR workflow. [web:36][cite:18]

In a later version, this same architecture could support richer baseline and longitudinal models, multi-device integration, and more sophisticated therapy personalization. [cite:17][cite:18]

## Suggested Frontend Modules

- Patient search and selection.
- Daily readiness dashboard.
- Session planning and decision capture.
- Post-session documentation.
- Minimal audit or activity history view.

These modules are enough to support a coherent challenge-ready implementation while leaving space for later growth. [web:40][web:46]

## Notes

This repository represents a challenge-focused implementation and is intentionally scoped for clarity, speed, and demonstrable interoperability. It can later evolve into a broader Verada workflow layer for remote neurorehabilitation and longitudinal rehabilitation intelligence. [cite:18][cite:20]
