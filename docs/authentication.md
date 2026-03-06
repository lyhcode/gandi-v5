# Authentication

Every request to Gandi's API requires authentication. The authentication is achieved using an Authorization header sent with a scheme.

## Personal Access Token

The Personal Access Token (PAT) is a token which can be created and configured in the Gandi Admin application. Each PAT has associated scoped permissions and resources that are defined when the token is created.

To consume an access token, the Bearer scheme has to be set in the Authorization header.

Here is a dummy example with a PAT string `abc` which demonstrates a complete header to authenticate using a PAT:

```
Authorization: Bearer abc
```

Note that Personal Access Tokens are restricted to resources, and a PAT cannot be shared across multiple organizations. PATs are created in the Account Settings of the Gandi Admin application, by clicking on the "Create a token" button. You will need to select an organization and then a form will let you choose a fine-grained scope for the PATs.

For security reasons, PATs expire and a token rotation strategy must be considered to properly implement authentication against the Gandi API using PATs. To renew a personal access token, the Renew API of the token has to be used. See Renew PAT API.

Finally, for use in the sandbox, the PAT has to be created in the Gandi Sandbox Admin.

## API Key (Deprecated)

The API Key is the previous mechanism used to do public API calls. Unlike PATs, they cannot be scoped and they have the same set of permissions as the owner of the API Key. Users can't have two API keys at the same time. Organization owners cannot audit or list which members of the organization generated an API key like they can with PATs.

You can generate or delete your production API key from the API Key Page (in the Authentication section).

You cannot create an API key if you don't have one, you can only regenerate an existing one.

Say your API Key is `0123456`, every request you perform must contain the following HTTP header:

```
Authorization: Apikey 0123456
```
