# Domain API

**Base URL:** `https://api.gandi.net/v5/domain`

## Domain Change Owner

**URL:** `https://api.gandi.net/v5/domain/changeowner/{domain}`

### POST - Initiate a change owner

This route is used to start a domain ownership change. Keep in mind that this is not always a free operation. Please check pricing before launching this operation and ensure your prepaid account has enough credit.

Warning: For domain, that is part of Website Pack subscription. Changing the owner will remove the domain name from the subscription. Completing this action during the two months following domain creation will result in your Website Pack being split and the domain being made unavailable. Your hosting subscription will continue as a monthly payment. You can stop your hosting subscription at any time.

**URI Parameters**

- domain ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredowner ⁠objectWith the following properties:Requiredcountry ⁠stringA country code. See the country code list for possible values.email ⁠stringfamily ⁠stringContact's family name (usualy the lastname)given ⁠stringContact's given name (usualy the firstname)streetaddr ⁠stringtype ⁠stringOne of: "individual", "company", "association", "publicbody", "reseller"Optionalbrand_number ⁠stringcity ⁠stringdata_obfuscated ⁠booleanDefault: trueLearn 

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
  "owner": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "data_obfuscated": true,
    "mail_obfuscated": true,
    "phone": "+33.123456789",
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  }
}
```

---

### GET - Change Owner followup.

**URI Parameters**

- domain ⁠string
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:created_at ⁠datetimeparams ⁠objectWith the following properties:Optionalanswer_new_owner ⁠stringanswer_old_owner ⁠stringinner_step ⁠stringnew_owner_email ⁠stringold_admin_email ⁠stringold_owner_email ⁠stringstep ⁠stringstep_nb ⁠integerupdated_at ⁠datetimeOptionaldate_start ⁠stringerrortype ⁠stringerrortype_label ⁠stringfoa ⁠arrayOf items of type:objectWith the following properties:answer ⁠stringemail ⁠stringinner_step ⁠stringExample:{ "created

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
  "created_at": "2021-01-20T00:00:00Z",
  "updated_at": "2021-01-20T00:00:00Z",
  "inner_step": "checking_foa_response",
  "step": "WAIT",
  "step_nb": 2,
  "params": {
    "answer_new_owner": "T",
    "answer_old_owner": "T",
    "inner_step": "checking_foa_response",
    "new_owner_email": "alice@example.org",
    "old_owner_email": "john@doe.com"
  }
}
```

---

## Resend the change owner FOA emails

**URL:** `https://api.gandi.net/v5/domain/changeowner/{domain}/foa`

### POST - Resend the change owner FOA emails

**URI Parameters**

- domain ⁠string
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredemail ⁠stringExample:{ "email": "alice@example.org" }

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
  "email": "alice@example.org"
}
```

---

## Domain Availability

**URL:** `https://api.gandi.net/v5/domain/check`

### GET - Domain availability

**Query String**

- Requiredname ⁠stringdomain name to queryOptionalcountry ⁠stringISO country code for which taxes are to be appliedcurrency ⁠stringrequest price for a specific ISO currency codeduration_unit ⁠stringdefine the unit for max_durationextension ⁠stringquery a specific extension for product optionsgrid ⁠stringrequest price for a specific ratelang ⁠stringlanguage codemax_duration ⁠integerset a limit on the duration range for returned pricesperiod ⁠stringspecific registration period to queryprocesses ⁠arr
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:currency ⁠stringgrid ⁠stringproducts ⁠arrayOf items of type:objectWith the following properties:name ⁠stringproduct nameprices ⁠arrayOf items of type:objectWith the following properties:duration_unit ⁠stringtime unit for durationmax_duration ⁠integermaximum duration for which this price unit appliesmin_duration ⁠integerminimum duration for which this price unit appliesprice_after_taxes ⁠numberpricing after tax is appliedprice_before_taxes ⁠num

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```
?name=example.com
```

```
?name=example.com&processes=create&processes=transfer&grid=C
```

```json
{
  "currency": "EUR",
  "grid": "A",
  "products": [
    {
      "status": "available",
      "periods": [
        {
          "name": "eap5",
          "starts_at": "2019-02-25T16:00:00Z",
          "ends_at": "2020-03-28T15:59:59Z"
        },
        {
          "name": "golive",
          "starts_at": "2020-03-28T16:00:00Z"
        }
      ],
      "name": "example.com",
      "process": "create",
      "taxes": [
        {
          "type": "service",
          "rate": 20,
          "name": "vat"
        }
      ],
      "prices": [
        {
          "max_duration": 1,
          "duration_unit": "y",
          "min_duration": 1,
          "discount": false,
          "price_after_taxes": 878.44,
          "price_before_taxes": 732.03,
          "type": "premium"
        },
        {
          "max_duration": 1,
          "duration_unit": "y",
          "min_duration": 1,
          "discount": false,
          "price_after_taxes": 775.12,
          "price_before_taxes": 645.93,
          "type": "premium"
        }
      ]
    }
  ],
  "taxes": [
    {
      "type": "service",
      "rate": 20,
      "name": "vat"
    }
  ]
}
```

```json
{
  "currency": "EUR",
  "grid": "C",
  "products": [
    {
      "status": "available",
      "name": "example.com",
      "process": "transfer",
      "taxes": [
        {
          "type": "service",
          "rate": 20,
          "name": "vat"
        }
      ],
      "prices": [
        {
          "max_duration": 1,
          "duration_unit": "y",
          "min_duration": 1,
          "discount": false,
          "price_after_taxes": 7.2,
          "price_before_taxes": 6
        }
      ]
    },
    {
      "status": "available",
      "name": "example.com",
      "process": "create",
      "taxes": [
        {
          "type": "service",
          "rate": 20,
          "name": "vat"
        }
      ],
      "prices": [
        {
          "max_duration": 2,
          "duration_unit": "y",
          "normal_price_after_taxes": 11.04,
          "min_duration": 1,
          "discount": true,
          "price_after_taxes": 5.52,
          "normal_price_before_taxes": 9.2,
          "price_before_taxes": 4.6
        },
        {
          "max_duration": 10,
          "duration_unit": "y",
          "normal_price_after_taxes": 9.38,
          "min_duration": 3,
          "discount": true,
          "price_after_taxes": 4.69,
          "normal_price_before_taxes": 7.82,
          "price_before_taxes": 3.91
        }
      ]
    }
  ],
  "taxes": [
    {
      "type": "service",
      "rate": 20,
      "name": "vat"
    }
  ]
}
```

---

## Domain Create and List

**URL:** `https://api.gandi.net/v5/domain/domains`

### GET - List domains

**Query String**

- Optionalfqdn ⁠stringFilters the list by domain name, with optional patterns.Example: example.netExample: example.*Example: *example.comnameserver ⁠stringOne of: "abc", "livedns", "other"Used to filter the type of nameserverspage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.resellee_id ⁠stringFilter the list by resellee_id, from the Organization APIExa
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/csv value, this route will return a CSV-formatted response.

**Headers**

- Filtered-Count ⁠integerOn a filtered list, this is the number of matching items.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:autorenew ⁠booleanAutomatic renewal status. Learn more about automatic renewal.dates ⁠objectDomain's life cycle dates.With the following properties:registry_created_at ⁠datetimeupdated_at ⁠datetimeOptionalauthinfo_expires_at ⁠datetimecreated_at ⁠datetimedeletes_at ⁠datetimehold_begins_at ⁠datetimehold_ends_at ⁠datetimepending_delete_ends_at ⁠datetimeregistry_ends_at ⁠datetimerenew_begins_at ⁠datetimerestore_ends_at ⁠datet
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
    "status": [
      "clientTransferProhibited"
    ],
    "dates": {
      "created_at": "2019-02-13T11:04:18Z",
      "registry_created_at": "2019-02-13T10:04:18Z",
      "registry_ends_at": "2021-02-13T10:04:18Z",
      "updated_at": "2019-02-25T16:20:49Z"
    },
    "tags": [],
    "fqdn": "example.net",
    "id": "ba1167be-2f76-11e9-9dfb-00163ec4cb00",
    "autorenew": false,
    "tld": "net",
    "owner": "alice_doe",
    "orga_owner": "alice_doe",
    "domain_owner": "Alice Doe",
    "nameserver": {
      "current": "livedns"
    },
    "href": "https://api.test/v5/domain/domains/example.net",
    "fqdn_unicode": "example.net"
  },
  {
    "status": [],
    "dates": {
      "created_at": "2019-01-15T14:19:59Z",
      "registry_created_at": "2019-01-15T13:19:58Z",
      "registry_ends_at": "2020-01-15T13:19:58Z",
      "updated_at": "2019-01-15T13:30:42Z"
    },
    "tags": [],
    "fqdn": "example.com",
    "id": "42927d64-18c8-11e9-b9b5-00163ec4cb00",
    "autorenew": false,
    "tld": "fr",
    "owner": "alice_doe",
    "orga_owner": "alice_doe",
    "domain_owner": "Alice Doe",
    "nameserver": {
      "current": "livedns"
    },
    "href": "https://api.test/v5/domain/domains/example.com",
    "fqdn_unicode": "example.com"
  }
]
```

---

### POST - Create a new domain

This route is used to register domain names. Warning! This is not a free operation. Please ensure your prepaid account has enough credit.

To pay with your user organization (ie: yourself as an individual), just use the regular required parameters. The invoice will be edited with your personal information.

For this to work, you need to:

To pay using another organization, you'll need to perform the request with the organization's ID as the sharing_id query string parameter (see reference). The invoice will be edited using this organization's information.

For this to work, you need to:

Should you want to buy a domain for a customer using a reseller account, you'll need the ID (see reference) of your reseller account and your customer's information for the owner. Then, you'll perform the request with sharing_id=<reseller-id> in the query string and the owner information in the payload. The invoice will be edited with the reseller organization's information.

For this to work, you need to:

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredfqdn ⁠stringowner ⁠objectWith the following properties:Requiredcountry ⁠stringA country code. See the country code list for possible values.email ⁠stringfamily ⁠stringContact's family name (usualy the lastname)given ⁠stringContact's given name (usualy the firstname)streetaddr ⁠stringtype ⁠stringOne of: "individual", "company", "association", "publicbody"Optionalbrand_number ⁠stringcity ⁠stringdata_obfuscated ⁠booleanDefault: trueLearn 

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
  "ns1.example.net": [
    "203.0.113.1"
  ],
  "ns2.example.net": [
    "203.0.113.2",
    "203.0.113.3"
  ]
}
```

```json
{
  "fqdn": "example.com",
  "duration": 5,
  "owner": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "phone": "+33.123456789",
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  }
}
```

---

## Domain Information

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}`

### DELETE - Domain delete

**URI Parameters**

- domain ⁠stringDomain name.
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

### GET - Domain details

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:autorenew ⁠objectWith the following properties:href ⁠stringOptionaldates ⁠array[ datetime ]duration ⁠integerDefault: 1enabled ⁠booleanDefault: falseorg_id ⁠stringUUIDcan_tld_lock ⁠booleancontacts ⁠objectWith the following properties:admin ⁠objectWith the following properties:country ⁠stringA country code. See the country code list for possible values.email ⁠stringfamily ⁠stringContact's family name (usualy the lastname)given ⁠stringContact's g

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
  "status": [
    "clientTransferProhibited"
  ],
  "dates": {
    "created_at": "2019-02-13T11:04:18Z",
    "deletes_at": "2021-03-30T00:04:18Z",
    "hold_begins_at": "2021-02-13T10:04:18Z",
    "hold_ends_at": "2021-03-30T10:04:18Z",
    "pending_delete_ends_at": "2021-05-04T10:04:18Z",
    "registry_created_at": "2019-02-13T10:04:18Z",
    "registry_ends_at": "2021-02-13T10:04:18Z",
    "renew_begins_at": "2012-01-01T00:00:00Z",
    "restore_ends_at": "2021-04-29T10:04:18Z",
    "updated_at": "2019-02-25T16:20:49Z",
    "authinfo_expires_at": "2020-02-25T16:20:49Z"
  },
  "can_tld_lock": true,
  "tags": [],
  "reachability": "done",
  "nameservers": [
    "ns-25-a.gnadi.net",
    "ns-113-b.gnadi.net",
    "ns-58-c.gnadi.net"
  ],
  "contacts": {
    "admin": {
      "city": "Paris",
      "given": "Alice",
      "family": "Doe",
      "zip": "75001",
      "extra_parameters": {},
      "country": "FR",
      "streetaddr": "5 rue neuve",
      "data_obfuscated": true,
      "mail_obfuscated": true,
      "phone": "+33.123456789",
      "same_as_owner": true,
      "state": "FR-IDF",
      "type": "individual",
      "email": "alice@example.org"
    },
    "bill": {
      "city": "Paris",
      "given": "Alice",
      "family": "Doe",
      "zip": "75001",
      "extra_parameters": {},
      "country": "FR",
      "streetaddr": "5 rue neuve",
      "data_obfuscated": true,
      "mail_obfuscated": true,
      "phone": "+33.123456789",
      "same_as_owner": true,
      "state": "FR-IDF",
      "type": "individual",
      "email": "alice@example.org"
    },
    "tech": {
      "city": "Paris",
      "given": "Alice",
      "family": "Doe",
      "zip": "75001",
      "extra_parameters": {},
      "country": "FR",
      "streetaddr": "5 rue neuve",
      "data_obfuscated": true,
      "mail_obfuscated": true,
      "phone": "+33.123456789",
      "same_as_owner": true,
      "state": "FR-IDF",
      "type": "individual",
      "email": "alice@example.org"
    },
    "owner": {
      "city": "Paris",
      "given": "Alice",
      "family": "Doe",
      "zip": "75001",
      "extra_parameters": {},
      "country": "FR",
      "streetaddr": "5 rue neuve",
      "data_obfuscated": true,
      "mail_obfuscated": true,
      "phone": "+33.123456789",
      "state": "FR-IDF",
      "type": "individual",
      "email": "alice@example.org"
    }
  },
  "fqdn": "example.net",
  "autorenew": {
    "dates": [
      "2021-01-13T09:04:18Z",
      "2021-01-29T10:04:18Z",
      "2021-02-12T10:04:18Z"
    ],
    "org_id": "fe0b931c-18c5-11e9-b9b5-00163ec4cb00",
    "duration": 1,
    "href": "http://api.test/v5/domain/domains/example.net/autorenew",
    "enabled": false
  },
  "authinfo": "8vyhljvJg+",
  "sharing_space": {
    "type": "user",
    "id": "fe0b931c-18c5-11e9-b9b5-00163ec4cb00",
    "name": "alice_doe"
  },
  "tld": "net",
  "services": [
    "gandilivedns",
    "mailboxv2"
  ],
  "id": "ba1167be-2f76-11e9-9dfb-00163ec4cb00",
  "trustee_roles": [],
  "href": "http://api.test/v5/domain/domains/example.net",
  "fqdn_unicode": "example.net"
}
```

---

## Authorization code management

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/authinfo`

### PUT - Reset of authorization code

**URI Parameters**

- domain ⁠stringDomain name.
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

## Domain Automatic Renewal

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/autorenew`

### PATCH - Edit autorenew status

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredenabled ⁠booleanOptionalduration ⁠integerDefault: 1Minimum: 1Maximum: 9org_id ⁠stringExample:{ "duration": 1, "enabled": true }

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
  "duration": 1,
  "enabled": true
}
```

---

## Domain claims information

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/claims`

### GET - Retrieve potential trademark information

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:claims ⁠arrayOf items of type:objectWith the following properties:contacts ⁠arraymanagers (agents) of the trademark on behalf of the ownersOf items of type:objectContact information related to a contact / holderWith the following properties:Optionalcc ⁠stringcity ⁠stringemail ⁠stringfax ⁠stringname ⁠stringorg ⁠stringpc ⁠stringphone ⁠stringsp ⁠stringstreet ⁠stringgoods_and_services ⁠stringA very long string describing the trademark categoriesho

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/josn⁠anyExpected response when no claim is accociated with this domain

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Accept a previously retrieved claims

You must first make a GET request to retrieve the information.

This route can be used to accept a claim after the domain has been ordered, in case the creation is blockeis blocked due to the precense of a claim

**URI Parameters**

- domain ⁠stringDomain name.
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

## Domain Contacts

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/contacts`

### GET - Domain contact list

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:admin ⁠objectWith the following properties:country ⁠stringA country code. See the country code list for possible values.email ⁠stringfamily ⁠stringContact's family name (usualy the lastname)given ⁠stringContact's given name (usualy the firstname)same_as_owner ⁠booleanWill be true when the contact used is the same as the owner.streetaddr ⁠stringtype ⁠stringOne of: "individual", "company", "association", "publicbody"Optionalbrand_number ⁠stringc

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
  "admin": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "extra_parameters": {},
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "data_obfuscated": true,
    "mail_obfuscated": true,
    "phone": "+33.123456789",
    "same_as_owner": true,
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  },
  "bill": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "extra_parameters": {},
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "data_obfuscated": true,
    "mail_obfuscated": true,
    "phone": "+33.123456789",
    "same_as_owner": true,
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  },
  "tech": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "extra_parameters": {},
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "data_obfuscated": true,
    "mail_obfuscated": true,
    "phone": "+33.123456789",
    "same_as_owner": true,
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  },
  "owner": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "extra_parameters": {},
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "data_obfuscated": true,
    "mail_obfuscated": true,
    "phone": "+33.123456789",
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  }
}
```

---

### PATCH - Domain contact update

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionaladmin ⁠objectWith the following properties:Requiredcountry ⁠stringA country code. See the country code list for possible values.email ⁠stringfamily ⁠stringContact's family name (usualy the lastname)given ⁠stringContact's given name (usualy the firstname)streetaddr ⁠stringtype ⁠stringOne of: "individual", "company", "association", "publicbody"Optionalbrand_number ⁠stringcity ⁠stringdata_obfuscated ⁠booleanDefault: trueLearn more about W

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
  "admin": {
    "lang": "en",
    "city": "Paris",
    "given": "Bob",
    "family": "Doe",
    "zip": "75001",
    "extra_parameters": {},
    "country": "FR",
    "streetaddr": "8 rue neuve",
    "data_obfuscated": true,
    "mail_obfuscated": true,
    "phone": "+33.123456788",
    "state": "FR-IDF",
    "type": "individual",
    "email": "bob@example.org"
  }
}
```

---

## Domain Owner

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/contacts/owner`

### PUT - Edit domain owner

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredcountry ⁠stringA country code. See the country code list for possible values.email ⁠stringstreetaddr ⁠stringOptionalbrand_number ⁠stringcity ⁠stringdata_obfuscated ⁠booleanDefault: trueLearn more about WHOIS privacy at Gandi here.extra_parameters ⁠objectExtra parameters needed for some extensions. See this list for possible values.family ⁠stringContact's family name (usualy the lastname)fax ⁠stringgiven ⁠stringContact's given name (usu

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

---

## Domain Creation Status

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/createstatus`

### GET - Domain Creation Status

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:step ⁠stringOne of: "BILL", "WAIT", "RUN", "SUPPORT", "ERROR"step_nb ⁠integerOptionalerrortype ⁠stringerrortype_label ⁠string

**Headers**

- Location ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## DNSSEC Keys Management

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/dnskeys`

### GET - DNS Key List

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:algorithm ⁠integerMinimum: 0Maximum: 255Algorithmdigest ⁠stringKey Digestdigest_type ⁠integerMinimum: 0Maximum: 255Key Digest Typehref ⁠stringURL to this DNS Keyid ⁠integerIdkeytag ⁠integerKey Tagtype ⁠stringOne of: "none", "zsk", "ksk"Key TypeOptionalpublic_key ⁠stringPublic Key

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Create a new DNS Key

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredalgorithm ⁠integerMinimum: 0Maximum: 255Algorithmpublic_key ⁠stringPublic Keytype ⁠stringOne of: "none", "zsk", "ksk"Key TypeExample:{ "algorithm": 13, "type": "zsk", "public_key": "ZhCa3rGLofZcndFN2aVd==" }

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
  "algorithm": 13,
  "type": "zsk",
  "public_key": "ZhCa3rGLofZcndFN2aVd=="
}
```

---

### PUT - Replace keys on this domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredkeys ⁠arrayOf items of type:objectWith the following properties:Requiredalgorithm ⁠integerMinimum: 0Maximum: 255Algorithmpublic_key ⁠stringPublic Keytype ⁠stringOne of: "none", "zsk", "ksk"Key TypeExample:{ "keys": [ { "algorithm": 13, "type": "zsk", "public_key": "ZhCa3rGLofZcndFN2aVd==" }, { "algorithm": 13, "type": "ksk", "public_key": "SWF0mbNsQJGzhjbB2jiqTcN9JM3Igg==" } ] }

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
  "keys": [
    {
      "algorithm": 13,
      "type": "zsk",
      "public_key": "ZhCa3rGLofZcndFN2aVd=="
    },
    {
      "algorithm": 13,
      "type": "ksk",
      "public_key": "SWF0mbNsQJGzhjbB2jiqTcN9JM3Igg=="
    }
  ]
}
```

---

## DNSSEC Key deletion

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/dnskeys/{id}`

### DELETE - Delete a DNSSEC Key

**URI Parameters**

- domain ⁠stringDomain name.id ⁠stringKey ID
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

## Glue Record Management

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/hosts`

### GET - Glue record list

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:fqdn ⁠stringFully qualified domain name, written in its native alphabet (IDN).fqdn_unicode ⁠stringFully qualified domain name, written in unicode.href ⁠stringURL to this host's details.ips ⁠array[ string ]List of this host's registered IP addresses.name ⁠stringName of this host (FQDN without the domain part).Example:[ { "ips": [ "203.0.113.1" ], "name": "ns1", "fqdn": "example.net", "href": "http://api.test/v5/domain/doma

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
    "ips": [
      "203.0.113.1"
    ],
    "name": "ns1",
    "fqdn": "example.net",
    "href": "http://api.test/v5/domain/domains/example.net/hosts/ns1",
    "fqdn_unicode": "example.net"
  },
  {
    "ips": [
      "203.0.113.2"
    ],
    "name": "@",
    "fqdn": "example.net",
    "href": "http://api.test/v5/domain/domains/example.net/hosts/@",
    "fqdn_unicode": "example.net"
  }
]
```

---

### POST - Create a new glue record

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredips ⁠array[ string ]List of IP addresses.name ⁠stringHost name of the glue record.Example:{ "name": "ns2", "ips": [ "203.0.113.2", "203.0.113.3", "2001:db8:0:0:0:0:0:00ff" ] }

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.

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
  "name": "ns2",
  "ips": [
    "203.0.113.2",
    "203.0.113.3",
    "2001:db8:0:0:0:0:0:00ff"
  ]
}
```

---

## Glue record information

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/hosts/{name}`

### GET - Glue record information

**URI Parameters**

- domain ⁠stringDomain name.name ⁠stringHost name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:fqdn ⁠stringFully qualified domain name, written in its native alphabet (IDN).fqdn_unicode ⁠stringFully qualified domain name, written in unicode.href ⁠stringURL to this host's details.ips ⁠array[ string ]List of this host's registered IP addresses.name ⁠stringName of this host (FQDN without the domain part).Example:{ "ips": [ "203.0.113.1" ], "name": "ns1", "fqdn": "example.net", "href": "http://api.test/v5/domain/domains/example.net/hosts/ns

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
  "ips": [
    "203.0.113.1"
  ],
  "name": "ns1",
  "fqdn": "example.net",
  "href": "http://api.test/v5/domain/domains/example.net/hosts/ns1",
  "fqdn_unicode": "example.net"
}
```

---

### PUT - Update a glue record

**URI Parameters**

- domain ⁠stringDomain name.name ⁠stringHost name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredips ⁠array[ string ]List of IP addresses.Example:{ "ips": [ "203.0.113.2", "203.0.113.3", "2001:db8:0:0:0:0:0:00ff" ] }

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
  "ips": [
    "203.0.113.2",
    "203.0.113.3",
    "2001:db8:0:0:0:0:0:00ff"
  ]
}
```

---

### DELETE - Delete a glue record

**URI Parameters**

- domain ⁠stringDomain name.name ⁠stringHost name.
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

## LiveDNS Management

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/livedns`

### GET - Domain LiveDNS Information

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:current ⁠stringOne of: "classic", "livedns", "premium_dns", "other"Type of nameservers currently set. classic corresponds to Gandi's classic nameservers, livedns is for the new, default, Gandi nameservers, premium_dns indicates the presence of Gandi's Premium DNS nameserver and the corresponding service subscription, and other is for custom nameservers.nameservers ⁠array[ string ]List of current nameservers.Optionaldnssec_available ⁠booleanInd

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
  "dnssec_available": true,
  "livednssec_available": true,
  "nameservers": [
    "ns-190-a.gnadi.net",
    "ns-193-b.gnadi.net",
    "ns-143-c.gnadi.net"
  ],
  "current": "livedns"
}
```

---

### POST - Enable LiveDNS

This route is used to apply the correct LiveDNS nameservers for the given domain. It takes no content. If you want to disable LiveDNS, change the nameservers.

Please note that if the domain is on the classic Gandi DNS, this will also perform a copy of all existing records immediately afterwards.

**URI Parameters**

- domain ⁠stringDomain name.
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

## /v5/domain/domains/{domain}/livedns/dnssec

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/livedns/dnssec`

### GET - Return informations about DNSSEC status for a domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:state ⁠stringOne of: "activation_error", "activating", "active", "deactivation_error", "deactivating", "inactive"DNSSEC status of a domain.Optionalerror ⁠stringMinimum length: 1An error message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Activate DNSSEC for a domain

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:state ⁠stringOne of: "activating"DNSSEC status of a domain after successfully launching the activation of the DNSSEC.

**Body**

- application/json⁠objectWith the following properties:state ⁠stringOne of: "active", "deactivation_error", "deactivating", "inactive"DNSSEC status of a domain after launching the activation of the DNSSEC.Optionalcause ⁠stringMinimum length: 1A message which explains why the DNSSEC is inactive.error ⁠stringMinimum length: 1An error message.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### DELETE - Disable DNSSEC for a domain

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:state ⁠stringOne of: "deactivating"DNSSEC status of a domain after successfully completing its deactivation.

**Body**

- application/json⁠objectWith the following properties:error ⁠stringMinimum length: 1An error message.state ⁠stringOne of: "activating", "activation_error", "deactivating", "inactive"DNSSEC status of a domain after launching the deactivation of the DNSSEC.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Nameservers Management

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/nameservers`

### GET - Domain Nameserver Information

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠array[ string ]List of FQDNs.Example - Nameserver list:[ "ns1.example.net", "ns2.example.net" ]Example - Nameserver list (livedns example):[ "ns-190-a.gnadi.net", "ns-193-b.gnadi.net", "ns-143-c.gnadi.net" ]

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
  "ns1.example.net",
  "ns2.example.net"
]
```

```json
[
  "ns-190-a.gnadi.net",
  "ns-193-b.gnadi.net",
  "ns-143-c.gnadi.net"
]
```

---

### PUT - Update Domain Nameserver List

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requirednameservers ⁠array[ string ]List of FQDNs.Example:{ "nameservers": [ "ns1.example.net", "ns2.example.net" ] }

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
  "nameservers": [
    "ns1.example.net",
    "ns2.example.net"
  ]
}
```

---

## Resend reachability email

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/reachability`

### PATCH - Resend reachability email

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredaction ⁠stringOne of: "resend"Example:{ "action": "resend" }

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
  "action": "resend"
}
```

---

## Domain Renewal

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/renew`

### GET - Domain renewal information

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:begins_at ⁠stringdurations ⁠array[ integer ]maximum ⁠integerminimum ⁠integerprohibited ⁠booleanOptionalends_at ⁠stringin_renew_period ⁠booleanExample:{ "in_renew_period": true, "durations": [ 1, 2, 3, 4, 5, 6, 7, 8 ], "maximum": 8, "minimum": 1, "prohibited": false, "begins_at": "2012-01-01T00:00:00Z", "ends_at": "2021-03-30T00:00:00Z" }

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
  "in_renew_period": true,
  "durations": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8
  ],
  "maximum": 8,
  "minimum": 1,
  "prohibited": false,
  "begins_at": "2012-01-01T00:00:00Z",
  "ends_at": "2021-03-30T00:00:00Z"
}
```

---

### POST - Renew a Domain

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Optionalduration ⁠integerDefault: 1Minimum: 1Maximum: 9The duration (in years) of the renewal.Example:{ "duration": 2 }

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
  "duration": 2
}
```

---

## Domain Restore

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/restore`

### GET - Domain restore information

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:restorable ⁠booleanOptionalcontracts ⁠arrayOf items of type:objectWith the following properties:id ⁠stringname ⁠stringOptionalhref ⁠stringregistry_contract_href ⁠stringExample:{ "restorable": true }

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
  "restorable": true
}
```

---

### POST - Restore a Domain

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠object

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

## Transfer lock status

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/status`

### PATCH - Transfer lock/unlock

Most extensions have a transfer protection mechanism, that consists of a lock that can be put on the domain. When the transfer lock is enabled, the domain can't be transferred. To unlock : clientTransferProhibited=false. To lock : clientTransferProhibited=true.

Warning: Transferring a domain name consists of entrusting its management to another domain name provider. During this process, an authorization code may be required. By transferring a domain away from Gandi, you will lose products that came with the domain. For example, any GandiMail mailboxes associated with the domain name will no longer work, and all emails will be deleted. When a domain is part of a Website Pack subscription, transferring this domain out will remove the domain from the subscription. Completing this action during the two months following domain creation will result in your Website Pack being split and the domain being made unavailable for a certain period, depending on the rules of the registry. The hosting subscription will continue as a monthly payment, though you can cancel the hosting subscription at any time.

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:RequiredclientTransferProhibited ⁠booleanExample:{ "clientTransferProhibited": true }

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
  "clientTransferProhibited": true
}
```

---

## Manage domain tags

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/tags`

### GET - Get the list of tags linked to a domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠array[ string ]Example:[ "to renew", "tag 2" ]

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
  "to renew",
  "tag 2"
]
```

---

### POST - Attach a new tag to the domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredtag ⁠stringExample:{ "tag": "to renew" }

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
  "tag": "to renew"
}
```

---

### PUT - Update all the tags of the domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredtags ⁠array[ string ]Example:{ "tags": [ "to renew", "tag 2" ] }

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
  "tags": [
    "to renew",
    "tag 2"
  ]
}
```

---

### PATCH - Update some of the tags of the domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredadd ⁠array[ string ]remove ⁠array[ string ]Example:{ "add": [ "premium", "need website" ], "remove": [ "to renew" ] }

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
  "add": [
    "premium",
    "need website"
  ],
  "remove": [
    "to renew"
  ]
}
```

---

### DELETE - Remove all tags from this domain

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:message ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Domain transfer to another registrar

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/transferout`

### POST - Accept or decline a transfer to another registrar

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredaccept ⁠booleanauthinfo ⁠stringExample:{ "authinfo": "xyz5500", "accept": true }

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
  "authinfo": "xyz5500",
  "accept": true
}
```

---

## Web redirections

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/webredirs`

### GET - List web redirections

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/csv value, this route will return a CSV-formatted response.

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:host ⁠stringSource hostname (including the domain name)type ⁠stringOne of: "cloak", "http301", "http302"Type of redirectionurl ⁠stringTarget URLOptionalcert_status ⁠stringcert_uuid ⁠stringcreated_at ⁠stringprotocol ⁠stringOne of: "http", "https", "httpsonly"updated_at ⁠string
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

### POST - Create a new web redirection

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredhost ⁠stringSource hostname (including the domain name)override ⁠booleanWhen you create a redirection on a domain a DNS record is created if it does not exist. When the record already exists and this parameter is set to true it will overwrite the record. Otherwise it will trigger an error.protocol ⁠stringOne of: "http", "https", "httpsonly"type ⁠stringOne of: "cloak", "http301", "http302"Type of redirectionurl ⁠stringTarget URLExample:

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.

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
  "host": "www.example.net",
  "override": true,
  "protocol": "https",
  "type": "http301",
  "url": "http://www.example.org/"
}
```

---

## Web redirection information

**URL:** `https://api.gandi.net/v5/domain/domains/{domain}/webredirs/{host}`

### GET - Get web redirection information

**URI Parameters**

- domain ⁠stringDomain name.host ⁠stringHost name
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:host ⁠stringSource hostname (including the domain name)type ⁠stringOne of: "cloak", "http301", "http302"Type of redirectionurl ⁠stringTarget URLOptionalcert_status ⁠stringcert_uuid ⁠stringcreated_at ⁠stringprotocol ⁠stringOne of: "http", "https", "httpsonly"updated_at ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### PATCH - Update a redirection

**URI Parameters**

- domain ⁠stringDomain name.host ⁠stringHost name
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionaloverride ⁠booleanIf true, a DNS record will be created. When the value is false and no matching DNS record exists, it will trigger an error.protocol ⁠stringOne of: "http", "https", "httpsonly"type ⁠stringOne of: "cloak", "http301", "http302"Type of redirectionurl ⁠stringTarget URLExample:{ "override": true, "protocol": "http", "type": "http302" }

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
  "override": true,
  "protocol": "http",
  "type": "http302"
}
```

---

### DELETE - Delete a redirection

**URI Parameters**

- domain ⁠stringDomain name.host ⁠stringHost name
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:message ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## List Available TLD Extensions

**URL:** `https://api.gandi.net/v5/domain/tlds`

### GET - List available TLD extensions

**Query String**

- Optionalcategory ⁠stringOne of: "ccTLD", "gTLD"Category of the TLDpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:href ⁠stringLink to TLD details.name ⁠stringName of the TLD.Example:[ { "name": "com", "href": "https://api.test/v5/domain/tlds/com" }, { "name": "eu", "href": "https://api.test/v5/domain/tlds/eu" }, { "name": "fr", "href": "https://api.test/v5/domain/tlds/fr" }, { "name": "info", "href": "https://api.test/v5/domain/tlds/info" }, { "name": "net", "href": "https://api.test/v5/domain/tlds/net" }, { "name": "org", "href": "h

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
    "name": "com",
    "href": "https://api.test/v5/domain/tlds/com"
  },
  {
    "name": "eu",
    "href": "https://api.test/v5/domain/tlds/eu"
  },
  {
    "name": "fr",
    "href": "https://api.test/v5/domain/tlds/fr"
  },
  {
    "name": "info",
    "href": "https://api.test/v5/domain/tlds/info"
  },
  {
    "name": "net",
    "href": "https://api.test/v5/domain/tlds/net"
  },
  {
    "name": "org",
    "href": "https://api.test/v5/domain/tlds/org"
  }
]
```

---

## TLD Information

**URL:** `https://api.gandi.net/v5/domain/tlds/{name}`

### GET - TLD Details

**URI Parameters**

- name ⁠stringName of the TLD, or a FQDN.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:authinfo_for_transfer ⁠booleantrue if authinfo is required prior to transfer.category ⁠stringOne of: "ccTLD", "gTLD"Category of the TLD.change_owner ⁠booleantrue if change owner is allowed.corporate ⁠booleantrue if this is a corporate TLD.ext_trade ⁠booleanfull_tld ⁠stringhref ⁠stringLink to TLD details.lock ⁠booleanname ⁠stringName of the TLD.Example:{ "category": "ccTLD", "name": "eu", "lock": false, "change_owner": true, "authinfo_for_trans

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
  "category": "ccTLD",
  "name": "eu",
  "lock": false,
  "change_owner": true,
  "authinfo_for_transfer": true,
  "full_tld": "eu",
  "corporate": false,
  "ext_trade": true,
  "href": "https://api.test/v5/domain/tlds/eu"
}
```

---

## Domain transfer operations

**URL:** `https://api.gandi.net/v5/domain/transferin`

### POST - Transfer a domain to Gandi

This route is used to start transferring a domain to Gandi. Warning! This is not a free operation. Please ensure your prepaid account has enough credit.

To pay with your user organization (ie: yourself as an individual), just use the regular required parameters. The invoice will be edited with your personal information.

For this to work, you need to:

To pay using another organization, you'll need to perform the request with the organization's ID as the sharing_id query string parameter (see reference). The invoice will be edited using this organization's information.

For this to work, you need to:

Should you want to transfer a domain for a customer using a reseller account, you'll need the ID (see reference) of your reseller account and your customer's information for the owner. Then, you'll perform the request with sharing_id=<reseller-id> in the query string and the owner information in the payload. The invoice will be edited with the reseller organization's information.

For this to work, you need to:

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredfqdn ⁠stringowner ⁠objectWith the following properties:Requiredcountry ⁠stringA country code. See the country code list for possible values.email ⁠stringfamily ⁠stringContact's family name (usualy the lastname)given ⁠stringContact's given name (usualy the firstname)streetaddr ⁠stringtype ⁠stringOne of: "individual", "company", "association", "publicbody"Optionalbrand_number ⁠stringcity ⁠stringdata_obfuscated ⁠booleanDefault: trueLearn 

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
  "ns1.example.net": [
    "203.0.113.1"
  ],
  "ns2.example.net": [
    "203.0.113.2",
    "203.0.113.3"
  ]
}
```

```json
{
  "fqdn": "example.com",
  "authinfo": "xyz5500",
  "duration": 2,
  "owner": {
    "city": "Paris",
    "given": "Alice",
    "family": "Doe",
    "zip": "75001",
    "country": "FR",
    "streetaddr": "5 rue neuve",
    "phone": "+33.123456789",
    "state": "FR-IDF",
    "type": "individual",
    "email": "alice@example.org"
  }
}
```

---

## Domain transfer followup

**URL:** `https://api.gandi.net/v5/domain/transferin/{domain}`

### GET - Get transfer status

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:created_at ⁠stringowner_contact ⁠stringparams ⁠objectWith the following properties:domain ⁠stringOptionalduration ⁠integerreseller ⁠stringtld ⁠stringversion ⁠integerstep ⁠stringstep_nb ⁠integerupdated_at ⁠stringOptionalerrortype ⁠stringerrortype_label ⁠stringfoa ⁠arrayOf items of type:objectWith the following properties:answer ⁠stringemail ⁠stringinner_step ⁠stringregac_at ⁠stringstart_at ⁠stringtransfer_link ⁠stringtransfer_procedure ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### PUT - Relaunch transfer process

**URI Parameters**

- domain ⁠stringDomain name.
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

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Update authinfo

**URL:** `https://api.gandi.net/v5/domain/transferin/{domain}/authinfo`

### PUT - Update authinfo code of a pending transfer

This route is used to update the authinfo code of a pending transfer, in case it was not specified or was invalid.

Note that the sharing_id is needed when trying to change the code for a given organization

**URI Parameters**

- domain ⁠stringDomain name.
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredauthinfo ⁠stringExample:{ "authinfo": ".example!authinfo02" }

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
  "authinfo": ".example!authinfo02"
}
```

---

## Check transfer availability

**URL:** `https://api.gandi.net/v5/domain/transferin/{domain}/available`

### POST - Check transfer availability

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalauthinfo ⁠stringExample:{ "authinfo": "xyz5500" }

**Body**

- application/json⁠objectWith the following properties:available ⁠booleanfqdn ⁠stringfqdn_alabel ⁠stringfqdn_ulabel ⁠stringOptionalcorporate ⁠booleandurations ⁠array[ integer ]internal ⁠booleanmaximum_duration ⁠integerminimum_duration ⁠integermsg ⁠string

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
  "authinfo": "xyz5500"
}
```

---

## Resend the transfer FOA emails

**URL:** `https://api.gandi.net/v5/domain/transferin/{domain}/foa`

### POST - Resend the transfer FOA emails

**URI Parameters**

- domain ⁠stringDomain name.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredemail ⁠stringExample:{ "email": "alice@example.net" }

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
  "email": "alice@example.net"
}
```

---


