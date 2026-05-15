# Architecture

Verada Neurorehab Readiness is designed as a lightweight workflow application layered on top of a FHIR server. Its purpose is to combine patient context, remote physiological monitoring, rehabilitation planning, and post-session documentation in one clinician-facing workflow.

The architecture is intentionally compact for rapid implementation. It prioritizes clear interoperability and a working end-to-end clinical use case over heavy infrastructure or advanced analytics in the first version. 

## Design Goals

- Keep the workflow clinically meaningful and easy to demonstrate. 
- Read real FHIR resources from a server and write structured outputs back. 
- Support home or hybrid neurorehabilitation pathways using physiological observations as pre-session context. 
- Remain extensible for broader Verada orchestration and intelligence layers in future versions. 

## High-Level Components

### 1. FHIR Server

The FHIR server acts as the system of record for patient context, device-linked observations, conditions, rehabilitation plans, and session outcomes. It provides the interoperable resource layer that the app reads from and writes to.

### 2. Monitoring and Device Inputs

Remote monitoring systems contribute physiological data such as heart rate, respiration, sleep-related measures, movement trends, or other relevant pre-session signals. These data are normalized into FHIR-compatible structures, primarily through `Device` and `Observation` resources.

### 3. Application Layer

The application presents a therapist-facing interface with patient lookup, daily readiness review, session planning, and post-session documentation. It translates FHIR resources into a clear workflow that supports real care delivery decisions. 

### 4. Documentation and Write-back

After the therapy session, the app records what happened using structured resources such as `Procedure`, `Observation`, `QuestionnaireResponse`, and encounter-linked updates. This creates continuity in the record and supports future longitudinal interpretation.

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
