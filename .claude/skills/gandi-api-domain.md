# Skill: Gandi Domain API

## When to use
Use this skill when working with domain management commands (`gandi domain`).
Full API reference: `docs/domain-api.md`

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
