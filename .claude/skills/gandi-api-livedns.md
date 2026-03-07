# Skill: Gandi LiveDNS API

## When to use
Use this skill when working with DNS record management commands (`gandi dns`).
Full API reference: `docs/livedns-api.md`

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
A, AAAA, ALIAS, CAA, CDS, CNAME, DNAME, DS, LOC, MX, NAPTR, NS, OPENPGPKEY, PTR, RP, SPF, SRV, SSHFP, TLSA, TXT, WKS
