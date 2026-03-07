# Skill: Gandi Organization API

## When to use
Use this skill when working with organization commands (`gandi org`).
API endpoint reference: `skills/api-reference.md` (Organization API section)
User docs reference: `skills/11-organizations.md`

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

## Business Rules & Constraints
- **PAT (Personal Access Token)** is the only supported auth method; API Key is deprecated
- **PAT expiration**: Configurable from 7 days to 1 year
- **PAT permissions**: Granular per-product (domains, DNS, email, certificates, etc.)
- **Organization as sharing_id**: The org `id` is used as `sharing_id` to scope API requests
- **Teams**: Organizations can have teams with different permission sets
- **Permission categories**: Domain management, DNS management, email management, billing, certificates, hosting, organization admin

## Workflow Tips
- `gandi auth status` should show PAT expiration date and warn when nearing expiry
- `gandi org pat renew` would be valuable to avoid auth disruption
- When PAT lacks permission for an operation, surface a clear error suggesting which permission is needed
