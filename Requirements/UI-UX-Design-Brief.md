# UI/UX Design Brief: Verada Neurorehab Readiness

## Design intent

Verada Neurorehab Readiness should feel like a calm, clinically credible, and workflow-oriented application. The user experience should support efficient patient management and longitudinal patient review first, while leaving a clear path into later neurorehabilitation-specific readiness workflows.

The interface should not feel like a generic admin console or a full hospital EPR. It should feel focused, readable, and deliberately scoped for clinicians who need to move from patient discovery to meaningful patient review quickly.

## Design principles

- Clinical clarity over visual novelty
- Fast patient lookup and low-friction navigation
- Strong information hierarchy
- Readability under time pressure
- Longitudinal context before specialty action
- Consistent interaction patterns across list, form, and details views
- Minimal cognitive load
- Future-ready for neurorehabilitation-specific extensions

## Aesthetic direction

The visual tone should be:

- Clean
- Clinical
- Trustworthy
- Modern
- Lightweight
- Structured
- Calm

The application should feel more like a focused specialty clinical product than a broad enterprise dashboard. Use restraint in color, spacing, and interaction design.

## Visual system

### Color palette

Use a restrained clinical palette:

- Primary: deep blue or blue-teal
- Secondary: slate or muted blue-gray
- Success: muted green
- Warning: amber
- Error: soft red
- Background: white or very light gray
- Surface: slightly elevated white or cool gray cards
- Text primary: dark slate or near-black
- Text secondary: medium gray

### Color usage guidance

- Use color to support meaning, not decorate screens
- Reserve stronger accent colors for actions, status, and critical signals
- Do not rely on color alone to communicate state
- Use warning and error colors sparingly and consistently

### Typography

- Use a clean sans-serif font such as Inter
- Prioritize readability over personality
- Maintain a clear type scale for page title, section title, label, body text, and helper text
- Use medium-weight labels for data points and form fields
- Keep dense data readable without making the UI visually heavy

Suggested hierarchy:
- Page title
- Section heading
- Card heading
- Field label
- Body text
- Helper text

### Spacing and layout

- Use generous spacing between major sections
- Keep internal card spacing consistent
- Avoid overly dense tables and dashboards
- Align content cleanly to a grid
- Support comfortable scanning of clinical data

## Component style

### General style

- Rounded corners, but not soft consumer-style rounding
- Light borders
- Minimal shadow depth
- Card-based grouping for related information
- Consistent button and input sizing
- Clear hover and focus states

### Buttons

Use a clear hierarchy:
- Primary button for save, create, continue
- Secondary button for cancel, back, or alternate actions
- Tertiary or ghost button for low-emphasis actions

### Inputs

- Inputs should be clearly labeled
- Validation states must be easy to understand
- Errors should appear close to the field
- Required fields should be obvious without cluttering the form
- Date fields should reduce input ambiguity

### Tables

- Tables should be clean and highly readable
- Use consistent column alignment
- Keep row density comfortable
- Highlight clickable rows clearly
- Preserve strong contrast for headers and values

### Cards and panels

Use cards or panels for:
- Demographics summary
- Vitals section
- Conditions table
- Medications table

Cards should create structure without making the screen feel fragmented.

## Epic 1 screen design

### 1. Patient List

#### Purpose
Support fast patient discovery and entry into patient creation, editing, or detail review.

#### Layout
- Search input at the top
- Primary Create Patient action near the page header
- Patient table or list below
- Edit action within each row
- Entire row should be visually identifiable as clickable for patient details

#### Content
Each row should show:
- Full name
- Gender
- Date of birth

#### UX notes
- Search should be prominent and easy to use
- Loading, empty, and error states must be clearly visible
- The page should feel operational and fast, not analytical

### 2. Create/Edit Patient Form

#### Purpose
Allow patient creation and editing using a single reusable form pattern.

#### Layout
- Simple vertically stacked form
- Short, focused field group
- Clear primary action
- Clear cancel path

#### Fields
- Given name
- Family name
- Gender
- Date of birth

#### UX notes
- The same form should be reused for create and edit
- Edit mode should pre-fill all fields
- Validation messages should be concise and placed near the relevant field
- The form should feel quick to complete

### 3. Patient Details

#### Purpose
Provide the main clinical review surface for Epic 1.

#### Layout
Recommended section order:
1. Demographics header
2. Vital signs section
3. Conditions section
4. Medications section

#### Demographics header
Display:
- Full name
- Gender
- Date of birth

The demographics section should anchor the page and orient the clinician quickly.

#### Vitals section
- Place near the top because it is the most dynamic longitudinal context
- Include a clear toggle between chart view and table view
- In chart view, show separate time-series charts for each vital
- For blood pressure, show systolic and diastolic on the same chart
- Keep charts simple and legible, with minimal visual noise

#### Conditions section
- Display as a clean table
- Show condition name and onset date
- Make the section easy to scan quickly

#### Medications section
- Display as a clean table
- Show medication name and status
- Keep the display compact and readable

#### UX notes
- The page should support longitudinal review, not just raw record display
- The layout should help clinicians move from summary to detail naturally
- It should be obvious that this page is the foundation for later readiness review

## Charting guidance

### Chart design principles

- Prefer simple line charts for time-series data
- Avoid overly decorative chart styling
- Use consistent axes and labeling conventions
- Show units where helpful
- Make dates readable
- Use minimal color variations
- Ensure blood pressure chart distinguishes systolic and diastolic clearly

### Chart interaction

- Chart view should be the default for vital signs
- Table view should be available for exact reading inspection
- Switching between chart and table should be immediate and intuitive
- Do not overload charts with unnecessary controls in v1

## States and feedback

### Loading states

Support visible loading states for:
- Patient list
- Search results
- Patient details
- Vitals
- Conditions
- Medications
- Form submission

Loading indicators should be subtle but clearly visible.

### Empty states

Support useful empty states for:
- No patients found
- No search results
- No vital signs available
- No conditions recorded
- No medications recorded

Empty states should explain what is missing and avoid making the interface feel broken.

### Error states

Support clear error messaging for:
- Failed list load
- Failed search
- Failed patient create
- Failed patient update
- Failed patient details fetch
- Failed vitals fetch
- Failed conditions fetch
- Failed medications fetch

Error states should be actionable and written in plain language.

### Success states

Support clear confirmation for:
- Patient created successfully
- Patient updated successfully

Success messaging should be noticeable but not disruptive.

## Responsiveness

The application should be:

- Desktop-first
- Tablet-friendly
- Functional on smaller screens where necessary

Desktop and laptop layouts are the primary target for v1 because the main users are clinicians reviewing structured data. Responsive behavior should preserve readability and avoid collapsing important data into unusable layouts.

## Accessibility

The interface should support:

- Strong color contrast
- Clear keyboard focus states
- Keyboard-accessible controls
- Explicit labels for form fields
- Text that remains readable at practical zoom levels
- State communication that does not rely on color alone

Accessibility should be treated as a baseline requirement, especially for dense clinical screens.

## Out of scope for v1

- Full EPR-style navigation complexity
- Advanced dashboard analytics views
- Heavy motion or animation
- Consumer wellness visual language
- Deep customization or theming controls
- Overly dense multi-panel data layouts

## Future-ready extensions

The design system should leave room for later neurorehabilitation-specific features, including:

- readiness summaries
- session planning controls
- proceed/modify/defer actions
- post-session documentation
- additional longitudinal rehabilitation context

These future features should be able to sit naturally on top of the Epic 1 interface without a full redesign.
