# HAPI FHIR on Railway

This folder contains a Railway-deployable HAPI FHIR JPA server for FHIR R4, adapted from the HAPI FHIR JPA starter project and deployed from the `/hapi-fhir-railway` subdirectory of this monorepo. [page:1][web:806]

The deployment is live and publicly accessible, and has been verified using the FHIR metadata endpoint, Swagger UI, and synthetic patient searches against the live API. [web:806][web:815]

## Live endpoints

- Base FHIR URL: `https://medblocks-byfrfa15d-production.up.railway.app/fhir` [web:806]
- CapabilityStatement: `https://medblocks-byfrfa15d-production.up.railway.app/fhir/metadata?_format=json` [web:806]
- Swagger UI: `https://medblocks-byfrfa15d-production.up.railway.app/fhir/swagger-ui/` [web:806]

## What this service does

This service exposes a HAPI FHIR R4 server over REST and supports standard FHIR interactions such as metadata, read, search, create, update, patch, and delete for supported resources. The running server returns a valid `CapabilityStatement`, confirming that the live deployment is functioning as a FHIR endpoint. [web:613][web:806]

The server has been tested with Synthea-generated transaction bundles and is successfully ingesting synthetic patient data into the live environment. Uploaded patients are queryable through standard FHIR search endpoints such as `/Patient?_count=5&_format=json`. [web:815][web:806]

## Railway deployment

This project is deployed on Railway from the `/hapi-fhir-railway` subdirectory in a monorepo configuration. Railway monorepo deployments require the service root directory to be pointed at the deployable subfolder instead of the repository root. [web:387][web:386]

The service was exposed publicly by generating a Railway public domain. Once exposed, the application became reachable at the public Railway URL listed above. [web:597][web:598]

## Local development

This project follows the HAPI FHIR JPA starter pattern, which supports local development through Spring Boot, Jetty, Docker, and WAR-based deployment options. The upstream starter project documents local startup via `mvn spring-boot:run`, Docker, and PostgreSQL-backed configurations. [page:1]

Typical local HAPI access patterns are:
- Base URL: `http://localhost:8080/fhir`
- Metadata endpoint: `http://localhost:8080/fhir/metadata` [page:1]

## Synthetic data loading

Synthetic patient bundles were generated separately using Synthea and uploaded into the live Railway deployment. The upload workflow uses FHIR transaction bundles and posts them to the server base URL at `/fhir`. [web:768][web:770]

A key implementation detail is that shared Synthea reference bundles must be loaded before patient bundles:
- `hospitalInformation....json`
- `practitionerInformation....json` [web:741][web:768]

Without these shared resources, patient uploads can fail with unresolved conditional references such as:

```text
Practitioner?identifier=http://hl7.org/fhir/sid/us-npi|...
```

This is expected FHIR transaction behavior when a conditional reference resolves to no matching resource. [web:728][web:731]

After uploading the hospital and practitioner reference bundles, patient bundle uploads succeeded and patients became searchable from the live server. [web:768][web:815]

## Postman and API testing

The live server is currently accessible without bearer-token authentication. Requests can be made directly from Postman using **No Auth** unless authentication is added later. [web:831][web:806]

Useful test requests include:

### Metadata
```http
GET /fhir/metadata?_format=json
```

### List patients
```http
GET /fhir/Patient?_count=5&_format=json
```

### Search patient by family name
```http
GET /fhir/Patient?family=MB15_Pagac496&_format=json
```

### Read patient by ID
```http
GET /fhir/Patient/{id}?_format=json
```

Recommended headers:
```http
Accept: application/fhir+json
Content-Type: application/fhir+json
```

FHIR JSON APIs commonly use these headers for content negotiation. [web:788][page:1]

## Current status

The deployment is live, publicly queryable, and returning valid FHIR responses. The server has been verified using:
- `CapabilityStatement` retrieval from `/fhir/metadata?_format=json`
- Swagger UI access
- successful Synthea patient import
- successful live `Patient` search responses [web:613][web:806][web:815]

## Known limitations

This project inherits the HAPI FHIR JPA starter caveat that it does **not** include production-ready security by default. The upstream HAPI starter also notes that enterprise logging and some multi-instance concerns must be implemented separately for production use. [page:1]

At the time of writing:
- API access is public and unauthenticated. [web:831][web:806]
- Some browser-rendered HTML responses may behave differently from raw JSON responses, so `_format=json` is the most reliable verification method. [web:627][web:806]
- Database persistence and operational hardening should be documented further if this deployment is evolved beyond sandbox/demo use. [page:1]

## Upstream basis

This deployment is based on the HAPI FHIR JPA starter project, which is intended as a deployable implementation starter rather than the HAPI FHIR library source repository itself. [page:1]
