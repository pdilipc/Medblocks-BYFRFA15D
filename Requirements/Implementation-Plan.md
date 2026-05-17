# Implementation Plan: Verada Neurorehab Readiness

## Purpose

This implementation plan defines the build order for Verada Neurorehab Readiness so that delivery follows a coherent dependency sequence.

The overall product vision is neurorehabilitation readiness on top of FHIR. However, the first implementation scope is Epic 1: Patient Management and Patient Details Foundation. That means the build must begin with patient CRUD, patient search, patient details, and observation-driven longitudinal review before later readiness and documentation workflows are added.

## Delivery structure

The implementation should follow a staged epic model:

- **Epic 1:** Patient Management and Patient Details Foundation
- **Epic 2:** Neurorehabilitation Readiness Review
- **Epic 3:** Session Planning, Documentation, and Structured Write-back

Epic 1 is the minimum deliverable and must be completed before Epic 2 or Epic 3 are built.

## Phase 1: Project setup and repository structure

### Goals

- Initialize the project
- Establish repository structure
- Configure environment variables
- Create the foundational documentation set

### Tasks

- Initialize the app with Next.js and TypeScript
- Add Tailwind CSS
- Create the `docs/requirements/` folder
- Add the six planning documents
- Configure `.env.example`
- Set up base application layout
- Set up utility folders for FHIR, validation, and shared types

### Done criteria

- Project runs locally
- TypeScript compiles successfully
- Base folder structure is in place
- Environment variable loading works

## Phase 2: Backend FHIR proxy foundation

### Goals

- Build the secure FHIR proxy layer required for all frontend data access

### Tasks

- Create backend proxy routes for:
  - `Patient`
  - `Observation`
  - `Condition`
  - `MedicationRequest`
- Add forwarding to the configured FHIR server
- Inject authorization headers on outbound requests
- Preserve query parameters from frontend requests
- Add consistent backend error handling
- Add request utilities for GET, POST, and PUT operations

### Done criteria

- Frontend can call the proxy successfully
- Proxy can reach the FHIR server
- Authorization is handled server-side only
- Proxy errors are returned in a predictable structure

## Phase 3: Patient list and search

### Goals

- Deliver the first usable patient management screen

### Tasks

- Build patient list page at `/` or `/patients`
- Fetch all patients from the FHIR server via proxy
- Display patient full name, gender, and date of birth
- Add search input using partial name search
- Add loading, empty, and error states
- Make patient rows clickable

### Done criteria

- Patient list loads from the FHIR server
- Search by partial name works
- Patient rows navigate correctly to patient details
- Loading and error states are visible and usable

## Phase 4: Patient create and edit flows

### Goals

- Support patient creation and update workflows using a reusable form

### Tasks

- Build reusable patient form component
- Add create flow
- Add edit flow with pre-filled values
- Validate:
  - given name
  - family name
  - gender
  - date of birth
- Map form input to FHIR Patient resource structure
- Submit create and update requests through the proxy
- Refresh patient list after success
- Add success and error feedback

### Done criteria

- Create patient works end to end
- Edit patient works end to end
- Form validation prevents invalid submissions
- Patient list updates after successful create or edit

## Phase 5: Patient details page foundation

### Goals

- Build the main clinical review surface for Epic 1

### Tasks

- Create route `/patient/[id]`
- Fetch patient demographics
- Display:
  - full name
  - gender
  - date of birth
- Add page-level loading and error states
- Add back navigation to patient list

### Done criteria

- Clicking a patient opens a working patient details page
- Demographics render correctly
- Page handles loading and error states gracefully

## Phase 6: Vitals and longitudinal observation display

### Goals

- Add longitudinal patient context using observations

### Tasks

- Fetch vital sign observations for:
  - heart rate
  - temperature
  - respiratory rate
  - oxygen saturation
  - height
  - weight
  - BMI
  - blood pressure
- Normalize observation data for UI use
- Build chart view
- Build table view
- Add chart/table toggle
- Handle blood pressure as systolic and diastolic lines on one chart
- Add empty, loading, and error states for vitals

### Done criteria

- Vitals load from FHIR observations
- Chart view works
- Table view works
- Blood pressure is displayed correctly
- The vitals section supports longitudinal review cleanly

## Phase 7: Conditions and medications

### Goals

- Complete the patient details clinical review surface

### Tasks

- Fetch conditions via proxy
- Display conditions table with:
  - condition name
  - onset date
- Fetch medications via proxy
- Display medications table with:
  - medication name
  - status
- Add loading, empty, and error states for both sections

### Done criteria

- Conditions display correctly
- Medications display correctly
- Patient details page now shows demographics, vitals, conditions, and medications

## Phase 8: Epic 1 refinement and validation

### Goals

- Stabilize Epic 1 as a complete, demo-ready foundation

### Tasks

- Improve UI consistency across patient list, form, and details
- Improve feedback messages
- Refine loading and error behavior
- Confirm all cross-check requirements pass
- Review accessibility basics
- Clean up data mapping edge cases
- Ensure patient details supports readiness-relevant observations as context

### Done criteria

- Epic 1 works end to end
- Cross-checks for patient management and patient details all pass
- UI is coherent and clinically readable
- Epic 1 is ready to act as the base for later neurorehabilitation workflows

## Phase 9: Epic 2 readiness workflow extension

### Goals

- Introduce neurorehabilitation readiness review on top of the Epic 1 foundation

### Tasks

- Add readiness-oriented review screen or section
- Use longitudinal observations and patient context as inputs
- Add neurorehabilitation context framing
- Define readiness interpretation logic
- Keep the workflow clearly separate from validated clinical decision support claims

### Done criteria

- Readiness review can be demonstrated on top of patient details
- Epic 1 data flows support the readiness layer cleanly

## Phase 10: Epic 3 planning, documentation, and write-back

### Goals

- Add clinician action and structured output capture

### Tasks

- Add proceed, modify, or defer decision capture
- Add rationale fields
- Add post-session documentation forms
- Write back structured `Procedure`, `Observation`, and `QuestionnaireResponse` resources
- Add confirmation and error handling for submission

### Done criteria

- Clinician actions can be captured and written back to the FHIR server
- The app supports an end-to-end readiness-to-documentation workflow

## Phase 11: Synthetic data and specialty workflow support

### Goals

- Support later development and demo workflows using synthetic neurorehabilitation data

### Tasks

- Document synthetic data workflow
- Add or refine custom Synthea module usage
- Ensure synthetic observations remain realistic and non-deterministic
- Use synthetic data to demonstrate readiness-oriented pathways where live data is not available

### Done criteria

- Synthetic cohorts can support testing and demonstration of later neurorehabilitation workflows
- Synthetic data is clearly positioned as development and demo support only

## Phase 12: Final validation and deployment

### Goals

- Prepare the application for review, pilot demonstration, or challenge submission

### Tasks

- Perform manual end-to-end testing
- Test proxy and FHIR connectivity in deployed environment
- Validate all Epic 1 requirements
- Validate readiness workflow if Epic 2 is included
- Finalize environment configuration
- Deploy the application
- Confirm hosted routes and data access work correctly

### Done criteria

- Hosted build is accessible
- Epic 1 is stable in the target environment
- Later epics, if included, operate without breaking the Epic 1 foundation

## Cross-check milestones

### Epic 1 acceptance milestone

Confirm:
- patient list loads from FHIR
- create form appears with correct fields
- edit opens pre-filled form
- saving updates the list
- search filters patients by partial name
- clicking a patient opens patient details
- patient demographics are visible
- vitals display correctly
- conditions display correctly
- medications display correctly

### Epic 2 acceptance milestone

Confirm:
- readiness-oriented review can be performed using Epic 1 patient context
- readiness-relevant observations are visible and usable as context

### Epic 3 acceptance milestone

Confirm:
- session decisions can be recorded
- documentation can be submitted
- write-back succeeds

## Build order principle

Do not build advanced neurorehabilitation workflow logic before the patient management and patient details foundation is stable.

The correct dependency order is:

1. Project setup
2. FHIR proxy
3. Patient list and search
4. Create and edit patient
5. Patient details
6. Vitals
7. Conditions and medications
8. Epic 1 stabilization
9. Readiness extension
10. Documentation and write-back

## Definition of success

Implementation is successful when Epic 1 delivers a complete, clinically readable FHIR-based patient management and patient details workflow, and the system remains structurally ready for later neurorehabilitation readiness and documentation extensions.
