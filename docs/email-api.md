# Email API (current version)

**Base URL:** `https://api.gandi.net/v5/email`

## Manage your forwarding addresses

**URL:** `https://api.gandi.net/v5/email/forwards/{domain}`

### GET - List forwarding addresses

**URI Parameters**

- domain ⁠stringDomain name.
- Optionaldestination ⁠stringFilters the list by a destination pattern.Example: *@toto.netExample: john.doe@toto*page ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.sort_by ⁠stringOne of: "source", "-source", "destination", "-destination"Default: "source"Result sorting field.source ⁠stringFilters the list by a source pattern.Example: *liceExample: alice
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/csv value, this route will return a CSV-formatted response.

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:destinations ⁠array[ string ]A list of email addresses.href ⁠stringURL to forwarding addresssource ⁠stringThe source email address.
- text/csv⁠anyCSV-formatted response.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Create a forwarding address

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddestinations ⁠array[ string ]A list of email addresses.source ⁠stringThe source email address.Example:{ "source": "alice", "destinations": [ "alice.doe@example.org", "ruth@example.org" ] }

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
  "source": "alice",
  "destinations": [
    "alice.doe@example.org",
    "ruth@example.org"
  ]
}
```

---

## Forwarding address details

**URL:** `https://api.gandi.net/v5/email/forwards/{domain}/{source}`

### PUT - Update a forwarding address

**URI Parameters**

- domain ⁠stringDomain name.source ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddestinations ⁠array[ string ]A list of email addresses.Example:{ "destinations": [ "alice@example.org" ] }

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
  "destinations": [
    "alice@example.org"
  ]
}
```

---

### DELETE - Delete a forwarding address

**URI Parameters**

- domain ⁠stringDomain name.source ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

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

---

## Manage your mailboxes

**URL:** `https://api.gandi.net/v5/email/mailboxes/{domain}`

### GET - List mailboxes

This route returns a list of all the mailboxes attached to a specific {domain}.

The "to_convert" field lets you know whether or not you need to convert your mailbox with the renew route.

**URI Parameters**

- domain ⁠stringDomain name.
- Optional<created_at ⁠datetimeSlot creation date.~login ⁠stringFilters the list by a login pattern.Example: *liceExample: alic*antispam ⁠booleanAntispam is enabled or disabledlogin ⁠stringFilters the list by exact login.mailbox_type ⁠stringOne of: "standard", "premium", "standard_2023", "premium_2023"page ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/csv value, this route will return a CSV-formatted response.

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:address ⁠stringFull email addressalias_count ⁠integerDefault: 0antispam ⁠booleanAntispam is enabledautorenew ⁠objectState of autorenewWith the following properties:duration ⁠integerDuration for autorenewduration_type ⁠stringType of duration ('m' for month)enabled ⁠booleanSpecify if autorenew is enabled on this mailboxOptionalsharing_id ⁠stringBilled organizationdomain ⁠stringDomain nameexpires_at ⁠datetimeExpiry datehref 
- text/csv⁠anyCSV-formatted response.

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
    "domain": "example.net",
    "login": "alice",
    "address": "alice@example.net",
    "id": "066743e5-96e4-4a1d-9195-8b8a700a8a79",
    "mailbox_type": "standard_2023",
    "quota_used": 1200,
    "alias_count": 2,
    "antispam": true,
    "href": "https://api.test/api/v5/email/example.net/066743e5-96e4-4a1d-9195-8b8a700a8a79",
    "expires_at": "2021-05-04T10:04:18Z",
    "to_convert": false,
    "autorenew": {
      "enabled": true,
      "duration": 1,
      "duration_type": "m"
    }
  }
]
```

---

### POST - Create a new mailbox

This route creates a new mailbox for the given domain. You will have to choose a mailbox_type.

Note that before you can create a mailbox, you must have a slot available (see Slot management).

Note If you continue to use premium_new and standard_new, the api will respond with premium_2023 and standard_2023.

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredlogin ⁠stringMinimum length: 1mailbox_type ⁠stringOne of: "standard", "premium", "standard_2023", "premium_2023", "standard_new (deprecated, replaced by standard_2023)", "premium_new (deprecated, replaced by premium_2023)"password ⁠stringMinimum length: 8Maximum length: 200Mailbox password.Must contain between 8 and 200 characters, containing at least 1 upper-case letter, 3 numbers, and a special character.You can also send a hashed pa

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
  "login": "alice",
  "mailbox_type": "standard",
  "password": "a*6@Xk86cPR2kcZ@qPAi",
  "aliases": [
    "bob",
    "bob*"
  ]
}
```

---

## Mailbox renew

**URL:** `https://api.gandi.net/v5/email/mailboxes/{domain}/{email}/renew`

### POST - Renew a mailbox

This method allows you to to renew a mailbox for 1 or 12 months.This route can also be used to convert your mailboxes from free to charged, if you don't convert them, they will be deleted on the expiration date.Warning! This is not a free operation. Please ensure your prepaid account has enough credit.

To find out which mailboxes to convert, you can use the "to_convert" field in the list of your mailboxes.

**URI Parameters**

- domain ⁠stringDomain name.email ⁠stringEmail
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

- application/json⁠objectWith the following properties:message ⁠stringstatus_code ⁠integer

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

## Mailbox details

**URL:** `https://api.gandi.net/v5/email/mailboxes/{domain}/{mailbox_id}`

### GET - Retrieve a mailbox

**URI Parameters**

- domain ⁠stringDomain name.mailbox_id ⁠stringMailbox ID, of type UUID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:address ⁠stringFull email addressaliases ⁠arrayDefault: []Mailbox alias listOf items of type:stringA local-part (what comes before the "@") of an email address. It can contain a wildcard "*" before or after at least two characters to redirect everything thats matches the local-part pattern.antispam ⁠booleanAntispam is enabledautorenew ⁠objectState of autorenewWith the following properties:duration ⁠integerDuration for autorenewduration_type ⁠s

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
  "domain": "mailbox-api-test-1.fr",
  "responder": {
    "message": "",
    "enabled": false
  },
  "mailbox_type": "standard",
  "login": "alice",
  "quota_used": 0,
  "antispam": true,
  "aliases": [
    "bob",
    "bob*"
  ],
  "address": "alice@example.net",
  "href": "https://api.test/api/v5/email/example.net/066743e5-96e4-4a1d-9195-8b8a700a8a79",
  "id": "066743e5-96e4-4a1d-9195-8b8a700a8a79",
  "expires_at": "2021-05-04T10:04:18Z",
  "autorenew": {
    "enabled": true,
    "duration": 1,
    "duration_type": "m"
  }
}
```

---

### PATCH - Update a mailbox

This route allows you to update a mailbox. This is how you can add aliases, change passwords, activate/deactivate out-of-office replies or change offer on a given mailbox.

In the event of a change of offer, the remaining time is calculated on the basis of the new offer.

**URI Parameters**

- domain ⁠stringDomain name.mailbox_id ⁠stringMailbox ID, of type UUID
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalaliases ⁠arrayOf items of type:stringA local-part (what comes before the "@") of an email address. It can contain a wildcard "*" before or after at least two characters to redirect everything thats matches the local-part pattern.antispam ⁠booleanEnable or disable antispamautorenew ⁠objectWith the following properties:Requiredactivated ⁠booleanActivate Autorenewduration ⁠integerOne of: 1, 12Activate autorenewfor each month or 12 monthsl

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
  "password": "lGv6KLZhbCgcX8pMK9Vx6mqrZC8vk84L"
}
```

```json
{
  "responder": {
    "enabled": true,
    "message": "Out of office",
    "starts_at": "2019-07-10T18:00:01Z",
    "ends_at": "2019-07-26T09:00:01Z"
  }
}
```

```json
{
  "aliases": [
    "bob",
    "bob*"
  ]
}
```

```json
{
  "mailbox_type": "premium_2023"
}
```

```json
{
  "autorenew": {
    "activated": true,
    "duration": 1
  }
}
```

---

### DELETE - Delete a mailbox

**URI Parameters**

- domain ⁠stringDomain name.mailbox_id ⁠stringMailbox ID, of type UUID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

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

---

## Mailbox content management

**URL:** `https://api.gandi.net/v5/email/mailboxes/{domain}/{mailbox_id}/contents`

### DELETE - Purge a mailbox

**URI Parameters**

- domain ⁠stringDomain name.mailbox_id ⁠stringMailbox ID, of type UUID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

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

---

## Renew all mailboxes for a given domain

**URL:** `https://api.gandi.net/v5/email/mailboxes/{domain}/renew`

### POST - Renew all mailboxes

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠anyExample:{ "sharing_id": "ac7205ab-5888-4e8a-af59-397db787d75f" }

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
  "sharing_id": "ac7205ab-5888-4e8a-af59-397db787d75f"
}
```

---

## Migrate from packmail to the new mailbox offer

**URL:** `https://api.gandi.net/v5/email/migration/{domain}`

### GET - Show migration details

**URI Parameters**

- domain ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:available ⁠booleanReturn True if mailbox can be migratedcurrency ⁠stringCurrency used.forward_count ⁠integerTotal number of forwards.free_mailboxes ⁠integerTotal number of free mailboxes.included_mailboxes ⁠integerTotal number of included mailboxes (offered with the domain).info ⁠arrayDetails of the mailbox migration.Of items of type:objectWith the following properties:login ⁠stringEmail login.offer_v2 ⁠stringMailbox type, it could be standard

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
  "available": true,
  "packmail": true,
  "included_mailboxes": 5,
  "free_mailboxes": 2,
  "forward_count": 0,
  "info": [
    {
      "login": "mb1",
      "offer_v2": "standard",
      "price_v2": 4.2,
      "price_v2_m": 0.35,
      "quota": 0,
      "usage": 2097152,
      "quota_v2": 3145728
    }
  ],
  "currency": "EUR",
  "price_v1": 12,
  "price_v2": 4.2,
  "quota_v1": 3145728,
  "usage_v1": 1887436,
  "token": "fa647dadedaeae4e6a3551e16907f36abe029ddc"
}
```

---

### POST - Launch migration

**URI Parameters**

- domain ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredtoken ⁠stringThe token needed to migrate.Example:{ "token": "fa647dadedaeae4e6a3551e16907f36abe029ddc" }

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
  "token": "fa647dadedaeae4e6a3551e16907f36abe029ddc"
}
```

---

## Offer details

**URL:** `https://api.gandi.net/v5/email/offers/{domain}`

### GET - Retrieve current email offer

**URI Parameters**

- domain ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:antispam ⁠stringOne of: "active", "inactive", "mixed"Antispam status on the domain. Note that a mixed value means that some mailboxes use the antispam while others don't.dkim ⁠stringOne of: "active", "inactive"DKIM status on the domain.status ⁠stringOne of: "active", "inactive"Offer statusversion ⁠integerOne of: 1, 2, 3Offer versionExample:{ "status": "active", "version": 2, "antispam": "active", "dkim": "active" }

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
  "status": "active",
  "version": 2,
  "antispam": "active",
  "dkim": "active"
}
```

---

### PATCH - Update global email options

**URI Parameters**

- domain ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredantispam ⁠stringOne of: "active", "inactive"Enable or disable the antispam at the domain's level.dkim ⁠stringOne of: "active", "inactive"Enable or disable DKIM on this domain.Example - Enable DKIM and antispam:{ "antispam": "active", "dkim": "active" }

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
  "antispam": "active",
  "dkim": "active"
}
```

---

## Manage slots

**URL:** `https://api.gandi.net/v5/email/slots/{domain}`

### GET - List existing mailbox slots

**URI Parameters**

- domain ⁠string
- Optionaldisplay_not_expired_and_inactive ⁠booleanDefault: falseOnly select inactive slots which have not expired.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Total-Count ⁠integerTotal number of items.
- application/json⁠arrayOf items of type:objectWith the following properties:capacity ⁠integerSlot capacity (in MB).created_at ⁠datetimeSlot creation date.href ⁠stringLink to slot detailsid ⁠integerSlot ID.mailbox_type ⁠stringType of mailbox this slot can handle.refundable ⁠booleantrue if this slot is refundablestatus ⁠stringSlot status.Example:[ { "status": "inactive", "capacity": 3072, "mailbox_type": "standard", "refundable": false, "id": 123, "href": "https://api.test/v5/email/slots/mailbox-ap

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
    "status": "inactive",
    "capacity": 3072,
    "mailbox_type": "standard",
    "refundable": false,
    "id": 123,
    "href": "https://api.test/v5/email/slots/mailbox-api-test-1.fr/123",
    "created_at": "2019-01-15T13:20:01Z"
  },
  {
    "status": "active",
    "capacity": 3072,
    "mailbox_type": "standard",
    "refundable": false,
    "id": 124,
    "href": "https://api.test/v5/email/slots/mailbox-api-test-1.fr/124",
    "created_at": "2019-01-15T13:20:01Z"
  }
]
```

---

### POST - Create a new mailbox slot

**URI Parameters**

- domain ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredduration ⁠integerThe duration (in month) of the renewal.mailbox_type ⁠stringOne of: "standard", "premium", "standard_2023", "premium_2023"Type of mailbox this slot can handle.Optionalautorenew ⁠booleanActivate autorenew on slot. (False by default)Example:{ "mailbox_type": "standard_2023", "duration": 12 }Example:{ "mailbox_type": "standard_2023", "duration": 12, "autorenew": true }

**Headers**

- Total-Count ⁠integerTotal number of items.

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
  "mailbox_type": "standard_2023",
  "duration": 12
}
```

```json
{
  "mailbox_type": "standard_2023",
  "duration": 12,
  "autorenew": true
}
```

---

## Slot details

**URL:** `https://api.gandi.net/v5/email/slots/{domain}/{slot_id}`

### GET - Get slot details

**URI Parameters**

- domain ⁠stringslot_id ⁠integerSlot ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:capacity ⁠integerSlot capacity (in MB).created_at ⁠datetimeSlot creation date.href ⁠stringLink to slot detailsid ⁠integerSlot ID.mailbox_type ⁠stringType of mailbox this slot can handle.refundable ⁠booleantrue if this slot is refundablestatus ⁠stringSlot status.Optionalrefund_amount ⁠numberRefunded amount if you delete this slot now.refund_currency ⁠stringRefund currency.Example:{ "status": "inactive", "capacity": 51200, "refund_amount": 16.16

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
  "status": "inactive",
  "capacity": 51200,
  "refund_amount": 16.16,
  "mailbox_type": "premium",
  "refundable": true,
  "refund_currency": "EUR",
  "id": 125,
  "href": "http://api.test/v5/email/slots/mailbox-api-test-1.fr/125",
  "created_at": "2019-04-08T08:48:41Z"
}
```

---

### DELETE - Refund a slot

**URI Parameters**

- domain ⁠stringslot_id ⁠integerSlot ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

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

---


