# Skill: Gandi LiveDNS API

## When to use
Use this skill when working with DNS record management commands (`gandi dns`).
API endpoint reference: `skills/api-reference.md` (LiveDNS API section)
User docs reference: `skills/02-dns-records.md`, `skills/03-dnssec.md`

## Currently Implemented Commands
- `gandi dns list <domain>` — List DNS records (with --type, --name filters)
- `gandi dns get <domain> <name> <type>` — Get specific record
- `gandi dns create <domain> <name> <type> <values...>` — Create record
- `gandi dns update <domain> <name> <type>` — Update record (--value, --ttl)
- `gandi dns delete <domain> <name> <type>` — Delete record (with --force)
- `gandi dns export <domain>` — Export zone as text (Accept: text/plain)

## Key API Endpoints

### DNS Records
- `GET /v5/livedns/domains/{fqdn}/records` — List all records
- `GET /v5/livedns/domains/{fqdn}/records/{name}/{type}` — Get specific record
- `POST /v5/livedns/domains/{fqdn}/records` — Create record
- `PUT /v5/livedns/domains/{fqdn}/records/{name}/{type}` — Replace record
- `DELETE /v5/livedns/domains/{fqdn}/records/{name}/{type}` — Delete record
- `PUT /v5/livedns/domains/{fqdn}/records` — Replace all records
- `PUT /v5/livedns/domains/{fqdn}/records/{name}` — Replace records by name

### Record Object
```json
{
  "rrset_name": "@",
  "rrset_type": "A",
  "rrset_ttl": 10800,
  "rrset_values": ["203.0.113.1"]
}
```

### Not Yet Implemented (potential new commands)
- `GET /v5/livedns/domains` — List LiveDNS domains
- `GET /v5/livedns/domains/{fqdn}` — Get domain LiveDNS info
- Snapshots: `GET/POST /v5/livedns/domains/{fqdn}/snapshots` — Manage snapshots
- TSIG keys: `GET/POST /v5/livedns/axfr/tsig` — Manage TSIG keys for AXFR
- DNSSEC keys: `GET/POST /v5/livedns/domains/{fqdn}/keys` — Manage DNSSEC
- Nameservers: `GET /v5/livedns/domains/{fqdn}/nameservers` — List NS

### Supported Record Types
A, AAAA, ALIAS, CAA, CDS, CNAME, DNAME, DS, HTTPS, KEY, LOC, MX, NAPTR, NS, OPENPGPKEY, PTR, RP, SOA, SPF, SRV, SSHFP, SVCB, TLSA, TXT, WKS

## Business Rules & Constraints
- DNS record changes take **~3 hours** to propagate; full propagation up to **72 hours**
- **ALIAS + DNSSEC incompatibility**: ALIAS records on bare domain (@) will break DNSSEC — must warn users
- CNAME cannot coexist with other record types on the same name
- Automatic snapshots are created on every record modification (if enabled)
- Snapshots can be used to restore DNS to a previous state (backup/restore workflow)
- Zone export supports `Accept: text/plain` header for BIND-format zone file

## Workflow Tips
- `gandi dns create` should hint about propagation delay after successful creation
- When creating MX records, remind about SPF/TXT record for email deliverability
- When detecting ALIAS on @ with DNSSEC enabled, emit a warning
- Snapshot commands (`gandi dns snapshot list/create/restore`) would be valuable for backup/restore
- DNS import (reverse of export) could parse zone files and batch-create records
