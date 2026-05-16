# Architecture

## Overview

Verada Neurorehab Readiness is designed as a lightweight workflow application layered on top of a FHIR server. Its purpose is to combine patient context, remote physiological monitoring, synthetic neurorehabilitation datasets, rehabilitation planning, and post-session documentation in one clinician-facing workflow.

The architecture is intentionally compact for rapid implementation. It prioritizes clear interoperability and a working end-to-end clinical use case over heavy infrastructure or advanced analytics in the first version.

The synthetic data generation layer is a dedicated component of the architecture, separate from the application’s clinician-facing workflow. Its role is to provide structured and plausible FHIR resources that exercise the readiness, routing, documentation, and write-back logic of the application.

## Design Goals

- Keep the workflow clinically meaningful and easy to demonstrate.
- Read real FHIR resources from a server and write structured outputs back.
- Support home or hybrid neurorehabilitation pathways using physiological observations as pre-session context.
- Use synthetic neurorehabilitation cohorts to simulate realistic specialty workflows without privacy constraints.
- Remain extensible for broader Verada orchestration and intelligence layers in future versions.

## High-Level Components

### 1. FHIR Server

The FHIR server acts as the system of record for patient context, device-linked observations, conditions, rehabilitation plans, and session outcomes. It provides the interoperable resource layer that the app reads from and writes to.

### 2. Synthetic Data Generation Layer

A custom Synthea Generic Module Framework module is used to generate synthetic stroke and neurorehabilitation-oriented patient pathways. This layer supports baseline impairment scenarios, longitudinal physiological observations, therapy-routing logic, and outcome trajectories relevant to the app workflow.

### 3. Monitoring and Device Inputs

Remote monitoring systems contribute physiological data such as heart rate, respiration, sleep-related measures, movement trends, or other relevant pre-session signals. In the challenge implementation, these may be represented through synthetic resource generation, mock device feeds, or uploaded bundles.

### 4. Application Layer

The application presents a therapist-facing interface with patient lookup, daily readiness review, session planning, therapy routing, and post-session documentation. It translates FHIR resources into a clear workflow that supports real care delivery decisions.

### 5. Documentation and Write-back

After the therapy session, the app records what happened using structured resources such as `Procedure`, `Observation`, `QuestionnaireResponse`, and encounter-linked updates. This creates continuity in the record and supports future longitudinal interpretation.

## Data Flow

```text
Custom Synthea Neurorehab Module
                |
                v
     Synthetic FHIR Patient Cohort
                |
                v
            FHIR Server
                |
     -------------------------------
     |              |              |
     v              v              v
  Patient       Conditions      Care Plans
  Context       + History       + Requests
     \              |              /
      \             |             /
       \            |            /
        v           v           v
      Verada Neurorehab Readiness
                |
                v
      Session Decision + Outcome
                |
                v
            FHIR Write-back
```

## Application Boundaries

The first version should not attempt to implement a full clinical intelligence engine or a full EPR replacement. Its purpose is to show that physiological context, rehabilitation planning, synthetic specialty data, and structured documentation can be connected in a focused FHIR workflow.

In a later version, this same architecture could support richer baseline and longitudinal models, multi-device integration, and more sophisticated therapy personalization.

## Suggested Frontend Modules

- Patient search and selection.
- Daily readiness dashboard.
- Session planning and routing.
- Post-session documentation.
- Minimal activity history or recent trend view.

These modules are enough to support a coherent challenge-ready implementation while leaving space for later growth.
