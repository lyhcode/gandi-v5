# Skill: Gandi Email API

## When to use
Use this skill when working with email management commands (`gandi email`).
API endpoint reference: `skills/api-reference.md` (Email API / Mailbox API sections)
User docs reference: `skills/09-email.md`

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

### Mailbox API (BETA) — `/v5/mailbox/`
Alternative newer API:
- `GET /v5/mailbox/domains` — List domains with email
- `GET /v5/mailbox/domains/{domain}/mailboxes` — List mailboxes
- `POST /v5/mailbox/domains/{domain}/mailboxes` — Create mailbox
- Forwards, products, quotas, slots management

## Business Rules & Constraints
- **Forward limits**: Max 1000 forwards per domain, max 100 creations/updates per week (HTTP 429 on exceed)
- **Mailbox lifecycle**: Expired mailboxes are permanently deleted after 60 days
- **Subdomain email not supported**: Cannot create mailbox for sub.domain.com
- **Password restrictions**: Avoid `@` and `!` in mailbox passwords — causes issues with mobile email apps
- **MX prerequisites**: Email requires proper MX and SPF records to be configured first
- **Gmail forwarding issue**: Gmail frequently marks forwarded email as spam
- **Forwards vs. Aliases vs. Dynamic aliases**:
  - **Forward**: Redirects to external email (cross-domain); consumes a forward slot
  - **Alias**: Additional address pointing to same mailbox (same domain); configured via mailbox PATCH
  - **Dynamic alias**: `user+anything@domain` works automatically with no configuration needed
- Mailbox offers: `standard_2023` (10GB), `premium_2023` (50GB)

## Workflow Tips
- `gandi email forward create` should warn about 100/week rate limit and Gmail spam issues
- `gandi email mailbox create` should verify MX records exist before creating
- When listing mailboxes, show `expires_at` and `autorenew` status prominently
- Consider implementing `gandi email alias` commands as wrappers around mailbox PATCH
