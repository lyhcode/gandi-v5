# Skill: Gandi Organization API

## When to use
Use this skill when working with organization commands (`gandi org`).
Full API reference: `docs/organization-api.md`

## Currently Implemented Commands
- `gandi org list` — List organizations
- `gandi org info <org_id>` — Show organization details
- `gandi org whoami` — Show current user info

## Key API Endpoints

### Organizations
- `GET /v5/organization/organizations` — List organizations
  - Query params: `name`, `type`, `sort_by`, `per_page`, `page`
- `GET /v5/organization/organizations/{id}` — Get organization details

### User Info
- `GET /v5/organization/user-info` — Get current user info (whoami)

### Access Tokens (PAT)
- `GET /v5/organization/user-info/access-tokens` — List PATs
- `POST /v5/organization/user-info/access-tokens` — Create PAT
- `DELETE /v5/organization/user-info/access-tokens/{id}` — Delete PAT
- `PATCH /v5/organization/user-info/access-tokens/{id}` — Renew/update PAT

### Not Yet Implemented (potential new commands)
- `gandi org pat list` — List personal access tokens
- `gandi org pat create` — Create new PAT
- `gandi org pat delete` — Delete PAT
- `gandi org pat renew` — Renew PAT

### Organization Object Key Fields
- `id` — Organization UUID (used as sharing_id)
- `name` — Organization name
- `type` — individual, company, association, etc.
- `corporate_name` — Legal name
- `email` — Contact email
