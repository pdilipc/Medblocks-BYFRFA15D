# Technical Requirements Document: Verada Neurorehab Readiness

## Purpose

This Technical Requirements Document translates the product requirements for Verada Neurorehab Readiness into concrete implementation choices. The product vision remains neurorehabilitation readiness on top of FHIR, but delivery begins with a foundational patient management and patient details layer that supports future readiness-specific workflows.

The goal of this document is to lock in the technical stack, architecture, routing, FHIR integration patterns, proxy behavior, validation rules, and module boundaries so implementation remains coherent across the repository.

## System scope

The system is a clinician-facing FHIR application with staged delivery.

### Epic 1: Patient Management and Patient Details Foundation

Epic 1 is the minimum implementation scope and includes:

- Listing all patients from the FHIR server
- Searching patients by name
- Creating new patients
- Editing existing patients
- Viewing a patient details page
- Displaying demographics
- Displaying longitudinal vital signs
- Displaying conditions
- Displaying medications
- Routing all browser FHIR calls through a backend proxy

### Epic 2: Neurorehabilitation Readiness Review

Epic 2 extends the patient details layer with neurorehabilitation-oriented readiness interpretation using longitudinal patient context, physiological observations, and rehabilitation-related context.

### Epic 3: Session Planning, Documentation, and Structured Write-back

Epic 3 adds session decisions, post-session documentation, and structured FHIR write-back using resources such as `Procedure`, `Observation`, and `QuestionnaireResponse`.

## Architecture overview

The application should follow a lightweight layered architecture:

1. **Frontend application layer**  
   Presents the clinician UI for patient management, patient review, and later readiness workflows.

2. **Backend FHIR proxy layer**  
   Receives browser requests, injects authorization headers, forwards requests to the FHIR server, and returns responses to the frontend.

3. **FHIR server layer**  
   Serves as the system of record for patient and clinical data.

4. **Optional synthetic data generation layer**  
   Supports development and demonstration datasets for later neurorehabilitation-oriented workflows, but is not required for Epic 1 runtime behavior.

## Recommended stack

### Frontend

- Next.js 14 with TypeScript and App Router
- Tailwind CSS
- shadcn/ui or similar component library
- TanStack Query for data fetching and caching
- Zod for validation
- Plotly, Recharts, or a similar charting library for time-series vitals

### Backend

- Next.js route handlers or a lightweight Node server for proxy endpoints
- Centralized FHIR client utilities
- Server-side request forwarding with authorization header injection

### Database

- No primary application database is required for Epic 1 clinical data
- The FHIR server remains the system of record
- Optional local relational storage may be used later for non-clinical metadata only

### Hosting

- Frontend and backend proxy can be deployed together on Vercel or another Node-compatible platform
- FHIR server is external or sandbox-hosted
- Synthetic generation can run locally or in a separate tooling environment

## Application routes

### Frontend routes

- `/` or `/patients`  
  Patient list and patient management screen

- `/patient/[id]`  
  Patient details page

- Optional later route: `/patient/[id]/readiness`  
  Neurorehabilitation readiness workflow entry point

### Backend proxy routes

Suggested route structure:

- `/api/fhir/Patient`
- `/api/fhir/Patient/[id]`
- `/api/fhir/Observation`
- `/api/fhir/Condition`
- `/api/fhir/MedicationRequest`

The backend proxy should accept query parameters from the frontend and forward them to the target FHIR server unchanged, except for required authorization and internal configuration handling.

## Frontend modules

### Epic 1 modules

- `patient-list`
- `patient-search`
- `patient-form`
- `patient-details-header`
- `vitals-section`
- `vitals-chart-view`
- `vitals-table-view`
- `conditions-table`
- `medications-table`
- `loading-state`
- `error-state`

### Epic 2 modules

- `readiness-summary`
- `neurorehab-context-panel`
- `readiness-review`

### Epic 3 modules

- `session-planning`
- `post-session-documentation`
- `writeback-confirmation`

## Backend FHIR proxy requirements

The backend proxy is required for all frontend FHIR traffic.

### Responsibilities

- Receive browser requests for FHIR resources
- Append the required `Authorization` header
- Forward the request to the configured FHIR server
- Return the raw or normalized FHIR response to the frontend
- Centralize request error handling
- Keep credentials and tokens out of browser code

### Supported Epic 1 operations

#### Patient

- `GET /Patient`
- `GET /Patient?name={partialName}`
- `GET /Patient/[id]`
- `POST /Patient`
- `PUT /Patient/[id]`

#### Observation

- `GET /Observation?subject=Patient/[id]&code=8867-4,8310-5,9279-1,59408-5,8302-2,29463-7,39156-5,55284-4`

#### Condition

- `GET /Condition?patient=[id]`

#### MedicationRequest

- `GET /MedicationRequest?patient=[id]`

## FHIR resource requirements

### Patient resource mapping

Patient create and update operations must follow FHIR R4 conventions:

- `name[0].given` must be an array
- `name[0].family` must be a string
- `gender` must use a valid FHIR administrative gender value
- `birthDate` must use `YYYY-MM-DD`

### Observation handling

The application must support retrieval and display of the following vital sign observations:

- Heart rate: `8867-4`
- Temperature: `8310-5`
- Respiratory rate: `9279-1`
- Oxygen saturation: `59408-5`
- Height: `8302-2`
- Weight: `29463-7`
- BMI: `39156-5`
- Blood pressure panel: `55284-4`

For blood pressure observations, the UI must extract:
- Systolic blood pressure: `8480-6`
- Diastolic blood pressure: `8462-4`

These should be displayed as two lines on the same chart.

### Condition handling

Conditions should be fetched by patient reference and displayed with:
- Condition name
- Onset date

### MedicationRequest handling

Medication requests should be fetched by patient reference and displayed with:
- Medication name
- Status

## Validation requirements

### Patient form validation

The patient form must validate:

- Given name is required
- Family name is required
- Gender is required
- Gender must be one of:
  - `male`
  - `female`
  - `other`
  - `unknown`
- Date of birth is required
- Date of birth cannot be in the future
- Date of birth must be in valid `YYYY-MM-DD` format

Validation should occur both:
- in the browser before submission
- in the server-side proxy or request-construction layer before forwarding to FHIR where appropriate

## Vitals display requirements

The patient details page must support two viewing modes for vital signs:

### Chart view

- Each vital sign should be shown as its own time-series line chart
- Blood pressure should be shown as a single chart with systolic and diastolic as separate lines
- Time should be on the x-axis
- Measured value should be on the y-axis

### Table view

The table should display:
- Observation date
- Vital sign name
- Value
- Unit where available

A user-facing toggle must switch between chart view and table view.

## UI state requirements

The frontend must clearly support:

### Loading states
- Patient list loading
- Patient details loading
- Vitals loading
- Conditions loading
- Medications loading
- Form submission loading

### Error states
- Failed patient list fetch
- Failed patient create
- Failed patient update
- Failed patient details fetch
- Failed vitals fetch
- Failed conditions fetch
- Failed medications fetch

### Success states
- Patient created successfully
- Patient updated successfully

## Security and access considerations

- Authorization credentials must never be exposed in browser code
- All FHIR server access from the frontend must pass through the backend proxy
- Secrets must be stored in environment variables
- The proxy should support secure bearer-token forwarding or equivalent authorization handling
- Logging should avoid exposing patient-sensitive data unnecessarily

## Environment variables

Suggested environment variables:

- `FHIR_BASE_URL`
- `FHIR_AUTH_TYPE`
- `FHIR_ACCESS_TOKEN`
- `FHIR_CLIENT_ID`
- `FHIR_CLIENT_SECRET`
- `FHIR_SCOPE`
- `APP_BASE_URL`
- `SESSION_SECRET`
- `NODE_ENV`
- `NEXT_PUBLIC_APP_NAME`

## Suggested folder structure

```text
docs/
  requirements/
    prd.md
    trd.md
    app-flow.md
    ui-ux-design-brief.md
    backend-schema.md
    implementation-plan.md

src/
  app/
    patients/
    patient/[id]/
    api/fhir/
  components/
    patient-list/
    patient-form/
    patient-details/
    vitals/
    conditions/
    medications/
    shared/
  lib/
    fhir/
    validation/
    charts/
    utils/
  types/
    fhir/
    app/
```

## Constraints

- Epic 1 must remain the first delivery priority
- The app should not try to become a full EPR in version one
- Neurorehab readiness remains the product direction, but should not be forced into the first implementation at the expense of the foundation
- The proxy layer is mandatory for secure FHIR access
- The patient details page must be clinically readable and support longitudinal review
- Synthetic neurorehabilitation datasets may be used later, but are not a blocker for Epic 1 implementation

## Done criteria

The TRD is satisfied when the implementation team can build Epic 1 without making foundational decisions ad hoc.

At minimum, the following should be explicit and stable:

- Frontend stack
- Backend proxy approach
- FHIR resource mapping
- Patient CRUD behavior
- Search behavior
- Patient details routing
- Vitals rendering approach
- Validation rules
- Environment variables
- Folder structure

The document should also leave a clear extension path into neurorehabilitation readiness and structured write-back without requiring a redesign of the Epic 1 foundation.
