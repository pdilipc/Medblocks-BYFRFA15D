# App Flow: Verada Neurorehab Readiness

## Purpose

This document maps the pages, navigation, and user journeys for Verada Neurorehab Readiness so the application behaves as one coherent clinician workflow. The target flow is intentionally narrow: review readiness, decide the session plan, deliver therapy, and record structured outcomes.

## Navigation model

The app should use a simple clinician-facing layout with a persistent top bar and a workflow step indicator. Navigation should be optimized for direct progression through the four core screens rather than open-ended browsing.

Primary navigation sequence:

1. Patient Selection
2. Readiness Dashboard
3. Session Planning
4. Post-Session Documentation

A patient context header should persist across the last three screens and show patient identity, pathway, and session date.

## Pages

### 1. Patient Selection

Purpose:
- Search for and select a patient from the FHIR server.
- Load basic demographics and current rehabilitation context.

Main elements:
- Search input
- Patient results table or list
- Quick demographic summary
- Select patient action

Primary actions:
- Search patient
- Select patient
- Continue to readiness dashboard

### 2. Readiness Dashboard

Purpose:
- Present a concise view of recent physiological observations and current clinical context before therapy begins.

Main elements:
- Recent observations panel
- Conditions summary
- CarePlan and ServiceRequest summary
- Optional trend strip for recent values
- Readiness notes area

Primary actions:
- Review context
- Mark concerns
- Continue to session planning
- Return to patient search

### 3. Session Planning

Purpose:
- Capture the clinician decision to proceed, modify, or defer the session.

Main elements:
- Decision selector
- Rationale field
- Suggested therapy pathway context
- Safety or escalation prompts

Primary actions:
- Proceed
- Modify
- Defer
- Save decision
- Continue to documentation

### 4. Post-Session Documentation

Purpose:
- Record therapy delivered, session outcome, and structured follow-up data.

Main elements:
- Procedure entry
- Observation entry
- QuestionnaireResponse prompts
- Follow-up communication notes
- Submit to FHIR action

Primary actions:
- Save draft
- Submit documentation
- Complete workflow

## Primary journey

### Journey 1: Standard daily session

1. Clinician searches for the patient.
2. Clinician selects the patient.
3. App loads readiness dashboard with recent observations and rehab context.
4. Clinician reviews the information and proceeds to session planning.
5. Clinician chooses proceed, modify, or defer and records rationale.
6. After therapy, clinician documents what was delivered and how the patient responded.
7. App writes structured outputs back to the FHIR server.

### Journey 2: Session deferred

1. Clinician selects the patient.
2. Readiness dashboard shows concerning physiological or contextual information.
3. Clinician chooses defer.
4. Clinician records rationale and escalation or follow-up details.
5. App writes the decision and related structured notes to the FHIR server.

## Entry points

- Default entry point: Patient Selection page.
- Optional direct entry point: deep link to a specific patient context in demo mode.

## Redirects

- After patient selection -> Readiness Dashboard.
- After saving session decision -> Post-Session Documentation.
- After successful submission -> Workflow completion state or return to Patient Selection.
- If patient context fails to load -> return to Patient Selection with error notice.

## Empty states

- No patient search results.
- No recent observations available.
- No active CarePlan or ServiceRequest.
- No prior session history.

Each empty state should explain what is missing and whether the clinician can still continue.

## Error states

- FHIR server unavailable.
- Patient search failed.
- Observation retrieval failed.
- Write-back submission failed.
- Validation error on required fields.

Each error state should present a clear recovery action such as retry, edit fields, or save locally for later submission.

## Loading states

- Patient search loading
- Patient context loading
- Documentation submission in progress

Loading indicators should be lightweight and never block the user without feedback.

## Design constraints

- The app should feel like one short clinical workflow, not a general-purpose health record UI.
- Each page should emphasize clarity and speed over dense information display.
- The total v1 flow should remain demonstrable within a short session.
