# Skill: Gandi Domain API

## When to use
Use this skill when working with domain management commands (`gandi domain`).
API endpoint reference: `skills/api-reference.md` (Domain API section)
User docs reference: `skills/01-domain-names.md`

## Currently Implemented Commands
- `gandi domain list` — List domains
- `gandi domain info <fqdn>` — Show domain details
- `gandi domain check <fqdn>` — Check domain availability

## Key API Endpoints

### List Domains
`GET /v5/domain/domains`
- Query params: `fqdn`, `tld`, `per_page`, `page`, `sort_by`, `sharing_id`
- Response: array of domain objects

### Get Domain Info
`GET /v5/domain/domains/{domain}`
- Response: domain object with `fqdn`, `status`, `dates`, `nameservers`, `owner`, `tags`, etc.

### Check Domain Availability
`GET /v5/domain/check`
- Query params: `name` (required), `processes[]`, `currency`, `period`, `sharing_id`
- Response: availability and pricing info

### Not Yet Implemented (potential new commands)
- `POST /v5/domain/domains` — Register a domain
- `PATCH /v5/domain/domains/{domain}` — Update domain (autorenew, tags, nameservers)
- `POST /v5/domain/domains/{domain}/contacts` — Change domain contacts
- `DELETE /v5/domain/domains/{domain}/tags/{tag}` — Remove a tag
- `GET /v5/domain/domains/{domain}/livedns` — Get LiveDNS status
- `POST /v5/domain/domains/{domain}/livedns` — Enable LiveDNS
- `GET /v5/domain/domains/{domain}/nameservers` — List nameservers
- `PUT /v5/domain/domains/{domain}/nameservers` — Update nameservers
- `POST /v5/domain/domains/{domain}/renew` — Renew domain
- `POST /v5/domain/domains/{domain}/restore` — Restore expired domain
- `POST /v5/domain/domains/{domain}/transfer` — Transfer domain
- `GET /v5/domain/tlds` — List available TLDs
- `GET /v5/domain/tlds/{name}` — Get TLD info

## Domain Object Key Fields
- `fqdn` — Fully qualified domain name
- `status` — clientHold, clientTransferProhibited, etc.
- `dates.created_at`, `dates.registry_ends_at`, `dates.updated_at`
- `nameservers` — array of NS hostnames
- `owner` — contact object
- `autorenew` — boolean
- `tags` — array of strings

## Business Rules & Constraints
- Nameserver changes take **12-24 hours** to propagate globally
- Domain transfer requires **EPP/auth code** from current registrar and domain must be **unlocked**
- Transfer lock must be disabled before initiating transfer out
- WHOIS privacy (anonymized contact) is available and can be toggled per domain
- Domain owner change is a separate workflow from contact updates (requires FOA email confirmation)
- Domains can be tagged for organization; tags are useful for filtering in `domain list`
- Glue records (host objects) are needed for vanity nameservers (e.g., ns1.yourdomain.com)

## Workflow Tips
- `gandi domain info` should show WHOIS privacy status and autorenew state
- When implementing `domain register`, support `--dry-run` via `Dry-Run: 1` header
- When implementing `domain transfer`, warn about unlock requirement and EPP code
