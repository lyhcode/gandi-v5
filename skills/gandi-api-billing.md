# Skill: Gandi Billing API

## When to use
Use this skill when implementing billing-related commands.
API endpoint reference: `skills/api-reference.md` (Billing API section)

## Currently Implemented Commands
None — billing commands not yet implemented.

## Key API Endpoints

### Billing Info
- `GET /v5/billing/info/{sharing_id}` — Get billing info for an organization
  - Response includes prepaid account balance, grid info

### Potential Commands
- `gandi billing info` — Show billing info (prepaid balance, etc.)

## Notes
- The billing API has limited endpoints: account info and product pricing
- `GET /v5/billing/info/{sharing_id}` requires organization ID as path parameter
- `GET /v5/billing/price/{type}` returns product catalog prices (currency, country, grid, duration)
- Prepaid balance of 0 can cause errors when renewing mailboxes — should warn user
- Dry-run (`Dry-Run: 1` header) on payment-triggering endpoints to preview cost before executing
