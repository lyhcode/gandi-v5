# Gandi API v5 Endpoint Reference

Source: https://api.gandi.net/docs/
Base URL: `https://api.gandi.net/v5`
Sandbox: `https://api.sandbox.gandi.net/v5`
Auth: Bearer PAT token | Rate limit: 1000 req/min | Content-Type: application/json
Last verified: 2026-02-13

## Domain API (`/domain`)

### Availability & TLDs
- GET /check — Check domain availability (name, processes[], currency, period)
- GET /tlds — List TLD extensions (page, per_page)
- GET /tlds/{name} — TLD details

### Domain CRUD
- GET /domains — List domains (fqdn, nameserver, page, per_page, resellee_id)
- POST /domains — Register domain (fqdn, owner, duration, mailbox_optin)
- GET /domains/{domain} — Domain details
- DELETE /domains/{domain} — Delete domain (restricted)
- GET /domains/{domain}/createstatus — Creation status

### Domain Settings
- PUT /domains/{domain}/authinfo — Reset auth code
- PATCH /domains/{domain}/autorenew — Edit autorenew (autorenew: bool)
- PATCH /domains/{domain}/status — Transfer lock (lock: bool)

### Contacts
- GET /domains/{domain}/contacts — List contacts
- PATCH /domains/{domain}/contacts — Update contacts
- PUT /domains/{domain}/contacts/owner — Change owner

### Change Owner (separate flow)
- POST /changeowner/{domain} — Initiate ownership change
- GET /changeowner/{domain} — Check followup status
- POST /changeowner/{domain}/foa — Resend FOA emails

### Trademark Claims
- GET /domains/{domain}/claims — Retrieve trademark info
- POST /domains/{domain}/claims — Accept claim

### Nameservers
- GET /domains/{domain}/nameservers — List nameservers
- PUT /domains/{domain}/nameservers — Update nameservers

### DNSSEC Keys
- GET /domains/{domain}/dnskeys — List DNSSEC keys
- POST /domains/{domain}/dnskeys — Create key
- PUT /domains/{domain}/dnskeys — Replace all keys
- DELETE /domains/{domain}/dnskeys/{id} — Delete key

### LiveDNS & DNSSEC
- GET /domains/{domain}/livedns — LiveDNS info
- POST /domains/{domain}/livedns — Enable LiveDNS
- GET /domains/{domain}/livedns/dnssec — DNSSEC status
- POST /domains/{domain}/livedns/dnssec — Activate DNSSEC
- DELETE /domains/{domain}/livedns/dnssec — Disable DNSSEC

### Glue Records (Hosts)
- GET /domains/{domain}/hosts — List glue records (page, per_page)
- POST /domains/{domain}/hosts — Create glue record
- GET /domains/{domain}/hosts/{name} — Glue record info
- PUT /domains/{domain}/hosts/{name} — Update glue record
- DELETE /domains/{domain}/hosts/{name} — Delete glue record

### Renewal & Restore
- GET /domains/{domain}/renew — Renewal info
- POST /domains/{domain}/renew — Renew domain (duration)
- GET /domains/{domain}/restore — Restore info
- POST /domains/{domain}/restore — Restore domain
- PATCH /domains/{domain}/reachability — Resend reachability email

### Tags
- GET /domains/{domain}/tags — List tags
- POST /domains/{domain}/tags — Add tag
- PUT /domains/{domain}/tags — Replace all tags
- PATCH /domains/{domain}/tags — Update tags
- DELETE /domains/{domain}/tags — Remove all tags

### Web Redirections
- GET /domains/{domain}/webredirs — List redirections (page, per_page)
- POST /domains/{domain}/webredirs — Create redirection (host, target, type)
- GET /domains/{domain}/webredirs/{host} — Redirection info
- PATCH /domains/{domain}/webredirs/{host} — Update redirection
- DELETE /domains/{domain}/webredirs/{host} — Delete redirection

### Transfer In
- POST /transferin — Transfer domain to Gandi (fqdn, authinfo, owner)
- GET /transferin/{domain} — Transfer status
- PUT /transferin/{domain} — Relaunch transfer
- PUT /transferin/{domain}/authinfo — Update authinfo
- POST /transferin/{domain}/available — Check transfer availability
- POST /transferin/{domain}/foa — Resend FOA emails

### Transfer Out
- POST /domains/{domain}/transferout — Accept/decline transfer out

---

## LiveDNS API (`/livedns`)

### Domains
- GET /domains — List LiveDNS domains (page, per_page)
- POST /domains — Add domain to LiveDNS (fqdn, zone)
- GET /domains/{fqdn} — Domain properties
- PATCH /domains/{fqdn} — Update properties (automatic_snapshots: bool)

### DNS Records
- GET /domains/{fqdn}/records — List all records
- POST /domains/{fqdn}/records — Create record (rrset_name, rrset_type, rrset_ttl, rrset_values[])
- PUT /domains/{fqdn}/records — Replace entire zone
- DELETE /domains/{fqdn}/records — Delete all records
- GET /domains/{fqdn}/records/{name} — Records by name
- POST /domains/{fqdn}/records/{name} — Create record by name
- PUT /domains/{fqdn}/records/{name} — Replace records by name
- DELETE /domains/{fqdn}/records/{name} — Delete records by name
- GET /domains/{fqdn}/records/{name}/{type} — Get specific record
- POST /domains/{fqdn}/records/{name}/{type} — Create specific record
- PUT /domains/{fqdn}/records/{name}/{type} — Replace specific record
- PATCH /domains/{fqdn}/records/{name}/{type} — Update specific record
- DELETE /domains/{fqdn}/records/{name}/{type} — Delete specific record

### Record types
A, AAAA, ALIAS, CAA, CDS, CNAME, DNAME, DS, HTTPS, KEY, LOC, MX, NAPTR, NS, OPENPGPKEY, PTR, RP, SOA, SPF, SRV, SSHFP, SVCB, TLSA, TXT, WKS

### Snapshots
- GET /domains/{fqdn}/snapshots — List snapshots
- POST /domains/{fqdn}/snapshots — Create snapshot
- GET /domains/{fqdn}/snapshots/{id} — Snapshot details (Accept: text/plain for zone file)
- PATCH /domains/{fqdn}/snapshots/{id} — Update snapshot
- DELETE /domains/{fqdn}/snapshots/{id} — Delete snapshot

### DNSSEC Keys
- GET /domains/{fqdn}/keys — List DNSSEC keys
- POST /domains/{fqdn}/keys — Create key
- GET /domains/{fqdn}/keys/{id} — Key info
- PATCH /domains/{fqdn}/keys/{id} — Undelete key
- DELETE /domains/{fqdn}/keys/{id} — Delete key

### Nameservers
- GET /domains/{fqdn}/nameservers — Domain nameservers
- GET /nameservers/{fqdn} — Generic (hashed) nameservers

### TSIG Keys
- GET /axfr/tsig — List TSIG keys
- POST /axfr/tsig — Create TSIG key
- GET /axfr/tsig/{id} — TSIG key info
- GET /axfr/tsig/{id}/config/{software} — TSIG config (bind|knot|nsd|powerdns)

### Zone Transfer Slaves
- GET /domains/{fqdn}/axfr/slaves — List slave IPs
- PUT /domains/{fqdn}/axfr/slaves/{ip} — Add slave IP
- DELETE /domains/{fqdn}/axfr/slaves/{ip} — Remove slave IP

### Domain TSIG Association
- GET /domains/{fqdn}/axfr/tsig — List associated TSIG keys
- PUT /domains/{fqdn}/axfr/tsig/{id} — Associate TSIG key
- DELETE /domains/{fqdn}/axfr/tsig/{id} — Remove TSIG association

### Record Types List
- GET /dns/rrtypes — List accepted record types

---

## Email API (`/email`)

### Forwards
- GET /forwards/{domain} — List forwards (source, destination, page, per_page, sort_by)
- POST /forwards/{domain} — Create forward (source, destinations[])
- PUT /forwards/{domain}/{source} — Update forward destinations
- DELETE /forwards/{domain}/{source} — Delete forward

### Mailboxes
- GET /mailboxes/{domain} — List mailboxes (login, mailbox_type, page, per_page, antispam)
- POST /mailboxes/{domain} — Create mailbox (login, mailbox_type, password, aliases[])
- GET /mailboxes/{domain}/{mailbox_id} — Mailbox details
- PATCH /mailboxes/{domain}/{mailbox_id} — Update mailbox (antispam, password, aliases[], mailbox_type)
- DELETE /mailboxes/{domain}/{mailbox_id} — Delete mailbox
- DELETE /mailboxes/{domain}/{mailbox_id}/contents — Purge mailbox contents

### Renewal
- POST /mailboxes/{domain}/renew — Renew all mailboxes (duration: 1|12)
- POST /mailboxes/{domain}/{email}/renew — Renew single mailbox

### Migration
- GET /migration/{domain} — Migration details
- POST /migration/{domain} — Launch migration (source, destination, email_list[])

### Offers & Slots
- GET /offers/{domain} — Current email offer
- PATCH /offers/{domain} — Update email options
- GET /slots/{domain} — List slots (page, per_page, display_not_expired_and_inactive)
- POST /slots/{domain} — Create slot
- GET /slots/{domain}/{slot_id} — Slot details
- DELETE /slots/{domain}/{slot_id} — Refund slot

---

## Mailbox API BETA (`/mailbox`)

### Domains
- GET /domains — List domains
- GET /domains/{domain} — Domain detail
- POST /domains/{domain}/validate — Validate domain config

### Forwards
- GET /forwards — List forwards
- POST /forwards — Create forward (source, destinations[])
- PUT /forwards/{source} — Update forward
- DELETE /forwards/{source} — Delete forward

### Mailboxes
- GET /mailboxes — List mailboxes
- POST /mailboxes — Create mailbox (login, mailbox_type, password)
- GET /mailboxes/{email} — Mailbox detail
- PATCH /mailboxes/{email} — Update mailbox
- DELETE /mailboxes/{email} — Delete mailbox
- POST /mailboxes/{email}/renew — Renew mailbox

### Products & Slots
- GET /products — List buyable products
- POST /products — Buy mailbox product
- GET /quotas — Mailbox quotas
- GET /slots — List slots
- GET /slots/{slot_id} — Slot detail

---

## Certificate API (`/certificate`)

### Certificates
- GET /issued-certs — List certs (cn, status, page, per_page, sort_by; Accept: text/csv)
- POST /issued-certs — Order cert (csr, package, dcv_method, alt_names[], apex_only)
- GET /issued-certs/{id} — Cert details
- POST /issued-certs/{id} — Renew cert
- PATCH /issued-certs/{id} — Reissue cert
- DELETE /issued-certs/{id} — Revoke cert
- GET /issued-certs/{id}/crt — Download PEM

### DCV (Domain Control Validation)
- POST /dcv_params — Get DCV params (fqdns[])
- POST /issued-certs/{id}/dcv_params — Cert-specific DCV params
- PUT /issued-certs/{id}/dcv — Resend DCV
- PATCH /issued-certs/{id}/dcv — Update DCV method

### Tags
- GET /issued-certs/{id}/tags — List tags
- POST /issued-certs/{id}/tags — Add tag
- PUT /issued-certs/{id}/tags — Replace tags
- PATCH /issued-certs/{id}/tags — Update tags
- DELETE /issued-certs/{id}/tags — Remove tags

### Packages & Intermediates
- GET /packages — List packages
- GET /packages/{name} — Package info
- GET /pem/{type} — Intermediate cert
- GET /pem/-/{filename} — Specific intermediate cert

---

## Organization API (`/organization`)

### User Info
- GET /user-info — Current user info (whoami)

### Access Tokens (PAT)
- POST /access-tokens — Renew current PAT

### Organizations
- GET /organizations — List organizations (page, per_page)
- POST /organizations — Create organization (name)
- GET /organizations/{id} — Organization details (orgname, type, vat_number, corporate)
- PATCH /organizations/{id} — Update organization
- DELETE /organizations/{id} — Delete organization
- POST /organizations/{id}/action — Organization action (release_resellee)

### Customers
- GET /organizations/{id}/customers — List customers (page, per_page)
- POST /organizations/{id}/customers — Create customer
- GET /organizations/{id}/customers/{cid} — Customer info
- PATCH /organizations/{id}/customers/{cid} — Update customer
- DELETE /organizations/{id}/customers/{cid} — Delete customer

---

## Billing API (`/billing`)

- GET /info — Account info
- GET /info/{sharing_id} — Organization billing info (prepaid balance)
- GET /price/{type} — Product catalog prices (currency, country, grid, duration)

---

## Comment API (`/comment`)

- GET /comments/{id} — Get comment
- POST /comments/{id} — Set comment (content)
- DELETE /comments/{id} — Delete comment

---

## Web Hosting API (`/simplehosting`)

### Applications
- GET /applications — List applications
- GET /applications/{name} — Application details

### Instances
- GET /instances — List instances
- POST /instances — Create instance (vhost_name, type, duration)
- GET /instances/{id} — Instance details
- PATCH /instances/{id} — Modify instance
- DELETE /instances/{id} — Delete instance
- POST /instances/{id}/action — Instance action
- GET /instances/{id}/usage — Disk usage

### Virtual Hosts
- GET /instances/{id}/vhosts — List vhosts
- POST /instances/{id}/vhosts — Create vhost (name, ssl)
- GET /instances/{id}/vhosts/{fqdn} — Vhost details
- PATCH /instances/{id}/vhosts/{fqdn} — Update vhost
- DELETE /instances/{id}/vhosts/{fqdn} — Delete vhost
- DELETE /instances/{id}/vhosts/{fqdn}/cache — Purge cache

---

## Linked Zone API (`/linkedzone`)

### Domains
- GET /domains — List domains (page, per_page)
- GET /domains/{domain} — Domain details

### Tasks
- GET /tasks — List tasks (page, per_page)
- GET /tasks/{task_id} — Task details

### Zones
- GET /zones — List zones (page, per_page)
- POST /zones — Create zone (name, domains[], slaves_ips[])
- GET /zones/{zone_id} — Zone details
- POST /zones/{zone_id} — Deploy/undeploy zone (action)
- PATCH /zones/{zone_id} — Update zone
- DELETE /zones/{zone_id} — Delete zone
- PATCH /zones/{zone_id}/link/domains — Link domains to zone
- PATCH /unlink/domains — Unlink domains from zone

---

## Template API (`/template`)

### Dispatch
- GET /dispatch/{id} — Dispatch info

### Templates
- GET /templates — List templates (page, per_page)
- POST /templates — Create template (name, items[])
- GET /templates/{id} — Template details
- PATCH /templates/{id} — Edit template
- DELETE /templates/{id} — Delete template
- POST /templates/{id} — Apply template (domains[])

---

## GandiCloud VPS API

Uses unmodified OpenStack Victoria API. Not a Gandi-specific REST API.
See: https://docs.openstack.org/api-quick-start/

---

## General Notes

- Auth: `Authorization: Bearer <PAT>` header
- `sharing_id` query param filters by organization (GET) or selects payer (POST/PATCH/PUT)
- Pagination: `page` + `per_page` params, `total-count` response header
- Dry-run: `Dry-Run: 1` header on POST to simulate without executing
- CSV export: `Accept: text/csv` header on supported list endpoints
- Error response: `{"cause": "", "code": 0, "message": "", "object": ""}`

## Statistics
- Total endpoints: ~208
- Domain API: 57 | LiveDNS: 36 | Email: 18 | Mailbox BETA: 15
- Certificate: 21 | Organization: 12 | Billing: 3 | Comment: 3
- Web Hosting: 18 | Linked Zone: 15 | Template: 7
