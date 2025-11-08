# Affinity API v1 Documentation (Markdown Copy)

> **⚠️ IMPORTANT DISCLAIMER**
>
> **This is an UNOFFICIAL markdown copy of the Affinity API v1 documentation.** The official and authoritative documentation is maintained by Affinity at:
>
> **📚 Official Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)
>
> **Always refer to the official Affinity documentation for the most up-to-date and accurate information.**

---

## About This Document

This markdown version of the Affinity API v1 documentation was created to provide:

- **Better compatibility with AI coding assistants** - Static markdown format is easier for AI tools to parse and reference
- **Offline access** - Work with the documentation without an internet connection
- **Text-based search** - Easier to search and navigate compared to interactive websites
- **Version control** - Track changes and updates over time

**Source:** Extracted from the live Affinity API documentation at https://api-docs.affinity.co/

**Documentation Version:** This copy is based on the official documentation as it appeared on **November 6, 2025 at 18:49:04** (Last updated: 11/06/2025 18:49:04). The official documentation may have been updated since this copy was created.

> **⚠️ Use at Your Own Risk**
>
> While every effort is made to ensure accuracy and keep this documentation synchronized with the official Affinity documentation, this is an **unofficial copy** and may contain:
>
> - Errors or omissions
> - Outdated information
> - Formatting differences from the original
>
> **For production use or critical implementations, always verify against the [official Affinity API documentation](https://api-docs.affinity.co/).**

## Contact & Support

For API support or questions about the Affinity API itself, contact Affinity directly:

- **Affinity Support:** support@affinity.co
- **Official v1 Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)
- **Official v2 Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Authentication](#authentication)
  - [Request & Response](#request--response)
- [Rate Limit](#rate-limit)
  - [API Rate Limit](#api-rate-limit)
  - [Webhook Subscription Limit](#webhook-subscription-limit)
  - [Rate Limit Header](#rate-limit-header)
- [Data Model](#data-model)
  - [Overview](#overview)
  - [Default Field](#default-field)
- [Common Use Case](#common-use-case)
  - [Getting Field Value for All List Entries on a List](#getting-field-value-for-all-list-entries-on-a-list)
  - [Getting Field Value Change for Status Field](#getting-field-value-change-for-status-field)
  - [Getting the Strongest Relationship Strength Connection to an Organization on a List](#getting-the-strongest-relationship-strength-connection-to-an-organization-on-a-list)
- [Useful Resources](#useful-resources)
- [Partner With Us](#partner-with-us)
- [List](#list)
  - [The List Resource](#the-list-resource)
  - [Get All List](#get-all-list)
  - [Get a Specific List](#get-a-specific-list)
  - [Create a New List](#create-a-new-list)
- [List Entries](#list-entries)
  - [The List Entry Resource](#the-list-entry-resource)
  - [Get All List Entries](#get-all-list-entries)
  - [Get a Specific List Entry](#get-a-specific-list-entry)
  - [Create a New List Entry](#create-a-new-list-entry)
  - [Delete a Specific List Entry](#delete-a-specific-list-entry)
- [Field](#field)
  - [The Field Resource](#the-field-resource)
  - [Get Field](#get-field)
  - [Create Field](#create-field)
  - [Delete a Field](#delete-a-field)
- [Field Value](#field-value)
  - [The Field Value Resource](#the-field-value-resource)
  - [Get Field Value](#get-field-value)
  - [Create a New Field Value](#create-a-new-field-value)
  - [Update a Field Value](#update-a-field-value)
  - [Delete a Field Value](#delete-a-field-value)
- [Field Value Change](#field-value-change)
  - [Supported fields type](#supported-fields-type)
  - [The Field Value Change Resource](#the-field-value-change-resource)
  - [Get Field Value Change](#get-field-value-change)
- [Person](#person)
  - [The Person Resource](#the-person-resource)
  - [Search for Person](#search-for-person)
  - [Get a Specific Person](#get-a-specific-person)
  - [Create a New Person](#create-a-new-person)
  - [Update a person](#update-a-person)
  - [Delete a Person](#delete-a-person)
  - [Get Global Person Field](#get-global-person-field)
- [Organization](#organization)
  - [The Organization Resource](#the-organization-resource)
  - [Search for Organization](#search-for-organization)
  - [Get a Specific Organization](#get-a-specific-organization)
  - [Create a New Organization](#create-a-new-organization)
  - [Update an Organization](#update-an-organization)
  - [Delete an Organization](#delete-an-organization)
  - [Get Global Organization Field](#get-global-organization-field)
- [Opportunities](#opportunities)
  - [The Opportunity Resource](#the-opportunity-resource)
  - [Search for Opportunities](#search-for-opportunities)
  - [Get a Specific Opportunity](#get-a-specific-opportunity)
  - [Create a New Opportunity](#create-a-new-opportunity)
  - [Update an Opportunity](#update-an-opportunity)
  - [Delete an Opportunity](#delete-an-opportunity)
- [Interaction](#interaction)
  - [The Interaction Resource](#the-interaction-resource)
  - [Get All Interaction](#get-all-interaction)
  - [Get a Specific Interaction](#get-a-specific-interaction)
  - [Create a New Interaction](#create-a-new-interaction)
  - [Update an Interaction](#update-an-interaction)
  - [Delete an Interaction](#delete-an-interaction)
- [Relationship Strength](#relationship-strength)
  - [The Relationship Strength Resource](#the-relationship-strength-resource)
  - [Get Relationship Strength](#get-relationship-strength)
- [Note](#note)
  - [The Note Resource](#the-note-resource)
  - [Get All Note](#get-all-note)
  - [Get a Specific Note](#get-a-specific-note)
  - [Create a New Note](#create-a-new-note)
  - [Update a Note](#update-a-note)
  - [Delete a Note](#delete-a-note)
- [Entity File](#entity-file)
  - [The Entity File Resource](#the-entity-file-resource)
  - [Get All File](#get-all-file)
  - [Get a Specific File](#get-a-specific-file)
  - [Download File](#download-file)
  - [Upload File](#upload-file)
- [Reminder](#reminder)
  - [The Reminder Resource](#the-reminder-resource)
  - [Get All Reminder](#get-all-reminder)
  - [Get a Specific Reminder](#get-a-specific-reminder)
  - [Create a New Reminder](#create-a-new-reminder)
  - [Update a Reminder](#update-a-reminder)
  - [Delete a Reminder](#delete-a-reminder)
- [Webhook](#webhook)
  - [The Webhook Subscription Resource](#the-webhook-subscription-resource)
  - [Supported Webhook Event](#supported-webhook-event)
  - [Get All Webhook Subscription](#get-all-webhook-subscription)
  - [Get a Specific Webhook Subscription](#get-a-specific-webhook-subscription)
  - [Create a New Webhook Subscription](#create-a-new-webhook-subscription)
  - [Update a Webhook Subscription](#update-a-webhook-subscription)
  - [Delete a Specific Webhook Subscription](#delete-a-specific-webhook-subscription)
- [Whoami](#whoami)
  - [The Whoami Resource](#the-whoami-resource)
  - [Get Whoami](#get-whoami)
- [Rate Limit Endpoint](#rate-limit-endpoint)
  - [The Rate Limit Resource](#the-rate-limit-resource)
  - [Get Rate Limit Information](#get-rate-limit-information)
- [Changelog](#changelog)

# Introduction

Welcome to the Affinity API! This API provides a RESTful interface for performing operations on the different objects that make up Affinity. If you are trying to accomplish an action through this API and need help, please contact us at [support@affinity.co](mailto:support@affinity.co).

## Getting Started

### Authentication

Authentication using HTTP Basic Auth.

```bash
curl "https://api.affinity.co/api_endpoint" -u :$APIKEY
```

Authentication using HTTP Bearer Auth.

```bash
curl "https://api.affinity.co/api_endpoint" -H "Authorization: Bearer ${APIKEY}"
```

To use the API, you will need to generate an API secret key. This can be done easily through the Settings Panel that is accessible through the left sidebar on the Affinity web app. For more support, visit the [How to obtain your API Key](https://support.affinity.co/hc/en-us/articles/360032633992-How-to-obtain-your-API-Key) article in our Help Center.

Requests are authenticated using one of the following:

| Authentication Type | Details |
|-------------------|---------|
| [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication) | Provide your API key as the basic auth password. You do not need to provide a username. |
| [HTTP Bearer Auth](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/) | Provide your API key as the bearer token. |

Currently, we support one key per user on your team. Once you have generated a key, you will need to pass in the key with every API request for us to process it successfully. Otherwise, an error with a code of 401 will be returned.

> **Note**  
> Changes made through the API will be attributed to the person the API key is assigned to.

### Request & Response

This is a full-featured RESTful API. We provide reading & writing functionality for each object type in Affinity. All requests use the base URL of https://api.affinity.co/.

Responses to each request are provided as a JSON object. The response is either the data requested, or a valid error message and error code as outlined below.

Here is a list of all the error codes the Affinity API returns in case something does not go as expected:

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - The request was invalid or cannot be served. |
| 401 | Unauthorized - Authentication required or has failed. |
| 403 | Forbidden - The request is understood, but it has been refused or access is not allowed. |
| 404 | Not Found - The requested resource could not be found. |
| 429 | Too Many Requests - Rate limit exceeded. |
| 500 | Internal Server Error - An error occurred on the server. |

> **Note**  
> Requests must be sent over HTTPS. Requests sent over HTTP will not return any data in order to ensure your sensitive information remains secure.

## Rate Limit

## API Rate Limit

The Affinity API sets a limit on the number of calls that a user can make per minute, and that all the users on an account can make per month. It also sets a reasonable limit on the number of concurrent requests.

Requests to both Affinity API versions will count toward the one pool of requests allowed for a user or account. Once a per-minute, monthly, or concurrent rate limit is hit, subsequent requests will return an error.

### Monthly Limit (Account-Level)

Your account plan tier will limit the overall number of requests you can make per month. Current rate limits by plan tier are:

| Plan Tier | Monthly Limit |
|-----------|---------------|
| Starter | 10,000 requests/month |
| Plus | 50,000 requests/month |
| Professional | 200,000 requests/month |
| Enterprise | Custom limits |

#### Per-minute and concurrent request limits still apply to Enterprise-tier customers.

#### Professional tier customers who signed up for Affinity before July 5, 2023 are allotted 40,000 calls per month.

This monthly account-level limit resets at the end of each calendar month.

#### Per Minute Limit (User-Level)

All API requests will be halted at 900 per user, per minute. We may also lower this limit on a temporary basis to manage API availability.

#### Once a rate limit is hit, all further requests will return an error code of 429.

### Concurrent Request Limit (Account-Level)

To protect our system and manage availability across customers, we set a reasonable limit on concurrent requests at the account level. Customers should not expect to hit this limit unless they are hitting it with a very high volume of concurrent requests.

#### Webhook Subscription Limit

There is a limit of three webhook subscriptions per Affinity instance.

## Rate Limit Header

Each external API call will include headers with information about monthly and per-minute limits. This is a convenient way to retrieve your rate limits and usage without needing to hit the /rate-limit endpoint.

| Header Name | Description |
|-------------|-------------|
| X-Affinity-RateLimit-Limit | The total number of requests allowed per month for your account. |
| X-Affinity-RateLimit-Remaining | The number of requests remaining in the current monthly period. |
| X-Affinity-RateLimit-Reset | The timestamp (Unix epoch) when the monthly rate limit resets. |
| X-Affinity-RateLimit-PerMinute-Limit | The maximum number of requests allowed per minute per user (typically 900). |
| X-Affinity-RateLimit-PerMinute-Remaining | The number of requests remaining in the current minute window. |

See the [/rate-limit](#rate-limit) endpoint for more details.

## Data Model

### Overview

The three top-level objects in Affinity are Persons, Organizations, and Opportunities, and everything in the product is centered around these three resources. We refer to a data model that is a person, organization, or opportunity as an "Entity".

The data stored in Affinity can be easily understood as a spreadsheet, with many rows, columns and cells. For each part of a spreadsheet, there are directly equivalent data models in Affinity.

The List view in Affinity represents the spreadsheet itself. A List is a collection of many rows, and the Affinity equivalent of a row is a **List Entry**. Each column in a spreadsheet is represented by a "Field". There are three types of Fields in Affinity: **Global Fields**, **List-specific Fields** and Smart Fields.

The data in each cell is represented by a "Field Value". There are both regular **Field Values** and **Smart Field Values**.

![Data Model Overview](https://api-docs.affinity.co/images/crm-field-mappings-47b2c3ba.png)

**Legend:**

- ![List Entry](https://img.shields.io/badge/List%20Entry-orange) (orange)
- ![Global Field](https://img.shields.io/badge/Global%20Field-blue) (blue)
- ![List-specific Field](https://img.shields.io/badge/List--specific%20Field-red) (red)
- ![Field Value](https://img.shields.io/badge/Field%20Value-purple) (purple)
- ![Smart Field Value](https://img.shields.io/badge/Smart%20Field%20Value-green) (green)

> **Note**  
> When working with Affinity's API, it is important to understand the differences between how data is organized in the CRM versus the API.  
> Although Smart Fields show up as a column in the List, they **do not** exist in the API in the same way **Global Fields** and **List-specific Fields** ones do.  
> To retrieve **Smart Field Values**, see the [Retrieving Field Values](#retrieving-field-values) section.

### Default Field

By default, Affinity creates some fields for you automatically. Below are the fields created by type:

## Common Use Cases

Use the common use cases below to learn how Affinity API endpoints work.

> **Helpful Tips**
>
> - To reduce API calls, create any initial backfills with the REST API then use [Webhooks](#webhook) to keep data synced. You may want to schedule occasional syncs via the REST API to fixed any inconsistencies
> - Your instance may contain multiple fields with the same name (e.g. Last Funding Date). To confirm the field ID, manually make an edit to the field in question and inspect the request payload for the bulk request. The field ID will be listed as `entityAttributeId`
>
> ![Request Payload Example](https://api-docs.affinity.co/images/request-payload-1136ff0a.png)
>
> - The ID for a list, person, organization and opportunity can be found via the URL in the CRM. For a list `affinity.affinity.co/lists/[**list_id**]` and for a company profile `affinity.affinity.co/companies/[**company_id**]`
> - For large lists, use `page_size` and `page_token` parameters in the [`GET /lists/{list_id}/list-entries`](#list-entries) endpoint to improve performance
## Getting Field Values for All List Entries on a List

1. Query [`GET /lists`](#list) to get all lists and filter results by list name to get the appropriate list ID

```
GET /lists Response:
[
  {
    "id": 12058,
    "type": 0,
    "name": "Current Prospects",
    "public": true,
    "owner_id": 477400,
    "list_size": 150
  }
  ...
]
```

2. Query [`GET /lists/{list_id}/list-entries`](#list-entries) to get all list entries. Store the `entity_id` associated with each list entry ID

```
GET /lists/{list_id}/list-entries Response:
[
  {
    "id": 37605676,
    "list_id": 113859,
    "creator_id": 63842761,
    "entity_id": 7133202,
    "entity_type": 8,
    "created_at": "2021-09-12T16:29:15.962-07:00",
    "entity": {
      "id": 7133202,
      "name": "Affinity Opportunity"
    }
  }
  ...
]
```

3. For each list entry, query [`GET /field-values`](#field-value) with the `entity_id` from the previous step. Make sure you are passing `entity_id` through the appropriate parameter (e.g person_id)

```
GET /field-values Response:
[
  {
    "id": 2448594830,
    "field_id": 61223,
    "list_entry_id": 37605676,
    "entity_type": 0,
    "value_type": 3,
    "entity_id": 7133202,
    "value": 5000.0
  }
  ...
]
```

4. Locate field values for a given set of fields (optional)
   1. Query [`GET /fields`](#field) to get all fields. If the given set of fields are all list-specific, it is helpful to pass along the `list_id` parameter to prefilter the results
   2. Filter results of [`GET /fields`](#field) by field name to get the appropriate field ID
   3. Cross-reference the `field_id` from Step 3 with the field ID

```
GET /fields Response:
[
  {
    "id": 61223,
    "name": "Amount",
    "list_id": 12058,
    "value_type": 3,
    "allows_multiple": false,
    "track_changes": true
  }
  ...
]
```

## Getting Field Value Changes for Status Fields

1. Query [`GET /lists`](#list) and filter results to get the appropriate list ID

```
GET /lists Response:
[
  {
    "id": 12058,
    "type": 0,
    "name": "Current Prospects",
    "public": true,
    "owner_id": 477400,
    "list_size": 150
  }
  ...
]
```

2. Locate the appropriate status field:
   1. Query [`GET /fields`](#field) to get all fields. If the given set of fields are all list-specific, it is helpful to pass along the list_id parameter to prefilter the results
   2. Filter results of [`GET /fields`](#field) by field name and cross-reference the `list_id` with the appropriate list ID from Step 1 to confirm you have the appropriate status field

```
GET /fields Response:
[
  {
    "id": 61223,
    "name": "Amount",
    "list_id": 12058,
    "value_type": 3,
    "allows_multiple": false,
    "track_changes": true
  }
  ...
]
```

3. Query [`GET /field-value-changes`](#field-value-change) passing in the `id` from Step 2

```
GET /field-values-changes Response:
[
  {
    "id": 7,
    "entity_attribute_id": 106,
    "changer": {
        "id": 2,
        "type": 1,
        "first_name": "Alice",
        "last_name": "Doe",
        "primary_email": "alice@affinity.co",
        "emails": [
            "alice@affinity.co"
        ]
    },
    "changed_at": "2021-09-17T10:43:12.781-04:00",
    "action_type": 2,
    "list_entry_id": 15709964,
    "person": {
        "id": 2,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "jdoe@alumni.stanford.edu",
        "emails": [
            "jdoe@alumni.stanford.edu"
        ]
    },
    "company": null,
    "opp": null,
    "value": {
        "id": 30,
        "text": "In Progress",
        "rank": 1,
        "color": 3
    },
    "entity_id": 38706,
    "field_id": 61223
  }
  ...
]
```

4. Filter results of [`GET /field-value-changes`](#field-value-change) (e.g.: If you only want status field changes for a specific organization in your list, search by the `list_entry_id`).

```
GET /field-values-changes Response:
[
  {
    "id": 7,
    "entity_attribute_id": 106,
    "changer": {
        "id": 2,
        "type": 1,
        "first_name": "Alice",
        "last_name": "Doe",
        "primary_email": "alice@affinity.co",
        "emails": [
            "alice@affinity.co"
        ]
    },
    "changed_at": "2021-09-17T10:43:12.781-04:00",
    "action_type": 2,
    "list_entry_id": 15709964,
    "person": {
        "id": 2,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "jdoe@alumni.stanford.edu",
        "emails": [
            "jdoe@alumni.stanford.edu"
        ]
    },
    "company": null,
    "opp": null,
    "value": {
        "id": 30,
        "text": "In Progress",
        "rank": 1,
        "color": 3
    },
    "entity_id": 38706,
    "field_id": 61223
  }
  ...
]
```

## Getting the Strongest Relationship Strength Connection to an Organization on a List

1. Query [`GET /lists`](#list) to get all lists and filter results to get the appropriate list ID

```
GET /lists Response:
[
  {
    "id": 12058,
    "type": 0,
    "name": "Current Prospects",
    "public": true,
    "owner_id": 477400,
    "list_size": 150
  }
  ...
]

```

2. Query [`GET /lists/{list_id}/list-entries`](#list-entries) to get all list entries. Store the `entity_id` associated with each list entry ID

```
GET /lists/{list_id}/list-entries Response:
[
  {
    "id": 37605676,
    "list_id": 12058,
    "creator_id": 63842761,
    "entity_id": 7133202,
    "entity_type": 8,
    "created_at": "2021-09-12T16:29:15.962-07:00",
    "entity": {
      "id": 7133202,
      "name": "Affinity",
      "domain": "affinity.co",
      "domains": [
        "affinity.co"
      ],
      "crunchbase_uuid": null,
      "global": false
    }
  }
  ...
]

```

3. For each list entry, query [`GET /organizations/{organization_id}`](#organization-organization_id) to get all list people associated with the organization. Store the `person_ids` associated with each organization

```

GET /organizations/7133202 Response:
{
  "id": 7133202,
  "name": "Affinity",
  "domain": "affinity.co",
  "domains": ["affinity.co"],
  "crunchbase_uuid": null,
  "global": false,
  "person_ids": [89734, 117270, 138123, 274492, 304848, ...],
  "list_entries": [
    {
      "id": 389,
      "list_id": 26,
      "creator_id": 38603,
      "entity_id": 7133202,
      "entity_type": 0,
      "created_at": "2020-12-11T02:26:56.537-08:00",
    }
    ...
  ]
}

```

4. For each person ID from Step 3, query [`GET /relationships-strengths`](#relationship-strength) passing in the person ID. Once all person IDs have been looped through, filter for the highest `strength`

```

GET /relationships-strengths Response:
[
  {
    "internal_id": 26317,
    "external_id": 89734,
    "strength": 0.5
  }
  ...
]

```

## Useful Resources

- [Postman Collection](/postman/collection.json) (Right-click and save as JSON then import into [Postman](https://www.postman.com/))
- [Affinity Zapier Integrations](https://zapier.com/apps/affinity/integrations)
- [Affinity Tray Connectors](https://tray.io/documentation/connectors/service/affinity)

# Partner With Us

If you're a developer interested in building an integration with Affinity's relationship intelligence platform for your customers, please [get in touch here](https://53mt2d9of77.typeform.com/to/LhEs2tzU).

#### List

Lists are the primary data structure that you can interact with in Affinity. Each list manages a collection of either people, organizations, or opportunities. We call people, organizations, and opportunities "entities".

A list in Affinity is easily represented as a spreadsheet. The rows of the spreadsheet are the list entries, and each list entry corresponds to a single person in a list of people, an organization in a list of organizations, or an opportunity in a list of opportunities.

Lists in Affinity can also have any number of custom attributes. These attributes allow you to fully customize your workflow and model the data for your use case. We call these attributes "fields", and they can be either global (applying to all lists) or list-specific (applying only to a particular list).

As a simple example: A list called "Important People" might have 25 people in it. Two of the columns in the spreadsheet could be "Title" and "Industry".

This list would have 25 "list entries". Each list entry would be associated with a single person entity. Furthermore, the list would have two "fields" with the names "Title" and "Industry".

#### The List Resource

| Attribute | Type | Description |
|-----------|------|-------------|
| id | integer | The unique identifier of the list object. |
| type | integer | The type of the entities (people, organizations, or opportunities) contained within the list. Each list only supports one entity type. |
| name | string | The title of the list that is displayed in Affinity. |
| public | boolean | When true, the list is publicly accessible to all users in your Affinity account. When false, the list is private to the list's owner and (explicitly set) additional users. |
| owner_id | integer | The unique ID of the internal person who owns the list. See [here](#list-level-role) for permissions held by a list's owner. |
| creator_id | integer | The unique ID of the internal person who created the list. If the list was created via API, this is the internal person corresponding to the API key that was used. |
| list_size | integer | The number of list entries contained within the list. |
| additional_permissions | object[] | The list of additional internal persons with permissions on the list. Should be a list of objects with `internal_person_id` and `role_id`, where `role_id` comes from the [list-level role](#list-level-role) table below. |

#### List Type

#### List-level Role

See here for details on the permissions held by the role.

#### Get All List

Returns a collection of all the lists visible to you.

#### Parameter

None

#### Return

An array of all the list resources for lists visible to you. Each list resource in the array includes the id, name, and type (refer to [the list resource](#the-list-resource) above for further help).

#### Get a Specific List

#### Example Request

```bash
# Returns an array relationship strengths matching the criteria.
curl "https://api.affinity.co/relationships-strengths?external_id=1234&internal_id=2345" -u :$APIKEY
```

```bash
# Returns an array relationship strengths matching the criteria.
curl "https://api.affinity.co/relationships-strengths?external_id=1234" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /list/{list_id}

Get the details for a specific list given the existing list id.

#### Path Parameter

#### Return

The details of the list resource corresponding to the list ID specified in the path parameter. These details include an array of the fields that are specific to this list. An appropriate error is returned if the list is not found or you do not have permission to access it.

#### Create a New List

#### Example Request

```bash
# Returns the list with the specified `list_id`
curl "https://api.affinity.co/lists/450" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /list

Create a new list with the supplied parameters.

#### Payload Parameter

name string true The title of the list that is displayed in Affinity.

| name | string | true | The title of the list that is displayed in Affinity. |
type integer true The type of the entities (people, organizations, or opportunities) contained within the list. Each list only supports one entity type.

| type | integer | true | The type of the entities (people, organizations, or opportunities) contained within the list. Each list only supports one entity type. |
is_public boolean true Set to true to make the list publicly accessible to all users in your Affinity account. Set to false to make the list private to the list's owner and additional users.

| is_public | boolean | true | Set to true to make the list publicly accessible to all users in your Affinity account. Set to false to make the list private to the list's owner and additional users. |
owner_id integer false The unique ID of the internal person who should own the list. Defaults to the owner of the API key being used. See [here](#list-level-role) for permissions held by a list's owner.

| owner_id | integer | false | The unique ID of the internal person who should own the list. Defaults to the owner of the API key being used. See [here](#list-level-role) for permissions held by a list's owner. |
additional_permission object[] false A list of additional internal persons and the permissions they should have on the list. Should be a list of objects with internal_person_id and role_id, where role_id comes from the list-level role table below.

| additional_permission | "object[]" | false | A list of additional internal persons and the permissions they should have on the list. Should be a list of objects with internal_person_id and role_id, where role_id comes from the [list-level role](#list-level-role) table below. |

#### Return

The list resource that was just created through this request.

#### List Entries

#### The List Entry Resource

Each list comprises a number of entries. Each list entry has a creator, a list that it belongs to, and the underlying entity it represents depending on the type of the list (people, organizations, or opportunities).

Operations like adding and removing entities from a list can be accomplished using the list entry abstraction.

> **Note**  
> Although list entries correspond to rows in an Affinity spreadsheet, the values associated with the entity are not stored inside the list entry resource. If you are trying to update, create, or delete field values, see the [Field Value](#field-value) section.

#### Get All List Entries

#### Example Request

```bash
curl -X POST “https://api.affinity.co/lists” \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{ "name": "My List of Organizations", "type": 1, "is_public": true, "owner_id": 38706, "additional_permissions": [ {"internal_person_id": 38701, "role_id": 0}, {"internal_person_id": 38703, "role_id": 1}, {"internal_person_id": 38900, "role_id": 0} ]}'
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /list/{list_id}/list-entries

If no page size is specified, fetch all the list entries in the list with the supplied list id. If a page size is specified, fetch up to that number of list entries in the list with the supplied list id.

#### Path Parameter

#### Query Parameter

#### Return

If the page_size is not passed in as a parameter, an array of all the list entry resources corresponding to the provided list will be returned. If the page_size is passed in as a parameter, an object with entries and page_token will be returned.

List Entry Resource

#### Get a Specific List Entry

## GET /list/{list_id}/list-entries/{list_entry_id}

Fetch a list entry with a specified id.

#### Path Parameter

#### Return

The list entry object corresponding to the list_entry_id.

#### Create a New List Entry

#### Example Request

```bash
curl "https://api.affinity.co/lists/450/list-entries/16367" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/lists/450/list-entries/56517" \
   -u :$APIKEY \
   -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /list/{list_id}/list-entries

Create a new list entry in the list with the supplied list id.

#### Payload Parameter

> **Note**
> Opportunities cannot be created using this endpoint. Instead, use the POST /opportunities endpoint.

#### Example Request

```bash
curl -X POST “https://api.affinity.co/lists/450/list-entries” \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"entity_id": 38706}'
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /opportunities

> **Note**
> Person and company lists can contain the same entity multiple times. Depending on your use case, before you add an entry, you may want to verify whether or not it exists in the list already.

#### The list entry resource that was just created through this request.

#### Delete a Specific List Entry

#### Example Request

```bash
curl -X POST "https://api.affinity.co/opportunities" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"name": "Penny Opportunity", "list_id": 6645, "person_ids": [38706], "organization_ids": [21442]}'
```

```bash
curl -X POST "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"name": "Penny Opp", "person_ids": [38706, 89734]}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /list/{list_id}/list-entries/{list_entry_id}

Delete a list entry with a specified list_entry_id.

#### Return

The JSON object {"success": true}.

> **Note**
> This will also delete all the field values, if any, associated with the list entry. Such field values will only exist in fields specific to this list.

> **Note**
> If the list entry belongs to an Opportunity list, then the opportunity that the list entry is associated with will also be deleted.

#### Field

As discussed in the previous section, fields as a data model represent the "columns" in a spreadsheet. A field can be specific to a given list, or it can be global. List-specific fields appear as columns only in that particular list, while global fields appear as columns in all lists.

Let us consider two examples:

- Assume you have a list called "Top Referrer", and a new list-specific field (column) called "Number of Referrals" is added to this list. In this case, the "Number of Referrals" column will only be visible in the "Top Referrer" list.

- Now assume you have three lists of people, "Top Referrer", "Friends in Media", "BD Lead", and a person X exists on all three lists. If you want to track where all the people in these 3 lists live, you would create a global field called "Location". This "Location" column would then appear in all three lists.

By default, Affinity provides all teams with a few default global fields: For people, the global fields include Location, Job Title, and Industries. For organizations, the global fields include Stage, Website, and more.

- Global field IDs for people are returned from GET /person/field

#### Example Request

```bash
curl "https://api.affinity.co/lists/450/list-entries/16367" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/lists/450/list-entries/56517" \
   -u :$APIKEY \
   -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /person/field

- Global field IDs for organizations are returned from GET /organization/field
#### Example Request

```bash
curl "https://api.affinity.co/persons/fields" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /organization/field

- List-specific field IDs are also returned from GET /list/{list_id}
#### Example Request

```bash
curl "https://api.affinity.co/organizations/fields" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /list/{list_id}

#### The Field Resource

Each field object has a unique id. It also has a name, which determines the name of the field, and allow_multiple, which determines whether multiple values can be added to a single cell for that field.

Affinity is extremely flexible and customizable, and a lot of that power comes from our ability to support many different value types for fields. Numbers, dates, and locations are all examples of value types.

#### Field Value Type

All the types listed below can be referenced by looking at the Affinity web app as well.

> **Note**
> The API currently does not support updating and modifying fields. This must be done through the web product.

#### Get Field

Returns all fields based on the parameters provided.

Pass the list_id to only fetch fields that are specific to that list. Otherwise, all global and list-specific fields will be returned.

Pass the value_type to fetch fields of a specific value type. Otherwise, all fields of any type will be returned.

Pass the entity_type to fetch fields of a specific entity type. Otherwise, any fields of any entity type will be returned.

Pass the with_modified_name flag to return the fields such that the names have the list name prepended to them in the format [List Name] Field Name (i.e. [Deal] Status).

Pass the exclude_dropdown_option flag to exclude dropdown options from the response. This may be useful when the payload is too large due to too many dropdown options.

#### Query Parameter

#### Return

An array of all the fields requested.

> **Note**
> Results returned with list_id: null mean they do not belong to a specific list and thus are global fields.

> **Note**
> Field endpoint does not return any Crunchbase fields.

#### Create Field

## POST /field

Create a new field with the supplied parameters.

#### Payload Parameter

name string true The name of the field.

entity_type integer true This describes what type of list this field will be associated with. This can be one of three values, see below for all value types.

| name | string | The name of the field. | entity_type |
value_type integer true This describes what values can be associated with the field. This can be one of many values, see the Field Resource section for all value types.

Field Resource

list_id integer false The unique identifier of the list that the field object belongs to if it is specific to a list. This is null if the field is global.

| This describe what type of lists this fields will be associated with the field. This can be one of three value, see below for all value type. | value_type | This describe what value can be associated with the field. This can be one of many value, see the Field Resource section for all value type. | list_id |
allow_multiple boolean false This determines whether multiple values can be added to a single cell for the field.

| false | The unique identifier of the lists that the fields objects belongs to if it is specific to a list. This is null if the fields is global. | allow _multiple | boolean |
is_list_specific boolean false This determines whether the field object belongs to a specific list. If set to true, you must pass in the appropriate list_id.

is_required boolean false This determines whether the field object is required.

| This determine whether multiple value can be added to a single cells for the field. | is _list_ specific | This determine whether the fields objects belongs to a specific list. If set to true, you must pass in the appropriate list_id. | is _required |
#### Field Entity Type

#### Return

The field resource that was just created through this request.

#### Delete a Field

#### Example Request

```bash
curl -X POST "https://api.affinity.co/fields" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"name": "[Deals] Amount", "list_id": 11, "entity_type": 1, "value_type": 3, "allows_multiple": false, "is_list_specific": true}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /fields/{id}

Delete a field with the specified id.

#### Return

{"success": true}

#### Field Value

Field values are displayed in Affinity as the data in the cells of an Affinity spreadsheet.

As an example for how a field value is created:

- Assume there exists a list of people called "Business Development Lead".
- A custom field called "Deal Size" is created on this list. Fields are visually displayed as columns.
- A person X is added to this list. This action creates a list entry for this person.
- A value, 50,000, is entered in the cell corresponding to person X in the Deal Size column.
- 50,000 is now a field value tied to the list entry corresponding to person X, and the "Deal Size" field.
> **Note**
> By default, Affinity creates some fields for you automatically. These include Location, Industry, Job Title, and more. See the Default Field section for more information.

> **Note**
> Opportunities cannot have global field values.

#### The Field Value Resource

Each field value object has a unique id.

A field value also has field_id, entity_id, and list_entry_id attributes that give it the appropriate associations, as noted in the example above.

Use the created_at and updated_at timestamps on field values to determine when the value(s) for a given field have last been added or changed. Please note that what might amount to an "update" in production may actually be a delete followed by a create in the API.

A field value can take on many different kinds of values, depending on the field value type (see Field section).

Field

> **Note**
> When retrieving Field Values from a specific cell in your Affinity list, it may be helpful to think about it as an XY coordinate system. The X coordinate is the List Entry or Entity and the Y coordinate is the Field.

#### Field Value Value Type

The Field Types specified below correspond to the value_type of a field.

#### Get Field Value

#### Example Request

```bash
GET /field-values
```

```bash
GET /field-values Response:
[
{
"id": 2448594830,
"field_id": 61223,
"list_entry_id": 37605676,
"entity_type": 0,
"value_type": 3,
"entity_id": 7133202,
"value": 5000.0
}
...
]
```

```bash
GET /field-values-changes
```

```bash
GET /field-values-changes Response:
[
{
"id": 7,
"entity_attribute_id": 106,
"changer": {
"id": 2,
"type": 1,
"first_name": "Alice",
"last_name": "Doe",
"primary_email": "alice@affinity.co",
"emails": [
"alice@affinity.co"
]
},
"changed_at": "2021-09-17T10:43:12.781-04:00",
"action_type": 2,
"list_entry_id": 15709964,
"person": {
"id": 2,
"type": 1,
"first_name": "John",
"last_name": "Doe",
"primary_email": "jdoe@alumni.stanford.edu",
"emails": [
"jdoe@alumni.stanford.edu"
]
},
"company": null,
"opp": null,
"value": {
"id": 30,
"text": "In Progress",
"rank": 1,
"color": 3
},
"entity_id": 38706,
"field_id": 61223
}
...
]
```

```bash
GET /field-values-changes
```

```bash
GET /field-values-changes Response:
[
{
"id": 7,
"entity_attribute_id": 106,
"changer": {
"id": 2,
"type": 1,
"first_name": "Alice",
"last_name": "Doe",
"primary_email": "alice@affinity.co",
"emails": [
"alice@affinity.co"
]
},
"changed_at": "2021-09-17T10:43:12.781-04:00",
"action_type": 2,
"list_entry_id": 15709964,
"person": {
"id": 2,
"type": 1,
"first_name": "John",
"last_name": "Doe",
"primary_email": "jdoe@alumni.stanford.edu",
"emails": [
"jdoe@alumni.stanford.edu"
]
},
"company": null,
"opp": null,
"value": {
"id": 30,
"text": "In Progress",
"rank": 1,
"color": 3
},
"entity_id": 38706,
"field_id": 61223
}
...
]
```

```bash
curl "https://api.affinity.co/field-values?person_id=38706" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/field-values?person_id=38706" -u :$APIKEY
```

```bash
GET /field-values
```

```bash
curl -X POST "https://api.affinity.co/field-values" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"field_id": 1284, "value": "Architecture", "entity_id": 38706}'
```

```bash
curl -X POST "https://api.affinity.co/field-values" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"field_id": 1284, "value": "Architecture", "entity_id": 38706}'
```

```bash
POST /field-values
```

```bash
curl -X PUT "https://api.affinity.co/field-values/20406836" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"value": "Healthcare"}'
```

```bash
curl -X PUT "https://api.affinity.co/field-values/20406836" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"value": "Healthcare"}'
```

```bash
PUT /field-values/{field_value_id}
```

```bash
curl "https://api.affinity.co/field-values/20406836" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/field-values/20406836" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /field-values/{field_value_id}
```

```bash
curl "https://api.affinity.co/field-value-changes?field_id=236333" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/field-value-changes?field_id=236333" -u :$APIKEY
```

```bash
GET /field-value-changes
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /field-value

Returns all field values attached to a person, organization, opportunity, or list_entry.

#### Query Parameter

#### Return

An array of all the field values associated with the supplied person, organization, opportunity, or list_entry.

> **Note**
> Exactly one of person_id, organization_id, opportunity_id, or list_entry_id must be specified to the endpoint.
>
> - If a person_id, organization_id, or opportunity_id is specified, the endpoint returns all field values tied to these entities - including those that are associated with all list entries that exist for these entities.

> **Note**
> Smart fields cannot be retrieved using the field value endpoint. Smart field values can be retrieved using the with_interaction_date parameter on the GET /person/{person_id} or GET /organization/{organization_id} endpoint.

> **Note**
> Field value endpoint does return Crunchbase fields, but with null values.

#### Create a New Field Value

## POST /field-value

Create a new field value with the supplied parameters.

field_id integer true The unique identifier of the field (column) that the field value is associated with.

entity_id integer true The unique identifier of the entity (person, organization, or opportunity) that the field value is associated with.

| This determine whether the fields objects is required. | field_id | The unique identifier of the fields (column) that the field value is associated with. | entity_id |
value custom true See the Field Value Resource section for all value type. The value specified must correspond to the value_type of the supplied fields. For ranked dropdowns fields like the default Sta

| The unique identifier of the entity (person, organization, or opportunity) that the field value is associated with. | value | custom | See the Field Value Resource section for all value type. The value specified must correspond to the value_type of the supplied fields. For ranked dropdowns fields like the default Status field, you must |
Field Value Resource

list_entry_id integer false The unique identifier of the list entry (list row) that the field value is associated with. Only specify the list_entry_id if the field that the field value is associated with is list-specific.

#### Return

The field value resource that was just created through this request.

#### Update a Field Value

#### Example Request

```bash
curl "https://api.affinity.co/field-values?person_id=38706" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /field-value/{field_value_id}

Update the existing field value with field_value_id with the supplied parameters.

#### value custom true See the Field Value Resource section for all value type. The value specified must correspond to the value_type of the supplied fields. For ranked dropdowns fields like the default Sta

| list_entry_id | The unique identifier of the list entry (lists row) that the field value is associated with. Only specify the list_entry_id if the fields that the field value is associated with is lists specific. | value | custom |
Field Value Resource

#### Return

The field value object that was just updated through this request.

> **Note**
> When updating a specific field value, make sure to use the field_value_id and not the field_id.

#### Delete a Field Value

#### Example Request

```bash
curl "https://api.affinity.co/field-values?person_id=38706" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /field-value/{field_value_id}

Delete a field value with the specified field_value_id.

#### Return

{"success": true}

#### Field Value Change

Field value changes allow you to see historical changes to the values of fields in Affinity. This is especially useful for tracking progress through statuses (e.g. Lead --> Closed Won).

#### Supported Field Types

Not all fields can track historical changes.

Fields that are automatically created and "enriched" by Affinity do not support change tracking.

Among fields that are not enriched, only the ones with the following data types support change tracking:

#### Multi-valued Field

#### Single-valued field

> **Note**
> You can also see if a field does so by looking at the track_change attribute in the Field Resource. The API will return an appropriate error if the field doesn't support historical tracking.
>
> Field Resource

#### The Field Value Change Resource

Each field value change object has a unique id.

A field value change also has field_id, entity_id, list_entry_id attributes that give it the appropriate associations, as noted in the example above.

#### Field Value Change action type

The action types specified below correspond to the action_type of a field value change. This attribute filters the field value changes that are returned. For example, when an action_type of 0 is specified, only created actions will be returned.

> **Note**
> There are some extra attributes returned by this endpoint; they will be deprecated soon and should not be used.

#### Get Field Value Change

#### Example Request

```bash
curl "https://api.affinity.co/field-values?person_id=38706" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /field-value-change

Returns all field value changes attached to a specific field. Field value changes can be filtered by action_type, person, organization, opportunity or list_entry by passing in the appropriate parameters.

#### Return

An array of all the field value changes associated with the supplied field and person, organization, opportunity or list_entry if specified.

> **Note**
> Exactly one of person_id, organization_id, opportunity_id, or list_entry_id must be specified to the endpoint.
>
> - If a person_id, organization_id, or opportunity_id is specified, the endpoint returns all field value changes tied to these entities.
> - If a list_entry_id is specified, the result is filtered by the person_id, organization_id or opportunity_id which is tied to the specified list_entry_id.

#### Person

The person API allows you to manage all the contacts of your organization. These people include anyone your team has ever been in email communication or meeting with, and all the people that your team has added to Affinity.

#### If you are looking to add or remove a person from a list, please check out the List Entries section of the API.

List Entries

- If you are looking to modify a person's field value (one of the cells on Affinity's spreadsheet), please check out the Field Value section of the API.
#### The Person Resource

Each person resource is assigned a unique id and stores the name, type, and email addresses of the person. A person resource also has access to a Smart attribute called primary_email. The value of primary_email is automatically computed and represents the most likely current active email address for the person.

The person resource organization_id is a collection of unique identifiers to the person's associated organizations.

> **Note**
> A person can be associated with multiple organizations. For example, say you have a person who works at Company A, and later moves to Company B. That person would be associated with both organizations.
>
> The person resource type indicate whether a person is internal or external to your team. Every internal person is a user of Affinity on your team, and all other people are external.
>
> Dates of the most recent and upcoming interactions with a person are available in the interaction_date field. This data is only included when passing with_interaction_date=true as a query parameter to the GET /person endpoint.
>
> id integer The unique identifier of the person object.
>
> type integer The type of person ( see below).
>
> | id | integer | The unique identifier of the person object. | type | integer | The type of person (see below). |
> first_name string The first name of the person.
>
> last_name string The last name of the person.
>
> | The type of person ( see below). | first_name | The first name of the person. | last_name |
> email string[] The email addresses of the person.
>
> | The last name of the person. | email | "string[]" | The email addresses of the person. |
> primary_email string The email (automatically computed) that is most likely to be the current active email address of the person.
>
> organization_id integer[] An array of unique identifiers of organizations that the person is associated with.
>
> | primary_email | string | The email (automatically computed) that is most likely to be the current active email address of the person. | organization_id | "integer[]" | An array of unique identifiers of organizations that the person is associated with. |
> opportunity_id integer[] An array of unique identifiers of opportunities that the person is associated with. Only returned when with_opportunities=true.
>
> | An array of unique identifiers of organizations that the person is associated with. | opportunity_id | "integer[]" | An array of unique identifiers of opportunities that the person is associated with. Only returned when with_opportunities=true. |
> current_organization_id integer[] An array of unique identifiers of organizations that the person is currently associated with according to the Affinity Data: Current Organization in-app column. Only returned when with_current_organization=true.
>
> list_entries ListEntry[] An array of list entry resources associated with the person, only returned as part of the Get a Specific Person endpoint.
>
> | current_organization_id | "integer[]" | An array of unique identifiers of organizations that the person is currently associated with according to the Affinity Data: Current Organization in-app column. Only returned when with_current_organization=true. | list_entries | "ListEntry[]" | An array of list entry resources associated with the person, only returned as part of the Get a Specific Person endpoint. |
> Get a Specific Person
>
> interaction_date objects An object with seven string date fields representing the most recent and upcoming interactions with this person: first_email_date, last_email_date, last_event_date, last_chat_message_date, last_interaction_date, next_event_date, next_meeting_date.
>
> | "ListEntry[]" | An array of list entry resources associated with the person, only returned as part of the Get a Specific Person endpoint. | interaction_date | objects | An object with seven string date fields representing the most recent and upcoming interactions with this person: first_email_date, last_email_date, last_event_date, last_chat_message_date, last_interaction_date, next_event_date, next_meeting_date. |
> interaction objects An object with seven fields nested underneath. Each field corresponds to one of the seven interactions, and includes nested fields for date and person_id which indicate the internal person associated with that interaction.
>
> | An object with seven string date fields representing the most recent and upcoming interactions with this person: first_email_date, last_email_date, last_event_date, last_chat_message_date, last_interaction_date, next_event_date, next_meeting_date. | interaction | objects | An object with seven fields nested underneath. Each field corresponds to one of the seven interactions, and includes nested fields for date and person_id which indicate the internal person associated with that interaction. |

#### Person type

#### Search for Person

## GET /person

Search your team's data and fetch all the people that meet the search criteria. The search term can be part of an email address, a first name or a last name.

This result is paginated. An initial request returns an object with two fields: person and next_page_token. person contains an array of person resources. The value of next_page_token should be sent as a query parameter in subsequent requests to get the next page of results.

The absence of a next_page_token indicates that all the records have been fetched, though its presence does not necessarily indicate that there are more resources to be fetched. The next page may be empty.

Pass with_interaction_date=true as a query parameter to include dates of the most recent and upcoming interactions with people. When this parameter is included, people with no interactions will not be returned.

You can filter by interaction date by providing additional query parameters like min_last_email_date or max_next_event_date. The value of these query parameters should be ISO 8601 formatted date strings.

#### Return

An object with two fields: person and next_page_token. person maps to an array of all the person resources that match the search criteria. Does not include the associated organization_id or list_entries.

#### Example Request

```bash
GET /persons/{person_id}
```

```bash
GET /persons/{person_id}
```

```bash
/persons
```

```bash
/persons/{person_id}
```

```bash
GET /persons
```

```bash
curl "https://api.affinity.co/persons?term=doe" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/persons?term=doe" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/persons?term=doe&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/persons?term=doe&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
# To get the results between min_last_email_interaction_date and max_last_email_interaction_date, issue the following query:
curl "https://api.affinity.co/persons" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"min_last_email_date": "2021-01-01T00:00:00", "with_interaction_dates": true, "max_last_email_date": "2021-01-12T23:59:59"}'
```

```bash
# To get the results between min_last_email_interaction_date and max_last_email_interaction_date, issue the following query:
curl "https://api.affinity.co/persons" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"min_last_email_date": "2021-01-01T00:00:00", "with_interaction_dates": true, "max_last_email_date": "2021-01-12T23:59:59"}'
```

```bash
curl "https://api.affinity.co/persons/38706?with_opportunities=true&with_current_organizations=true" \
-u :$APIKEY \
```

```bash
curl "https://api.affinity.co/persons/38706?with_opportunities=true&with_current_organizations=true" \
-u :$APIKEY \
```

```bash
GET /persons/{person_id}
```

```bash
curl -X POST "https://api.affinity.co/persons" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"first_name": "Alice", "last_name": "Doe", "emails": ["alice@affinity.co"], "organization_ids": [1687449]}'
```

```bash
curl -X POST "https://api.affinity.co/persons" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"first_name": "Alice", "last_name": "Doe", "emails": ["alice@affinity.co"], "organization_ids": [1687449]}'
```

```bash
POST /persons
```

```bash
curl -X PUT "https://api.affinity.co/persons/860197" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"first_name": "Allison", "emails": ["allison@affinity.co", "allison@gmail.com"]}'
```

```bash
curl -X PUT "https://api.affinity.co/persons/860197" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"first_name": "Allison", "emails": ["allison@affinity.co", "allison@gmail.com"]}'
```

```bash
PUT /persons/{person_id}
```

```bash
curl "https://api.affinity.co/persons/860197" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/persons/860197" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /persons/{person_id}
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /person/{person_id}

Fetch a person with a specified person_id.

#### Return

The person resource corresponding to the person_id.

#### Create a New Person

#### Example Request

```bash
curl "https://api.affinity.co/persons/38706?with_opportunities=true&with_current_organizations=true" \
  -u :$APIKEY \
```

```bash
curl "https://api.affinity.co/persons/860197" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /person

Create a new person with the supplied parameters.

#### Return

The person resource that was newly created from this successful request.

> **Note**
> If one of the supplied email addresses conflicts with another person object, this request will fail and an appropriate error will be returned.
>
> - If you are looking to add an existing person to a list, please check the List Entries section of the API.

#### Update a person

#### Example Request

```bash
curl -X POST "https://api.affinity.co/persons" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"first_name": "Alice", "last_name": "Doe", "emails": ["alice@affinity.co"], "organization_ids": [1687449]}'
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /person/{person_id}

Update an existing person with person_id with the supplied parameters. Only attributes that need to be changed must be passed in.

#### Return

The person object that was just updated through this request.

#### If you are looking to add an existing person to a list, please check the List Entries section of the API.

> **Note**
> If you are trying to add a new email or organization to a person, the existing values for email and organization_id must also be supplied as parameters.

#### Delete a Person

#### Example Request

```bash
curl -X PUT "https://api.affinity.co/persons/860197" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"first_name": "Allison", "emails": ["allison@affinity.co", "allison@gmail.com"]}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /person/{person_id}

Delete a person with a specified person_id.

#### Return

{"success": true}

> **Note**
> This will also delete all the field values, if any, associated with the person. Such field values exist linked to either global or list-specific fields.

#### Get Global Person Field

#### Example Request

```bash
curl "https://api.affinity.co/persons/38706?with_opportunities=true&with_current_organizations=true" \
  -u :$APIKEY \
```

```bash
curl "https://api.affinity.co/persons/860197" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /person/field

Fetch an array of all the global fields that exist on people. If you aren't sure about what fields are, please read the Field section first.

#### Parameter

None.

#### Return

An array of the global fields that exist on people for your team.

#### Organization

An organization in Affinity represents an external company that your team is in touch with - this could be an organization you're trying to invest in, sell to, or establish a relationship with.

An organization has many people associated with it - these are your team's points of contact at that organization. Just like people, organizations can be added to multiple lists and can be assigned field values.

To make the data quality as good as possible, we have our own proprietary database of organizations that we have developed through third-party partnerships and web scraping. We use this database to enrich organization data automatically.

#### If you are looking to add or remove an organization from a list, please check out the List Entries section of the API.

- If you are looking to modify a field value (one of the cells on Affinity' spreadsheet), please check out the Field Value section of the API.
#### The Organization Resource

Each organization object has a unique id. It also has a name, domain (the website of the organization), and people associated with it. The domain is an important attribute from an automation perspective, as it's used to automatically associate person objects with organizations.

Each organization also has a flag determining whether it's global or not. As mentioned above, Affinity maintains its own database of global organizations that each customer has access to.

> **Note**
> You cannot modify or delete global organizations. If you need to modify data for a global organization, you should create a new organization instead.
>
> Of course, if an organization is manually created by your team, all fields can be modified and the organization can be deleted.
>
> Dates of the most recent and upcoming interactions with an organization are available in the interaction_date field. This data is only included when passing with_interaction_date=true as a query parameter to the GET /organization endpoint.

## GET /organization

id integer The unique identifier of the organization object.

name string The name of the organization.

domain string The website name of the organization. This is used by Affinity to automatically associate person objects with an organization.

| id | The unique identifier of the organization object. | The name of the organization. | domain |
domain string[] An array of all the websites associated with the organization. These are also used to automatically associate person objects with an organization.

| The website name of the organization. This is used by Affinity to automatically associate person objects with an organization. | domain | "string[]" | An array of all the websites associated with the organization. These are also used to automatically associate person objects with an organization. |
person_id integer[] An array of unique identifiers of people that are associated with the organization.

opportunity_id integer[] An array of unique identifiers of opportunities that are associated with the organization.

| person_id | "integer[]" | An array of unique identifiers of people that are associated with the organization. | opportunity_id | "integer[]" | An array of unique identifiers of opportunities that are associated with the organization. |
global boolean Returns whether this organization is a part of Affinity's global data set of organizations. This is always false if the organization was created by you.

list_entries ListEntry[] An array of list entry resources associated with the organization, only returned as part of the Get a Specific Organization endpoint.

| global | boolean | Returns whether this organization is a part of Affinity's global data set of organizations. This is always false if the organization was created by you. | list_entries | "ListEntry[]" | An array of list entry resources associated with the organization, only returned as part of the Get a Specific Organization endpoint. |
Get a specific organization

interaction_date objects An object with seven string date fields representing the most recent and upcoming interactions with this organization: first_email_date, last_email_date, last_event_date, last_chat_message_date, last_interaction_date, next_event_date, next_meeting_date.

| An array of list entry resources associated with the organization, only returned as part of the Get a Specific Organization endpoint. | interaction_date | objects | An object with seven string date fields representing the most recent and upcoming interactions with this organization: first_email_date, last_email_date, last_event_date, last_chat_message_date, last_interaction_date, next_event_date, next_meeting_date. |
interaction objects An object with seven fields nested underneath. Each field corresponds to one of the seven interactions, and includes nested fields for date and person_id which indicate the internal person associated with that interaction.

#### Search for Organization

#### Example Request

```bash
GET /organizations/{organization_id}
```

```bash
GET /organizations/7133202 Response:
{
"id": 7133202,
"name": "Affinity",
"domain": "affinity.co",
"domains": ["affinity.co"],
"crunchbase_uuid": null,
"global": false,
"person_ids": [89734, 117270, 138123, 274492, 304848, ...],
"list_entries": [
{
"id": 389,
"list_id": 26,
"creator_id": 38603,
"entity_id": 7133202,
"entity_type": 0,
"created_at": "2020-12-11T02:26:56.537-08:00",
}
...
]
}
```

```bash
GET /organizations/{organization_id}
```

```bash
GET /organizations/{organization_id}
```

```bash
GET /organizations
```

```bash
GET /organizations/{organization_id}
```

```bash
GET /organizations
```

```bash
curl "https://api.affinity.co/organizations?term=affinity" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/organizations?term=affinity" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/organizations" \
-u :$APIKEY \
-d page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/organizations" \
-u :$APIKEY \
-d page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9
```

```bash
# To get the results between min_last_email_interaction_date and max_last_email_interaction_date, issue the following query:
curl "https://api.affinity.co/organizations" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"min_last_email_date": "2021-01-01T00:00:00", "with_interaction_dates": true, "max_last_email_date": "2021-01-12T23:59:59"}'
```

```bash
# To get the results between min_last_email_interaction_date and max_last_email_interaction_date, issue the following query:
curl "https://api.affinity.co/organizations" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"min_last_email_date": "2021-01-01T00:00:00", "with_interaction_dates": true, "max_last_email_date": "2021-01-12T23:59:59"}'
```

```bash
curl "https://api.affinity.co/organizations/64779194" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/organizations/64779194" -u :$APIKEY
```

```bash
GET /organizations/{organization_id}
```

```bash
curl -X POST "https://api.affinity.co/organizations" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Acme Corporation", "domain": "acme.co", "person_ids": [38706]}'
```

```bash
curl -X POST "https://api.affinity.co/organizations" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Acme Corporation", "domain": "acme.co", "person_ids": [38706]}'
```

```bash
POST /organizations
```

```bash
curl -X PUT "https://api.affinity.co/organizations/120611418" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Acme Corp.", "person_ids": [38706, 89734]}'
```

```bash
curl -X PUT "https://api.affinity.co/organizations/120611418" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Acme Corp.", "person_ids": [38706, 89734]}'
```

```bash
PUT /organizations/{organization_id}
```

```bash
curl "https://api.affinity.co/organizations/120611418" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/organizations/120611418" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /organizations/{organization_id}
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /organization

Search your team's data and fetch all the organizations that meet the search criteria. The search term can be a part of an organization's name or domain.

This result is paginated. An initial request returns an object with two fields: organization and next_page_token. organization contains an array of organization resources. The value of next_page_token should be sent as a query parameter in subsequent requests to get the next page of results.

The absence of a next_page_token indicates that all the records have been fetched, though its presence does not necessarily indicate that there are more resources to be fetched. The next page may be empty.

Pass with_interaction_date=true as a query parameter to include dates of the most recent and upcoming interactions with organizations. When this parameter is included, organizations with no interactions will not be returned.

You can filter by interaction date by providing additional query parameters like min_last_email_date or max_next_event_date. The value of these query parameters should be ISO 8601 formatted date strings.

#### Return

An object with two fields: organization and next_page_token. organization maps to an array of all the organization resources that match the search criteria. next_page_token includes a token to be sent as a query parameter in subsequent requests to get the next page of results.

> **Note**
> When only a search term is supplied, Affinity will search organization resources that are also outside of your instance.

#### Get a Specific Organization

## GET /organization/{organization_id}

Fetch an organization with a specified organization_id.

#### Return

The organization object corresponding to the organization_id.

#### Create a New Organization

## POST /organization

Create a new organization with the supplied parameters.

#### Return

The organization resource that was just created by a successful request.

#### If you are looking to add an existing organization to a list, please check the List Entries section of the API.

#### Update an Organization

#### Example Request

```bash
curl -X POST "https://api.affinity.co/organizations" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"name": "Acme Corporation", "domain": "acme.co", "person_ids": [38706]}'
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /organization/{organization_id}

Update an existing organization with organization_id with the supplied parameters.

#### Return

The organization resource that was just updated through a successful request.

#### If you are looking to add an existing organization to a list, please check the List Entries section of the API.

> **Note**
> If you are trying to add a person to an organization, the existing values for person_id must also be passed into the endpoint.

#### Delete an Organization

#### Example Request

```bash
curl -X PUT "https://api.affinity.co/organizations/120611418" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"name": "Acme Corp.", "person_ids": [38706, 89734]}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /organization/{organization_id}

Delete an organization with a specified organization_id.

#### Return

{"success": true}

> **Note**
> An appropriate error will be returned if you are trying to delete a global organization.
>
> This will also delete all the field values, if any, associated with the organization. Such field values exist linked to either global or list-specific fields.

#### Get Global Organization Field

#### Example Request

```bash
POST /opportunities
```

```bash
GET /opportunities
```

```bash
curl "https://api.affinity.co/opportunities?term=affinity" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/opportunities?term=affinity" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/opportunities?term=affinity&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/opportunities?term=affinity&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/opportunities/117" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/opportunities/117" -u :$APIKEY
```

```bash
GET /opportunities/{opportunity_id}
```

```bash
curl -X POST "https://api.affinity.co/opportunities" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Penny Opportunity", "list_id": 6645, "person_ids": [38706], "organization_ids": [21442]}'
```

```bash
curl -X POST "https://api.affinity.co/opportunities" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Penny Opportunity", "list_id": 6645, "person_ids": [38706], "organization_ids": [21442]}'
```

```bash
POST /opportunities
```

```bash
curl -X POST "https://api.affinity.co/opportunities/120611418" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Penny Opp", "person_ids": [38706, 89734]}'
```

```bash
curl -X POST "https://api.affinity.co/opportunities/120611418" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"name": "Penny Opp", "person_ids": [38706, 89734]}'
```

```bash
PUT /opportunities/{opportunity_id}
```

```bash
curl "https://api.affinity.co/opportunities/120611418" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/opportunities/120611418" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /opportunities/{opportunity_id}
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /organization/field

Fetch an array of all the global fields that exist on organizations. If you aren't sure about what fields are, please read the Field section first.

#### Parameter

None.

#### Return

An array of the fields that exist on all organizations for your team.

#### Opportunities

An opportunity in Affinity represents a potential future sale or deal for your team. It can have multiple people - your team's main points of contact for the opportunity - and organizations associated with it.

Unlike people and organizations, an opportunity can only belong to a single list and, thus, does not have global fields. This list must be provided at the creation of the opportunity. If the list or list-specific fields are deleted, the opportunity will also be deleted.

> **Note**
> If you are looking to remove an opportunity from a list, note that deleting an opportunity is the same as removing an opportunity from a list because an opportunity can only exist on a single list within Affinity.
>
> - If you are looking to modify a field value (one of the cells on Affinity' spreadsheet), please check out the Field Value section of the API.

#### The Opportunity Resource

Each opportunity object has a unique id. It also has a name, person_id and organization_id associated with it, and an array of list_entries. An important attribute to note is list_entries. Because an opportunity can only belong to a single list, the list_entries array will always contain exactly one entry.

Of course, all fields can be modified and the opportunity can be deleted.

#### Search for Opportunities

## GET /opportunities

Search your team's data and fetch all the opportunities that meet the search criteria. The search term can be a part of an opportunity's name.

This result is paginated. An initial request returns an object with two fields: opportunities and next_page_token. opportunities contains an array of opportunity resources. The value of next_page_token should be sent as a query parameter in subsequent requests to get the next page of results.

The absence of a next_page_token indicates that all the records have been fetched, though its presence does not necessarily indicate that there are more resources to be fetched. The next page may be empty.

#### Return

An object with two fields: opportunities and next_page_token. opportunities maps to an array of all the opportunity resources that match the search criteria. next_page_token includes a token to be sent as a query parameter in subsequent requests to get the next page of results.

#### Get a Specific Opportunity

#### Example Request

```bash
curl "https://api.affinity.co/opportunities?term=affinity" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/opportunities?term=affinity&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/opportunities/117" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /opportunities/{opportunity_id}

Fetch an opportunity with a specified opportunity_id.

#### Return

The opportunity object corresponding to the opportunity_id.

#### Create a New Opportunity

#### Example Request

```bash
curl "https://api.affinity.co/opportunities/117" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /opportunities

Create a new opportunity with the supplied parameters.

#### Return

The opportunity resource that was just created by a successful request (without person_id and organization_id).

#### Update an Opportunity

## PUT /opportunities/{opportunity_id}

Update an existing opportunity with opportunity_id with the supplied parameters.

#### Return

The opportunity resource that was just updated through a successful request.

> **Note**
> If you are trying to add a person to an opportunity, the existing values for person_id must also be passed into the endpoint.
>
> If you are trying to add an organization to an opportunity, the existing values for organization_id must also be passed into the endpoint.

#### Example Request

```bash
curl -X POST "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"name": "Penny Opp", "person_ids": [38706, 89734]}'
```

#### Example Response

```json
{
  "id": 123
}
```

#### Delete an Opportunity

## DELETE /opportunities/{opportunity_id}

Delete an opportunity with a specified opportunity_id.

#### Example Request

```bash
curl "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "success": true
}
```

#### Return

{"success": true}

> **Note**
> This will also delete all the field values, if any, associated with the opportunity.

#### Interaction

The interaction API allows you to manage interactions.

#### The Interaction Resource

Different types of interactions have different interaction resources.

> **Note**
> The combination of ID and type for an interaction is unique.

#### Interaction Type

#### Direction Type

#### Logging Type

#### Get All Interaction

#### Example Request

```bash
curl "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /interaction

Return all interactions that meet the query parameters.

#### type integer true The type of interaction to be retrieved.

logging_type integer false The logging type of interaction to be retrieved.

| interaction | objects | An object with seven fields nested underneath. Each field corresponds to one of the seven interactions, and includes nested fields for date and person_id which indicate the internal person associated with that interaction. | type | integer | The type of interaction to be retrieved. | logging_type | integer | The logging type of interaction to be retrieved. |
person_id integer custom* A unique identifier that represents an external Person that was involved in the interaction.

| The logging type of interaction to be retrieved. | person_id | integer | A unique identifier that represents an external Person that was involved in the interaction. |
organization_id integer custom* A unique identifier that represents an Organization that was involved in the interaction.

opportunity_id integer custom* A unique identifier that represents an Opportunity that was involved in the interaction.

| organization_id | integer | A unique identifier that represents an Organization that was involved in the interaction. | opportunity_id | integer | A unique identifier that represents an Opportunity that was involved in the interaction. |
internal_person_id integer false A unique identifier that represents an internal person that was involved in the interaction. This parameter cannot be used to find all of an internal person's interactions. It only filters down the set of interactions returned.

| A unique identifier that represents an Opportunity that was involved in the interaction. | internal_person_id | integer | A unique identifier that represents an internal person that was involved in the interaction. This parameter cannot be used to find all of an internal person's interactions. It only filters down the set of interactions returned. |
direction integer false The direction of the interaction. Only applies to chat messages and emails.

start_time string true A string (formatted according to ISO 8601) representing the start of the time range for the interaction to be retrieved. Must be before end_time. Date range must not exceed one year.

| direction | integer | The direction of the interaction. Only applies to chat messages and emails. | start_time | string | A string (formatted according to ISO 8601) representing the start of the time range for the interaction to be retrieved. Must be before end_time. Date range must not exceed one year. |
ISO 8601

end_time string true A string (formatted according to ISO 8601) representing the end of the time range for the interaction to be retrieved. Must be after start_time. Date range must not exceed one year.

ISO 8601

page_size number false How many results to return per page. (Default is the maximum value of 100.)

| end_time | string | A string (formatted according to ISO 8601) representing the end of the time range for the interaction to be retrieved. Must be after start_time. Date range must not exceed one year. | page_size | number | How many results to return per page. (Default is the maximum value of 100.) |
page_token string false The next_page_token from the previous response required to retrieve the next page of result.

#### One person_id, organization_id or opportunity_id must be specified per request.

- Only one type of interaction can be specified per request.
- An error will be returned if an internal person is used in the person_id parameter.
#### Return

An array of all the interactions filtered by query parameters. next_page_token includes a token to be sent along with the next request as the page_token parameter to fetch the next page of results.

#### Interaction in the API response may not be visible on a CRM profile page if they have the exact same timestamp as another interaction.

#### Get a Specific Interaction

#### Example Request

```bash
curl "https://api.affinity.co/interactions?organization_id=1609909&type=3&start_time=2021-01-01T07:00:00Z&end_time=2021-02-25T21:00:00Z&" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/interactions?organization_id=1609909&type=3&start_time=2021-01-01T07:00:00Z&end_time=2021-02-25T21:00:00Z&" -u :$APIKEY
```

```bash
GET /interactions
```

```bash
# Returns the interactions with the specified `id`
curl "https://api.affinity.co/interactions/15326?type=2" -u :$APIKEY
```

```bash
# Returns the interactions with the specified `id`
curl "https://api.affinity.co/interactions/15326?type=2" -u :$APIKEY
```

```bash
GET /interactions/{id}
```

```bash
curl -X POST "https://api.affinity.co/interactions" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [443, 2021], "type": 0, "date": "2021-02-07T10:56:29.546-08:00", "content": "Create interaction from external API."}'
```

```bash
curl -X POST "https://api.affinity.co/interactions" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [443, 2021], "type": 0, "date": "2021-02-07T10:56:29.546-08:00", "content": "Create interaction from external API."}'
```

```bash
POST /interactions
```

```bash
curl -X PUT "https://api.affinity.co/interactions/3007" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"type": 0, "date": "2022-02-07T10:56:29.546-08:00", "content": "Update interaction from external API."}'
```

```bash
curl -X PUT "https://api.affinity.co/interactions/3007" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"type": 0, "date": "2022-02-07T10:56:29.546-08:00", "content": "Update interaction from external API."}'
```

```bash
PUT /interactions/{id}
```

```bash
curl "https://api.affinity.co/interactions/22984?type=0" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/interactions/22984?type=0" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /interactions/{id}
```

```bash
/interactions
```

```bash
/interactions
```

```bash
/interactions
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /interaction/{id}

Get the detail for a specific interaction given the existing ID and type.

#### Return

The details of the interaction corresponding to the ID and type specified in the path parameters. An appropriate error is returned if an invalid ID and type are supplied.

#### Create a New Interaction

#### Example Request

```bash
# Returns the interactions with the specified `id`
curl "https://api.affinity.co/interactions/15326?type=2" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/interactions/22984?type=0" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /interaction

Create a new interaction with the supplied parameters.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| type | integer | true | The type of interaction to be created. Only meeting (type == 0), calls (type == 1) and chat messages (type == 2) are supported. |

| person_id | integer[] | true | The list of person IDs that are associated with the event. At least one internal person ID must be included (see [Person Resource](#person) for more details on internal persons). |

| content | string | true | The string containing the content of the new interaction. |
| direction | integer | false | The direction of the chat message to be created. Only applies to chat messages (type == 2). |

| date | string | true | A string (formatted according to ISO 8601) representing the date time the interaction occurred. |
ISO 8601

#### Return

The interaction created through this request.

#### When creating an interaction using the API, the users corresponding to the API token will be the creator by default.

#### Update an Interaction

#### Example Request

```bash
curl -X POST "https://api.affinity.co/interactions" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [443, 2021], "type": 0, "date": "2021-02-07T10:56:29.546-08:00", "content": "Create interaction from external API."}'
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /interaction/{id}

Update the content of an existing interaction with the supplied parameters.

> **Note**
> Updating the content of an interaction using the API is not supported when mentioned IDs are in the content.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| type | integer | true | The type of interaction to be updated. |
| person_id | integer[] | true | The list of person IDs that are associated with the event. |
| content | string | false | The string containing the content of the interaction. |
| date | string | false | A string (formatted according to ISO 8601) representing the date time the interaction occurred. |

#### Return

The interaction object that was just updated through this request.

#### Delete an Interaction

#### Example Request

```bash
curl -X PUT "https://api.affinity.co/interactions/3007" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"type": 0, "date": "2022-02-07T10:56:29.546-08:00", "content": "Update interaction from external API."}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /interaction/{id}

Delete the interaction with the specified id.

#### Relationship Strength

Affinity calculates relationship strength between internal and external people based on previous interactions (emails, logged calls, calendar events).

A higher numeric value means that the relationship strength between the two people is higher. Emails, calls, and meetings don't tell the whole story of a relationship, so treat the strength as an estimate rather than an absolute measure.

Relationship strength is usually recalculated daily.

#### The Relationship Strength Resource

The relationship strength resource specifies the two Persons the relationship strength is about, along with the actual value.

Person

There may be at most one resource for every (internal, external) pair. If an internal and external person have no previous interaction, there may be no relationship strength resource for the pair.

#### Get Relationship Strength

#### Example Request

```bash
# Returns the interactions with the specified `id`
curl "https://api.affinity.co/interactions/15326?type=2" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/interactions/22984?type=0" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /relationship-strength

#### Return

An array of the relationship strength matching the criteria.

If an internal_id is given, returns the relationship strength between the given internal and external person. The returned list will have a length of 1 or 0 (if no relationship strength is available between the two people).

If no internal_id is given, returns the relationship strength between all internal people and the given external person. The results are not guaranteed to be sorted in any way.

> **Note**
> Just like field values, notes are used to keep track of state on an entity. They could be notes manually taken from due diligence, a meeting, or a call. Or, notes could be used to store logged activities.

#### The Note Resource

A note object contains content, which is a string containing the note body. In addition, a note can be associated with multiple people, organizations, or opportunities. Each person, organization, or opportunity can have multiple notes associated with it.

id integer The unique identifier of the note object.

creator_id integer The unique identifier of the person object who created the note.

| id | integer | The unique identifier of the note object. | creator_id | integer | The unique identifier of the person object who created the note. |
person_id integer[] An array containing the unique identifiers for all the people relevant to the note. This is the union of associated_person_id and interaction_person_id.

associated_person_id integer[] An array containing the unique identifiers for the people directly associated with the note.

| person_id | "integer[]" | An array containing the unique identifiers for all the people relevant to the note. This is the union of associated_person_id and interaction_person_id. | associated_person_id | "integer[]" | An array containing the unique identifiers for the people directly associated with the note. |
interaction_person_id integer[] An array containing the unique identifiers for the people on the interaction the note is attached to, if any. This will be an empty array if there is no such interaction or there aren't any attendees.

interaction_id integer The unique identifier of the interaction the note is attached to, if any.

| interaction_person_id | "integer[]" | An array containing the unique identifiers for the people on the interaction the note is attached to, if any. This will be an empty array if there is no such interaction or there aren't any attendees. | interaction_id | integer | The unique identifier of the interaction the note is attached to, if any. |
interaction_type integer The type of the interaction the note is attached to, if any.

is_meeting boolean True if the note is attached to a meeting or a call.

| interaction_type | integer | The type of the interaction the note is attached to, if any. | is_meeting | boolean | True if the note is attached to a meeting or a call. |
mentioned_person_id integer[] An array containing the unique identifiers for the people who are @mentioned in the note. If there are no mentioned people, this will be an empty array.

organization_id integer[] An array of unique identifiers of organization objects that are associated with the note.

| mentioned_person_id | "integer[]" | An array containing the unique identifiers for the people who are @mentioned in the note. If there are no mentioned people, this will be an empty array. | organization_id | "integer[]" | An array of unique identifiers of organization objects that are associated with the note. |
opportunity_id integer[] An array of unique identifiers of opportunity objects that are associated with the note.

parent_id integer The unique identifier of the note that this note is a reply to. If this field is null, the note is not a reply.

> **Note**
> Replies will never have values for opportunity_id, person_id, and organization_id.
>
> content string The string containing the content of the note.
>
> | opportunity_id | "integer[]" | An array of unique identifiers of opportunity objects that are associated with the note. | parent_id | integer | The unique identifier of the note that this note is a reply to. If this field is null, the note is not a reply. | content | string | The string containing the content of the note. |
> type integer The type of the note. The supported types for new note creation via API are 0 and 2, which represent plain text and HTML note, respectively.

> **Note**
> Notes with type 3 are AI meeting summaries generated by Affinity Notetaker.
>
> created_at datetime The string representing the time when the note was created.
>
> | type | integer | The type of the note. The supported types for new note creation via API are 0 and 2, which represent plain text and HTML note, respectively. | created_at | datetime | The string representing the time when the note was created. |
> updated_at datetime The string representing the last time the note was updated.
>
> | updated_at | datetime | The string representing the last time the note was updated. |

#### Formatting content as HTML

If you would like to format your note, create them with type equal to 2, as described in Create a New Note. All currently supported formatting options are described below.

Create a New Note

#### Get All Note

## GET /note

Return all notes attached to a person, organization, or opportunity.

#### Return

An array of all the note resources available to you.

#### Get a Specific Note

#### Example Request

```bash
curl "https://api.affinity.co/notes" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/notes" -u :$APIKEY
```

```bash
GET /notes
```

```bash
# Returns the note with the specified `note_id`
curl "https://api.affinity.co/notes/22984" -u :$APIKEY
```

```bash
# Returns the note with the specified `note_id`
curl "https://api.affinity.co/notes/22984" -u :$APIKEY
```

```bash
GET /notes/{note_id}
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "content": "Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "content": "Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&content=Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&content=Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "type": 2, "content": "Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "type": 2, "content": "Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&type=2&content=Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&type=2&content=Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [38706], "organization_ids": [120611418], "parent_id": 22984, "content": "This is a <strong> reply </strong>to the previous note.", "type":2}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"person_ids": [38706], "organization_ids": [120611418], "parent_id": 22984, "content": "This is a <strong> reply </strong>to the previous note.", "type":2}'
```

```bash
POST /notes
```

```bash
curl -X PUT "https://api.affinity.co/notes/22984" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"content": "Had another meeting with Jane and John today"}'
```

```bash
curl -X PUT "https://api.affinity.co/notes/22984" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"content": "Had another meeting with Jane and John today"}'
```

```bash
PUT /notes/{notes_id}
```

```bash
curl "https://api.affinity.co/notes/22984" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/notes/22984" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /notes/{note_id}
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /note/{note_id}

Get the details for a specific note given the existing note id.

#### Return

The details of the note resource corresponding to the note ID specified in the path parameter. An appropriate error is returned if an invalid note is supplied.

#### Example Request

```bash
# Returns the note with the specified `note_id`
curl "https://api.affinity.co/notes/22984" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/notes/22984" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /note

Create a new note with the supplied parameters.

Set the type parameter to 2 to create an HTML note. See [here](#formatting-content-as-html) for more information on the sort of rich text formatting we support in notes. Please note that `<a>` tags aren't currently clickable inside notes.

It is possible to create a reply to an existing note by setting parent_id. The parent note should not have a parent_id itself. It is possible for a single parent note to have multiple reply notes — the replies will be ordered by creation time.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| content | string | true | The string containing the content of the new note. See [formatting options](#formatting-content-as-html) for HTML support. |
| person_id | integer[] | custom* | An array of unique identifiers of person objects that are associated with the new note. |
| organization_id | integer[] | custom* | An array of unique identifiers of organization objects that are associated with the new note. |
| opportunity_id | integer[] | custom* | An array of unique identifiers of opportunity objects that are associated with the new note. |
| type | integer | false | The type of the new note. Defaults to 0. The types 0 and 2 represent plain text and HTML note, respectively. If submitting HTML, see the [formatting options](#formatting-content-as-html). |
| parent_id | integer | custom* | The unique identifier of the note to which the newly created note should reply. See comment above. |
| creator_id | integer | false | The ID of a Person resource who should be recorded as the author of the note. Must be a person who can access Affinity. If not provided, the creator defaults to the owner of the API key. |
| created_at | datetime | false | A string (formatted according to ISO 8601) representing the creation time to be recorded for the note. If not provided, defaults to the current time. Does not support time in the future. |

#### Return

The note resource created through this request.

> **Note**
> At least one person_id, organization_id, opportunity_id, or parent_id must be specified to the endpoint.
>
> When creating a note using the API, the user corresponding to the API token will be the creator by default.
>
> To ensure that content gets encoded properly, it is recommended to submit either application/json or application/x-www-form-urlencoded instead of query parameters.

#### Update a Note

#### Example Request

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "content": "Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&content=Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."
```

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "type": 2, "content": "Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."}'
```

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&type=2&content=Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."
```

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [38706], "organization_ids": [120611418], "parent_id": 22984, "content": "This is a <strong> reply </strong>to the previous note.", "type":2}'
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /note/{note_id}

Update the content of an existing note with note_id with the supplied content parameter.

#### Return

The note object that was just updated through this request.

> **Note**
> You cannot update the content of a note that has mentions. You also cannot update the content of a note associated with an email. You cannot update the type of a note.

#### Delete a Note

#### Example Request

```bash
curl -X PUT "https://api.affinity.co/notes/22984" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"content": "Had another meeting with Jane and John today"}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /note/{note_id}

Delete a note with a specified note_id.

#### Return

{"success": true}

> **Note**
> An appropriate error will be returned if you are not the creator of the note you are trying to delete.

#### Entity File

Entity files are files uploaded to a relevant entity. Possible files, for example, would be a pitch deck for an opportunity or a physical mail correspondence for a person.

#### The Entity File Resource

#### Get All File

#### Example Request

```bash
# Returns the note with the specified `note_id`
curl "https://api.affinity.co/notes/22984" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/notes/22984" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /entity-file

Return all entity files within your organization. This result will be an object with two fields: entity_file and next_page_token. entity_file maps to an array of all the entity file resources. The value of next_page_token should be sent as a query parameter in subsequent requests to get the next page of results.

Can optionally be filtered to return only entity files associated with a specific person, organization, or opportunity.

#### Return

An object with two fields: entity_file and next_page_token. entity_file maps to an array of all the entity file resources. See description for more details on pagination.

#### Get a Specific File

#### Example Request

```bash
curl "https://api.affinity.co/entity-files" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/entity-files" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/entity-files?page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/entity-files?page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

```bash
GET /entity-files
```

```bash
curl "https://api.affinity.co/entity-files/43212" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/entity-files/43212" -u :$APIKEY
```

```bash
GET /entity-files/{entity_file_id}
```

```bash
curl "https://api.affinity.co/entity-files/download/12345" \
-u :$APIKEY \
-L \
-o Downloads/file.png
```

```bash
curl "https://api.affinity.co/entity-files/download/12345" \
-u :$APIKEY \
-L \
-o Downloads/file.png
```

```bash
GET /entity-files/download/{entity_file_id}
```

```bash
# Single file upload
curl -X POST "https://api.affinity.co/entity-files" \
-u :$APIKEY \
-H 'Content-Type: multipart/form-data' \
-F file=@file.txt \
-F person_id=1
```

```bash
# Single file upload
curl -X POST "https://api.affinity.co/entity-files" \
-u :$APIKEY \
-H 'Content-Type: multipart/form-data' \
-F file=@file.txt \
-F person_id=1
```

```bash
# Multi file upload
curl -X POST "https://api.affinity.co/entity-files" \
-u :$APIKEY \
-H 'Content-Type: multipart/form-data' \
-F 'files[]=@file1.txt' \
-F 'files[]=@file2.txt' \
-F person_id=1
```

```bash
# Multi file upload
curl -X POST "https://api.affinity.co/entity-files" \
-u :$APIKEY \
-H 'Content-Type: multipart/form-data' \
-F 'files[]=@file1.txt' \
-F 'files[]=@file2.txt' \
-F person_id=1
```

```bash
POST /entity-files
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /entity-file/{entity_file_id}

Fetch an entity file with a specified entity_file_id.

#### Return

The entity file resource corresponding to the entity_file_id.

#### Download File

#### Example Request

```bash
curl "https://api.affinity.co/entity-files" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /entity-file/download/{entity_file_id}

Download an entity file with a specified entity_file_id.

#### Return

The actual entity file corresponding to the entity_file_id.

> **Note**
> The download location of entity files is provided via a redirect from our endpoint and requires the -L flag.

#### Upload File

#### Example Request

```bash
curl "https://api.affinity.co/entity-files/download/12345" \
  -u :$APIKEY \
  -L \
  -o Downloads/file.png
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /entity-file

Upload file attached to the entity with the given id.

The file will display on the entity's profile, provided that the entity is not a person internal to the user's organization.

#### Return

{"success": true}

> **Note**
> File must be attached to a single entity, specified using one of the three entity ID parameters (person_id, organization_id, and opportunity_id).
>
> At least one file must be uploaded using the file parameter.

#### Reminder

The reminder API allows you to manage reminders.

#### The Reminder Resource

A reminder object contains content, which is a string containing the reminder content. In addition, a person, organization or opportunity can be tagged to the reminder.

#### Reminder Type

#### Reminder Reset Type

#### Reminder Status Type

#### Get All Reminder

#### Example Request

```bash
curl "https://api.affinity.co/entity-files" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /reminder

Return all reminders that meet the query parameters.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| person_id | integer | false | A unique identifier that represents a Person that was directly attached to the retrieved reminder. |
| organization_id | integer | false | A unique identifier that represents an Organization that was directly attached to the retrieved reminder. |
| opportunity_id | integer | false | A unique identifier that represents an Opportunity that was directly attached to the retrieved reminder. |
| creator_id | integer | false | A unique identifier that represents an internal person whose created reminders should be retrieved. |
| owner_id | integer | false | A unique identifier that represents an internal person that was assigned to the retrieved reminder. |
| completer_id | integer | false | A unique identifier that represents an internal person whose completed reminders should be retrieved. |
| type | integer | false | The type of reminder to be retrieved. |
| reset_type | integer | false | The reset type of reminder to be retrieved. Required when type == 1. |
| status | integer | false | The status of reminder to be retrieved. |
| due_before | string | false | A string (formatted according to ISO 8601) representing the date that reminders to be retrieved are due before. |
| due_after | string | false | A string (formatted according to ISO 8601) representing the date that reminders to be retrieved are due after. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The next_page_token from the previous response required to retrieve the next page of results. |

#### Return

An array of all the reminders filtered by query parameters. next_page_token includes a token to be sent along with the next request as the page_token parameter to fetch the next page of results.

#### Get a Specific Reminder

#### Example Request

```bash
curl "https://api.affinity.co/reminders?page_size=2&status=2" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/reminders?page_size=2&status=2" -u :$APIKEY
```

```bash
GET /reminders
```

```bash
# Returns the reminder with the specified `reminder_id`
curl "https://api.affinity.co/reminders/15326" -u :$APIKEY
```

```bash
# Returns the reminder with the specified `reminder_id`
curl "https://api.affinity.co/reminders/15326" -u :$APIKEY
```

```bash
GET /reminders/{reminder_id}
```

```bash
curl -X POST "https://api.affinity.co/reminders" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"owner_id": 443, "person_id": 2021, "type": 0, "due_date": "2021-11-30", "content": "Create reminder from external API."}'
```

```bash
curl -X POST "https://api.affinity.co/reminders" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"owner_id": 443, "person_id": 2021, "type": 0, "due_date": "2021-11-30", "content": "Create reminder from external API."}'
```

```bash
POST /reminders
```

```bash
curl -X PUT "https://api.affinity.co/reminders/15385" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"type": 1, "reset_type": 0, "reminder_days": 30}'
```

```bash
curl -X PUT "https://api.affinity.co/reminders/15385" \
-u :$APIKEY \
-H "Content-Type: application/json" \
-d '{"type": 1, "reset_type": 0, "reminder_days": 30}'
```

```bash
PUT /reminders/{reminder_id}
```

```bash
curl "https://api.affinity.co/reminders/22984" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/reminders/22984" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /reminders/{reminder_id}
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /reminder/{reminder_id}

Get the details for a specific reminder given the existing reminder id.

#### Return

The details of the reminder corresponding to the reminder ID specified in the path parameter. An appropriate error is returned if an invalid reminder ID is supplied.

#### Create a New Reminder

#### Example Request

```bash
# Returns the reminder with the specified `reminder_id`
curl "https://api.affinity.co/reminders/15326" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/reminders/22984" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /reminder

Create a new reminder with the supplied parameters.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| owner_id | integer | true | A unique identifier that represents an internal person that is assigned to the reminder. |

| content | string | false | The string containing the content of the new reminder. |
type integer true The type of reminder to be created.

| type | integer | true | The type of reminder to be created. |
reset_type integer false The reset type of reminder to be created. Required when type == 1.

| reset_type | integer | false | The reset type of reminder to be created. Required when type == 1. |
person_id integer false A unique identifier that represents a Person that is tagged in the reminder to be created.

| person_id | integer | false | A unique identifier that represents a Person that is tagged in the reminder to be created. |
organization_id integer false A unique identifier that represents an Organization that is tagged in the reminder to be created.

| organization_id | integer | false | A unique identifier that represents an Organization that is tagged in the reminder to be created. |
opportunity_id integer false A unique identifier that represents an Opportunity that is tagged in the reminder to be created.

| opportunity_id | integer | false | A unique identifier that represents an Opportunity that is tagged in the reminder to be created. |
due_date string false A string (formatted according to ISO 8601) representing the due date of the reminder to be created. Required when type == 0.

| due_date | string | false | A string (formatted according to ISO 8601) representing the due date of the reminder to be created. Required when type == 0. |
reminder_day integer false When a recurring reminder is completed or reset, the number of days before the reminder is due again. Required when type == 1.

| reminder_day | integer | false | When a recurring reminder is completed or reset, the number of days before the reminder is due again. Required when type == 1. |
is_completed integer false Indicator if the reminder has been completed.

| is_completed | integer | false | Indicator if the reminder has been completed. |

> **Note**
> At most one of person_id, organization_id or opportunity_id can be specified.

#### Return

The reminder created through this request.

> **Note**
> When creating a reminder using the API, the user corresponding to the API token will be the creator by default.

#### Update a Reminder

#### Example Request

```bash
curl -X POST "https://api.affinity.co/reminders" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"owner_id": 443, "person_id": 2021, "type": 0, "due_date": "2021-11-30", "content": "Create reminder from external API."}'
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /reminder/{reminder_id}

Update the content of an existing reminder with reminder_id with the supplied parameters.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| owner_id | integer | false | A unique identifier that represents an internal person that is assigned to the reminder. |
| content | string | false | The string containing the content of the reminder. |
| type | integer | false | The type of reminder to be updated. |
| reset_type | integer | false | The reset type of reminder to be updated. Required when type == 1. |
| due_date | string | false | A string (formatted according to ISO 8601) representing the due date of the reminder to be updated. Required when type == 0. |
| reminder_day | integer | false | When a recurring reminder is completed or reset, the number of days before the reminder is due again. Required when type == 1. |
| is_completed | integer | false | Indicator if the reminder has been completed. |

#### Return

The reminder object that was just updated through this request.

#### Delete a Reminder

#### Example Request

```bash
curl -X PUT "https://api.affinity.co/reminders/15385" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"type": 1, "reset_type": 0, "reminder_days": 30}'
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /reminder/{reminder_id}

Delete the reminder with the specified reminder_id.

#### Return

{"success": true}

#### Webhook

Webhooks allow you to be notified of events that happen on your Affinity instance. For example, your app can be notified when a list is created, a field value is updated, a person is deleted, and more.

#### The Webhook Subscription Resource

Each webhook subscription object has a unique id. It also has a webhook_url and subscription associated with it.

| id | integer | The unique identifier of the webhook subscription object. | webhook_url | string | The URL to which the webhooks are sent. |
webhook_url string The URL to which the webhooks are sent.

subscription string[] An array of webhook events that are enabled for that endpoint. An empty array indicates subscription to all webhook events. See below for the complete list of supported webhook events.

| subscription | "string[]" | An array of webhook events that are enabled for that endpoint. An empty array indicates subscription to all webhook events. See [below](#supported-webhook-event) for the complete list of supported webhook events. | disabled | boolean | If the subscription is disabled, this is true. Otherwise, this is false by default. A subscription may be disabled manually via API or automatically if we are not able to process it. |
disabled boolean If the subscription is disabled, this is true. Otherwise, this is false by default. A subscription may be disabled manually via API or automatically if we are not able to process it.

created_by integer The unique identifier of the user who created the webhook subscription.

| created_by | integer | The unique identifier of the user who created the webhook subscription. |

> **Note**
> If webhooks cannot be delivered as a result of a timeout or a connectivity issue with the webhook URL, Affinity will retry the delivery with an exponential backoff for up to 10 hours. If Affinity is still unable to deliver the webhook after this time, the webhook subscription will be automatically disabled.

#### Supported Webhook Event

> **Note**
> The Field Value webhook events do not include enrichment events; updates to enrichment field values are not supported.
>
> - Example of our webhook response can be found in the [Help Center](https://help.affinity.co).
> - Field webhooks are not fired for Crunchbase fields.
> - Field value webhooks are fired with `null` value for Crunchbase fields.

#### Get All Webhook Subscription

#### Example Request

```bash
# Returns the reminder with the specified `reminder_id`
curl "https://api.affinity.co/reminders/15326" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/reminders/22984" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /webhook

Return all of your organization's webhook subscriptions.

#### Return

An array of all the webhook subscription resources.

#### Get a Specific Webhook Subscription

#### Example Request

```bash
curl "https://api.affinity.co/webhook" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/webhook" -u :$APIKEY
```

```bash
GET /webhook
```

```bash
curl "https://api.affinity.co/webhook/1234" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/webhook/1234" -u :$APIKEY
```

```bash
GET /webhook/{webhook_subscription_id}
```

```bash
curl -X POST "https://api.affinity.co/webhook/subscribe" \
-u :$APIKEY \
-d webhook_url="https://hooks.example.com/webhook"
```

```bash
curl -X POST "https://api.affinity.co/webhook/subscribe" \
-u :$APIKEY \
-d webhook_url="https://hooks.example.com/webhook"
```

```bash
POST /webhook/subscribe
```

```bash
curl "https://api.affinity.co/webhook/1234" \
-u :$APIKEY \
-d webhook_url="https://hooks.example.com/webhook" \
-d disabled=true \
-X "PUT"
```

```bash
curl "https://api.affinity.co/webhook/1234" \
-u :$APIKEY \
-d webhook_url="https://hooks.example.com/webhook" \
-d disabled=true \
-X "PUT"
```

```bash
PUT /webhook/{webhook_subscription_id}
```

```bash
curl "https://api.affinity.co/webhook/1234" \
-u :$APIKEY \
-X "DELETE"
```

```bash
curl "https://api.affinity.co/webhook/1234" \
-u :$APIKEY \
-X "DELETE"
```

```bash
DELETE /webhook/{webhook_subscription_id}
```

#### Example Response

```json
{
"id": 1234,
"webhook_url": "https://hooks.example.com/webhook",
"subscriptions": [
"list.created",
"person.created",
"organization.created",
"opportunity.created"
],
"disabled": false,
"created_by": 5678
}
```

## GET /webhook/{webhook_subscription_id}

Get the details for a specific webhook subscription given the specified webhook_subscription_id.

#### Return

The webhook subscription object corresponding to the webhook_subscription_id.

#### Create a New Webhook Subscription

#### Example Request

```bash
curl "https://api.affinity.co/webhook/1234" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -d webhook_url="https://hooks.example.com/webhook" \
  -d disabled=true \
  -X "PUT"
```

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## POST /webhook/subscribe

Create a new webhook subscription with the supplied parameters. If the endpoint returns an invalid response, the webhook creation will fail.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| webhook_url | string | true | The URL to which the webhook will be sent. |
| subscription | string[] | false | An array of webhook events that will be enabled for that endpoint. Leave out this parameter or pass an empty array to subscribe to all webhook events. You can find the complete list of supported webhook events in the [Supported Webhook Event](#supported-webhook-event) section. |

#### Return

The webhook subscription object that was just created from this successful request per organization.

> **Note**
> There is a limit of three webhook subscriptions per Affinity instance.

#### Update a Webhook Subscription

#### Example Request

```bash
curl -X POST "https://api.affinity.co/webhook/subscribe" \
-u :$APIKEY \
-d webhook_url="https://hooks.example.com/webhook"
```

#### Example Response

```json
{
  "id": 123
}
```

## PUT /webhook/{webhook_subscription_id}

Update webhook subscription with the supplied parameters. A webhook subscription can only be updated by its creator. If the endpoint returns an invalid response, the webhook update will fail.

#### Parameter

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| webhook_url | string | false | The URL to which the webhook will be sent. |
| subscription | string[] | false | An array of webhook events that will be enabled for that endpoint. Leave out this parameter or pass an empty array to subscribe to all webhook events. You can find the complete list of supported webhook events in the [Supported Webhook Event](#supported-webhook-event) section. |

#### Return

The webhook subscription object that was just updated through this request.

| disabled | boolean | false | Change the status of a subscription. To enable a subscription, provide the value as false. Otherwise, provide the value as true. |

#### Return

The webhook subscription object that was just updated from this successful request.

#### Delete a Specific Webhook Subscription

#### Example Request

```bash
curl "https://api.affinity.co/webhook/1234" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -d webhook_url="https://hooks.example.com/webhook" \
  -d disabled=true \
  -X "PUT"
```

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## DELETE /webhook/{webhook_subscription_id}

Delete a webhook subscription with a specified webhook_subscription_id. A webhook subscription can only be deleted by its creator, or an admin.

#### Return

{"success": true}

#### Whoami

The Whoami API gives the user metadata about the user's authentication and Affinity instance information, including the instance subdomain. This can be used for linking back to the user's Affinity instance.

#### The Whoami Resource

Querying the Whoami endpoint will give information about the user, Affinity instance, and authentication method.

#### Get Whoami

#### Example Request

```bash
curl "https://api.affinity.co/webhook/1234" -u :$APIKEY
```

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -d webhook_url="https://hooks.example.com/webhook" \
  -d disabled=true \
  -X "PUT"
```

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{
  "id": 123
}
```

## GET /auth/whoami

Get information about the user sending the request, and their affiliated company.

There are no query or path parameters for this method. The information needed is contained within the API key.

#### Return

JSON body of data including tenant, user, and grant information.

#### Example Request

```bash
curl "https://api.affinity.co/auth/whoami" -u :$API_KEY
```

```bash
curl "https://api.affinity.co/auth/whoami" -u :$API_KEY
```

```bash
GET /auth/whoami
```

```bash
/auth/whoami
```

#### Example Response

```json
{
  "id": 123
}
```

## Rate Limit Endpoint

The rate limit endpoint allows you to see your monthly account-level and per minute user-level API limits and usage. The monthly account-level calls limit resets at the end of each calendar month.

## The Rate Limit Resource

The rate limit resource includes information about account (AKA organization)-level and API key-level rate limits and usage.

> **Note**
> /rate-limit and /auth/whoami endpoints are exempt from organization-level monthly rate limit.

## Get Rate Limit Information

## GET /rate-limit

Querying the rate limit endpoint will yield information about account (AKA organization)-level and API key-level rate limits and usage.

#### Return

The rate limit resource, a JSON body of data including limit, calls remaining, seconds until reset and calls count.

#### Changelog

#### 2025-11-05

- Added support for bearer authentication
#### 2024-07-17

- At least one associated person, company, opportunity, or parent note must be specified when creating a note.
creating a note

#### 2024-05-01

- /interaction now restricts the duration between start_time and end_time to a maximum of one year
- /interaction now ensures that the provided start_time is before the provided end_time
- /interaction now has a maximum page_size of 100
#### 2023-08-07

- Added associated_person_id, interaction_person_id, interaction_id, and interaction_type to the note resource. The person_id, associated_person_id, and interaction_person_id properties on a note have been updated. See [the note resource](#the-note-resource) for more details.

#### 2023-07-27

- Datetime values in webhook bodies and API responses are ISO 8601-formatted date strings. For example: "2023-06-21T16:00:28.315-07:00".
#### 2023-07-17

- Added information about notes with type 1. See [note with type 1](#the-note-resource) for more details.

#### 2023-07-03

- Updated API access information for Professional tier customers.
#### 2023-06-13

- The created_at parameter on the POST endpoint for notes no longer accepts timestamps in the future. See [POST /note](#post-note) for more details.

#### 2023-05-17

- Added 403 error codes for permission-related errors. See [error codes](#introduction) for more details.

#### 2023-03-27

- Added the ability to create a List. See [Create a New List](#create-a-new-list) for more details.

- Updated Postman collection to help developers get started.
Postman collection

- Added documentation on formatting option for HTML note.
documentation

#### 2023-03-09

- Account for chat message when returning interaction info on the GET endpoint for Person and Organization.
Organization

#### 2023-02-28

- Added the ability to create HTML note.
create HTML note

- Added the ability to create a note within a thread.
create a note within a thread

#### 2023-02-10

- Added Rate Limit Header section to the Rate Limit documentation.
#### 2023-02-08

- Added created_at and updated_at timestamp to Field Value.
- Added an updated_at timestamp to Note.
#### 2023-02-07

- Added the ability to retrieve Current Organization columns data on Person.
#### 2022-09-06

- Added Rate Limit endpoint and documentation. Moved from a daily to a per minute per user limit. Monthly per account limit remain the same.
#### 2022-09-02

- Added entity_type and exclude_dropdown_option documentation to Field.
#### 2022-05-05

- Added enrichment_source documentation to Field.
#### 2022-04-11

- Added Partner With Us section.
#### 2022-03-21

- Added opportunity_id fields to person and organization response.
#### 2022-02-23

- Added Interaction API documentation.
Interaction API

#### 2022-02-17

- Updated GET entity file and entity file webhook to exclude non-users uploaded file.
GET entity file

#### 2022-02-03

- Added Whoami API documentation.

#### 2022-02-01

- Added Reminder API documentation.
Reminder API

- Added Reminder webhook event.
Reminder webhook

#### 2022-01-28

- Added organization.merged event to Webhook.
- Added mentioned_person_id and is_meeting fields to Note.
#### 2021-11-22

- Added link out to Help Center for webhook response
Help Center

#### 2021-11-19

- Updated GET field value change to be filterable by action_type, person, organization, opportunity or list_entry by passing in the appropriate parameter.
GET field value change

#### 2021-10-15

- Minor content update
#### 2021-10-04

- Update to Example Response.
- Responsive tweak.
#### 2021-09-07

- Revamped API documentation Added Common Use Case section. Added Rate Limit section. Update to PUT and POST cURL example.
- Added Common Use Case section.
Common Use Case

- Added Rate Limit section.
- Update to PUT and POST cURL example.
#### 2021-08-18

- Fixed typo in the API doc where entity_id and creator_id wa in path paramater when they should be inside the payload parameter for Create a New List Entry.
#### 2021-07-28

- Fixed typo in Relationship Strength section.
#### 2021-05-05

- Updated API rate limit information.

#### Example Request

```bash
/rate-limit
```

```bash
/rate-limit
```

```bash
curl "https://api.affinity.co/rate-limit" -u :$API_KEY
```

```bash
curl "https://api.affinity.co/rate-limit" -u :$API_KEY
```

```bash
GET /rate-limit
```

#### Example Response

```json
{
  "id": 123
}
```
