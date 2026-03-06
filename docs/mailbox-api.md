# Mailbox API (BETA version)

**Base URL:** `https://api.gandi.net/v5/mailbox`

## Listing domains and get information about them

**URL:** `https://api.gandi.net/v5/mailbox/domains`

### GET - Lists all your domains

**Query String**

- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:fqdn ⁠stringExample:[ { "fqdn": "domain.com" } ]

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
[
  {
    "fqdn": "domain.com"
  }
]
```

---

## Domain detail

**URL:** `https://api.gandi.net/v5/mailbox/domains/{domain}`

### GET - Get domain detail

**URI Parameters**

- domain ⁠stringThe domain
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:antispam ⁠booleanconfiguration ⁠arrayOf items of type:objectWith the following properties:key ⁠stringvalues ⁠array[ string ]dkim ⁠booleaninternal ⁠booleanis_livedns ⁠booleanmx ⁠booleanspf ⁠booleantxt ⁠booleanOptionaldate_last_validation ⁠datetimeExample - Domain details and configuration for DNS records.:{ "dkim": false, "mx": false, "spf": false, "txt": false, "internal": false, "antispam": false, "is_livedns": false, "configuration": [ { "ke

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "dkim": false,
  "mx": false,
  "spf": false,
  "txt": false,
  "internal": false,
  "antispam": false,
  "is_livedns": false,
  "configuration": [
    {
      "key": "TXT",
      "values": [
        "mailsa 10800 IN TXT \"03c77e4fabebde501d83d55cd937671a6a3760d9aa4b2e0fe47f754dc4fa213f\""
      ]
    },
    {
      "key": "DKIM",
      "values": [
        "gm1._domainkey 1200 IN CNAME gm1.gandimail.net.",
        "gm2._domainkey 1200 IN CNAME gm2.gandimail.net.",
        "gm3._domainkey 1200 IN CNAME gm3.gandimail.net."
      ]
    }
  ]
}
```

---

## Validate configuration

**URL:** `https://api.gandi.net/v5/mailbox/domains/{domain}/validate`

### POST - Validate configuration

**URI Parameters**

- domain ⁠stringThe domain
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredrecords_to_validate ⁠array[ string ]List of elements to validateExample - Validate DNS records.:{ "records_to_validate": [ "dkim", "spf", "txt" ] }

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "records_to_validate": [
    "dkim",
    "spf",
    "txt"
  ]
}
```

---

## Manage your forwarding addresses

**URL:** `https://api.gandi.net/v5/mailbox/forwards`

### POST - Create a forwarding address

This route creates a new forwarding address to one or several destinations forward route.

Warning! You must create at least one mailbox on the domain source to create forward.

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddestinations ⁠array[ string ]A list of email addresses.source ⁠stringThe source email address.Example:{ "source": "alice@gandi.net", "destinations": [ "alice.doe@example.org", "ruth@example.org" ] }

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "source": "alice@gandi.net",
  "destinations": [
    "alice.doe@example.org",
    "ruth@example.org"
  ]
}
```

---

### GET - List forwarding addresses

**Query String**

- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.search ⁠stringFilter the list by source or destination.Example: lice@mydomainExample: aliceExample: domain.comsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.sort_by ⁠stringOne of: "source", "-source"Default: "source"Result sorting fi
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- X-Total-Count ⁠integerTotal number of items after filtering.
- application/json⁠arrayOf items of type:objectWith the following properties:destinations ⁠stringemail addresses to forward emails to.source ⁠stringThe source email address.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Forwarding address details

**URL:** `https://api.gandi.net/v5/mailbox/forwards/{source}`

### PUT - Update a forwarding address

This route replaces a forwarding address' destinations forward route.

Warning! You must have at least one mailbox on the domain source to update forward.

**URI Parameters**

- source ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddestinations ⁠array[ string ]A list of email addresses.Example:{ "destinations": [ "alice@example.org", "hello.world@gandi.net" ] }

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "destinations": [
    "alice@example.org",
    "hello.world@gandi.net"
  ]
}
```

---

### DELETE - Delete a forwarding address

**URI Parameters**

- source ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Manage your mailboxes

**URL:** `https://api.gandi.net/v5/mailbox/mailboxes`

### GET - List mailboxes

**Query String**

- Optionaladdress ⁠stringFilter by exact loginExample: alicedomain_part ⁠stringFilter by exact fqdnExample: mydomain.comlocal_part ⁠stringFilter by exact loginExample: alicepage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.search ⁠stringSearch by login, complete email or domain name.Example: lice@mydomainExample: aliceExample: domain.comsharing_id ⁠stri
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- X-Total-Count ⁠integerTotal number of items after filtering.
- application/json⁠arrayOf items of type:objectWith the following properties:address ⁠stringComplete address of mailboxantispam ⁠booleanAntispam is enabledconfig ⁠objectMailbox configurationWith the following properties:label ⁠stringLabel of configurationname ⁠stringTechnical name of configurationquota_kb ⁠integerQuota in Kbuuid ⁠stringConfiguration IDcreated_at ⁠datetimeCreation datedata_access ⁠booleanInformation about accessdomain_part ⁠stringDomain nameexpires_at ⁠datetimeExpiry dateinternal_d

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Create new mailbox

You can create a mailbox with config config_name could be standard (10GB) or premium (50 GB).You can set the config_name , email and password.And add alias if it is not already on the DNS zone record domain.

Add records to your domain zone.

We make a DNS check to ensure the domain is correctly owned by you.These records are mandatory to validate your mailbox product :

The MX records:

The records below are strongly suggest to have functional mailbox and to send/received mails, add SPF and DKIM records to prove your mails are legitimate and diminish the possibilty for your mails to be marked as spam:

You can retrieve this records using domain details API.

In case of domain registered at gandi and when you use livedns nameservers, when you have the correct right to write on livedns zone, this records are automatically added.

For external domain, you must change the zone of your domain from your registrar web admin or API, when it provides it.

Validate your DNS records.

Several times, we check your domain zone in order to validate your mailbox.But you can also manually launch a check using this API. This call is asynchronous.To check the response the validated or not validated records use domain details API:

For the records dkim, mx, spf, txt:

For the flag internal:

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredconfig_name ⁠stringSpecify the config of the product (standard/premium).email ⁠stringpassword ⁠stringMinimum length: 8Maximum length: 200Password of the mailbox.Optionalaliases ⁠arrayOf items of type:stringA local-part (what comes before the "@") of an email address. It can contain a wildcard "*" before or after at least two characters to redirect everything thats matches the local-part pattern.duration_month ⁠integerOne of: 1, 12The d

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```
mailsa 10800 IN TXT "{value}"
```

```
@               10800        IN        MX        50 fb.mail.gandi.net.
@               10800        IN        MX        10 spool.mail.gandi.net.
```

```
@               10800        IN        TXT        "v=spf1 include:_mailcust.gandi.net ?all"
gm1._domainkey  10800        IN        CNAME      gm1.gandimail.net.
gm2._domainkey  10800        IN        CNAME      gm2.gandimail.net.
gm3._domainkey  10800        IN        CNAME      gm3.gandimail.net.
```

```json
{
   "dkim": true,
   "mx": true,
   "spf": true,
   "txt": true,
   "internal": false
}
```

```json
{
  "duration_month": 1,
  "config_name": "standard",
  "email": "hello@domain.com",
  "password": "fds678fdsDdsç!è"
}
```

```json
{
  "duration_month": 12,
  "config_name": "premium",
  "email": "premium@domain.com",
  "password": "4f56&dsqf4s"
}
```

```json
{
  "duration_month": 12,
  "config_name": "premium",
  "email": "hi@domain.com",
  "password": "4f56&dsqf4s",
  "aliases": [
    "contact",
    "redir"
  ]
}
```

---

## Mailbox detail

**URL:** `https://api.gandi.net/v5/mailbox/mailboxes/{email}`

### GET - Get mailbox detail

**URI Parameters**

- email ⁠stringThe email address
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:address ⁠stringComplete address of mailboxantispam ⁠booleanAntispam is enabledconfig ⁠objectMailbox configurationWith the following properties:label ⁠stringLabel of configurationname ⁠stringTechnical name of configurationquota_kb ⁠integerQuota in Kbuuid ⁠stringConfiguration IDcreated_at ⁠datetimeCreation datedata_access ⁠booleanInformation about accessdomain_part ⁠stringDomain nameexpires_at ⁠datetimeExpiry dateinternal_domain ⁠booleanInformat

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### PATCH - Update mailbox

**URI Parameters**

- email ⁠stringThe email address
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalaliases ⁠arrayOf items of type:stringA local-part (what comes before the "@") of an email address. It can contain a wildcard "*" before or after at least two characters to redirect everything thats matches the local-part pattern.antispam ⁠booleanDefault: trueEnable or disable antispam.autorenew ⁠objectWith the following properties:Requiredactivated ⁠booleanSpecify true to enable autorenew, false to disable it.duration ⁠integerOne of: 1

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "password": "xXXXxx4f56&dsqf4sXXxx"
}
```

```json
{
  "config_name": "premium"
}
```

```json
{
  "config_name": "standard"
}
```

```json
{
  "responder": {
    "activated": true,
    "starts_at": "2025-04-20T09:00:00Z",
    "ends_at": "2025-05-07T19:00:00Z",
    "message": "Out of office"
  }
}
```

```json
{
  "responder": {
    "activated": false
  }
}
```

```json
{
  "aliases": [
    "hello",
    "contact"
  ]
}
```

---

### DELETE - Delete mailbox

**URI Parameters**

- email ⁠stringThe email address
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Renew mailbox

**URL:** `https://api.gandi.net/v5/mailbox/mailboxes/{email}/renew`

### POST - Renew a mailbox

**URI Parameters**

- email ⁠stringThe email address
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredduration ⁠integerThe duration (in month) of the renewal.Example - Renewal for 1 month:{ "duration": 1 }Example - Renewal for 12 months:{ "duration": 12 }

**Headers**

- OptionalWarning ⁠stringWarning message
- application/json⁠objectWith the following properties:status ⁠stringOne of: "success", "error"Response status.Optionalerrors ⁠arrayA list of all the errors encountered during validation.Of items of type:objectWith the following properties:description ⁠stringError message.location ⁠stringOne of: "header", "path", "querystring", "body"The field's location in the HTTP response.name ⁠stringThe xpath of the field.

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "duration": 1
}
```

```json
{
  "duration": 12
}
```

---

## Buy mailbox and list all available products

**URL:** `https://api.gandi.net/v5/mailbox/products`

### POST - Buy new mailbox

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredconfig_name ⁠stringOne of: "standard", "premium"Specify the name of the product (standard/premium).duration_month ⁠integerOne of: 1, 12The duration of the subscription 1 or 12 month(s).quantity ⁠integerThe quantity of slots to purchase.Optionalautorenew ⁠booleanDefault: falsetrue to enable the autorenewal.Example - buy 2 standard mailboxes with mensual subscription:{ "config_name": "standard", "duration_month": 1, "quantity": 2 }Exampl

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "config_name": "standard",
  "duration_month": 1,
  "quantity": 2
}
```

```json
{
  "config_name": "premium",
  "duration_month": 12,
  "quantity": 1,
  "autorenew": true
}
```

---

### GET - Lists all buyable product

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Total-Count ⁠integerTotal number of items.
- application/json⁠arrayOf items of type:objectWith the following properties:config ⁠arrayList config apply to this productOf items of type:objectWith the following properties:label ⁠stringname ⁠stringuuid ⁠stringUUIDconfig_name ⁠stringdescription ⁠stringlabel ⁠stringprices ⁠arrayList of pricesOf items of type:objectWith the following properties:currency ⁠stringduration_unit ⁠stringmax_duration ⁠integermin_duration ⁠integernormal_price_after_taxes ⁠numbernormal_price_before_taxes ⁠numberprice_afte

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Get mailboxes quotas.

**URL:** `https://api.gandi.net/v5/mailbox/quotas`

### GET - Get mailboxes available and mailboxes already used.

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠arrayOf items of type:objectWith the following properties:annually ⁠objectQuota for mailboxes paid in annually subscription.With the following properties:available ⁠integerThe count of mailboxes available to create mailbox.total ⁠integerThe total represents mailboxes available to create mailbox and mailbox already used.used ⁠integerThe count of mailboxes already used.config_name ⁠stringConfiguration name of the mailbox.label ⁠stringLabel of the offer.monthly ⁠objectQuota for mai

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
[
  {
    "annually": {
      "available": 0,
      "total": 1,
      "used": 1
    },
    "config_name": "standard",
    "label": "Standard 10Gb",
    "monthly": {
      "available": 1,
      "total": 1,
      "used": 0
    },
    "quota": "10Gb"
  },
  {
    "annually": {
      "available": 1,
      "total": 3,
      "used": 2
    },
    "config_name": "premium",
    "label": "Premium 50Gb",
    "monthly": {
      "available": 0,
      "total": 0,
      "used": 0
    },
    "quota": "50Gb"
  }
]
```

---

## Listing slots

**URL:** `https://api.gandi.net/v5/mailbox/slots`

### GET - Lists all your slots

**Query String**

- Optionalconfig_name ⁠stringFilter the list by configuration nameexpires_at_gte ⁠datetimeSlot expiration date.expires_at_lte ⁠datetimeSlot expiration date.last_paid_duration ⁠integerOne of: 1, 12Filters the list by last paid durationpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.refundable ⁠stringOne of: "true", "false"Filter the list by slots that 
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:config ⁠objectInformation on the configuration applied to this slotWith the following properties:label ⁠stringCommercial label of configurationname ⁠stringInternal name of configurationuuid ⁠stringConfig idrefund_info ⁠objectInformation about the refundable process, may be false if there no refundable possibilityWith the following properties:currency ⁠stringRefund currencyprice ⁠numberRefund amoutrefund_expires_at ⁠dateti

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
[
  {
    "uuid": "5156f881-cf33-11ee-aa2a-c889f3cdfda1",
    "autorenew": {
      "duration_month": 12,
      "sharing_id": "5156f881-cf33-11ee-aa2a-c000f3cdfda8"
    },
    "config": {
      "label": "Premium 50 Go",
      "name": "premium-50go",
      "uuid": "5156f876-cf33-11ee-aa4a-c889f3cdfda7"
    },
    "expires_at": "2024-03-20T14:29:41Z",
    "last_paid_duration": 1,
    "refund_info": {
      "currency": "EUR",
      "price": 61.8,
      "refund_expires_at": "2025-03-04T14:29:41Z"
    },
    "refundable": true,
    "webhosting_pack": false
  }
]
```

---

## Slot detail

**URL:** `https://api.gandi.net/v5/mailbox/slots/{slot_id}`

### GET - Get slot detail

**URI Parameters**

- slot_id ⁠stringIdentifier of the slot, an uuid.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:config ⁠objectInformation on the configuration applied to this slotWith the following properties:label ⁠stringCommercial label of configurationname ⁠stringInternal name of configurationuuid ⁠stringConfig idrefund_info ⁠objectInformation about the refundable process, may be false if there no refundable possibilityWith the following properties:currency ⁠stringRefund currencyprice ⁠numberRefund amoutrefund_expires_at ⁠datetimeThis is the date on 

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---


