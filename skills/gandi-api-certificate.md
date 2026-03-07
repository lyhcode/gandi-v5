# Skill: Gandi Certificate API

## When to use
Use this skill when working with SSL certificate commands (`gandi cert`).
API endpoint reference: `skills/api-reference.md` (Certificate API section)
User docs reference: `skills/10-ssl-certificates.md`

## Currently Implemented Commands
- `gandi cert list` — List certificates
- `gandi cert info <cert_id>` — Show certificate details

## Key API Endpoints

### Certificates
- `GET /v5/certificate/issued-certs` — List certificates
  - Query params: `cn`, `status`, `sort_by`, `per_page`, `page`, `sharing_id`
- `GET /v5/certificate/issued-certs/{id}` — Get certificate details
- `POST /v5/certificate/issued-certs` — Create/order certificate
  - Body: `{"csr": "...", "package": "cert_std_1_0_0", "dcv_method": "dns"}`
- `PATCH /v5/certificate/issued-certs/{id}` — Update certificate
- `DELETE /v5/certificate/issued-certs/{id}` — Revoke certificate

### DCV (Domain Control Validation)
- `GET /v5/certificate/issued-certs/{id}/dcv` — Get DCV status

### Certificate Packages
- `GET /v5/certificate/packages` — List available packages
- `GET /v5/certificate/packages/{name}` — Get package info

### Not Yet Implemented (potential new commands)
- `POST /v5/certificate/issued-certs` — Order new certificate
- `PATCH /v5/certificate/issued-certs/{id}` — Reissue certificate
- `DELETE /v5/certificate/issued-certs/{id}` — Revoke certificate
- `GET /v5/certificate/issued-certs/{id}/dcv` — Check DCV status
- `GET /v5/certificate/packages` — List certificate packages

### Certificate Object Key Fields
- `id` — Certificate UUID
- `cn` — Common name
- `status` — pending, valid, revoked, expired
- `dates.created_at`, `dates.ends_at`
- `package` — Certificate package name
- `dcv_method` — dns, email, http, cname

## Business Rules & Constraints
- **Certificate types**: Standard (DV, single domain), Pro (DV, wildcard/multi-domain), Business (OV)
- **CSR generation**: Required for certificate creation; typical openssl command:
  ```
  openssl req -new -newkey rsa:2048 -nodes -keyout domain.key -out domain.csr
  ```
- **DCV methods**: DNS (add TXT record), Email (admin@domain), HTTP (file on server), CNAME
- **DNS DCV**: Easiest with CLI — can automate TXT record creation via `gandi dns create`
- Providers: Sectigo (default) and Digicert (added 2024)
- `apex_only` parameter available for certificates that only need bare domain coverage
- Tags can be attached to certificates for organization
- CSV export supported via `Accept: text/csv` header on list endpoint

## Workflow Tips
- `gandi cert create` could include CSR generation helper or accept key+domain to auto-generate
- After ordering, automate DCV by creating the required DNS TXT record via `gandi dns create`
- `gandi cert list` should highlight certificates nearing expiration
