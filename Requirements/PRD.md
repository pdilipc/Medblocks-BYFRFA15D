# Product Requirements Document: Verada Neurorehab Readiness

## Product overview

**App name:** Verada Neurorehab Readiness  
**Tagline:** A clinician-facing FHIR application for patient management, longitudinal patient review, and neurorehabilitation readiness workflows.

Verada Neurorehab Readiness is a specialty-care interoperability application designed for remote and hybrid neurorehabilitation workflows. It supports neurorehabilitation readiness as the overarching business requirement, while delivery begins with a foundational patient management and patient details layer built on top of a FHIR server.

The product is intentionally scoped as a lightweight workflow application rather than a full electronic patient record. The first implementation phase prioritizes a clinically meaningful patient management and patient review experience, which then supports later readiness-specific decision-making, session planning, and structured write-back.

## Problem

In neurorehabilitation pathways, clinicians need both longitudinal patient context and workflow-specific readiness signals before they can make informed therapy decisions. In practice, patient discovery, demographic review, vital signs, conditions, medications, and rehabilitation-specific context are often fragmented across systems or difficult to review in one place.

This creates two connected workflow problems. First, practitioners need a reliable way to find, create, update, and review patient records from a FHIR server. Second, once a patient is selected, clinicians need a concise but meaningful view of longitudinal context that can later support neurorehabilitation readiness review, session planning, and outcome documentation.

## Target user

The primary user is a clinician or therapist working in neurorehabilitation or a related pathway who needs to manage patients, review clinical context, and eventually make readiness-informed therapy decisions. This user needs a compact, clinically meaningful workflow that begins with patient discovery and longitudinal review before moving into specialty-specific action.

A secondary user is a technical or clinical innovation team demonstrating a specialty-care FHIR workflow in a sandbox, pilot, or challenge environment. This audience needs a practical app that clearly shows interoperability, patient data handling, patient detail review, and future extensibility into neurorehabilitation-specific workflows.

## Core value proposition

Verada Neurorehab Readiness combines patient management, patient longitudinal review, and neurorehabilitation-specific workflow potential in one focused FHIR-based application. Its value lies in creating a clean clinical foundation where practitioners can manage patient records, review vital patient context, and then build toward neurorehabilitation readiness and structured outcome workflows without switching systems.

## Product structure

The product should be framed through a staged epic structure:

- **Epic 1: Patient Management and Patient Details Foundation**  
  Build the foundational FHIR-based workflow for listing patients, creating and editing patients, searching patients by name, and reviewing demographics, vital signs, conditions, and medications.

- **Epic 2: Neurorehabilitation Readiness Review**  
  Extend the patient details foundation with neurorehabilitation-oriented readiness interpretation using recent physiological context, rehabilitation plans, and relevant clinical background.

- **Epic 3: Session Planning, Documentation, and Structured Write-back**  
  Add clinician workflow steps for proceed/modify/defer decisions, post-session documentation, and structured FHIR write-back.

## Goals

- Support a clinician-facing patient management workflow for listing, creating, editing, and searching patients from a FHIR server.
- Provide a patient details page that presents demographics, longitudinal vital signs, conditions, and medications in a clinically useful way.
- Establish the foundational clinical context needed for later neurorehabilitation readiness review and session planning.
- Read patient context and related resources from a FHIR server through a controlled backend proxy.
- Demonstrate a specialty-care interoperability app that is clinically coherent, technically feasible, and extensible.
- Preserve a path toward synthetic neurorehabilitation datasets, therapy-routing logic, and later write-back workflows.

## Non-goals

- A full electronic patient record or broad rehabilitation platform.
- A validated clinical decision-support or prediction engine in version one.
- A production-grade statistical disease model derived from synthetic data.
- Full modeling of every rehabilitation process in the first implementation phase.
- Replacing the FHIR server as the system of record.

## Core features

### Must-have

#### Epic 1: Patient Management and Patient Details Foundation

- List all patients from the FHIR server with full name, gender, and date of birth.
- Search patients by name using FHIR search with partial matching.
- Create new patients using a validated form with given name, family name, gender, and date of birth.
- Edit existing patients using the same pre-filled patient form and save updates back to the FHIR server.
- Navigate from a patient list to a dedicated patient details page at `/patient/[id]`.
- Display patient demographics at the top of the details page.
- Display vital signs including heart rate, temperature, respiratory rate, oxygen saturation, height, weight, BMI, and blood pressure over time.
- Provide a toggle between chart view and table view for vital signs.
- Display conditions in a table with condition name and onset date.
- Display medications in a table with medication name and status.
- Use a backend FHIR proxy that injects authorization headers and forwards browser requests to the FHIR server.

#### Epic 2: Neurorehabilitation Readiness Review

- Layer a neurorehabilitation-oriented interpretation workflow on top of patient details and recent physiological context.
- Use longitudinal patient context as an input into readiness-oriented clinical review rather than presenting isolated data.

#### Epic 3: Session Planning and Documentation

- Support proceed, modify, or defer session decisions with clinician rationale.
- Capture structured post-session documentation and write it back using FHIR resources such as `Procedure`, `Observation`, and `QuestionnaireResponse`.

### Nice-to-have

- Lightweight recent trend highlighting or compact summary tiles on the patient details page.
- Therapy-routing logic for differentiated neurorehabilitation pathways in later phases.
- Multiple device or monitoring inputs through a more flexible integration layer.
- Richer baseline and longitudinal neurorehabilitation context beyond minimum challenge scope.
- Synthetic neurorehabilitation cohorts for development, sandbox testing, and later specialty workflow demonstrations.

## User stories

### Epic 1: Patient Management and Patient Details Foundation

- As a practitioner, I want to see all patients from the FHIR server so that I can select the correct patient for review.
- As a practitioner, I want to search patients by partial name so that I can quickly find the patient I need.
- As a practitioner, I want to create a patient with validated demographics so that new records are entered correctly.
- As a practitioner, I want to edit a patient’s demographic information so that the FHIR record stays accurate and current.
- As a practitioner, I want to click a patient and open a detailed page so that I can review demographics and medical history in one place.
- As a practitioner, I want to see longitudinal vital signs, conditions, and medications so that I can build a clinically meaningful picture of the patient before making decisions.

### Epic 2: Neurorehabilitation Readiness Review

- As a neurorehabilitation clinician, I want to review longitudinal patient context before a session so that I can assess readiness in a more informed way.
- As a neurorehabilitation clinician, I want the app to present patient details in a way that supports rehabilitation decision-making rather than generic chart browsing.

### Epic 3: Session Planning and Documentation

- As a clinician, I want to record whether I will proceed, modify, or defer the session so that the treatment plan reflects the patient’s current state.
- As a clinician, I want to document what therapy was delivered and how the patient responded so that the patient record supports continuity and longitudinal interpretation.

## Primary workflow

### Epic 1 workflow

1. The practitioner opens the patient list and loads patients from the FHIR server.
2. The practitioner searches by name or browses the list.
3. The practitioner can create a new patient or edit an existing patient using a validated demographic form.
4. The practitioner clicks a patient and navigates to `/patient/[id]`.
5. The app displays the patient’s demographics, longitudinal vital signs, conditions, and medications.

### Epic 2 workflow

6. The clinician uses patient details and longitudinal context as the basis for neurorehabilitation readiness review.

### Epic 3 workflow

7. The clinician records session planning decisions and post-session outcomes.
8. The app writes structured outputs back to the FHIR server for continuity of care.

## Minimum viable scope

The minimum credible first implementation should be **Epic 1**:

1. Patient list
2. Create/edit patient form
3. Search by name
4. Patient details page
5. Demographics
6. Vital signs with chart/table toggle
7. Conditions table
8. Medications table
9. Backend FHIR proxy with authorization handling

This creates the operational and clinical foundation needed before neurorehabilitation-specific readiness and documentation workflows are layered in.

## Data and interoperability assumptions

The application is built on a compact FHIR resource model centered on `Patient`, `Observation`, `Condition`, and `MedicationRequest` for Epic 1, with additional support from `Encounter`, `CarePlan`, `ServiceRequest`, `Procedure`, and `QuestionnaireResponse` in later neurorehabilitation-oriented phases.

Patient data must conform to FHIR R4 conventions, including `name[0].given`, `name[0].family`, `gender`, and `birthDate`. Browser requests should be routed through a backend FHIR proxy that forwards search parameters and injects authorization headers before calling the target FHIR server.

Synthetic neurorehabilitation data remains relevant for development and later-stage specialty workflows, but it is not the primary dependency for Epic 1 patient management and patient details features. Where synthetic data is used in later phases, it should remain a development and demonstration tool rather than a source of clinical evidence.

## Success metrics

### Product success

- A practitioner can load the patient list from the FHIR server successfully.
- A practitioner can create and edit patient records with validation and see those updates reflected in the list.
- A practitioner can search patients by name with partial matching.
- Clicking a patient opens a usable patient details page with demographics, vital signs, conditions, and medications.
- The product is understandable as a foundation for neurorehabilitation readiness rather than a generic patient viewer alone.

### Build success

- The first release ships with Epic 1 functionality working end to end and no major scope creep.
- The architecture remains extensible for later readiness review, documentation, multi-device inputs, and broader orchestration capabilities.

## Risks and constraints

- Trying to deliver all readiness, documentation, and patient management features at once could weaken implementation quality and demo clarity.
- Without careful framing, the product could be mistaken for a generic patient viewer rather than a neurorehabilitation-focused foundation.
- Real clinical deployment would require additional governance, validation, operational controls, and production-grade security outside this first version.
- Synthetic data must not be positioned as validated clinical evidence or a clinical recommendation engine.

## Release framing

Version one should be presented as **Epic 1: Patient Management and Patient Details Foundation** for a broader neurorehabilitation readiness platform. It should show that clinicians can manage patients, review longitudinal context from FHIR resources, and establish the foundation for later readiness-oriented workflows, session planning, and structured write-back.
