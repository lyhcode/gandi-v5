# Linked Zone API

**Base URL:** `https://api.gandi.net/v5/linkedzone`

## Domains

**URL:** `https://api.gandi.net/v5/linkedzone/domains`

### GET - List domains

**Query String**

- Optionalname ⁠stringTo search for a domain pattern. This parameter can be used more than once. You can also use special characters ? and * for pattern matching filters. ? represents a single character search and * means at least one character. For example, fo?.com will find foo.com but not foobar.com and fo*.com will find foo.com and foobar.com.page ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerM
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:deployed ⁠booleanDefault: falseExplain whether the DNS zone has been updated on the DNS server.id ⁠stringThe identifier of the domain resource.name ⁠stringA Fully Qualified Domain Name (FQDN).owner ⁠stringEntity who or which owns the domain. This entity can be a user, an organization or the client of a reseller.zone ⁠objectWith the following properties:id ⁠stringThe identifier of the zone resource.name ⁠stringName of the 

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
    "id": "d6208438-1ebf-4727-9e8a-166568d35855",
    "deployed": false,
    "name": "example.com",
    "owner": "065efe68-2c84-495d-be9b-82f20360293f",
    "zone": {
      "id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
      "name": "www",
      "status": "BEING_DEPLOYED"
    }
  },
  {
    "id": "2422145a-25ee-4e39-9239-06ab48d78726",
    "deployed": true,
    "name": "hello-world.org",
    "owner": "065efe68-2c84-495d-be9b-82f20360293f",
    "zone": {
      "id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
      "name": "www",
      "status": "DEPLOYED"
    }
  }
]
```

---

## Domain

**URL:** `https://api.gandi.net/v5/linkedzone/domains/{domain}`

### GET - Domain details

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:deployed ⁠booleanDefault: falseExplain whether the DNS zone has been updated on the DNS server.id ⁠stringThe identifier of the domain resource.name ⁠stringA Fully Qualified Domain Name (FQDN).owner ⁠stringEntity who or which owns the domain. This entity can be a user, an organization or the client of a reseller.zone ⁠objectWith the following properties:id ⁠stringThe identifier of the zone resource.name ⁠stringName of the record.status ⁠stringO

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
  "id": "d6208438-1ebf-4727-9e8a-166568d35855",
  "deployed": false,
  "name": "example.com",
  "owner": "065efe68-2c84-495d-be9b-82f20360293f",
  "zone": {
    "id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
    "name": "www",
    "status": "BEING_DEPLOYED"
  }
}
```

---

## Tasks

**URL:** `https://api.gandi.net/v5/linkedzone/tasks`

### GET - List tasks

**Query String**

- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:created_at ⁠datetimeThe date and hour when the task has been launched.id ⁠stringThe identifier of the task resource.result ⁠objectWith the following properties:errored ⁠arrayOf items of type:objectWith the following properties:domain ⁠stringAn error occurred during the task.message ⁠stringExplain the error.type ⁠stringOne of: "DATABASE_ERROR", "DOMAIN_EXISTS", "DOMAIN_NOT_EXIST", "DOMAIN_PERMISSION", "DOMAIN_STATUS_ERROR"

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
    "id": "055152cc-a258-48d4-b395-ddad6517d0b5",
    "zone_id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
    "type": "DEACTIVATE_ZONE",
    "status": "PENDING",
    "created_at": "2025-04-01T08:01:47.589312+00:00",
    "updated_at": "2025-04-01T08:03:04.474962+00:00",
    "result": {
      "succeeded": [],
      "errored": [
        {
          "domain": "example.com",
          "type": "ZONE_BEING_DEPLOYED",
          "message": "You cannot remove a domain on a zone under deployment"
        }
      ]
    }
  }
]
```

---

## Task

**URL:** `https://api.gandi.net/v5/linkedzone/tasks/{task_id}`

### GET - Task details

**URI Parameters**

- task_id ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:created_at ⁠datetimeThe date and hour when the task has been launched.id ⁠stringThe identifier of the task resource.result ⁠objectWith the following properties:errored ⁠arrayOf items of type:objectWith the following properties:domain ⁠stringAn error occurred during the task.message ⁠stringExplain the error.type ⁠stringOne of: "DATABASE_ERROR", "DOMAIN_EXISTS", "DOMAIN_NOT_EXIST", "DOMAIN_PERMISSION", "DOMAIN_STATUS_ERROR", "DNS_PERMISSION", "N

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
  "id": "055152cc-a258-48d4-b395-ddad6517d0b5",
  "zone_id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
  "type": "DEACTIVATE_ZONE",
  "status": "PENDING",
  "created_at": "2025-04-01T08:01:47.589312+00:00",
  "updated_at": "2025-04-01T08:03:04.474962+00:00",
  "result": {
    "succeeded": [],
    "errored": [
      {
        "domain": "example.com",
        "type": "ZONE_BEING_DEPLOYED",
        "message": "You cannot remove a domain on a zone under deployment"
      }
    ]
  }
}
```

---

## Unlink domains

**URL:** `https://api.gandi.net/v5/linkedzone/unlink/domains`

### PATCH - Unlink domains from a linked zone

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddomains ⁠array[ string ]Example:{ "domains": [ "hello-world.org", "example.com" ] }

**Body**

- application/json⁠objectWith the following properties:errored ⁠arrayOf items of type:objectWith the following properties:domain ⁠stringAn error occurred during the task.message ⁠stringExplain the error.type ⁠stringOne of: "DATABASE_ERROR", "DOMAIN_NOT_EXIST", "DOMAIN_PERMISSION", "DOMAIN_STATUS_ERROR", "DNS_PERMISSION", "ZONE_BEING_DEPLOYED"Possible errors which could occurred.succeeded ⁠array[ string ]Domains which has been correctly detached from a zone.Example:{ "succeeded": [ "hello-world.org

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
  "domains": [
    "hello-world.org",
    "example.com"
  ]
}
```

```json
{
  "succeeded": [
    "hello-world.org"
  ],
  "errored": [
    {
      "domain": "example.com",
      "type": "ZONE_BEING_DEPLOYED",
      "message": "You cannot remove a domain on a zone under deployment"
    }
  ]
}
```

---

## Linked zones managament

**URL:** `https://api.gandi.net/v5/linkedzone/zones`

### GET - List linked zones

**Query String**

- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.sharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:created_at ⁠datetimeThe date and hour when the zone resource has been created.default_records ⁠booleanApply default values for DNS settings. This default records are applied when a new zone is created.domain_count ⁠integerThe number of domains linked to the zone.id ⁠stringThe identifier of the zone resource.name ⁠stringName of the record.sharing_space ⁠objectWith the following properties:id ⁠stringIdentifier of the linked

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
    "id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
    "name": "www",
    "status": "DEPLOYED",
    "default_records": false,
    "created_at": "2025-04-04T14:35:57.525313+00:00",
    "domain_count": 2,
    "domains": [
      "domain-a.com",
      "domain-b.com"
    ],
    "sharing_space": {
      "id": "dff4caf7-c319-42fd-a055-3932933f662f",
      "name": "Front desk zone"
    },
    "record_text": "abc 3600 IN A 1.2.3.5\ndef 3600 IN A 1.2.3.5\nghi 300 IN TXT tutu"
  }
]
```

---

### POST - Create a zone

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredname ⁠stringName of a zone.Optionaldefault_records ⁠booleanDefault: falserecord_list ⁠arrayOf items of type:objectWith the following properties:Requiredname ⁠stringName of the recordttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this record.type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "S

**Headers**

- Location ⁠stringURI of the created zone resource.
- application/json⁠objectWith the following properties:message ⁠stringA success message sent after creating a zone.Example:{ "message": "Zone created" }

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
  "name": "Dead Zone",
  "default_records": false,
  "record_text": "abc 3600 IN A 1.2.3.5\ndef 3600 IN A 1.2.3.5\nghi 300 IN TXT tutu"
}
```

```json
{
  "message": "Zone created"
}
```

---

## Linked zone actions

**URL:** `https://api.gandi.net/v5/linkedzone/zones/{zone_id}`

### GET - Linked zone details

**URI Parameters**

- zone_id ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:created_at ⁠datetimeThe date and hour when the zone resource has been created.default_records ⁠booleanApply default values for DNS settings. This default records are applied when a new zone is created.domain_count ⁠integerThe number of domains linked to the zone.id ⁠stringThe identifier of the zone resource.name ⁠stringName of the record.sharing_space ⁠objectWith the following properties:id ⁠stringIdentifier of the linked-zone entity resource.

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
  "id": "50a8e8fb-765c-4533-8ed3-f222d25bdb9a",
  "name": "www",
  "status": "DEPLOYED",
  "default_records": false,
  "created_at": "2025-04-04T14:35:57.525313+00:00",
  "domain_count": 2,
  "domains": [
    "domain-a.com",
    "domain-b.com"
  ],
  "sharing_space": {
    "id": "dff4caf7-c319-42fd-a055-3932933f662f",
    "name": "Front desk zone"
  },
  "record_text": "abc 3600 IN A 1.2.3.5\ndef 3600 IN A 1.2.3.5\nghi 300 IN TXT tutu"
}
```

---

### POST - Deploy or undeploy a zone

**URI Parameters**

- zone_id ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddeploy ⁠booleanDeploy or deactivate the specified zone.Example:{ "deploy": true }

**Headers**

- Location ⁠stringURI of the task resource.
- application/json⁠objectWith the following properties:message ⁠stringA success message sent after deploying or deactivating a zone.Example:{ "message": "Zone deployment is in progress" }

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:message ⁠stringExample:{ "message": "zone Dead Zone is already deployed." }

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```json
{
  "deploy": true
}
```

```json
{
  "message": "Zone deployment is in progress"
}
```

```json
{
  "message": "zone Dead Zone is already deployed."
}
```

---

### PATCH - Update a linked zone

**URI Parameters**

- zone_id ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionaldefault_records ⁠booleanApply default values for DNS settings. This default records are applied when a new zone is created.name ⁠stringName of a zone.record_list ⁠arrayOf items of type:objectWith the following properties:Requiredname ⁠stringName of the recordttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this record.type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "D

**Body**

- application/json⁠objectWith the following properties:message ⁠stringA success message sent after updating a zone.Example:{ "message": "Zone updated" }

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
  "name": "Quarantine Zone"
}
```

```json
{
  "message": "Zone updated"
}
```

---

### DELETE - Delete a linked zone

**URI Parameters**

- zone_id ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

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

## Link domains to a zone

**URL:** `https://api.gandi.net/v5/linkedzone/zones/{zone_id}/link/domains`

### PATCH - Link domains to a specific zone

**URI Parameters**

- zone_id ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddomains ⁠array[ string ]Example:{ "domains": [ "hello-world.org", "example.com" ] }

**Body**

- application/json⁠objectWith the following properties:errored ⁠arrayOf items of type:objectWith the following properties:domain ⁠stringAn error occurred during the task.message ⁠stringExplain the error.type ⁠stringOne of: "DATABASE_ERROR", "DNS_PERMISSION", "DOMAIN_EXISTS", "DOMAIN_NOT_EXIST", "DOMAIN_PERMISSION", "DOMAIN_STATUS_ERROR", "NOT_LIVEDNS", "ZONE_BEING_DEPLOYED"Possible errors which could occurred.succeeded ⁠array[ string ]Domains which has been correctly attached to a zone.Example:{ "

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
  "domains": [
    "hello-world.org",
    "example.com"
  ]
}
```

```json
{
  "succeeded": [
    "hello-world.org"
  ],
  "errored": [
    {
      "domain": "example.com",
      "type": "ZONE_BEING_DEPLOYED",
      "message": "You cannot remove a domain on a zone under deployment"
    }
  ]
}
```

---


