# Technical Requirements Document: Verada Neurorehab Readiness

## Purpose

This Technical Requirements Document translates the product intent for Verada Neurorehab Readiness into concrete implementation choices so that engineering work remains coherent across the repository. The vibecoding guidance explicitly recommends a TRD to lock in framework, backend, database, APIs, environment variables, and constraints before code generation begins. [file:38]

The repo materials define the application as a lightweight clinician-facing workflow layered on top of a FHIR server, with a synthetic data generation layer kept separate from the main application workflow. The technical stack below is therefore optimized for rapid implementation, clean interoperability, and a credible challenge-ready demo rather than a production-scale clinical platform. [file:43][file:39]

## System scope

The system must support four core functions in the first version: patient selection, daily readiness review, session planning, and post-session documentation. It must read relevant FHIR resources from a target server and write structured documentation back after the clinician completes the session workflow. [file:39][file:40][file:42]

The technical design must also support synthetic cohort generation using a custom Synthea GMF module. That synthetic data layer is a testing and demonstration dependency, not the application runtime itself, and should remain operationally separated from clinician-facing UI logic. [file:43][file:41][file:45]

## Recommended stack

### Frontend

- Next.js 14 with TypeScript and App Router.
- Tailwind CSS for fast UI implementation and consistent styling.
- A component library such as shadcn/ui for cards, tables, dialogs, forms, and tabs.
- React Query or TanStack Query for FHIR data fetching, cache management, and mutation handling.
- Zod for runtime validation of form payloads and environment configuration.

This frontend choice aligns with the need for a compact, implementation-friendly clinician workflow with four primary screens and room for future expansion. The vibecoding guidance specifically asks that the TRD decide the frontend stack upfront rather than leaving it to agent guesswork. [file:38][file:39][file:40]

### Backend

- Next.js server components plus route handlers for server-side FHIR proxying and write-back actions.
- Lightweight service layer for FHIR resource retrieval, search composition, write-back mapping, and validation.
- Optional background scripts for fixture loading, synthetic bundle ingestion, and demo environment seeding.

This keeps the initial architecture compact, consistent with the repo’s emphasis on a focused workflow application rather than a heavily separated microservice architecture. The app is explicitly described as a lightweight layer on top of a FHIR server. [file:43][file:39]

### Database

- No primary clinical database in v1 for the core patient record; the FHIR server remains the system of record.
- Optional local application database using PostgreSQL for non-clinical app metadata only, such as clinician preferences, audit helper tables, cached demo mappings, or saved UI configuration.
- Prisma may be used only if a local relational store becomes necessary for non-FHIR application state.

This follows the repo’s architectural position that patient context, observations, conditions, care plans, and session outcomes are stored and served through the FHIR server. [file:43][file:39]

### Authentication

- Initial demo mode: simple protected local access without full enterprise auth, if the target environment is a sandbox or challenge deployment.
- Preferred production-oriented path: SMART-on-FHIR compatible OAuth2/OIDC or a thin clinician auth layer integrated with the hosting environment.
- Session management via secure HTTP-only cookies if custom auth is added.

The current repo materials do not define a concrete auth mechanism, so the technical requirement is to avoid overengineering authentication in the first version while leaving a clean upgrade path to standards-based healthcare authentication. This is consistent with the repo’s challenge-focused scope and compact implementation philosophy. [file:38][file:39][file:43]

### Hosting

- Frontend and server routes: Vercel or a similar Node-compatible deployment platform for rapid iteration.
- FHIR server: external sandbox or local development instance.
- Synthetic generation environment: local Synthea runtime or containerized script execution environment.
- Optional object storage for example bundles, seed files, and exported demo artifacts.

### Third-party systems and dependencies

- FHIR server endpoint as the primary interoperability dependency. [file:43][file:42]
- Synthea with support for custom GMF modules for synthetic cohort generation. [file:39][file:45]
- Optional charting library for lightweight trend displays if a recent-history panel is added. [file:43]
- SNOMED-CT and LOINC coding support through resource content and terminology mapping already reflected in the synthetic module. [file:44][file:45]

## Application modules

The frontend should be organized into a small number of workflow-aligned modules:

- `patient-search`: FHIR patient lookup and selection.
- `readiness-dashboard`: recent observations, condition summary, care plan context, and service request context.
- `session-planning`: proceed/modify/defer decision capture with rationale.
- `documentation`: post-session recording using `Procedure`, `Observation`, and `QuestionnaireResponse` payloads.
- `history-trends`: optional recent observation history or recent activity strip.

These modules map directly to the suggested frontend modules in the architecture document and the minimum demo scope in the README and workflow docs. [file:43][file:39][file:40]

## FHIR integration requirements

### Read operations

The application must support retrieval of:

- `Patient` for demographic identity and selection context. [file:42]
- `Encounter` for active or recent session context. [file:42]
- `Condition`, `CarePlan`, and `ServiceRequest` for rehabilitation and baseline planning context. [file:42]
- `Device` and `Observation` for recent physiological and therapy-related measurements. [file:42]

### Write operations

The application must support creation or update flows for:

- `Observation` for readiness-related capture and outcome logging. [file:42]
- `QuestionnaireResponse` for structured readiness, tolerance, or clinician-entered rationale. [file:42]
- `Procedure` for therapy delivered. [file:42]
- `Communication` or selective `CarePlan` updates where follow-up or escalation needs to be represented. [file:42]

### FHIR handling approach

- Use typed wrappers around FHIR JSON payloads.
- Normalize search parameters in a single service layer.
- Centralize terminology constants and resource construction helpers.
- Validate outbound resources before submission.
- Keep the resource footprint intentionally compact to avoid over-modeling the rehabilitation domain in v1. [file:42]

## Synthetic data requirements

The current synthetic module includes example exact values such as heart rate 76 bpm, sleep efficiency 81%, imagery accuracy 87%, ARAT 34, and FMA-UE outcome 51. Those values are useful as illustrative defaults, but the attached synthetic data strategy explicitly says exact values may be replaced with distributions, randomized variation, or expert-calibrated rules in future iterations. [file:44][file:41][file:45]

Accordingly, the technical requirement for the next iteration is that physiological and outcome-oriented synthetic data should not be treated as strictly deterministic. Instead, generation should support realistic variability using bounded probability distributions, clinically sensible ranges, cohort stratification, and optional longitudinal correlation across repeated observations. [file:41][file:44]

### Synthetic variability design

- Heart rate, sleep efficiency, respiration-related measures, fatigue indicators, and selected assessment scores should be generated around clinically plausible central tendencies rather than fixed constants. [file:39][file:41]
- Use configurable distributions such as truncated normal, beta, log-normal, or mixture distributions depending on the variable type and boundedness. [file:41]
- Respect hard physiological bounds and pathway-specific constraints so generated values remain believable.
- Allow subgroup variation by severity, care pathway, device track, age band, or recovery phase.
- Support longitudinal drift so repeated observations for the same synthetic patient show continuity rather than independent random jumps.
- Preserve branch probabilities, such as the recoveriX versus SynPhNe routing split, while allowing those probabilities to become conditional on baseline severity or generated assessments over time. [file:44][file:45]

### Example implementation rule

For example, overnight resting heart rate should not always equal 76 bpm for every synthetic patient. Instead, it should be sampled from a clinically plausible bounded distribution with patient-level baseline anchoring and day-level variation. Sleep efficiency should similarly vary within realistic limits rather than being fixed at 81 percent across the cohort. The same principle should apply to FMA-UE, ARAT, and imagery-accuracy observations, which should reflect scenario-specific distributions instead of single hard-coded outputs. [file:44][file:45][file:41]

### Separation of concerns

The synthetic generation runtime should remain separate from the clinician-facing application. Generated bundles should be exported, reviewed, and loaded into the FHIR server used by the app, rather than generated ad hoc inside the main UI runtime. This follows the architecture guidance that the synthetic data layer is a dedicated component distinct from the clinician workflow layer. [file:43][file:39]

## API and service design

### Internal routes

Suggested internal route groups:

- `/api/fhir/patients/search`
- `/api/fhir/patient/[id]/context`
- `/api/fhir/patient/[id]/observations`
- `/api/fhir/patient/[id]/plan`
- `/api/fhir/session/decision`
- `/api/fhir/session/documentation`
- `/api/synthetic/import` for local admin use only

These routes can proxy to the FHIR server, simplify client logic, and provide a place to enforce validation, mapping, logging, and eventual auth controls.

### Validation

- Zod schemas for request payloads and environment variables.
- FHIR resource shape validation for outbound resource construction.
- Guardrails for required identifiers, encounter references, coding systems, and unit consistency.

## Folder structure

A recommended repository layout is:

```text
src/
  app/
    patients/
    dashboard/
    planning/
    documentation/
    api/
  components/
    patient-search/
    readiness/
    planning/
    documentation/
    shared/
  lib/
    fhir/
    validation/
    terminology/
    synthetic/
  types/
    fhir/
    app/
docs/
  architecture.md
  workflow.md
  fhir-resources.md
  synthetic-data.md
  prd.md
  trd.md
data/
  synthetic/
public/
examples/
```

This structure is compatible with the repository layout described in the README while adding clearer separation for UI modules, FHIR logic, validation, and synthetic utilities. [file:39]

## Environment variables

Suggested environment variables:

- `FHIR_BASE_URL`
- `FHIR_AUTH_TYPE`
- `FHIR_CLIENT_ID`
- `FHIR_CLIENT_SECRET`
- `FHIR_SCOPE`
- `APP_BASE_URL`
- `SESSION_SECRET`
- `NODE_ENV`
- `SYNTHETIC_IMPORT_ENABLED`
- `SYNTHETIC_BUNDLE_PATH`
- `NEXT_PUBLIC_APP_NAME`

These align with the vibecoding requirement that a TRD should explicitly list environment variables and technical constraints rather than leaving them implicit. [file:38]

## Key libraries

- `next`
- `react`
- `typescript`
- `tailwindcss`
- `@tanstack/react-query`
- `zod`
- `fhir/r4` or equivalent FHIR typings/utilities
- `date-fns`
- `clsx`
- optional `prisma` and `@prisma/client` if local metadata persistence is introduced

## Constraints

- The first version must remain limited to a coherent four-screen workflow. [file:39][file:40]
- The app should not attempt to replace the FHIR server or act as a full EPR. [file:43]
- The clinical intelligence layer should remain lightweight in the first version. [file:39][file:43]
- The synthetic module must be clearly positioned as a development and demonstration asset, not a clinical recommendation engine. [file:41][file:43]
- Synthetic physiological and assessment values should move away from deterministic constants and toward realistic distributions and patient-level variation. [file:41][file:44][file:45]
- The implementation should privilege interoperability, clarity, and demo reliability over broad feature scope. [file:43][file:39]

## Done criteria

The TRD is satisfied when the implementation team can build the app without making foundational stack decisions ad hoc. In particular, the frontend, backend pattern, FHIR integration approach, environment variables, module structure, and synthetic-data variability rules should all be explicit enough that an AI coding agent or developer can use this as the technical source of truth. [file:38][file:39][file:43]
