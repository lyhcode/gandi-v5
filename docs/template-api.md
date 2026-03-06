# Template API

**Base URL:** `https://api.gandi.net/v5/template`

## Dispatch

**URL:** `https://api.gandi.net/v5/template/dispatch/{id}`

### GET - Dispatch information

This route returns the current state of a template dispatch. It provides the payload as it was given to the dispatch, the state, and the history of each operation.

The current state of the dispatch is indicated by two values:

The state values take 4 possible values:

A dispatch is not running any longer when one of these conditions are met:

**URI Parameters**

- id ⁠stringDispatch ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:attempt ⁠integerCurrent number of attempts at performing the tasks.created_at ⁠stringid ⁠stringpayload ⁠objectThe template payload as it was when it was applied. This is the only source of data for a dispatch which means that when you change a template's payload it will never affect the related running dispatches.With the following properties:Optionaldns:records ⁠objectThis namespace defines the DNS records that will be set on a domain. It is 

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
  "sharing_id": "fe0b931c-18c5-11e9-b9b5-00163ec4cb00",
  "payload": {
    "domain:nameservers": {
      "addresses": [],
      "service": "livedns"
    },
    "dns:records": {
      "default": true
    }
  },
  "id": "0f7326c2-0264-11eb-b47b-00163e7504b8",
  "state": 0,
  "target_id": "ba1167be-2f76-11e9-9dfb-00163ec4cb00",
  "template_id": "881f8c9a-fe7d-11ea-b2fe-00163e7504b8",
  "task_history": [
    {
      "namespace": "dns:records",
      "date": "2020-09-29T14:57:47Z",
      "message": "",
      "status": 20
    },
    {
      "namespace": "domain:nameservers",
      "date": "2020-09-29T14:58:48Z",
      "message": "",
      "status": 20
    }
  ],
  "target": {
    "type": "domain",
    "name": "domain-api-test1.net"
  },
  "attempt": 1,
  "task_status": {
    "domain:nameservers": {
      "status": 20
    },
    "dns:records": {
      "status": 20
    }
  },
  "template_name": "test",
  "state_msg": "",
  "created_at": "2020-09-29T14:57:14Z",
  "task_updated_at": "2020-09-29T14:58:48Z"
}
```

---

## Templates

**URL:** `https://api.gandi.net/v5/template/templates`

### GET - List of templates

**Query String**

- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:description ⁠stringTemplate purpose's description.editable ⁠booleantrue when you can edit the template.href ⁠stringAPI URL to the template's details.id ⁠stringTemplate ID.name ⁠stringTemplate's name.namespaces ⁠array[ string ]A list of namespaces that this template implements. The possible values are the keys of a template's payload, as described in the creation route.orgname ⁠stringOptionalsharing_space ⁠objectWith the f

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Create a new template

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredname ⁠stringTemplate's name. Please note that this name must be unique within an organization.payload ⁠objectThe payload is the actual "recipe" of your template. Each property, or namespace, is optional.With the following properties:Optionaldns:records ⁠objectThis namespace defines the DNS records that will be set on a domain. It is only usefull when the domain is using LiveDNS. Even though it is not required, it's best to combine it w

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
  "name": "test",
  "payload": {
    "domain:nameservers": {
      "addresses": [],
      "service": "livedns"
    },
    "dns:records": {
      "records": [
        {
          "type": "A",
          "name": "@",
          "values": [
            "203.0.113.1"
          ]
        },
        {
          "type": "MX",
          "name": "@",
          "ttl": 10800,
          "values": [
            "10 spool.mail.gandi.net.",
            "50 fb.mail.gandi.net."
          ]
        }
      ]
    }
  }
}
```

```json
{
  "name": "test",
  "payload": {
    "domain:mailboxes": {
      "values": [
        {
          "login": "alice"
        },
        {
          "login": "contact"
        }
      ]
    }
  }
}
```

```json
{
  "name": "test",
  "payload": {
    "domain:webredirs": {
      "values": [
        {
          "type": "http301",
          "host": "www",
          "url": "https://www.gandi.net/"
        }
      ]
    }
  }
}
```

---

## Template management

**URL:** `https://api.gandi.net/v5/template/templates/{id}`

### GET - Template details

**URI Parameters**

- id ⁠stringTemplate ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:description ⁠stringTemplate purpose's description.editable ⁠booleantrue when you can edit the template.href ⁠stringAPI URL to the template's details.id ⁠stringTemplate ID.name ⁠stringTemplate's name.namespaces ⁠array[ string ]A list of namespaces that this template implements. The possible values are the keys of a template's payload, as described in the creation route.orgname ⁠stringpayload ⁠objectWith the following properties:Optionaldns:reco

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
  "payload": {
    "domain:nameservers": {
      "addresses": [],
      "service": "livedns"
    },
    "dns:records": {
      "default": true
    }
  },
  "id": "881f8c9a-fe7d-11ea-b2fe-00163e7504b8",
  "editable": true,
  "orgname": "my-organization",
  "description": "",
  "namespaces": [
    "domain:nameservers",
    "dns:records"
  ],
  "variables": [],
  "sharing_space": {
    "id": "fe0b931c-18c5-11e9-b9b5-00163ec4cb00",
    "name": "my-organization"
  },
  "name": "test",
  "href": "http://api.test/v5/template/templates/881f8c9a-fe7d-11ea-b2fe-00163e7504b8"
}
```

---

### PATCH - Edit a template

**URI Parameters**

- id ⁠stringTemplate ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionaldescription ⁠stringTemplate description.name ⁠stringTemplate's name. Please note that this name must be unique within an organization.payload ⁠objectThe payload is the actual "recipe" of your template. Each property, or namespace, is optional.With the following properties:Optionaldns:records ⁠objectThis namespace defines the DNS records that will be set on a domain. It is only usefull when the domain is using LiveDNS. Even though it is

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
  "payload": {
    "domain:nameservers": {
      "addresses": [],
      "service": "livedns"
    },
    "dns:records": {
      "default": true
    }
  }
}
```

---

### DELETE - Delete a template

**URI Parameters**

- id ⁠stringTemplate ID.
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

### POST - Apply a template

This route applies a template to a domain. You must send the parameter object_type to domain and the object_id to a domain id, that you'll find in the domain list.

The response will contain a location header containing the API URL of the operation being performed. Refer to our dispatch documentation for more information.

**URI Parameters**

- id ⁠stringTemplate ID.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredobject_id ⁠stringThe ID of the object to which the template applies.object_type ⁠stringOne of: "domain"The object type to which the template applies. For now, only domain is available.Example:{ "object_type": "domain", "object_id": "ba1167be-2f76-11e9-9dfb-00163ec4cb00" }

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:dispatch_href ⁠stringThe API URL to the operation being performed.message ⁠stringConfirmation message.payload ⁠objectWith the following properties:Optionaldns:records ⁠objectThis namespace defines the DNS records that will be set on a domain. It is only usefull when the domain is using LiveDNS. Even though it is not required, it's best to combine it with the domain:namservers namespace and set its service to livedns.Both properties default and

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
  "object_type": "domain",
  "object_id": "ba1167be-2f76-11e9-9dfb-00163ec4cb00"
}
```

---


