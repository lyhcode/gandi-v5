# Web Hosting API

**Base URL:** `https://api.gandi.net/v5/simplehosting/`

## Web Hosting applications list

**URL:** `https://api.gandi.net/v5/simplehosting/applications`

### GET - List Web Hosting applications

**Query String**

- Optionaldatabase ⁠stringFilters the list with the database they can use, with optional patterns.Example: mysqlExample: pg*language ⁠stringFilters the list by the language they use, with optional patterns.Example: phpExample: py*name ⁠stringFilters the list by application name, with optional patterns.Example: nextcloudExample: mato*Example: *presspage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integer
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:name ⁠stringname_label ⁠stringrequirements ⁠arrayOf items of type:objectWith the following properties:database ⁠objectDatabase supported by the applicationWith the following properties:name ⁠stringstatus ⁠stringversion ⁠stringinstance_minimum_size ⁠stringMinimum required PaaS size for this applicationlanguage ⁠objectLanguage used by the applicationWith the following properties:name ⁠stringsingle_application ⁠booleantrue i

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Web Hosting application information

**URL:** `https://api.gandi.net/v5/simplehosting/applications/{application_name}`

### GET - Application details

**URI Parameters**

- application_name ⁠stringName of an application.

**Body**

- application/json⁠objectWith the following properties:name ⁠stringname_label ⁠stringrequirements ⁠arrayOf items of type:objectWith the following properties:database ⁠objectDatabase supported by the applicationWith the following properties:name ⁠stringstatus ⁠stringversion ⁠stringinstance_minimum_size ⁠stringMinimum required PaaS size for this applicationlanguage ⁠objectLanguage used by the applicationWith the following properties:name ⁠stringsingle_application ⁠booleantrue if the application must

---

## Web Hosting instances list and create

**URL:** `https://api.gandi.net/v5/simplehosting/instances`

### GET - List Web Hosting instances

**Query String**

- Optionalfqdn ⁠stringFilters the list by vhost domain name, with optional patterns.The FQDN must be encoded in ASCII form (Punycode).Example: example.netExample: example.*Example: *example.comname ⁠stringFilters the list by instance name, with optional patterns.Example: exampleExample: examp*Example: *mplepage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per pa
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:available_upgrade ⁠booleancreated_at ⁠datetimedatabase ⁠objectWith the following properties:name ⁠stringstatus ⁠stringversion ⁠stringdatacenter ⁠objectWith the following properties:code ⁠stringOne of: "FR-SD3", "FR-SD5", "FR-SD6", "LU-BI1"name ⁠stringregion ⁠stringOne of: "FR", "LU"expire_at ⁠datetimeid ⁠stringUUIDlanguage ⁠objectWith the following properties:name ⁠stringsingle_application ⁠booleantrue if the application 

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Create Web Hosting instances

This route creates a new Web Hosting instance

Warning! This is not a free operation. Please ensure your prepaid account has enough credit, or that you have a registered credit card.

**Query String**

- Optionalsharing_id ⁠stringOrganization ID used as a billing identifier.(Deprecated: cannot be used with Personal Access Tokens. See Authentication).
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredlocation ⁠stringOne of: "FR", "LU"Indicates where the instance will be created.size ⁠stringOne of: "starter", "advanced", "pro", "business"The size of the instancetype ⁠objectThe database and language to use for the Web Hosting instance.With the following properties:Requireddatabase ⁠objectWith the following properties:Requiredname ⁠stringOne of: "mysql", "pgsql"The database management system to use.Optionalversion ⁠stringThe database 

**Headers**

- OptionalWarning ⁠stringWarning message
- application/json⁠objectWith the following properties:status ⁠stringOne of: "success", "error"Response status.Optionalerrors ⁠arrayA list of all the errors encountered during validation.Of items of type:objectWith the following properties:description ⁠stringError message.location ⁠stringOne of: "header", "path", "querystring", "body"The field's location in the HTTP response.name ⁠stringThe xpath of the field.

**Headers**

- Content-Location ⁠stringLink to the created instance
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

## Web Hosting instance information

**URL:** `https://api.gandi.net/v5/simplehosting/instances/{instance_id}`

### GET - Instance details

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:access_information ⁠objectWith the following properties:admin_url ⁠stringdatabase ⁠objectWith the following properties:admins ⁠arrayOf items of type:objectWith the following properties:type ⁠stringOne of: "phpMyAdmin", "phpPgAdmin", "Adminer"url ⁠stringOptionalusername ⁠stringhost ⁠stringOptionalport ⁠integerIn case the database listens to an inet-type socket this field will contain the port number used by the databasesocket ⁠stringIn the even

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### PATCH - Web Hosting instance modification

This route allows to modify a given instance

Be mindful that it can induce a payment, typically if the instance size or storage additional size is modified.

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalbooster ⁠booleanbooster_options ⁠objectWith the following properties:Optionalsize ⁠stringOne of: "s", "s+", "m", "l", "xl", "xxl", "starter", "advanced", "pro", "business", "boosted"language_id ⁠stringUUID of the language to upgrade to. This value can be found in the upgrade_to field of the return of a GET of this instance (which lists the available upgrades).name ⁠stringpassword ⁠stringThe password for sftp, git and advanced control p

**Headers**

- Content-Location ⁠stringLink to the modified instance.
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

### DELETE - 

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
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

## Web Hosting instance actions

**URL:** `https://api.gandi.net/v5/simplehosting/instances/{instance_id}/action`

### POST - Perform an action on the instance

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredaction ⁠stringOne of: "restart", "console", "reset_database_password"

**Headers**

- Content-Location ⁠stringLink to the instance on which the action is taken
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

## Web Hosting instance usage metrics

**URL:** `https://api.gandi.net/v5/simplehosting/instances/{instance_id}/usage`

### GET - Usage metrics

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:disk_size_bytes ⁠integerThe total disk space in bytes.Optionaldisk_used_bytes ⁠integerThe used disk space in bytes.

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Web Hosting instance vhost list and create

**URL:** `https://api.gandi.net/v5/simplehosting/instances/{instance_id}/vhosts`

### GET - List vhosts

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
- Optionalfqdn ⁠stringFilters the list by vhost domain name, with optional patterns.The FQDN must be encoded in ASCII form (Punycode).Example: example.netExample: example.*Example: *example.compage ⁠integerDefault: 1Minimum: 1Which result page to retrieve. If the number is greater than the last page, an empty list is returned.per_page ⁠integerMinimum: 1How many items to display per page.sort_by ⁠stringDefault: "-created_at"Indicate the field used to sort the results. The field's name may start wit
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Headers**

- Filtered-Count ⁠integerNumber of items returned by the API call.Total-Count ⁠integerTotal number of items.OptionalLink ⁠stringLinks to next and last page.
- application/json⁠arrayOf items of type:objectWith the following properties:created_at ⁠datetimefqdn ⁠stringFQDN linked to the vhost in ASCII (Punycode) format.is_a_test_vhost ⁠booleanTrue if the vhost is intended for testing purposes only.linked_dns_zone ⁠objectThis field contains information on the DNS zone the vhost is linked to.With the following properties:allow_alteration ⁠booleanTrue if you authorized Gandi to modify your DNS zone so that your vhost points to our Web Hosting public endpoin

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### POST - Create a new vhost

**URI Parameters**

- instance_id ⁠stringUUID of an instance.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Requiredfqdn ⁠stringfqdn of the vhost.Optionalapplication ⁠objectWith the following properties:Requiredname ⁠stringOptionalparameters ⁠objectlinked_dns_zone ⁠objectWith the following properties:Requiredallow_alteration ⁠booleanTrue if you authorized Gandi to modify your DNS zone so that your vhost points to our Web Hosting public endpoints. If set to True and your DNS zone is managed by our liveDNS platform, you will not have to manually chang

**Headers**

- Content-Location ⁠stringLink to the new vhost.
- application/json⁠objectWith the following properties:fqdn ⁠stringfqdn of the vhost.https_strategy ⁠stringOne of: "HTTP_only", "allow_HTTP_and_HTTPS", "redirect_HTTP_to_HTTPS"Describes the strategy used regarding secure connection to your vhost (HTTP/HTTPS). This field is only present if you have a certificate.linked_dns_zone ⁠objectWith the following properties:allow_alteration ⁠booleanTrue if you authorized Gandi to modify your DNS zone so that your vhost points to our Web Hosting public endpoi

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

## Web Hosting vhost information

**URL:** `https://api.gandi.net/v5/simplehosting/instances/{instance_id}/vhosts/{vhost_fqdn}`

### GET - Vhost details

**URI Parameters**

- instance_id ⁠stringUUID of an instance.vhost_fqdn ⁠stringfqdn of a vhost.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:created_at ⁠datetimefqdn ⁠stringFQDN linked to the vhost in ASCII (Punycode) format.is_a_test_vhost ⁠booleanTrue if the vhost is intended for testing purposes only.linked_dns_zone ⁠objectThis field contains information on the DNS zone the vhost is linked to.With the following properties:allow_alteration ⁠booleanTrue if you authorized Gandi to modify your DNS zone so that your vhost points to our Web Hosting public endpoints. If set to True and

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### PATCH - Update a vhost

**URI Parameters**

- instance_id ⁠stringUUID of an instance.vhost_fqdn ⁠stringfqdn of a vhost.
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key
- application/json⁠objectWith the following properties:Optionalapplication ⁠objectWith the following properties:Requiredname ⁠stringOptionalparameters ⁠objecthttps_strategy ⁠stringOne of: "HTTP_only", "allow_HTTP_and_HTTPS", "redirect_HTTP_to_HTTPS"Describes the strategy used regarding secure connection to your vhost (HTTP/HTTPS). This field is only present if you have a certificate.linked_dns_zone ⁠objectWith the following properties:Requiredallow_alteration ⁠booleanTrue if you authorized Gandi t

**Body**

- application/json⁠objectWith the following properties:fqdn ⁠stringfqdn of the vhost.https_strategy ⁠stringOne of: "HTTP_only", "allow_HTTP_and_HTTPS", "redirect_HTTP_to_HTTPS"Describes the strategy used regarding secure connection to your vhost (HTTP/HTTPS). This field is only present if you have a certificate.linked_dns_zone ⁠objectWith the following properties:allow_alteration ⁠booleanTrue if you authorized Gandi to modify your DNS zone so that your vhost points to our Web Hosting public endpoi

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Body**

- application/json⁠objectWith the following properties:cause ⁠stringcode ⁠integermessage ⁠stringobject ⁠string

**Headers**

- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

---

### DELETE - Delete a vhost

**URI Parameters**

- instance_id ⁠stringUUID of an instance.vhost_fqdn ⁠stringfqdn of a vhost.
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

## Web Hosting vhost cache information

**URL:** `https://api.gandi.net/v5/simplehosting/instances/{instance_id}/vhosts/{vhost_fqdn}/cache`

### DELETE - Purge a vhost's cache

**URI Parameters**

- instance_id ⁠stringUUID of an instance.vhost_fqdn ⁠stringfqdn of a vhost.
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


