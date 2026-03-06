# Organization API

**Base URL:** `https://api.gandi.net/v5/organization`

## Renew a Personal Access Token (PAT)

**URL:** `https://api.gandi.net/v5/organization/access-tokens`

### POST - Renew the current personal access token

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalexpires_at ⁠stringNew expiration date. By default, the same TTL as the current PAT is applied.name ⁠stringNew name for the token.Example:{ "name": "Certbot" }

**Body**

- application/json⁠objectWith the following properties:access_token ⁠stringthe secret token that should be saved safely.entities ⁠arrayscoped entities of the tokenOf items of type:objectWith the following properties:id ⁠stringUnique identifier of the scoped entity.name ⁠stringName of the scoped entity.type ⁠stringType of the scoped entity.expires_at ⁠datetimeexpiration date of the new tokenid ⁠stringID of the Personal Access Token.name ⁠stringhuman readable name of the Personal Access Token.scopes

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
  "name": "Certbot"
}
```

---

## Organization Management

**URL:** `https://api.gandi.net/v5/organization/organizations`

### GET - List organizations

**Query String**

- Optional~name ⁠stringFilters the list by a name pattern.Example: *liceExample: alic*name ⁠stringFilters the list by exact name.permission ⁠stringFilters the list by the permission the authenticated user has on that organization and products in it.sort_by ⁠stringOne of: "name", "type", "id"Default: "name"Used to specify how you want the results sorted.type ⁠stringOne of: "individual", "company", "association", "publicbody"Filters the list by type of organization.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠arrayOf items of type:objectWith the following properties:id ⁠stringThe main identifier of the organization. Also known as sharing_id in many routes.name ⁠stringUnique name of the organization.Optionalcorporate ⁠booleanFlag to indicate the corporate status for the organization.email ⁠stringThe email address of the organization.firstname ⁠stringThe first name of the organization.lastname ⁠stringThe last name of the organization.orgname ⁠stringThe company, association, or public b

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
    "name": "alice",
    "firstname": "Alice",
    "lastname": "Doe",
    "id": "80548b45-e18d-4cab-adef-e10a8406de4a",
    "reseller": false,
    "corporate": true,
    "type": "individual",
    "email": "alice@example.net"
  },
  {
    "name": "bob",
    "firstname": "Bob",
    "orgname": "Bob's Roads",
    "lastname": "Doe",
    "email": "bob@example.net",
    "reseller": false,
    "corporate": false,
    "type": "publicbody",
    "id": "e1ab1204-e638-4fd8-85a4-34dd95013cdc"
  },
  {
    "name": "ron",
    "firstname": "Ron",
    "orgname": "Ron Inc.",
    "lastname": "Doe",
    "email": "ron@example.net",
    "reseller": false,
    "corporate": false,
    "type": "company",
    "id": "b018061c-a4e3-4d6d-8445-e3837bd23815"
  }
]
```

---

### POST - Create an organization

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredcity ⁠stringthe city name of the address.email ⁠stringThe email address of the organization.firstname ⁠stringThe first name of the organization.lastname ⁠stringThe last name of the organization.name ⁠stringUnique name of the organization.orgname ⁠stringThe company, association, or public body name of the organization.phone ⁠stringphone number.streetaddr ⁠stringthe street address of the organization.type ⁠stringOne of: "company", "assoc

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:id ⁠stringCreated Organization ID.message ⁠stringConfirmation message.

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
  "type": "company",
  "name": "Poppy Red LLC",
  "firstname": "John",
  "lastname": "Do",
  "orgname": "Poppy Red LLC",
  "email": "jd@example.net",
  "streetaddr": "42 Rue du Soleil Levant",
  "zip": "17000",
  "city": "La Rochelle",
  "country": "FR",
  "state": "FR-NAQ",
  "phone": "+33.612345678",
  "reseller": false
}
```

---

## /v5/organization/organizations/{org_id}

**URL:** `https://api.gandi.net/v5/organization/organizations/{org_id}`

### GET - Show organization information

**URI Parameters**

- org_id ⁠stringOrganization ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:city ⁠stringthe city name of the address.corporate ⁠booleanFlag set for corporate organization.country ⁠stringcountry ISO code of the address.email ⁠stringthe email address of the organization.firstname ⁠stringthe first name of the organization.id ⁠stringthe sharing id of the organization.lastname ⁠stringthe last name of the organization.name ⁠stringthe sharing name of the organization.reseller ⁠booleanFlag set for reseller organization.street

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### PATCH - Update an organization

**URI Parameters**

- org_id ⁠stringOrganization ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalcity ⁠stringthe city name of the address.country ⁠stringcountry (ISO 3166-1 alpha-2) code of the address.email ⁠stringThe email address of the organization.fax ⁠stringfax number.firstname ⁠stringThe first name of the organization.lang ⁠stringOne of: "en", "es", "fr", "ja", "zh-hans", "zh-hant"language code of the organization for emails.lastname ⁠stringThe last name of the organization.name ⁠stringUnique name of the organization.phone 

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

### DELETE - Delete an organization

**URI Parameters**

- org_id ⁠stringOrganization ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:message ⁠stringExplanation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Actions on organization customers

**URL:** `https://api.gandi.net/v5/organization/organizations/{org_id}/action`

### POST - 

**URI Parameters**

- org_id ⁠stringOrganization ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredaction ⁠stringOne of: "release_resellee"params ⁠objectWith the following properties:Requiredid ⁠stringIdentifier of the customer to releaseExample:{ "action": "release_resellee", "params": { "id": "000000000000-0000-0000-0000-000000000000" } }

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:message ⁠stringConfirmation message.

**Body**

- application/json⁠objectWith the following properties:message ⁠stringAccepted.

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
  "action": "release_resellee",
  "params": {
    "id": "000000000000-0000-0000-0000-000000000000"
  }
}
```

---

## Management Of Customers Under a Reseller Organization

**URL:** `https://api.gandi.net/v5/organization/organizations/{org_id}/customers`

### GET - List customers

**URI Parameters**

- org_id ⁠stringOrganization ID.
- Optionalname ⁠stringFilters the list by name, with optional patterns.Example: *liceExample: alic*page ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.permission ⁠stringFilters the list by the permission the authenticated user has on that organization and products in it.sort_by ⁠stringOne of: "name", "type", "id"Default: "name"Used to specify how you want
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:email ⁠stringEmail of the customer.firstname ⁠stringFirst name of the customer.id ⁠stringThe main identifier of the customer. Also known as sharing_id in many routes.lastname ⁠stringLast name of the customer.name ⁠stringName of the customer.type ⁠stringOne of: "individual", "company", "association", "publicbody"Type of the customer organization.Optionalorgname ⁠stringOrganization legal name of the customer.Example:[ { "id

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
    "id": "80548b45-e18d-4cab-adef-e10a8406de4a",
    "name": "alice",
    "firstname": "Alice",
    "lastname": "Doe",
    "type": "individual",
    "email": "alice@example.net"
  },
  {
    "id": "e1ab1204-e638-4fd8-85a4-34dd95013cdc",
    "name": "bob",
    "firstname": "Bob",
    "lastname": "Doe",
    "type": "publicbody",
    "orgname": "Bob's Roads",
    "email": "bob@example.net"
  },
  {
    "id": "b018061c-a4e3-4d6d-8445-e3837bd23815",
    "name": "ron",
    "firstname": "Ron",
    "lastname": "Doe",
    "type": "company",
    "orgname": "Ron Inc.",
    "email": "ron@example.net"
  }
]
```

---

### POST - Create a new customer

**URI Parameters**

- org_id ⁠stringOrganization ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredcity ⁠stringcountry ⁠stringCountry code.email ⁠stringfirstname ⁠stringFirst name.lastname ⁠stringLast name.phone ⁠stringstreetaddr ⁠stringStreet address.type ⁠stringOne of: "individual", "company", "association", "publicbody"Type of the customer organization.Optionalfax ⁠stringorgname ⁠stringOrganization legal name.reference ⁠stringOptional text to display on the invoice, such as your own customer reference info.state ⁠stringState/Prov

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:id ⁠stringCreated customer ID.message ⁠stringConfirmation message.

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
  "type": "company",
  "firstname": "John",
  "lastname": "Do",
  "orgname": "R&D",
  "email": "jd@example.net",
  "streetaddr": "21 jump street",
  "streetaddr2": "Appt31",
  "zip": "17137",
  "city": "Nieul-sur-mer",
  "country": "FR",
  "state": "FR-NAQ",
  "phone": "+33.612345678",
  "fax": "+33.612345699",
  "reference": "abc/3458"
}
```

---

## Management Of A Customer Under a Reseller Organization

**URL:** `https://api.gandi.net/v5/organization/organizations/{org_id}/customers/{id}`

### GET - Show customer's information

**URI Parameters**

- org_id ⁠stringOrganization ID.id ⁠stringCustomer ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:city ⁠stringthe city name of the address.country ⁠stringcountry ISO code of the address.email ⁠stringEmail of the customer.firstname ⁠stringFirst name of the customer.id ⁠stringThe main identifier of the customer. Also known as sharing_id in many routes.lastname ⁠stringLast name of the customer.name ⁠stringName of the customer.streetaddr ⁠stringthe street address of the user.type ⁠stringOne of: "individual", "company", "association", "publicbo

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
  "id": "80548b45-e18d-4cab-adef-e10a8406de4a",
  "name": "alice",
  "firstname": "Alice",
  "lastname": "Doe",
  "type": "individual",
  "email": "alice@example.net",
  "streetaddr": "5000 Fraise",
  "zip": "17540",
  "city": "Les Rivieres d'Anais",
  "country": "FR"
}
```

---

### PATCH - Update customer's information

**URI Parameters**

- org_id ⁠stringOrganization ID.id ⁠stringCustomer ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalcity ⁠stringthe city name of the address.country ⁠stringcountry (ISO 3166-1 alpha-2) code of the address.email ⁠stringThe email address of the customer.fax ⁠stringfax number.firstname ⁠stringThe first name of the customer; clients with type 'individual' cannot update their firstname.lang ⁠stringOne of: "en", "es", "fr", "ja", "zh-hans", "zh-hant"language code of the organization for emails.lastname ⁠stringThe last name of the customer;

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
  "email": "hello@example.net",
  "sync_contact_email": "match"
}
```

```json
{
  "reference": "POPPYRED500"
}
```

---

### DELETE - Delete customer

**URI Parameters**

- org_id ⁠stringOrganization ID.id ⁠stringCustomer ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:message ⁠stringExplanation message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Authenticated User Information

**URL:** `https://api.gandi.net/v5/organization/user-info`

### GET - Get user information

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:city ⁠stringthe city name of the address.email ⁠stringthe email address of the user.id ⁠stringthe sharing id of the user.lang ⁠stringlanguage used by the user.name ⁠stringthe sharing name of the user.username ⁠stringthe username of the user.Optionalcountry ⁠stringcountry ISO code of the address.fax ⁠stringfax number.firstname ⁠stringthe first name of the user.lastname ⁠stringthe last name of the user.phone ⁠stringphone number.state ⁠stringstat

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
  "id": "ebfcd3cd-e014-4a3d-8216-6e342f227c3d",
  "username": "alice",
  "email": "alice@example.org",
  "name": "alice",
  "firstname": "Alice",
  "lastname": "Doe",
  "streetaddr": "5 rue neuve",
  "zip": "75001",
  "city": "Paris",
  "state": "FR-IDF",
  "country": "FR",
  "phone": "+33.123456789",
  "lang": "en"
}
```

---


