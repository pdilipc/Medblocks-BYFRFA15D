# Workflow

This project is built around a single clinical workflow: use recent physiological context to inform whether a patient should proceed with today’s neurorehabilitation session, then document the result in a structured and interoperable way. That focused workflow makes the application easier to build, demonstrate, and explain.

## Clinical Scenario

A patient is receiving neurorehabilitation at home or in a hybrid care pathway. Before the scheduled session begins, passive physiological monitoring provides recent signals that may help the clinician understand the patient’s condition that day. 

The clinician opens the app, reviews the patient’s current context and recent observations, checks the planned rehabilitation pathway, and makes a session decision. After the session, the clinician records what was delivered and how the patient responded.

## Workflow Steps

### 1. Select the patient

The clinician searches for and selects the patient from the FHIR server. The app loads demographics and active session context.
### 2. Review readiness context

The app displays recent physiological observations along with relevant conditions and the rehabilitation plan. This gives the clinician a concise view of the patient’s readiness before therapy begins.

### 3. Decide the session plan

Based on the available information, the clinician chooses whether to proceed, modify, or defer the session. The rationale for that decision can be captured in a structured way.
### 4. Deliver and document therapy

The therapy session is delivered according to the plan, and the clinician records treatment details and the patient response. Structured documentation is then written back to the FHIR server. 

## Demo Scope

For a short implementation cycle, the workflow should be demonstrated through four screens:

- Patient lookup.
- Daily readiness dashboard.
- Session planning.
- Post-session documentation. 

This scope is enough to show a complete and credible FHIR workflow without turning the app into a broad rehabilitation platform too early.
## Positioning

The app should be positioned as a neurorehabilitation readiness workflow, not as a generic RPM dashboard and not as a full AI prediction platform. Its value lies in connecting pre-session physiological context, rehabilitation planning, and structured outcome documentation in one interoperable pathway. 
