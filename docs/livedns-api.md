# LiveDNS API

**Base URL:** `https://api.gandi.net/v5/livedns`

## TSIG keys

**URL:** `https://api.gandi.net/v5/livedns/axfr/tsig`

### GET - List existing TSIG keys

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠arrayOf items of type:objectWith the following properties:href ⁠stringURL of the keyid ⁠stringIdentifier of the keykey_name ⁠stringUnique "name" for the key, based on its idsecret ⁠stringshared secret of the keyExample:[ { "href": "https://api.test/v5/livedns/axfr/tsig/2e21af2b-3d85-4ad9-b51b-698c242a13e5", "id": "2e21af2b-3d85-4ad9-b51b-698c242a13e5", "key_name": "2e21af2b-3d85-4ad9-b51b-698c242a13e5.gandi.net", "secret": "aiG5ji3Necheisho" } ]

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
    "href": "https://api.test/v5/livedns/axfr/tsig/2e21af2b-3d85-4ad9-b51b-698c242a13e5",
    "id": "2e21af2b-3d85-4ad9-b51b-698c242a13e5",
    "key_name": "2e21af2b-3d85-4ad9-b51b-698c242a13e5.gandi.net",
    "secret": "aiG5ji3Necheisho"
  }
]
```

---

### POST - Creates a new TSIG key

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Location ⁠string
- application/json⁠objectWith the following properties:href ⁠stringURL of the keyid ⁠stringIdentifier of the keykey_name ⁠stringUnique "name" for the key, based on its idExample:{ "href": "https://api.test/v5/livedns/axfr/tsig/2e21af2b-3d85-4ad9-b51b-698c242a13e5", "id": "2e21af2b-3d85-4ad9-b51b-698c242a13e5", "key_name": "2e21af2b-3d85-4ad9-b51b-698c242a13e5.gandi.net" }

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
  "href": "https://api.test/v5/livedns/axfr/tsig/2e21af2b-3d85-4ad9-b51b-698c242a13e5",
  "id": "2e21af2b-3d85-4ad9-b51b-698c242a13e5",
  "key_name": "2e21af2b-3d85-4ad9-b51b-698c242a13e5.gandi.net"
}
```

---

## Manage TSIG keys

**URL:** `https://api.gandi.net/v5/livedns/axfr/tsig/{id}`

### GET - GET information about a TSIG key

**URI Parameters**

- id ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:config_samples ⁠objectURL samples for each of those softwareWith the following properties:bind ⁠stringknot ⁠stringnsd ⁠stringpowerdns ⁠stringhref ⁠stringURL of the keyid ⁠stringIdentifier of the keykey_name ⁠stringUnique "name" for the key, based on its idsecret ⁠stringshared secret of the keyExample:{ "href": "https://api.test/v5/v5/livedns/axfr/tsig/2e21af2b-3d85-4ad9-b51b-698c242a13e5", "id": "2e21af2b-3d85-4ad9-b51b-698c242a13e5", "key_nam

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
  "href": "https://api.test/v5/v5/livedns/axfr/tsig/2e21af2b-3d85-4ad9-b51b-698c242a13e5",
  "id": "2e21af2b-3d85-4ad9-b51b-698c242a13e5",
  "key_name": "2e21af2b-3d85-4ad9-b51b-698c242a13e5.gandi.net",
  "secret": "aiG5ji3Necheisho",
  "config_samples": {
    "bind": "https://api.test/v5/v5/livedns/axfr/tsig/id-tsig-001/config/bind",
    "knot": "https://api.test/v5/v5/livedns/axfr/tsig/id-tsig-001/config/knot",
    "nsd": "https://api.test/v5/v5/livedns/axfr/tsig/id-tsig-001/config/nsd",
    "powerdns": "hhttps://api.test/v5/v5/livedns/axfr/tsig/id-tsig-001/config/"
  }
}
```

---

## Software configuration information

**URL:** `https://api.gandi.net/v5/livedns/axfr/tsig/{id}/config/{software}`

### GET - Software configuration information

**URI Parameters**

- id ⁠stringsoftware ⁠stringOne of: "bind", "knot", "nsd", "powerdns"
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠stringString representation of the configuration for that key

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## List accepted record types

**URL:** `https://api.gandi.net/v5/livedns/dns/rrtypes`

### GET - List record types

Returns the list of known record types (A, CNAME, …)

Current list (might be outdated):

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠array[ string ]

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Domains

**URL:** `https://api.gandi.net/v5/livedns/domains`

### GET - List of domains handled by LiveDNS

**Query String**

- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.sharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:domain_href ⁠stringdomain_records_href ⁠stringfqdn ⁠stringExample:[ { "fqdn": "example.org", "domain_href": "https://api.test/v5/livedns/domains/example.org", "domain_records_href": "https://api.test/v5/livedns/domains/example.org/records" }, { "fqdn": "example.net", "domain_href": "https://api.test/v5/livedns/domains/example.net", "domain_records_href": "https://api.test/v5/livedns/domains/example.net/records" } ]

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
    "fqdn": "example.org",
    "domain_href": "https://api.test/v5/livedns/domains/example.org",
    "domain_records_href": "https://api.test/v5/livedns/domains/example.org/records"
  },
  {
    "fqdn": "example.net",
    "domain_href": "https://api.test/v5/livedns/domains/example.net",
    "domain_records_href": "https://api.test/v5/livedns/domains/example.net/records"
  }
]
```

---

### POST - Add a new domain to LiveDNS

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredfqdn ⁠stringThe domain nameOptionalzone ⁠objectWith the following properties:Optionalitems ⁠arrayOf items of type:objectWith the following properties:Requiredrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A

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
  "fqdn": "example.org"
}
```

```json
{
  "fqdn": "example.org",
  "zone": {
    "items": [
      {
        "rrset_name": "@",
        "rrset_type": "A",
        "rrset_values": [
          "192.0.2.1"
        ]
      }
    ]
  }
}
```

---

## Domain information

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}`

### GET - Show domain's properties

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:automatic_snapshots ⁠booleanTrue if new snapshots are automatically created when a modification is made to this domain's recordsdomain_href ⁠stringdomain_keys_href ⁠stringdomain_records_href ⁠stringfqdn ⁠stringExample:{ "fqdn": "example.com", "domain_href": "https://api.test/v5/livedns/domains/example.com", "domain_records_href": "https://api.test/v5/livedns/domains/example.com/records", "domain_keys_href": "https://api.test/v5/livedns/domains

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
  "fqdn": "example.com",
  "domain_href": "https://api.test/v5/livedns/domains/example.com",
  "domain_records_href": "https://api.test/v5/livedns/domains/example.com/records",
  "domain_keys_href": "https://api.test/v5/livedns/domains/example.com/keys",
  "automatic_snapshots": true
}
```

---

### PATCH - Update domain's properties

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalautomatic_snapshots ⁠booleanEnable or disable the automatic creation of new snapshots when records are changed. Disabling this will improve performance of modifications for domains with a large number of recordsExample:{ "automatic_snapshots": true }

**Body**

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
  "automatic_snapshots": true
}
```

---

## Zone transfer slaves

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/axfr/slaves`

### GET - List current slave's IP addresses

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠array[ string ]A simple list of IP addressesExample:[ "192.0.2.1", "2001:0db8:0000:0000:0000:0000:0000:0001" ]

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
  "192.0.2.1",
  "2001:0db8:0000:0000:0000:0000:0000:0001"
]
```

---

## Zone slaves' IP

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/axfr/slaves/{ip}`

### PUT - Add a new slave IP address to a domain

**URI Parameters**

- fqdn ⁠stringDomain name.ip ⁠stringIP address (v4 or v6)
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

### DELETE - Remove a slave IP address from a domain

**URI Parameters**

- fqdn ⁠stringDomain name.ip ⁠stringIP address (v4 or v6)
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

## TSIG keys associated with a domain

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/axfr/tsig`

### GET - List TSIG keys associated with a domain

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠arrayOf items of type:objectWith the following properties:href ⁠stringURL of the keyid ⁠stringIdentifier of the keykey_name ⁠stringUnique "name" for the key, based on its idExample:[ { "id": "9c87db4b-5624-4547-a006-8ac5c9343c6a", "key_name": "9c87db4b-5624-4547-a006-8ac5c9343c6a.gandi.net", "href": "https://api.test/v5/livedns/domains/example.com/axfr/tsig/9c87db4b-5624-4547-a006-8ac5c9343c6a" } ]

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
    "id": "9c87db4b-5624-4547-a006-8ac5c9343c6a",
    "key_name": "9c87db4b-5624-4547-a006-8ac5c9343c6a.gandi.net",
    "href": "https://api.test/v5/livedns/domains/example.com/axfr/tsig/9c87db4b-5624-4547-a006-8ac5c9343c6a"
  }
]
```

---

## Manage TSIG key association

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/axfr/tsig/{id}`

### PUT - Associate a domain with a TSIG key

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringTSIG identifier
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
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

### DELETE - Remove association between a domain and a TSIG key

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringTSIG identifier
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

## DNSSEC keys

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/keys`

### GET - List DNSSEC keys of a domain

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠arrayOf items of type:objectWith the following properties:algorithm ⁠integerAlgorithm number (see IANA for full list)algorithm_name ⁠stringAlgorithm as "human readable" (eg: ECDSAP256SHA256)deleted ⁠booleanIs this key deleted? (no longer active)ds ⁠stringDS record as RFC1035 line (absolute)flags ⁠integerOne of: 256, 257Key flagsfqdn ⁠stringassociated domain nameid ⁠stringIdentifier of the keykey_href ⁠stringURL of the keystatus ⁠stringCurrent status of the keyExample:[ { "algori

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
    "algorithm": 13,
    "algorithm_name": "ECDSAP256SHA256",
    "deleted": false,
    "ds": "example.com. 3600 IN DS 50651 13 2 01cc01ee6b2750339245aba473340f589356b889a360380e80a11a36824dfb0d",
    "flags": 257,
    "fqdn": "example.com",
    "key_href": "https://api.test/v5/livedns//domains/example.com/keys/key-001",
    "status": "active",
    "id": "key-001"
  }
]
```

---

### POST - Creates a new DNSSEC Key

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredflags ⁠integerOne of: 256, 257Key flags (ZSK=256, KSK=257)Example:{ "flags": 256 }Example:{ "flags": 257 }

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
  "flags": 256
}
```

```json
{
  "flags": 257
}
```

---

## Manipulate a specific DNSSEC key

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/keys/{id}`

### GET - Get information about a key

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringKey identifier
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:algorithm ⁠integerAlgorithm number (see IANA for full list)algorithm_name ⁠stringAlgorithm as "human readable" (eg: ECDSAP256SHA256)deleted ⁠booleanIs this key deleted? (no longer active)ds ⁠stringDS record as RFC1035 line (absolute)fingerprint ⁠stringThe digest of the keyflags ⁠integerOne of: 256, 257Key flagsfqdn ⁠stringassociated domain nameid ⁠stringIdentifier of the keykey_href ⁠stringURL of the keypublic_key ⁠stringPublic part of the key

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
  "algorithm": 13,
  "algorithm_name": "ECDSAP256SHA256",
  "deleted": false,
  "ds": "example.com. 3600 IN DS 50651 13 2 01cc01ee6b2750339245aba473340f589356b889a360380e80a11a36824dfb0d",
  "fingerprint": "ed5317ae0f6726cc694332d2d636e72f7ec616b96475a0cf3dd9801d0d64f619",
  "flags": 257,
  "fqdn": "example.com",
  "id": "key-001",
  "key_href": "https://api.test/v5/livedns//domains/example.com/keys/key-001",
  "public_key": "rtvYYzLKH/O9IlWUyP5/eMNymj1svKZhK9PVcih019T0KyJ99eyfL6VeOVys22+JQ0Xua7b/0B0RNFfEBsIImg==",
  "status": "active",
  "tag": 33695
}
```

---

### PATCH - Undelete a key

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringKey identifier
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireddeleted ⁠booleanOne of: falseExample:{ "deleted": false }

**Body**

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
  "deleted": false
}
```

---

### DELETE - Deletes a key

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringKey identifier
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

## Domain's nameserver information

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/nameservers`

### GET - Retrieve this domain's nameservers

This route returns the list of nameservers that this domain is using according to LiveDNS' systems.

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠array[ string ]List of nameserversExample:[ "ns-154-a.gandi.net", "ns-232-b.gandi.net", "ns-109-c.gandi.net" ]Example:[ "ns1.example.net", "ns2.example.net" ]

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
  "ns-154-a.gandi.net",
  "ns-232-b.gandi.net",
  "ns-109-c.gandi.net"
]
```

```json
[
  "ns1.example.net",
  "ns2.example.net"
]
```

---

## Domain's records

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/records`

### GET - List records associated with a domain

**URI Parameters**

- fqdn ⁠stringDomain name.
- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.rrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"Filter records by typesort_by ⁠stringDefault: "rrset_name"
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/plain value, this route will return The contents of the zone as it would appear in a standard master zone file (see RFC1035)

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:rrset_href ⁠stringURL for the recordrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds tha
- text/plain⁠stringThe contents of the zone as it would appear in a standard master zone file (see RFC1035)

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
    "rrset_name": "@",
    "rrset_ttl": 10800,
    "rrset_type": "A",
    "rrset_values": [
      "192.0.2.1"
    ],
    "rrset_href": "https://api.test/v5/livedns/domains/example.com/records/%40/A"
  },
  {
    "rrset_name": "www",
    "rrset_ttl": 10800,
    "rrset_type": "CNAME",
    "rrset_values": [
      "www.example.net."
    ],
    "rrset_href": "https://api.test/v5/livedns/domains/example.com/records/www/CNAME"
  }
]
```

---

### POST - Creates a new record

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this recordExample:{ 

**Headers**

- Location ⁠stringURL of record
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Headers**

- Location ⁠stringURL of record
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

```json
{
  "rrset_name": "www",
  "rrset_type": "A",
  "rrset_values": [
    "192.0.2.1"
  ]
}
```

```json
{
  "rrset_name": "www",
  "rrset_type": "AAAA",
  "rrset_values": [
    "2001:db8::1",
    "2001:db8::2"
  ]
}
```

```json
{
  "rrset_name": "@",
  "rrset_type": "TXT",
  "rrset_values": [
    "\"v=spf1 include:_mailcust.gandi.net ?all\""
  ]
}
```

---

### PUT - Replace the whole zone with new records

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireditems ⁠arrayOf items of type:objectWith the following properties:Requiredrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000
- text/plain⁠stringThe contents of the zone as it would appear in a standard master zone file (see RFC1035)

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
  "items": [
    {
      "rrset_name": "www",
      "rrset_type": "A",
      "rrset_values": [
        "192.0.2.1"
      ]
    },
    {
      "rrset_name": "www",
      "rrset_type": "AAAA",
      "rrset_values": [
        "2001:db8::1",
        "2001:db8::2"
      ]
    },
    {
      "rrset_name": "@",
      "rrset_type": "TXT",
      "rrset_values": [
        "\"v=spf1 include:_mailcust.gandi.net ?all\""
      ]
    }
  ]
}
```

---

### DELETE - Delete all records

**URI Parameters**

- fqdn ⁠stringDomain name.
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

## Domain's records, by name

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/records/{rrset_name}`

### GET - Zone records list {rrset_name} linked to a domain

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠arrayOf items of type:objectWith the following properties:rrset_href ⁠stringURL for the recordrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds tha

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
    "rrset_name": "www",
    "rrset_type": "A",
    "rrset_values": [
      "192.0.2.1"
    ],
    "rrset_ttl": 320,
    "rrset_href": "https://api.test/v5/livedns/domains/example.com/records/www/A"
  },
  {
    "rrset_name": "www",
    "rrset_type": "TXT",
    "rrset_values": [
      "some-text-value"
    ],
    "rrset_ttl": 320,
    "rrset_href": "https://api.test/v5/livedns/domains/example.com/records/www/TXT"
  }
]
```

---

### POST - Create a new record whose name is defined by the path

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this recordExample:{ "rrset_type": "A", "rrset_values": [

**Headers**

- Location ⁠stringURL of record
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Headers**

- Location ⁠stringURL of record
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

```json
{
  "rrset_type": "A",
  "rrset_values": [
    "192.0.2.1"
  ]
}
```

```json
{
  "rrset_type": "AAAA",
  "rrset_values": [
    "2001:db8::1",
    "2001:db8::2"
  ]
}
```

```json
{
  "rrset_type": "TXT",
  "rrset_values": [
    "some-text-value"
  ]
}
```

---

### PUT - Replace all records named {rrset_name}

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requireditems ⁠arrayOf items of type:objectWith the following properties:Requiredrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolve

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
  "items": [
    {
      "rrset_type": "A",
      "rrset_values": [
        "192.0.2.1"
      ]
    },
    {
      "rrset_type": "AAAA",
      "rrset_values": [
        "2001:db8::1",
        "2001:db8::2"
      ]
    },
    {
      "rrset_type": "TXT",
      "rrset_values": [
        "some-text-value"
      ]
    }
  ]
}
```

---

### DELETE - Delete all records named {rrset_name}

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.
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

## Single domain's record, by name and type

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/records/{rrset_name}/{rrset_type}`

### GET - Get a single single record with its name and type

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.rrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"Type of the record
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:rrset_href ⁠stringURL for the recordrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should

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
  "rrset_name": "www",
  "rrset_type": "CNAME",
  "rrset_values": [
    "www.example.net"
  ],
  "rrset_ttl": 10800,
  "rrset_href": "https://api.test/v5/livedns/domains/example.com/records/www/CNAME"
}
```

---

### PATCH - Update a record (RRset) in the zone records linked to a domain

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.rrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"Type of the record
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionaladd_rrset_values ⁠arrayDefault: []Resource record set values to add in a DNS zone.Of items of type:stringMaximum length: 16384Pattern: ^[\x20-\x7E]+$remove_rrset_values ⁠arrayDefault: []Resource record set values to remove from a DNS zone.Of items of type:stringMaximum length: 16384Pattern: ^[\x20-\x7E]+$rrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this record.Example:{ "add_rrset_va

**Body**

- application/json⁠objectWith the following properties:rrset_href ⁠stringURL for the recordrrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"rrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should

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
  "add_rrset_values": [
    "www.example.org."
  ],
  "rrset_ttl": 11000
}
```

```json
{
  "rrset_name": "www",
  "rrset_type": "CNAME",
  "rrset_values": [
    "www.example.org."
  ],
  "rrset_ttl": 11000,
  "rrset_href": "https://api.test/v5/livedns/domains/example.com/records/www/CNAME"
}
```

---

### POST - Create a new record whose name and type are defined by the path

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.rrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"Type of the record
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredrrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this recordExample:{ "rrset_values": [ "www.example.org" ], "rrset_ttl": 320 }

**Headers**

- Location ⁠stringURL of record
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Headers**

- Location ⁠stringURL of record
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

```json
{
  "rrset_values": [
    "www.example.org"
  ],
  "rrset_ttl": 320
}
```

---

### PUT - Overwrites a single record with {rrset_name} and {rrset_type}

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.rrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"Type of the record
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredrrset_values ⁠array[ string ]A list of values for this recordOptionalrrset_ttl ⁠integerMinimum: 300Maximum: 2592000The time in seconds that DNS resolvers should cache this recordExample:{ "rrset_values": [ "www.example.org" ], "rrset_ttl": 320 }

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
  "rrset_values": [
    "www.example.org"
  ],
  "rrset_ttl": 320
}
```

---

### DELETE - Delete record with {rrset_name} and {rrset_type}

**URI Parameters**

- fqdn ⁠stringDomain name.rrset_name ⁠stringName of the record.rrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC", "MX", "NAPTR", "NS", "OPENPGPKEY", "PTR", "RP", "SOA", "SPF", "SRV", "SSHFP", "SVCB", "TLSA", "TXT", "WKS"Type of the record
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

## Snapshots of a domain

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/snapshots`

### GET - List available snapshots

**URI Parameters**

- fqdn ⁠stringDomain name.
- Optionalautomatic ⁠booleanOnly list automatic/non-automatic snapshotspage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.sort_by ⁠stringOne of: "date_created", "-date_created"Default: "date_created"Allow sorting result by creation date or reverse creation date
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:automatic ⁠booleantrue if the snapshot was automatically created after a zone changecreated_at ⁠stringCreation date of the snapshot (UTC)href ⁠stringURL of the snapshotid ⁠stringIdentifier of the snapshotname ⁠stringName of the snapshotExample:[ { "id": "f975042c-e219-11ea-b22b-00163e867a15", "name": "My new snapshot", "created_at": "2019-08-30T12:44:41Z", "automatic": false, "href": "http://api.test/v5/livedns/domains/ex

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
    "id": "f975042c-e219-11ea-b22b-00163e867a15",
    "name": "My new snapshot",
    "created_at": "2019-08-30T12:44:41Z",
    "automatic": false,
    "href": "http://api.test/v5/livedns/domains/example.com/snapshots/f975042c-e219-11ea-b22b-00163e867a15"
  }
]
```

---

### POST - Creates a new snapshot

**URI Parameters**

- fqdn ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalname ⁠stringOptional name for the snapshot. When not specified, the name will be today's date with an incremental number added to itExample:{ "name": "My new snapshot" }

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:id ⁠stringIdentifier of the snapshotmessage ⁠stringConfirmation message.

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
  "name": "My new snapshot"
}
```

---

## Snapshots operations

**URL:** `https://api.gandi.net/v5/livedns/domains/{fqdn}/snapshots/{id}`

### GET - Snapshot details

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringSnapshot identifier
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/plain value, this route will return The contents of the snapshot as it would appear in a standard master zone file (see RFC1035)

**Body**

- application/json⁠objectWith the following properties:automatic ⁠booleantrue if the snapshot was automatically created after a zone changecreated_at ⁠stringCreation date of the snapshot (UTC)href ⁠stringURL of the snapshotid ⁠stringIdentifier of the snapshotname ⁠stringName of the snapshotzone_data ⁠arrayOf items of type:objectWith the following properties:rrset_name ⁠stringName of the recordrrset_type ⁠stringOne of: "A", "AAAA", "ALIAS", "CAA", "CDS", "CNAME", "DNAME", "DS", "HTTPS", "KEY", "LOC
- text/plain⁠stringThe contents of the zone as it would appear in a standard master zone file (see RFC1035)

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
  "name": "My new snapshot",
  "id": "f975042c-e219-11ea-b22b-00163e867a15",
  "created_at": "2022-12-15T15:20:03Z",
  "href": "http://api.test/v5/livedns/domains/example.com/snapshots/f975042c-e219-11ea-b22b-00163e867a15",
  "automatic": true,
  "zone_data": [
    {
      "rrset_name": "@",
      "rrset_type": "A",
      "rrset_ttl": 10800,
      "rrset_values": [
        "192.0.2.1"
      ]
    },
    {
      "rrset_name": "@",
      "rrset_type": "MX",
      "rrset_ttl": 10800,
      "rrset_values": [
        "10 spool.mail.gandi.net.",
        "50 fb.mail.gandi.net."
      ]
    },
    {
      "rrset_name": "@",
      "rrset_type": "TXT",
      "rrset_ttl": 10800,
      "rrset_values": [
        "\"v=spf1 include:_mailcust.gandi.net ?all\""
      ]
    },
    {
      "rrset_name": "www",
      "rrset_type": "CNAME",
      "rrset_ttl": 10800,
      "rrset_values": [
        "webredir.vip.gandi.net."
      ]
    }
  ]
}
```

---

### PATCH - Update a snapshot

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringSnapshot identifier
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredname ⁠stringNew snapshot nameExample:{ "name": "Snapshot by SRE on 2022-02-06" }

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
  "name": "Snapshot by SRE on 2022-02-06"
}
```

---

### DELETE - Delete a snapshot

**URI Parameters**

- fqdn ⁠stringDomain name.id ⁠stringSnapshot identifier
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

## Generic nameservers

**URL:** `https://api.gandi.net/v5/livedns/nameservers/{fqdn}`

### GET - Retrieve the generic (hashed) nameservers

This route returns the list of nameservers that this domain is using according to LiveDNS' systems when no NS resource record exists in the zone for that domain

This is a generic route for hashing any domain and thus is not authenticated.

To retrieve the nameservers that takes into account any NS resource records in the domain's zone, use the authenticated version instead.

**URI Parameters**

- fqdn ⁠stringDomain name.

**Body**

- application/json⁠array[ string ]List of nameservers

---


