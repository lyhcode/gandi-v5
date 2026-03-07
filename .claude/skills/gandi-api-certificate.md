# Skill: Gandi Certificate API

## When to use
Use this skill when working with SSL certificate commands (`gandi cert`).
Full API reference: `docs/certificate-api.md`

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
