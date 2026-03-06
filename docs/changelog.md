# Changelog

Gandi's Public API Changelog

## 2026-02-13
- **LiveDNS API** - Change the description: GET /v5/livedns/domains.

## 2026-01-28
- **Domain API** - Can not update the owner's contact informations of a domain: PATCH /v5/domain/domains/{domain}/contacts.

## 2026-01-19
- **Email API** - Add a querystring parameter to only select inactive slots with an expiration date which has not been passed: GET /v5/email/slots/{email}.

## 2026-01-05
- **Linked Zone API** - Replace the limit and offset parameters by the per_page and page parameters to paginate the responses: GET /v5/linkedzone/domains, GET /v5/linkedzone/tasks, GET /v5/linkedzone/zones.

## 2025-09-15
- **Certificate API** - Certificate list in CSV format with "Accept" header.

## 2025-09-04
- **Organization API** - Add a method to renew Personal Access Tokens. See Renew PAT API.

## 2025-08-14
- The sharing_id query string parameters is now deprecated for web hosting routes.

## 2025-07-28
- **Email API** - Email API is now available in sandbox environment.

## 2025-07-22
- **Linked Zone API** - Add domains in response of: GET /v5/linkedzone/zones and GET /v5/linkedzone/zones/{zone_id}.

## 2025-06-05
- **Mailbox API** - Change the HTTP status to 429 when a limit number of modified forwards per week occurred.

## 2025-05-19
- **Linked Zone API**:
  - Add the list domains endpoint: GET /v5/linkedzone/domains.
  - Add the domain details endpoint: GET /v5/linkedzone/domains/{domain}.
  - Add the list tasks endpoint: GET /v5/linkedzone/tasks.
  - Add the task details endpoint: GET /v5/linkedzone/tasks/{task_id}.
  - Add the detach domains from their linked zone endpoint: PATCH /v5/linkedzone/unlink/domains.
  - Add the list zones endpoint: GET /v5/linkedzone/zones.
  - Add the create a zone endpoint: POST /v5/linkedzone/zones.
  - Add the zone details endpoint: GET /v5/linkedzone/zones/{zone_id}.
  - Add the deploy or deactivate a zone endpoint: POST /v5/linkedzone/zones/{zone_id}.
  - Add the update a zone endpoint: PATCH /v5/linkedzone/zones/{zone_id}.
  - Add the delete a zone endpoint: DELETE /v5/linkedzone/zones/{zone_id}.
  - Add the link domains to a specific zone endpoint: PATCH /v5/linkedzone/zones/{zone_id}/link/domains.

## 2025-04-10
- **Certificate API** - dns_records field added in /dcv_params response body route.

## 2025-03-20
- **LiveDNS API** - Add the verb PATCH for /v5/livedns/domains/{domain}/records/{rrset_name}/{rrset_type}.
- **Domain API** - Add GET, POST, DELETE verbs for the route /v5/domains/{domain}/livedns/dnssec.

## 2025-03-12
- **Domain API** - Add the parameter mailbox_optin to the request for POST /v5/domain/domains and POST /v5/domain/transferin.

## 2025-03-04
- **Web Hosting API** - The deprecated deploy attribute on the instance route has been removed. Use the deployment attribute on the vhost route or the sftp attribute on the instance route instead.

## 2025-02-12
- **Certificate API** - Add parameter apex_only for create certificate route.

## 2025-02-06
- **Mailbox API** - Add warning to create forwards.

## 2025-01-20
- Add new Mailbox API.

## 2024-08-31
- **Certificate API** - Add new certificates provider Digicert.

## 2024-07-26
- Update Authentication documentation about PATs and deprecated API keys.

## 2024-07-23
- **Web Hosting API** - Deprecate access_information.deploy field on Web Hosting instance detail route. Add access_information.sftp field on instance detail route and deployment field on vhost detail route.

## 2024-04-24
- **Domain API** - Allow owner update on given and family for company: PUT /v5/domain/domains/{domain}/contacts/owner, PATCH /v5/domain/domains/{domain}/contacts.

## 2024-04-11
- **Domain API** - Add parameter icann_contract_accept needed to update the owner email route.

## 2024-02-02
- **Email API** - When renewing a mailbox an error occurs if the organization has a prepaid with 0 and no other way to pay.

## 2024-02-01
- **Web Hosting API** - Remove all references to the subscription_ended attribute.
- **Email API** - Added an example to document how to send a sharing_id when renewing a mailbox.

## 2024-01-15
- **Certificate API** - Added resellee_id option to create certificate for third parties instead of the owner organization.
- **LiveDNS API** - Added missing sort_by option on snapshot route. Added text/plain output (via Accept header) on snapshots details.

## 2024-01-02
- **Domain API** - Added /{domain}/transferout route that validates transfer out request (POST).

## 2023-12-14
- **Certificate API** - Add sort_by on certificate list route.

## 2023-11-28
- **Organization API** - Add new fields orgname, type, vat_number and corporate in the response of Show organization information route.

## 2023-10-16
- **Web Hosting API** - Add usage route on instances. Allows to get disk usage of the instance.

## 2023-10-10
- **Email API** - Add information about autorenew status on mailbox listing route and mailbox detail route. You can now activate and deactivate autorenew on mailbox detail PATCH route. You can now activate autorenew when you buy a slot route.

## 2023-10-02
- **Web Hosting API** - Fix the status value of an active Web Hosting instance. The status of an active instance is active and no longer running.

## 2023-09-29
- **Certificate API** - We now manage intermediate certificates on a per-certificate basis. The "intermediate" href of the certificate will change depending on the actual issuer, pointing to a new route: /pem/-/{Intermediate.pem}.

## 2023-09-21
- **Email API** - Add field mailbox_type on PATCH route. This new field allows you to change your offer.

## 2023-09-20
- **Certificate API** - Intermediate certificates can be downloaded directly with Accept header.

## 2023-09-11
- **Certificate API** - New intermediate certificates available in /certificate/pem/{type} route.

## 2023-08-31
- **Authentication** - The Authorization header supports Bearer tokens. Personal Access Tokens are now the preferred authentication mechanism. The API Key is deprecated.

## 2023-08-28
- **Email API** - Add field to_convert for /mailboxes/{domain}/ route.

## 2023-08-07
- **Email API** - Add field expires_at for /mailboxes/{domain}/ route and /mailboxes/{domain}/{mailbox_id} route.

## 2023-07-27
- **Email API** - Added /mailboxes/{domain}/renew route (POST). Added /mailboxes/{domain}/{email}/renew route (POST). These routes can also be used to convert mailboxes from free to charged.

## 2023-07-21
- **Email API** - New offers available: standard_2023 (standard 10GB) and premium_2023 (premium 50GB).

## 2023-07-12
- **Certificate API** - altnames field added in /dcv_params response body.

## 2023-05-11
- **Domain API** - Added information about the status field in the /domain/check api.

## 2023-05-26
- **Email API** - Add missing total-count header on /slots/{fqdn} (GET).

## 2023-03-22
- **Certificate API** - Tag management added: tags property added to "issued-certs" routes (GET), /certificate/issued-cert/{id}/tags route added.

## 2023-03-09
- **Domain API** - Added reachability in domain details returned information GET /v5/domain/domains/{domain}.

## 2023-03-07
- **Email API** - Fix routes for email migration API.

## 2023-03-06
- **Domain API** - Add missing total-count header on /domain/{fqdn}/webredirs.

## 2023-02-21
- **Email API** - Add methods to migrate mailboxes.

## 2023-02-17
- Added Content-Type header notes for POST/PUT/PATCH requests.

## 2023-02-16
- **Organization API** - Add an api /organization/{id}/action for non CRUD operations. Currently, the only action is release_resellee.

## 2023-02-03
- **Domain API** - Add paging on /tlds.

## 2023-01-04
- **Domain API** - Added the claims route that allows the creation of some domains protected by trademark claims.

## 2022-11-10
- **Domain API** - Added the domain deletion (restricted feature).
- **Simplehosting API** - Added the possibility to register a free domain during Web Hosting creation.

## 2022-10-12
- **Domain API** - Added the domain creation status route.

## 2022-10-04
- **Email API** - Added filters for antispam and mailbox type in mailbox list.

## 2022-08-30
- **Email API** - Added antispam switch per domain and mailbox. Added DKIM switch per domain.

## Earlier Changes

See the full changelog at https://api.gandi.net/docs/changelog/ for entries before 2022-08-30.
