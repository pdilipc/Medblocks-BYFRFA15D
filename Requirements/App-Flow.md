# App Flow: Verada Neurorehab Readiness

## Purpose

This document maps the pages, navigation, user journeys, and screen states for Verada Neurorehab Readiness. The product vision remains neurorehabilitation readiness, but the first implementation scope is Epic 1: Patient Management and Patient Details Foundation.

The app flow should therefore begin with patient management and longitudinal patient review, then leave a clear extension path into later neurorehabilitation-specific workflows.

## Navigation model

The application should use a simple clinician-facing navigation model with a clear primary workflow.

### Primary navigation sequence for Epic 1

1. Patient List
2. Create/Edit Patient
3. Patient Details

### Later navigation extensions

4. Neurorehabilitation Readiness Review
5. Session Planning
6. Post-Session Documentation

For Epic 1, the core interaction pattern should prioritize fast patient lookup, clean patient creation and editing, and readable access to patient history and vitals.

## Pages

### 1. Patient List

**Route:** `/` or `/patients`

**Purpose:**
- Display all patients from the FHIR server
- Allow search by name
- Allow navigation to patient details
- Allow entry into patient creation
- Allow entry into patient editing

**Main elements:**
- Search input
- Patient table or list
- Create patient button
- Edit action on each row
- Clickable patient rows

**Displayed fields:**
- Full name
- Gender
- Date of birth

**Primary actions:**
- Search patients
- Open create patient form
- Open edit patient form
- Open patient details page

### 2. Create/Edit Patient

**Route:** modal, drawer, or dedicated page depending on implementation

**Purpose:**
- Create a new patient
- Edit an existing patient using the same validated form

**Main elements:**
- Given name input
- Family name input
- Gender select
- Date of birth input
- Validation messages
- Save and cancel actions

**Primary actions:**
- Submit patient form
- Cancel form
- Return to patient list after success

### 3. Patient Details

**Route:** `/patient/[id]`

**Purpose:**
- Display the patient’s demographics and medical history foundation
- Support longitudinal review of vital signs
- Show conditions and medications
- Prepare the clinician for later neurorehabilitation-oriented review

**Main elements:**
- Demographics header
- Vitals section
- Chart/table toggle
- Conditions table
- Medications table
- Back navigation to patient list

**Displayed demographics:**
- Full name
- Gender
- Date of birth

**Displayed clinical sections:**
- Vital signs
- Conditions
- Medications

### 4. Neurorehabilitation Readiness Review

**Route:** optional later route, for example `/patient/[id]/readiness`

**Purpose:**
- Build on the patient details foundation to support readiness interpretation in a neurorehabilitation context

**Main elements:**
- Readiness summary
- Relevant physiological context
- Rehabilitation context
- Decision support framing

### 5. Session Planning

**Purpose:**
- Capture proceed, modify, or defer decisions with rationale

### 6. Post-Session Documentation

**Purpose:**
- Record therapy delivered and structured outcomes
- Support write-back to FHIR

## Core user journeys

### Journey 1: Review an existing patient

1. Practitioner opens the Patient List page.
2. The app loads patients from the FHIR server.
3. Practitioner browses the list or searches by name.
4. Practitioner clicks a patient row.
5. The app navigates to `/patient/[id]`.
6. Practitioner reviews demographics, vital signs, conditions, and medications.

### Journey 2: Create a new patient

1. Practitioner opens the Patient List page.
2. Practitioner clicks Create Patient.
3. The patient form opens.
4. Practitioner enters given name, family name, gender, and date of birth.
5. Validation runs before submit.
6. The app sends the create request through the backend FHIR proxy.
7. On success, the patient list refreshes and shows the new patient.

### Journey 3: Edit an existing patient

1. Practitioner opens the Patient List page.
2. Practitioner clicks Edit on a patient row.
3. The patient form opens pre-filled with the patient’s data.
4. Practitioner updates the fields.
5. Validation runs before submit.
6. The app sends the update request through the backend FHIR proxy.
7. On success, the patient list refreshes with the updated values.

### Journey 4: Review longitudinal vital signs

1. Practitioner opens a patient details page.
2. The app loads demographics, observations, conditions, and medications.
3. Practitioner reviews vital signs in chart view.
4. Practitioner switches to table view if needed.
5. Practitioner uses this information as longitudinal clinical context.

### Journey 5: Later readiness workflow extension

1. Practitioner opens a patient details page.
2. Practitioner reviews the longitudinal clinical context.
3. Practitioner enters a later neurorehabilitation readiness workflow.
4. The app uses the patient context as the basis for readiness review and downstream documentation.

## Entry points

### Epic 1 entry points

- Default entry point: Patient List
- Secondary entry point: direct deep link to `/patient/[id]`

### Later entry points

- Deep link from patient details into readiness workflow
- Possible dashboard shortcut into recently reviewed patients

## Redirects

- After successful patient creation -> return to Patient List and refresh results
- After successful patient update -> return to Patient List and refresh results
- After clicking a patient row -> navigate to `/patient/[id]`
- After failed patient load -> stay on current screen and show error message
- After future readiness action -> continue to session planning or documentation flow

## Screen states

### Patient List states

#### Loading
- Initial patient list loading
- Search loading

#### Empty
- No patients found on initial load
- No search results for the entered name

#### Error
- Failed patient list fetch
- Failed search request

#### Success
- Patient list displayed
- Search results displayed

### Create/Edit Patient states

#### Default
- Empty form for create
- Pre-filled form for edit

#### Validation error
- Missing given name
- Missing family name
- Missing gender
- Invalid or future date of birth

#### Submission loading
- Save in progress

#### Submission success
- Patient created successfully
- Patient updated successfully

#### Submission error
- Failed create request
- Failed update request

### Patient Details states

#### Loading
- Patient demographics loading
- Vitals loading
- Conditions loading
- Medications loading

#### Empty
- No vitals available
- No conditions available
- No medications available

#### Error
- Failed patient details fetch
- Failed vitals fetch
- Failed conditions fetch
- Failed medications fetch

#### Populated
- Demographics displayed
- Vitals displayed
- Conditions displayed
- Medications displayed

## Vitals interaction flow

The vitals section should support two display modes:

### Chart view
- Default view for longitudinal interpretation
- Each vital sign shown as a separate time-series line chart
- Blood pressure shown as one chart with systolic and diastolic lines

### Table view
- Alternate view for direct inspection of raw readings
- Each row shows date, vital sign, value, and unit where available

### Toggle behavior
- A visible toggle sits above the vitals section
- Switching views should not trigger unnecessary full-page reloads
- The user should remain on the same patient details page

## Design constraints

- Epic 1 should feel like a coherent patient management and review workflow, not a generic admin panel
- Patient rows must be clearly clickable
- Create and edit should reuse the same patient form
- The patient details page should be the main clinical review surface in v1
- Vitals, conditions, and medications should be easy to scan quickly
- The app should preserve a clear extension path into neurorehabilitation readiness without forcing that complexity into the first implementation

## Summary flow map

```text
Patient List
  -> Search by name
  -> Create Patient
  -> Edit Patient
  -> Open Patient Details

Create/Edit Patient
  -> Validate fields
  -> Save through backend proxy
  -> Return to Patient List

Patient Details
  -> Review demographics
  -> Review vitals in chart or table view
  -> Review conditions
  -> Review medications
  -> Later extend into readiness workflow
```
