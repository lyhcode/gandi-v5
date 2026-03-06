# Comment API

**Base URL:** `https://api.gandi.net/v5/comment`

## Manage your comments on gandi products

**URL:** `https://api.gandi.net/v5/comment/comments/{id}`

### GET - Return the comment

**URI Parameters**

- id ⁠stringThe gandi product entity_id
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-key

**Body**

- application/json⁠objectWith the following properties:content ⁠stringid ⁠stringThe gandi product entity_id.Optionalcreated_at ⁠datetimeupdated_at ⁠datetimeuser ⁠objectWith the following properties:id ⁠stringUUIDname ⁠stringsharing_id ⁠stringUUIDExample:{ "id": "ae5680b2-8c8f-11eb-8460-00163ec4cb00", "content": "This is a comment.", "created_at": "2021-05-18T11:36:59Z", "updated_at": "2021-05-18T11:36:59Z", "user": { "sharing_id": "3c2f29e4-17be-4db3-b8eb-ec8a3fa96bc0", "id": "3c2f29e4-17be-4db3-b

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
  "id": "ae5680b2-8c8f-11eb-8460-00163ec4cb00",
  "content": "This is a comment.",
  "created_at": "2021-05-18T11:36:59Z",
  "updated_at": "2021-05-18T11:36:59Z",
  "user": {
    "sharing_id": "3c2f29e4-17be-4db3-b8eb-ec8a3fa96bc0",
    "id": "3c2f29e4-17be-4db3-b8eb-ec8a3fa96bc0",
    "name": "alicia"
  }
}
```

---

### POST - Set the comment for the entity corresponding to the id

**URI Parameters**

- id ⁠stringThe gandi product entity_id
- RequiredAuthorization ⁠stringThe Authorization header must start with Bearer for access token, or Apikey depending of the authentication scheme. Apikey is deprecated and be replaced by personal access token.Example: Bearer pat_abc-123Example: Apikey your-api-keyOptionalDry-Run ⁠integerIf this header's value is 1 the request's parameters will only be checked; the operation will not actually be performed.
- application/json⁠objectWith the following properties:Requiredcontent ⁠stringThe note content.Example:{ "content": "This domain must be renewed." }

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
  "content": "This domain must be renewed."
}
```

---

### DELETE - Delete the comment for the entity corresponding to the id.

**URI Parameters**

- id ⁠stringThe gandi product entity_id
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


