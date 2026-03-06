# Certificate API

**Base URL:** `https://api.gandi.net/v5/certificate/`

## DCV parameters

**URL:** `https://api.gandi.net/v5/certificate/dcv_params`

### POST - Retrieve DCV parameters

Get parameters for DCV (Domain Control Validation). DCV is a security check that validates/grants access to the registred domain name.

Despite being a post method, this route does not perform any change on your existing certificates.

If you want to perform a DCV through DNS, pass the parameter dcv_method with dns.

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalaltnames ⁠array[ string ]Alt Name list, when the certificate package permits itcsr ⁠stringCertificate Signing Requestdcv_method ⁠stringOne of: "email", "dns", "file", "http", "https"The certificate validation methodpackage ⁠stringCertificate package name as returned in the package list route.Example:{ "altnames": [ "a.example.com", "www.python.domain" ], "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbX

**Body**

- application/json⁠objectWith the following properties:altnames ⁠array[ string ]Extracted SANs list from the CSR if any, else an empty data structure.dcv_method ⁠stringOne of: "email", "dns", "file", "http", "https"The certificate validation methodfqdns ⁠array[ string ]md5 ⁠stringsha256 ⁠stringOptionaldns_records ⁠array[ string ]DNS records to be added for DCV validationmessages ⁠array[ string ]raw_messages ⁠array[ array[ string ] ]

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
  "altnames": [
    "a.example.com",
    "www.python.domain"
  ],
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns",
  "package": "cert_std_1_10_0_digicert"
}
```

---

## Certificate Create and List

**URL:** `https://api.gandi.net/v5/certificate/issued-certs`

### GET - List certificates

**Query String**

- Optionalcn ⁠stringFilters the list by CN name, with optional patterns.Example: example.netExample: example*Example: *example.comcovered_cn ⁠stringFilters the list by certificates valid for a given CN.package ⁠stringName of the certificate package.page ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.sharing_id ⁠stringSharing ID. Organization ID used as a 
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed text/csv value, this route will return a CSV-formatted response.

**Headers**

- Filtered-Count ⁠integerOn a filtered list, this is the number of matching items.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:altnames ⁠array[ string ]Alt Name list, when the certificate package permits italtnames_unicode ⁠array[ string ]Alt Name list, when the certificate package permits itcn ⁠stringMaximum length: 64Common Namecn_unicode ⁠stringMaximum length: 64Common Namecontact ⁠objectWith the following properties:Optionalcity ⁠stringcountry ⁠stringemail ⁠stringfamily ⁠stringgiven ⁠stringorgname ⁠stringstate ⁠stringstreetaddr ⁠stringzip ⁠st
- text/csv⁠anyCSV-formatted response.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```
?cn=example.com&package=cert_std_1_10_0_digicert&status=valid
```

---

### POST - Create a new certificate

This route creates a new certificate.

The parameters can receive either a CSR or a CN.

Important: All certificates are valid for one year regardless of the duration value. For longer durations, you must update the certificate using PATCH /issued-certs/{id}.

**Query String**

- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredpackage ⁠stringCertificate package name as returned in the package list route.Optionalaltnames ⁠array[ string ]Alt Name list, when the certificate package permits itapex_only ⁠booleanWhether it's a certificate with apex or both apex and www (Digicert only)cn ⁠stringMaximum length: 64Common Namecsr ⁠stringCertificate Signing Requestdcv_method ⁠stringOne of: "email", "dns", "file", "http", "https"The certificate validation methodduration

**Headers**

- OptionalWarning ⁠stringWarning message
- application/json⁠objectWith the following properties:status ⁠stringOne of: "success", "error"Response status.Optionalerrors ⁠arrayA list of all the errors encountered during validation.Of items of type:objectWith the following properties:description ⁠stringError message.location ⁠stringOne of: "header", "path", "querystring", "body"The field's location in the HTTP response.name ⁠stringThe xpath of the field.

**Headers**

- OptionalLocation ⁠string
- application/json⁠objectWith the following properties:href ⁠stringid ⁠stringCertificate IDmessage ⁠stringConfirmation message.

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
  "package": "cert_std_1_10_0_digicert",
  "apex_only": true,
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns",
  "resellee_id": "my_resellee_id"
}
```

```json
{
  "package": "cert_std_1_0_0",
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns",
  "resellee_id": "my_resellee_id"
}
```

```json
{
  "package": "cert_std_3_10_0_digicert",
  "altnames": [
    "a.example.com",
    "www.python.domain"
  ],
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns",
  "resellee_id": "my_resellee_id"
}
```

---

## Certificate information

**URL:** `https://api.gandi.net/v5/certificate/issued-certs/{id}`

### GET - Certificate details

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:altnames ⁠array[ string ]Alt Name list, when the certificate package permits italtnames_unicode ⁠array[ string ]Alt Name list, when the certificate package permits itcn ⁠stringMaximum length: 64Common Namecn_unicode ⁠stringMaximum length: 64Common Namecontact ⁠objectWith the following properties:Optionalcity ⁠stringcountry ⁠stringemail ⁠stringfamily ⁠stringgiven ⁠stringorgname ⁠stringstate ⁠stringstreetaddr ⁠stringzip ⁠stringdates ⁠objectWith 

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Renew a certificate

**URI Parameters**

- id ⁠stringCertificate ID
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Optionalcsr ⁠stringdcv_method ⁠stringduration ⁠integerExample:{ "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF

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
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns",
  "duration": 1
}
```

---

### PATCH - Update a certificate

**URI Parameters**

- id ⁠stringCertificate ID
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Optionalaltnames ⁠array[ string ]csr ⁠stringdcv_method ⁠stringExample:{ "altnames": [ "a.example.com", "www.python.domain" ], "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG

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
  "altnames": [
    "a.example.com",
    "www.python.domain"
  ],
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns"
}
```

---

### DELETE - Revoke a certificate

**URI Parameters**

- id ⁠stringCertificate ID
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

## Retrieve certificate

**URL:** `https://api.gandi.net/v5/certificate/issued-certs/{id}/crt`

### GET - Retrieve certificate

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- text/plain⁠stringthe certificate

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Certificate validation

**URL:** `https://api.gandi.net/v5/certificate/issued-certs/{id}/dcv`

### PUT - Resend the DCV

**URI Parameters**

- id ⁠stringCertificate ID
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

### PATCH - Update the DCV method

**URI Parameters**

- id ⁠stringCertificate ID
- Optionalsharing_id ⁠stringSharing ID. Organization ID used as a filter or as a billing identifier. See the reference.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredmethod ⁠stringOne of: "email", "dns", "file", "http", "https"

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

## DCV parameters

**URL:** `https://api.gandi.net/v5/certificate/issued-certs/{id}/dcv_params`

### POST - Retrieve DCV parameters

Get parameters for DCV (Domain Control Validation). DCV is a security check that validates/grants access to the registred domain name.

Despite being a post method, this route does not perform any change on your existing certificates.

If you want to perform a DCV through DNS, pass the parameter dcv_method with dns.

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalcsr ⁠stringCertificate Signing Requestdcv_method ⁠stringOne of: "email", "dns", "file", "http", "https"The certificate validation methodpackage ⁠stringCertificate package name as returned in the package list route.Example:{ "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRan

**Body**

- application/json⁠objectWith the following properties:altnames ⁠array[ string ]Extracted SANs list from the CSR if any, else an empty data structure.dcv_method ⁠stringOne of: "email", "dns", "file", "http", "https"The certificate validation methodfqdns ⁠array[ string ]md5 ⁠stringsha256 ⁠stringOptionaldns_records ⁠array[ string ]DNS records to be added for DCV validationmessages ⁠array[ string ]raw_messages ⁠array[ array[ string ] ]unique_value ⁠string

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
  "csr": "-----BEGIN CERTIFICATE REQUEST----- MIICWzCCAUMCAQAwFjEUMBIGA1UEAwwLZXhhbXBsZS5jb20wggEiMA0GCSqGSIb3 DQEBAQUAA4IBDwAwggEKAoIBAQCwl28HV/Z+CSk6ENgOcERPRfRQRTpqsO+tIHhG Sa/FdvgMFOqrLn7T5a6Vz6bXsEl/vN9Kmo1CSwRanpJOgEKaR39uzxj9JK3XsWqb yizdTkn07xLngSyZ/jw7Zg5zsiEeGADrjFdWH+Kv7Rd1gbIoeaoFJKPYiUlVhU6f GphjMViJSIMuJxeMG4uarSsUGevOoCemIPafGUwTVEWbmp0cPXRJ1mKTw3z7NehM V25FZUAeBf0LRF/lciA+PsZiU3qDN44gj+vWXIi/+Kz9FR17ciog8oBcl1xnL6CY gymIvwO1EPYBtsiTJ+7zzVW+95bEd/Z7Zg8j8mLbZm7yf0LhAgMBAAGgADANBgkq hkiG9w0BAQsFAAOCAQEAkkh7sZd+Js+JfO2LfBon9c/ndinev6/XniDiQAJC40Gb fykuEQOB7CVcYT6b6uQfpOvUCjHY1CCFRWXYzOeJAn91fEz9CHK5iKepwyJhLHmT l6eE3lP4NpSB+FS10a3pBJIUVJ3gkIOfuABBBSY7JGRdZ60nmWPeknwoB0A5erlS LAFGulmOYQAu2LDYEXSMkbtPKs/KgUYBiWTTl+Bmsriy+s/1qyuX+KiU31XQTeEF 2/nNPFevmHjRrgZUUr3m5kVW/6hToipUzhK7PamcUvSYPMC9ORRBHea/Io9GIOkD HrHVCn3XXTyOzokbXIpd+d165/QBopaITmmodf6xhw== -----END CERTIFICATE REQUEST-----",
  "dcv_method": "dns",
  "package": "cert_std_1_10_0_digicert"
}
```

---

## Manage certificate tags

**URL:** `https://api.gandi.net/v5/certificate/issued-certs/{id}/tags`

### GET - Get the list of tags linked to a certificate

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠array[ string ]Example:[ "server1", "server2" ]

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
  "server1",
  "server2"
]
```

---

### POST - Attach a new tag to the certificate

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredtag ⁠stringExample:{ "tag": "server42" }

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
  "tag": "server42"
}
```

---

### PUT - Replace all the tags of the certificate

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredtags ⁠array[ string ]Example:{ "tags": [ "server42", "server55" ] }

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
    "server42",
    "server55"
  ]
}
```

---

### PATCH - Update some of the tags of the certificate

**URI Parameters**

- id ⁠stringCertificate ID
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredadd ⁠array[ string ]remove ⁠array[ string ]Example:{ "add": [ "server79" ], "remove": [ "server55" ] }

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
    "server79"
  ],
  "remove": [
    "server55"
  ]
}
```

---

### DELETE - Remove all tags from this certificate

**URI Parameters**

- id ⁠stringCertificate ID
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

## Certificate Packages

**URL:** `https://api.gandi.net/v5/certificate/packages`

### GET - Package list

**Query String**

- Optionalcategory ⁠stringmax_domains ⁠integermin_domains ⁠integerpage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.trustlogo ⁠booleanwarranty ⁠integerwildcard ⁠boolean
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:category ⁠objectWith the following properties:name ⁠stringcategory of the package (standard, pro, business, …)href ⁠stringmax_domains ⁠integermaximum number of associated namesmin_domains ⁠integerminimum number of associated names (always 1)name ⁠stringreference that should be used when requesting a new certificate. See this list for possible values.provider ⁠stringProvider of this packagesgc ⁠booleandeprecated "Server Ga

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```
?category=standard&min_domains=1&max_domains=5
```

---

## Package information

**URL:** `https://api.gandi.net/v5/certificate/packages/{name}`

### GET - Package information

**URI Parameters**

- name ⁠stringPackage name, see this list for possible values
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:category ⁠objectWith the following properties:name ⁠stringcategory of the package (standard, pro, business, …)href ⁠stringmax_domains ⁠integermaximum number of associated namesmin_domains ⁠integerminimum number of associated names (always 1)name ⁠stringreference that should be used when requesting a new certificate. See this list for possible values.provider ⁠stringProvider of this packagesgc ⁠booleandeprecated "Server Gated Cryptography", pac

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Intermediate certificate, by filename

**URL:** `https://api.gandi.net/v5/certificate/pem/-/{filename}`

### GET - Intermediate certificate

**URI Parameters**

- filename ⁠stringFilename
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed application/x-pem-file value, this route will download the intermediate certificate.

**Body**

- text/plain⁠stringPlain text intermediate certificate.
- application/x-pem-file⁠fileDownload the intermediate certificate.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Intermediate certificate

**URL:** `https://api.gandi.net/v5/certificate/pem/{type}`

### GET - Intermediate certificate

**URI Parameters**

- type ⁠stringOne of: "cert_std", "cert_pro"Certificate type
- Optionalprovider ⁠stringOne of: "Sectigo", "Digicert"Provider of this certificate
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalAccept ⁠stringWhen passed application/x-pem-file value, this route will download the intermediate certificate.

**Body**

- text/plain⁠stringPlain text intermediate certificate.
- application/x-pem-file⁠fileDownload the intermediate certificate.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

```
?provider=Digicert
```

---


