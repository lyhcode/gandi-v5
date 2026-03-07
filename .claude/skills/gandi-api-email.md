# Skill: Gandi Email API

## When to use
Use this skill when working with email management commands (`gandi email`).
Full API reference: `docs/email-api.md` and `docs/mailbox-api.md`

## Currently Implemented Commands
- `gandi email forward list <domain>` — List email forwards
- `gandi email forward create <domain> <source> <destinations...>` — Create forward
- `gandi email forward delete <domain> <source>` — Delete forward
- `gandi email mailbox list <domain>` — List mailboxes
- `gandi email mailbox info <domain> <mailbox_id>` — Show mailbox details

## Key API Endpoints

### Email Forwards (email-api.md)
- `GET /v5/email/forwards/{domain}` — List forwards
- `POST /v5/email/forwards/{domain}` — Create forward
  - Body: `{"source": "user", "destinations": ["ext@example.com"]}`
- `GET /v5/email/forwards/{domain}/{source}` — Get forward details
- `PUT /v5/email/forwards/{domain}/{source}` — Update forward destinations
- `DELETE /v5/email/forwards/{domain}/{source}` — Delete forward

### Mailboxes (email-api.md)
- `GET /v5/email/mailboxes/{domain}` — List mailboxes
- `GET /v5/email/mailboxes/{domain}/{mailbox_id}` — Get mailbox info
- `PATCH /v5/email/mailboxes/{domain}/{mailbox_id}` — Update mailbox (aliases, password)
- `POST /v5/email/mailboxes/{domain}` — Create mailbox (requires slot)

### Not Yet Implemented (potential new commands)
- `PUT /v5/email/forwards/{domain}/{source}` — Update forward destinations
- `POST /v5/email/mailboxes/{domain}` — Create mailbox
- `PATCH /v5/email/mailboxes/{domain}/{mailbox_id}` — Update mailbox
- `DELETE /v5/email/mailboxes/{domain}/{mailbox_id}` — Delete mailbox
- `GET /v5/email/offers/{domain}` — List email offers
- `POST /v5/email/mailboxes/{domain}/{mailbox_id}/renew` — Renew mailbox
- `GET /v5/email/slots/{domain}` — List email slots

### Mailbox API (BETA) — docs/mailbox-api.md
Alternative newer API at `/v5/mailbox/`:
- `GET /v5/mailbox/domains` — List domains with email
- `GET /v5/mailbox/domains/{domain}/mailboxes` — List mailboxes
- `POST /v5/mailbox/domains/{domain}/mailboxes` — Create mailbox
- Forwards, products, quotas, slots management
