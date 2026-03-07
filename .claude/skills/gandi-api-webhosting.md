# Skill: Gandi Web Hosting API

## When to use
Use this skill when implementing web hosting management commands.
Full API reference: `docs/webhosting-api.md`

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
