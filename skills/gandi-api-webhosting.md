# Skill: Gandi Web Hosting API

## When to use
Use this skill when implementing web hosting management commands.
API endpoint reference: `skills/api-reference.md` (Web Hosting API section)
User docs reference: `skills/08-link-domain-to-website.md`

## Currently Implemented Commands
None — web hosting commands not yet implemented.

## Key API Endpoints

### Instances
- `GET /v5/web/hosting/instances` — List hosting instances
- `GET /v5/web/hosting/instances/{id}` — Get instance details
- `POST /v5/web/hosting/instances` — Create instance
- `PATCH /v5/web/hosting/instances/{id}` — Update instance
- `DELETE /v5/web/hosting/instances/{id}` — Delete instance

### Virtual Hosts
- `GET /v5/web/hosting/instances/{id}/vhosts` — List vhosts
- `POST /v5/web/hosting/instances/{id}/vhosts` — Create vhost
- `GET /v5/web/hosting/instances/{id}/vhosts/{fqdn}` — Get vhost
- `PATCH /v5/web/hosting/instances/{id}/vhosts/{fqdn}` — Update vhost
- `DELETE /v5/web/hosting/instances/{id}/vhosts/{fqdn}` — Delete vhost

### Potential Commands
```
gandi hosting list
gandi hosting info <id>
gandi hosting vhost list <id>
gandi hosting vhost create <id> <fqdn>
```

## Business Rules & Constraints
- `sharing_id` query param is **deprecated** for web hosting routes (since 2025-08-14)
- Instance status values: `active` (not `running`)
- The `deploy` attribute is removed; use `deployment` on vhost or `sftp` on instance
- Three methods to link domain to hosting: A record, CNAME record, or Gandi nameservers
- Actual base path is `/v5/simplehosting/` (not `/v5/web/hosting/`)
- Instance actions include restart; cache purge is per-vhost
