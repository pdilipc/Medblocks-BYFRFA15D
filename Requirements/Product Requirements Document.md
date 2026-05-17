# Product Requirements Document: Verada Neurorehab Readiness

## Product overview

**App name:** Verada Neurorehab Readiness  
**Tagline:** A clinician-facing FHIR application for daily neurorehabilitation readiness review, session planning, and structured outcome documentation. [file:39]

Verada Neurorehab Readiness is a specialty-care interoperability application designed for remote and hybrid neurorehabilitation workflows. It combines patient context, recent physiological observations, rehabilitation plans, and post-session documentation in a focused clinician workflow rather than functioning as a generic patient viewer. [file:39][file:43]

The product is intentionally scoped as a lightweight workflow layer on top of a FHIR server. The first version emphasizes a credible end-to-end clinical use case, rapid implementation, and interoperability over broad platform coverage or advanced predictive intelligence. [file:43][file:39]

## Problem

In neurorehabilitation pathways, clinically useful home-generated physiological data is often disconnected from the therapist’s day-of-session decision-making process. Clinicians may need to review patient context, recent observations, the current rehabilitation pathway, and therapy documentation across fragmented systems or incomplete records. [file:39]

This creates a workflow gap before treatment begins. A clinician still needs to decide whether to proceed with a session, modify its intensity or format, or defer it for review, but that decision is not always supported by a concise interoperable interface that ties readiness context to structured documentation and longitudinal follow-up. [file:39][file:40]

## Target user

The primary user is a clinician or therapist delivering neurorehabilitation in a home-based or hybrid care pathway. This user needs a compact, clinically meaningful workflow to review patient readiness, align the session with the active care plan, and record structured outcomes efficiently. [file:39][file:40]

A secondary user is a technical or clinical innovation team demonstrating a specialty-care FHIR workflow in a sandbox, pilot, or challenge setting. This audience needs a practical app that clearly shows interoperability, synthetic testability, and future extensibility without overbuilding the first version. [file:39][file:43][file:41]

## Core value proposition

Verada Neurorehab Readiness connects pre-session physiological context, rehabilitation planning, and structured write-back into one neurorehabilitation-specific workflow. Its value lies in making daily therapy readiness review actionable, interoperable, and easy to demonstrate using a small, coherent set of FHIR resources and synthetic neurorehabilitation datasets. [file:40][file:42][file:43]

## Goals

- Support a clinician-facing workflow for patient lookup, readiness review, session planning, and post-session documentation. [file:39][file:40]
- Read patient context and recent observations from a FHIR server and write structured updates back after the session. [file:43][file:42]
- Use synthetic neurorehabilitation datasets to simulate realistic stroke and longitudinal rehab pathways for development and demonstration. [file:39][file:45][file:44]
- Demonstrate a specialty-care interoperability app that is clinically coherent and implementation-ready within a short build cycle. [file:39][file:43]
- Create a foundation that can later expand into broader orchestration, multi-device integration, and richer intelligence layers. [file:43][file:39]

## Non-goals

- A full electronic patient record or broad rehabilitation platform. [file:43]
- A validated clinical decision-support or prediction engine. [file:43][file:41]
- A statistically validated or production-grade disease model derived from synthetic data. [file:41][file:45]
- A generic remote patient monitoring dashboard without neurorehabilitation-specific workflow framing. [file:40]
- Complete modeling of every rehabilitation data element or workflow in version one. [file:42]

## Core features

### Must-have

- Patient lookup and selection with core demographic and rehabilitation context. [file:39]
- Daily readiness dashboard with recent physiological observations and relevant clinical context. [file:39][file:40]
- Session planning workflow supporting proceed, modify, or defer decisions with clinician rationale. [file:39][file:40]
- Post-session documentation using structured FHIR resources such as `Procedure`, `Observation`, and `QuestionnaireResponse`. [file:43][file:42]
- Bidirectional FHIR workflow that reads from a FHIR server and writes structured updates back into the patient record. [file:39][file:43]
- Synthetic neurorehabilitation cohort support through a custom Synthea GMF module for development and demonstration. [file:39][file:45]

### Nice-to-have

- Lightweight recent trend or minimal activity history view. [file:43]
- Therapy-routing logic for differentiated neurorehabilitation pathways based on baseline impairment and recent readiness context. [file:39][file:45]
- Multiple device or monitoring inputs through a more flexible integration layer. [file:39]
- Richer baseline and longitudinal context beyond the minimum challenge scope. [file:39]

## User stories

- As a clinician, I want to search for and select a patient from a FHIR server so that I can begin the day’s session review in the correct clinical context. [file:40][file:42]
- As a clinician, I want to see recent physiological observations alongside conditions, care plans, and service requests so that I can assess readiness before therapy begins. [file:40][file:42]
- As a clinician, I want to decide whether to proceed, modify, or defer today’s session so that the treatment plan reflects the patient’s current state. [file:40][file:39]
- As a clinician, I want to record what therapy was delivered and how the patient responded so that the patient record supports continuity and longitudinal interpretation. [file:39][file:43]
- As a developer or evaluator, I want to load realistic synthetic neurorehabilitation cohorts so that I can test the workflow without privacy constraints. [file:39][file:41][file:45]
- As a product team, I want the first version to remain compact and clinically credible so that the implementation is achievable and persuasive in a challenge or pilot setting. [file:39][file:43]

## Primary workflow

1. The clinician searches for and selects the patient from the FHIR server. [file:40]
2. The app loads demographics, active context, conditions, care plans, service requests, and recent observations. [file:40][file:42]
3. The clinician reviews readiness context and decides to proceed, modify, or defer the session. [file:40]
4. The therapy session is delivered according to the chosen plan. [file:40]
5. The clinician records treatment details, rationale, and patient response as structured FHIR documentation. [file:40][file:42]
6. The app writes the resulting outputs back to the FHIR server for continuity of care. [file:43]

## Minimum viable scope

The minimum credible demo should be limited to four screens: patient selection, daily readiness dashboard, session planning, and post-session documentation. This scope is explicitly recommended in the repo materials because it demonstrates a complete and coherent workflow without overextending implementation effort. [file:39][file:40][file:43]

## Data and interoperability assumptions

The application is built on a compact FHIR resource model centered on `Patient`, `Encounter`, `Device`, `Observation`, `Condition`, `CarePlan`, `ServiceRequest`, `Procedure`, and `QuestionnaireResponse`, with optional use of `MedicationStatement`, `AllergyIntolerance`, and `Communication`. This resource set is intended to keep the workflow small, coherent, and clinically meaningful in the first version. [file:42][file:39]

Synthetic data is generated through a custom Synthea GMF module that models longitudinal stroke rehabilitation pathways, physiological monitoring, therapy routing, and unified outcome tracking. The synthetic module is a development and demonstration tool, not a source of clinical evidence or patient-specific recommendations. [file:45][file:44][file:41]

## Success metrics

### Product success

- A clinician can complete the end-to-end workflow from patient selection to structured FHIR write-back within a single session demo. [file:39][file:40]
- The app correctly reads required FHIR resources and persists structured session outputs back to the server. [file:43][file:42]
- A synthetic cohort can be generated and loaded to exercise the full workflow without using real patient data. [file:39][file:45]
- The application is understandable as a neurorehabilitation readiness workflow rather than a generic dashboard. [file:40]

### Build success

- The first release ships as a focused prototype with four core screens and no major scope creep. [file:39][file:40]
- The architecture remains extensible for future multi-device, longitudinal, and orchestration capabilities. [file:43][file:39]

## Risks and constraints

- Overexpanding the scope beyond the core readiness workflow could weaken implementation quality and demo clarity. [file:39][file:43]
- Synthetic data may appear overly deterministic or illustrative if not clearly positioned as development-only. [file:41][file:45]
- Without disciplined workflow framing, the product could be mistaken for either a generic RPM dashboard or a full AI prediction platform, both of which the repo explicitly advises against. [file:40]
- Real clinical deployment would require additional governance, validation, and operational layers that are outside this first version. [file:43][file:41]

## Release framing

Version one should be presented as a focused specialty-care interoperability prototype for neurorehabilitation readiness and session documentation. It should show that physiological context, rehabilitation planning, synthetic specialty datasets, and structured FHIR write-back can be connected in one clinically meaningful pathway. [file:39][file:43]
