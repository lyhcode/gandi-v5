# Billing API

**Base URL:** `https://api.gandi.net/v5/billing`

## /v5/billing/info

**URL:** `https://api.gandi.net/v5/billing/info`

### GET - Get your user account's information

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:annual_balance ⁠numberamount of purchased over the past 12 months since the requestgrid ⁠stringprice rate that is applied depending on the amount purchased over the last 12 monthsoutstanding_amount ⁠numberamount of outstanding orders (payment by terms) since the last invoiceOptionalprepaid ⁠objectprepaid account informationWith the following properties:amount ⁠numbercurrent amount available in the prepaid accountcreated_at ⁠datetimecreation da

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
  "prepaid": {
    "amount": 49856.3,
    "currency": "EUR",
    "warning_threshold": 100,
    "created_at": "2019-01-15T12:11:35Z",
    "updated_at": "2019-03-08T15:14:53Z"
  },
  "outstanding_amount": 0,
  "annual_balance": 120,
  "grid": "A"
}
```

---

## /v5/billing/info/{sharing_id}

**URL:** `https://api.gandi.net/v5/billing/info/{sharing_id}`

### GET - Get Account Information

**URI Parameters**

- sharing_id ⁠stringtarget organization id
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:annual_balance ⁠numberamount of purchased over the past 12 months since the requestgrid ⁠stringprice rate that is applied depending on the amount purchased over the last 12 monthsoutstanding_amount ⁠numberamount of outstanding orders (payment by terms) since the last invoiceOptionalprepaid ⁠objectprepaid account informationWith the following properties:amount ⁠numbercurrent amount available in the prepaid accountcreated_at ⁠datetimecreation da

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
  "prepaid_monthly_invoice": false,
  "outstanding_amount": 0,
  "annual_balance": 250,
  "grid": "A"
}
```

---

## /v5/billing/price/{type}

**URL:** `https://api.gandi.net/v5/billing/price/{type}`

### GET - Return product catalog prices.

**URI Parameters**

- type ⁠stringOne of: "cloud", "domain", "domain_option", "issued-cert", "mailboxv2", "openstack", "phone_advisory", "simple-hosting", "tmch"Minimum length: 1
- Requiredname ⁠arrayOf items of type:stringMinimum length: 1processes ⁠arrayOf items of type:stringMinimum length: 1Optionalactive_phase ⁠booleanactive phasecountry ⁠stringcountrycurrency ⁠stringcurrencydiscounts ⁠arrayOf items of type:stringMinimum length: 1duration_unit ⁠stringduration unitextension ⁠stringextensionfeatures ⁠booleanfeaturesgrid ⁠stringgridlang ⁠stringlangmax_duration ⁠integermax durationpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater tha
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠objectWith the following properties:currency ⁠stringMinimum length: 1grid ⁠stringMinimum length: 1products ⁠arrayDefault: []list of productsOf items of type:objectWith the following properties:name ⁠stringMinimum length: 1phases ⁠arrayDefault: []list of phasesOf items of type:objectWith the following properties:name ⁠stringMinimum length: 1namestarts_at ⁠datetimestart date of the phaseOptionalends_at ⁠datetimeend date of the phaseprices ⁠arrayDefault: []list of pricesOf items of

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
  "currency": "EUR",
  "grid": "A",
  "taxes": [
    {
      "name": "vat",
      "name_label": "VAT",
      "rate": 25,
      "type": "service"
    }
  ],
  "products": [
    {
      "name": ".com",
      "phases": [],
      "prices": [
        {
          "discount": false,
          "duration_unit": "y",
          "features": [],
          "max_duration": 2,
          "min_duration": 1,
          "options": {
            "phase": "golive"
          },
          "price_before_taxes": 12.54,
          "price_after_taxes": 15.68
        },
        {
          "discount": false,
          "duration_unit": "y",
          "features": [],
          "max_duration": 10,
          "min_duration": 3,
          "options": {
            "phase": "golive"
          },
          "price_before_taxes": 10.66,
          "price_after_taxes": 13.32
        }
      ],
      "status": "available",
      "process": "create",
      "taxes": [
        {
          "name": "vat",
          "name_label": "VAT",
          "rate": 25,
          "type": "service"
        }
      ]
    }
  ]
}
```

---


