# Skill: Gandi Billing API

## When to use
Use this skill when implementing billing-related commands.
Full API reference: `docs/billing-api.md`

## Currently Implemented Commands
None — billing commands not yet implemented.

## Key API Endpoints

### Billing Info
- `GET /v5/billing/info/{sharing_id}` — Get billing info for an organization
  - Response includes prepaid account balance, grid info

### Potential Commands
- `gandi billing info` — Show billing info (prepaid balance, etc.)

## Notes
- The billing API is limited — only one endpoint documented
- Requires `sharing_id` (organization ID) as path parameter
