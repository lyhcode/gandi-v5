# Reference

General Documentation for Gandi's Public API

## Introduction

Welcome to Gandi's v5 API!

Gandi provides remote RESTful APIs over HTTPS, making it easy to manage your products and build third-party applications.

This document is a complete reference guide to using Gandi's v5 API.

If you encounter any errors and need assistance, please use the online form to contact the customer support team.

## RESTful Interface

**Endpoint:** `https://api.gandi.net/v5/`

All connections to `https://api.gandi.net` must be issued over HTTPS.

### Stateless

Gandi's API does not maintain sessions. In other words, a request does not depend on previous requests, only its arguments. It only provides object descriptions.

### Rate Limit

Gandi's API is rate limited; you can perform a maximum of 1000 requests per minute from the same IP address.

### Content-Type Header

POST, PUT and PATCH requests you perform must contain the following HTTP header:

```
Content-Type: application/json
```

## Sharing ID

You can pass one of your organization IDs with the `sharing_id` query string parameter for some requests. This parameter, unless stated otherwise, serves two purposes:

- For GET requests on collections, it acts like a filter on returned data.
- For POST, PATCH, or PUT requests that trigger a payment, it indicates the organization that will pay for the ordered product.

You can retrieve your organization list using the Organization API.

## Sandbox API

A Sandbox API is available on `https://api.sandbox.gandi.net/docs/`. Please read the guide to learn more and activate a sandbox account.
