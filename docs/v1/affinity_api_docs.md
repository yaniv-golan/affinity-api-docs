# Affinity API v1 Documentation (Auto-synced)

> **⚠️ IMPORTANT DISCLAIMER**
>
> **This is an UNOFFICIAL markdown copy of the Affinity API v1 documentation.** The official and authoritative documentation is maintained by Affinity at:
>
> **📚 Official Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)
>
> **Always refer to the official Affinity documentation for the most up-to-date and accurate information.**

---

## About This Document

This markdown version of the Affinity API v1 documentation was generated automatically to provide:

- **Better compatibility with AI coding assistants**
- **Offline access**
- **Text-based search**
- **Version control**
- **Direct raw access**

**Source:** Extracted from the live Affinity API documentation at https://api-docs.affinity.co/
**Documentation Version:** This copy is based on the official documentation as it appeared on **November 06, 2025 at 16:49:04 UTC** (Last updated: 11/06/2025 16:49:04 UTC).
**Raw Markdown URL:** `https://raw.githubusercontent.com/yaniv-golan/affinity-api-docs/main/docs/v1/affinity_api_docs.md`

> **⚠️ Use at Your Own Risk**
>
> While every effort is made to ensure accuracy, this is an unofficial copy and may contain errors or outdated information.

## Contact & Support

- **Affinity Support:** [support@affinity.co](mailto:support@affinity.co)
- **Official v1 Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)
- **Official v2 Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Authentication](#authentication)
  - [Requests & Responses](#requests--responses)
- [Rate Limits](#rate-limits)
  - [API Rate Limits](#api-rate-limits)
    - [Monthly Limits (Account-Level)](#monthly-limits-account-level)
    - [Per Minute Limits (User-Level)](#per-minute-limits-user-level)
    - [Concurrent Request Limits (Account-Level)](#concurrent-request-limits-account-level)
  - [Webhook Subscription Limit](#webhook-subscription-limit)
  - [Rate Limit Headers](#rate-limit-headers)
- [Data Model](#data-model)
  - [Overview](#overview)
  - [Default Fields](#default-fields)
    - [Global Fields](#global-fields)
    - [Smart Fields](#smart-fields)
    - [List-specific Fields](#list-specific-fields)
- [Common Use Cases](#common-use-cases)
      - [Helpful Tips](#helpful-tips)
  - [Getting Field Values for All List Entries on a List](#getting-field-values-for-all-list-entries-on-a-list)
  - [Getting Field Value Changes for Status Fields](#getting-field-value-changes-for-status-fields)
  - [Getting the Strongest Relationship Strength Connection to an Organization on a List](#getting-the-strongest-relationship-strength-connection-to-an-organization-on-a-list)
  - [Useful Resources](#useful-resources)
- [Partner With Us](#partner-with-us)
- [Lists](#lists)
  - [The List Resource](#the-list-resource)
    - [List Types](#list-types)
    - [List-level Roles](#list-level-roles)
  - [Get All Lists](#get-all-lists)
  - [Get a Specific List](#get-a-specific-list)
  - [Create a New List](#create-a-new-list)
- [List Entries](#list-entries)
  - [The List Entry Resource](#the-list-entry-resource)
  - [Get All List Entries](#get-all-list-entries)
  - [Get a Specific List Entry](#get-a-specific-list-entry)
  - [Create a New List Entry](#create-a-new-list-entry)
      - [Notes](#notes)
  - [Delete a Specific List Entry](#delete-a-specific-list-entry)
      - [Notes](#notes-1)
- [Fields](#fields)
      - [Notes](#notes-2)
  - [The Field Resource](#the-field-resource)
    - [Field Value Types](#field-value-types)
  - [Get Fields](#get-fields)
  - [Create Field](#create-field)
    - [Field Entity Types](#field-entity-types)
  - [Delete a Field](#delete-a-field)
- [Field Values](#field-values)
      - [Notes](#notes-3)
  - [The Field Value Resource](#the-field-value-resource)
    - [Field Value Value Types](#field-value-value-types)
  - [Get Field Values](#get-field-values)
      - [Notes](#notes-4)
  - [Create a New Field Value](#create-a-new-field-value)
  - [Update a Field Value](#update-a-field-value)
      - [Notes](#notes-5)
  - [Delete a Field Value](#delete-a-field-value)
- [Field Value Changes](#field-value-changes)
  - [Supported field types](#supported-field-types)
    - [Multi-valued Fields](#multi-valued-fields)
    - [Single-valued fields](#single-valued-fields)
  - [The Field Value Change Resource](#the-field-value-change-resource)
    - [Field Value Change action types](#field-value-change-action-types)
  - [Get Field Values Changes](#get-field-values-changes)
      - [Notes](#notes-6)
- [Persons](#persons)
      - [Notes](#notes-7)
  - [The Person Resource](#the-person-resource)
    - [Person types](#person-types)
  - [Search for Persons](#search-for-persons)
  - [Get a Specific Person](#get-a-specific-person)
  - [Create a New Person](#create-a-new-person)
      - [Notes](#notes-8)
  - [Update a person](#update-a-person)
  - [Delete a Person](#delete-a-person)
  - [Get Global Person Fields](#get-global-person-fields)
- [Organizations](#organizations)
      - [Notes](#notes-9)
  - [The Organization Resource](#the-organization-resource)
  - [Search for Organizations](#search-for-organizations)
  - [Get a Specific Organization](#get-a-specific-organization)
  - [Create a New Organization](#create-a-new-organization)
      - [Notes](#notes-10)
  - [Update an Organization](#update-an-organization)
      - [Notes](#notes-11)
  - [Delete an Organization](#delete-an-organization)
      - [Notes](#notes-12)
  - [Get Global Organizations Fields](#get-global-organizations-fields)
- [Opportunities](#opportunities)
      - [Notes](#notes-13)
  - [The Opportunity Resource](#the-opportunity-resource)
  - [Search for Opportunities](#search-for-opportunities)
  - [Get a Specific Opportunity](#get-a-specific-opportunity)
  - [Create a New Opportunity](#create-a-new-opportunity)
  - [Update an Opportunity](#update-an-opportunity)
      - [Notes](#notes-14)
  - [Delete an Opportunity](#delete-an-opportunity)
- [Interactions](#interactions)
  - [The Interactions Resource](#the-interactions-resource)
    - [Interactions Types](#interactions-types)
    - [Direction Types](#direction-types)
    - [Logging Types](#logging-types)
  - [Get All Interactions](#get-all-interactions)
      - [Notes](#notes-15)
  - [Get a Specific Interaction](#get-a-specific-interaction)
  - [Create a New Interaction](#create-a-new-interaction)
  - [Update an Interaction](#update-an-interaction)
  - [Delete an Interaction](#delete-an-interaction)
- [Relationship Strengths](#relationship-strengths)
  - [The Relationship Strength Resource](#the-relationship-strength-resource)
  - [Get Relationship Strength](#get-relationship-strength)
- [Notes](#notes-16)
  - [The Note Resource](#the-note-resource)
    - [Formatting `content` as HTML](#formatting-content-as-html)
  - [Get All Notes](#get-all-notes)
  - [Get a Specific Note](#get-a-specific-note)
  - [Create a New Note](#create-a-new-note)
  - [Update a Note](#update-a-note)
  - [Delete a Note](#delete-a-note)
- [Entity Files](#entity-files)
  - [The Entity File Resource](#the-entity-file-resource)
  - [Get All Files](#get-all-files)
  - [Get a Specific File](#get-a-specific-file)
  - [Download File](#download-file)
      - [Notes](#notes-17)
  - [Upload Files](#upload-files)
      - [Notes](#notes-18)
- [Reminders](#reminders)
  - [The Reminder Resource](#the-reminder-resource)
    - [Reminder Types](#reminder-types)
    - [Reminder Reset Types](#reminder-reset-types)
    - [Reminder Status Types](#reminder-status-types)
  - [Get All Reminders](#get-all-reminders)
  - [Get a Specific Reminder](#get-a-specific-reminder)
  - [Create a New Reminder](#create-a-new-reminder)
  - [Update a Reminder](#update-a-reminder)
  - [Delete a Reminder](#delete-a-reminder)
- [Webhooks](#webhooks)
  - [The Webhook Subscription Resource](#the-webhook-subscription-resource)
  - [Supported Webhook Events](#supported-webhook-events)
  - [Get All Webhook Subscriptions](#get-all-webhook-subscriptions)
  - [Get a Specific Webhook Subscription](#get-a-specific-webhook-subscription)
  - [Create a New Webhook Subscription](#create-a-new-webhook-subscription)
  - [Update a Webhook Subscription](#update-a-webhook-subscription)
  - [Delete a Specific Webhook Subscription](#delete-a-specific-webhook-subscription)
- [Whoami](#whoami)
  - [The Whoami Resource](#the-whoami-resource)
  - [Get Whoami](#get-whoami)
- [Rate Limit](#rate-limit)
  - [The Rate Limit Resource](#the-rate-limit-resource)
  - [Get Rate Limit Information](#get-rate-limit-information)
- [Changelog](#changelog)
# Introduction

Welcome to the Affinity API! This API provides a RESTful interface for performing operations on the different objects that make up Affinity. If you are trying to accomplish an action through this API and are not sure on what endpoints to use, or if you have ideas on more endpoints we could create to make your workflow easier, please do not hesitate to contact us at [support@affinity.co](mailto:support@affinity.co).

# Getting Started

## Authentication

> Authentication using HTTP Basic Auth.

```bash
curl "https://api.affinity.co/api_endpoint" -u :$APIKEY
```

> Authentication using HTTP Bearer Auth.

```bash
curl "https://api.affinity.co/api_endpoint" -H "Authorization: Bearer ${APIKEY}"
```

To use the API, you will need to generate an API secret key. This can be done easily through the Settings Panel that is accessible through the left sidebar on the Affinity web app. For more support, visit the [How to obtain your API Key](https://support.affinity.co/hc/en-us/articles/360032633992-How-to-obtain-your-API-Key) article in our Help Center.

Requests are authenticated using one of the following:

| Authentication Type | Details |
| --- | --- |
| [HTTP Basic Auth](http://en.wikipedia.org/wiki/Basic_access_authentication) | Provide your API key as the basic auth password. You do not need to provide a username. |
| [HTTP Bearer Auth](https://swagger.io/docs/specification/v3_0/authentication/bearer-authentication/) | Provide your API key as the bearer token. |

Currently, we support one key per user on your team. Once you have generated a key, you will need to pass in the key with every API request for us to process it successfully. Otherwise, an error with a code of `401` will be returned.

#### Note

> Changes made through the API will be attributed to the person the API key is assigned to.

## Requests & Responses

This is a full-featured RESTful API. We provide reading & writing functionality for each object type in Affinity. All requests use the base URL of `https://api.affinity.co/`.

Responses to each request are provided as a JSON object. The response is either the data requested, or a valid error message and error code as outlined below.

Here is a list of all the error codes the Affinity API returns in case something does not go as expected:

| Error Code | Meaning |
| --- | --- |
| 401 | Unauthorized -- Your API key is invalid. |
| 403 | Forbidden -- Insufficient rights to a resource. |
| 404 | Not Found -- Requested resource does not exist. |
| 422 | Unprocessable Entity -- Malformed parameters supplied. This can also happen in cases the parameters supplied logically cannot complete the request. In this case, an appropriate error message is delivered. |
| 429 | Too Many Requests -- You have exceed the rate limit. |
| 500 | Internal Server Error -- We had a problem with our server. Try again later. |
| 503 | Service Unavailable -- This shouldn't generally happen. Either a deploy is in process, or Affinity services are down. |

#### Note

> Requests must be sent over HTTPS. Requests sent over HTTP will not return any data in order to ensure your sensitive information remains secure.

# Rate Limits

## API Rate Limits

The Affinity API sets a limit on the number of calls that a user can make per minute, and that all the users on an account can make per month. It also sets a reasonable limit on the number of concurrent requests it will support from an account at one time.

Requests to both Affinity API versions will count toward the one pool of requests allowed for a user or account. Once a per-minute, monthly, or concurrent rate limit is hit, subsequent requests will return an error code of 429. We highly recommend designing your application to handle 429 errors.

### Monthly Limits (Account-Level)

Your account plan tier will limit the overall number of requests you can make per month. Current rate limits by plan tier are:

| Plan Tier | Calls per month |
| --- | --- |
| Essentials | None |
| Scale | 100,000 |
| Advanced | 100,000 |
| Enterprise | Unlimited* |
| Professional (Legacy) | None* |
| Premium (Legacy) | 100,000 |
| Enterprise (Legacy) | Unlimited* |

#### Note

> Per-minute and concurrent request limits still apply to Enterprise-tier customers.

#### Note

> Professional tier customers who signed up for Affinity before July 5, 2023 are alotted 40,000 calls per month.

This monthly account-level limit resets at the end of each calendar month.

### Per Minute Limits (User-Level)

All API requests will be halted at 900 per user, per minute. We may also lower this limit on a temporary basis to manage API availability.

#### Note

> Once a rate limit is hit, all further requests will return an error code of 429.

### Concurrent Request Limits (Account-Level)

To protect our systems and manage availability across customers, we set a reasonable limit on concurrent requests at the account level. Customers should not expect to hit this limit unless they are hitting the API with heavy operations from many concurrent threads at once.

## Webhook Subscription Limit

There is a limit of three webhook subscriptions per Affinity instance.

## Rate Limit Headers

Each external API call will include headers with information about monthly and per-minute limits. This is a convenient way to retrieve your rate limits and usage without needing to hit the [`/rate-limit`](#rate-limit) endpoint. Every API call will respond with the following headers:

| Header | Description |
| --- | --- |
| X-Ratelimit-Limit-User | Number of requests allowed per minute for the user |
| X-Ratelimit-Limit-User-Remaining | Number of requests remaining for the user |
| X-Ratelimit-Limit-User-Reset | Time in seconds before the limit resets for the user |
| X-Ratelimit-Limit-Org | Number of requests allowed per month for the organization |
| X-Ratelimit-Limit-Org-Remaining | Number of requests remaining for the organization |
| X-Ratelimit-Limit-Org-Reset | Time in seconds before the limit resets for the organization |

# Data Model

## Overview

The three top-level objects in Affinity are Persons, Organizations, and Opportunities, and everything in the product is centered around these three resources. We refer to a data model that is a person, organization, or opportunity as an Entity.

The data stored in Affinity can be easily understood as a spreadsheet, with many rows, columns and cells. For each part of a spreadsheet, there are directly equivalent data models in Affinity.

The List view in Affinity represents the spreadsheet itself. A List is a collection of many rows, and the Affinity equivalent of a row is a List Entry. Each column in a spreadsheet is represented by a "Field". There are three types of Fields in Affinity: **Global Fields**, **List-specific Fields** and Smart Fields.

The data in each cell is represented by a "Field Value". There are both regular Field Values and Smart Field Values.

![](https://api-docs.affinity.co/images/crm-field-mappings-47b2c3ba.png)

**Legend:**

- ![List Entry](https://img.shields.io/badge/List%20Entry-orange) (orange)
- ![Global Field](https://img.shields.io/badge/Global%20Field-blue) (blue)
- ![List-specific Field](https://img.shields.io/badge/List--specific%20Field-red) (red)
- ![Field Value](https://img.shields.io/badge/Field%20Value-purple) (purple)
- ![Smart Field Value](https://img.shields.io/badge/Smart%20Field%20Value-green) (green)

#### Note

> When working with Affinity's API, it is important to understand the differences between how data is organized in the CRM versus the API.
> Although Smart Fields show up as a column in the List, they do not exist in the API in the same way **Global Fields** and **List-specific Fields** ones do.
> To retrieve Smart Field Values, see the [Retrieving Field Values](#get-field-values) section.

## Default Fields

By default, Affinity creates some fields for you automatically. Below are the fields created by type:

### Global Fields

- Location
- Industry
- Job Titles
- LinkedIn URL
- Phone Number
- Connections
- Source of Introduction
- Lists
- Crunchbase Data
- Affinity Data
- Pitchbook Data

### Smart Fields

- First Email
- Last Email
- First Event (First Meeting)
- Next Event (Next Meeting)
- Last Event (Last Meeting)
- Last Interaction
- Date Added

### List-specific Fields

- Status
- Owners
- Amount

# Common Use Cases

Use the common use cases below to learn how Affinity API endpoints work.

#### Helpful Tips

> - To reduce API calls, create any initial backfills with the REST API then use [Webhooks](#webhooks) to keep data synced. You may want to schedule occasional syncs via the REST API to fixed any inconsistencies
> - Your instance may contain multiple fields with the same name (e.g. Last Funding Date). To confirm the field ID, manually make an edit to the field in question and inspect the request payload for the bulk request. The field ID will be listed as `entityAttributeId` ![](https://api-docs.affinity.co/images/request-payload-1136ff0a.png)
> - The ID for a list, person, organization and opportunity can be found via the URL in the CRM. For a list `affinity.affinity.co/lists/[list_id]` and for a company profile `affinity.affinity.co/companies/[company_id]`
> - For large lists, use `page_size` and `page_token` parameters in the [`GET /lists/list_id}/list-entries`](#get-all-list-entries) endpoint to improve performance

## Getting Field Values for All List Entries on a List

1. Query [`GET /lists`](#get-all-lists) to get all lists and filter results by list name to get the appropriate list ID

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

2. Query [`GET /lists/12058/list-entries`](#get-all-list-entries) to get all list entries. Store the `entity_id` associated with each list entry ID

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

3. For each list entry, query [`GET /field-values`](#get-field-values) with the `entity_id` from the previous step. Make sure you are passing `entity_id` through the appropriate parameter (e.g person_id)

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

1. Query
  [`GET /fields`](#get-fields)
  to get all fields. If the given set of fields are all list-specific, it is helpful to pass along the
  `list_id`
  parameter to prefilter the results
2. Filter results of
  [`GET /fields`](#get-fields)
  by field name to get the appropriate field ID
3. Cross-reference the
  `field_id`
  from Step 3 with the field ID

```
GET /fields Response:
[
  {
    "id": 61223,
    "name": "Amount",
    "list_id": 12058,
    "value_type": 3,
    "allows_multiple": false,
    "track_changes": true,
  }
  ...
]
```

## Getting Field Value Changes for Status Fields

1. Query [`GET /lists`](#get-all-lists) and filter results to get the appropriate list ID

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

1. Query
  [`GET /fields`](#get-fields)
  to get all fields. If the given set of fields are all list-specific, it is helpful to pass along the list_id parameter to prefilter the results
2. Filter results of
  [`GET /fields`](#get-fields)
  by field name and cross-reference the
  `list_id`
  with the appropriate list ID from Step 1 to confirm you have the appropriate status field

```
GET /fields Response:
[
  {
    "id": 61223,
    "name": "Amount",
    "list_id": 12058,
    "value_type": 3,
    "allows_multiple": false,
    "track_changes": true,
  },
  ...
]
```

3. Query [`GET /field-values-changes`](#field-value-changes) passing in the `id` from Step 2

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

4. Filter results of [`GET /field-values-changes`](#field-value-changes) (e.g.: If you only want status field changes for a specific organization in your list, search by the `list_entry_id`).

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

1. Query [`GET /lists`](#get-all-lists) to get all lists and filter results to get the appropriate list ID

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

2. Query [`GET /lists/12058/list-entries`](#get-all-list-entries) to get all list entries. Store the `entity_id` associated with each list entry ID

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

3. For each list entry, query [`GET /organizations/{organization_id}`](#get-a-specific-organization) to get all list people associated with the organization. Store the `person_ids` associated with each organization

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

4. For each person ID from Step 3, query [`GET /relationships-strengths`](#get-relationship-strength) passing in the person ID. Once all person IDs have been looped through, filter for the highest `strength`

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

- [Postman Collection](/postman/collection.json)
  (Right-click and save as JSON then import into
  [Postman](https://www.postman.com/)
  )
- [Affinity Zapier Integrations](https://zapier.com/apps/affinity/integrations)
- [Affinity Tray Connectors](https://tray.io/documentation/connectors/service/affinity)

# Partner With Us

If you're a developer interested in building an integration with Affinity's relationship intelligence platform for your customers, please [get in touch here](https://53mt2d9of77.typeform.com/to/LhEs2tzU).

# Lists

Lists are the primary data structure that you can interact with in Affinity. Each list manages a collection of either people, organizations or opportunities. We call people, organizations and opportunities "entities".

A list in Affinity is easily represented as a spreadsheet. The rows of the spreadsheet are the list entries, and each list entry corresponds to a single person in a list of people, an organization in a list of organizations or an opportunity in a list of opportunities.

Lists in Affinity can also have any number of custom attributes. These attributes allow you to fully customize your workflow and model the data for your use case. We call these attributes "fields", and each fields represents a column in the spreadsheet representation.

As a simple example: A list called "Important People" might have 25 people in it. Two of the columns in the sheet could be "Title" and "Industry".

This list would have 25 "list entries". Each list entry would be associated with a single person entity. Furthermore, the list would have two "fields" with the names "Title" and "Industry".

## The List Resource

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the list object. |
| type | integer | The type of the entities (people, organizations, or opportunities) contained within the list. Each list only supports one entity type. |
| name | string | The title of the list that is displayed in Affinity. |
| public | boolean | When true, the list is publicly accessible to all users in your Affinity account. When false, the list is private to the list's owner and (explicitly set) additional users. |
| owner_id | integer | The unique ID of the internal person who owns the list. See [here](https://support.affinity.co/hc/en-us/articles/360029432951-List-Level-Permissions) for permissions held by a list's owner. |
| creator_id | integer | The unique ID of the internal person who created the list. If the list was created via API, this is the internal person corresponding to the API key that was used. |
| list_size | integer | The number of list entries contained within the list. |
| additional_permissions | object[] | The list of additional internal persons with permissions on the list. Should be a list of objects with `internal_person_id` and `role_id`, where `role_id` comes from the [list-level roles](#list-level-roles) table below. See sample response to the right for expected shape. |

### List Types

| List Type | Value | Description |
| --- | --- | --- |
| person | 0 | Type specifying a list of people. |
| organization | 1 | Type specifying a list of organizations. |
| opportunity | 8 | Type specifying a list of opportunities. |

### List-level Roles

| Role IDs | Description |
| --- | --- |
| 0 | List-level "Admin" role |
| 1 | List-level "Basic" role |
| 2 | List-level "Standard" role |

See [here](https://support.affinity.co/hc/en-us/articles/360029432951-List-Level-Permissions) for details on the permissions held by these roles.

#### Example Response

```json
{
  "id": 450,
  "type": 0,
  "name": "My List of People",
  "public": true,
  "owner_id": 38706,
  "creator_id": 38901,
  "list_size": 67,
  "additional_permissions": [
    {
      "internal_person_id": 38706,
      "role_id": 0
    }
  ]
}
```
## Get All Lists

#### Example Request

```bash
# Returns an array of all lists that you have access to.
curl "https://api.affinity.co/lists" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 450,
    "type": 0,
    "name": "My List of People",
    "public": true,
    "owner_id": 38706,
    "list_size": 67
  },
  {
    "id": 383,
    "type": 1,
    "name": "My List of Organizations",
    "public": true,
    "owner_id": 38706,
    "list_size": 50
  },
  ...
]
```

`GET /lists`

Returns a collection of all the lists visible to you.

### Parameters

None

#### Returns

An array of all the list resources for lists visible to you. Each list resource in the array includes the `id`, `name`, and `type` (refer to the [list resource](#the-list-resource) above for further help).

## Get a Specific List

#### Example Request

```bash
# Returns the list with the specified `list_id`
curl "https://api.affinity.co/lists/450" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 450,
  "type": 0,
  "name": "My List of People",
  "public": true,
  "owner_id": 38706,
  "list_size": 67
  "fields": [
    {
      "id": 1625,
      "name": "Status",
      "value_type": 7,
      "allows_multiple": false,
      "dropdown_options": [
        {
          "id": 886,
          "text": "Interested",
          "rank": 1,
          "color": 0
        }
      ]
    },
    {
      "id": 1626,
      "name": "Owners",
      "value_type": 0,
      "allows_multiple": true,
      "dropdown_options": [],
    },
    ...
  ]
}
```

`GET /lists/{list_id}`

Gets the details for a specific list given the existing list id.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| list_id | integer | true | The unique ID of the list object to be retrieved. |

#### Returns

The details of the list resource corresponding to the list ID specified in the path parameter. These details include an array of the fields that are specific to this list. An appropriate error is returned if an invalid list is supplied.

## Create a New List

`POST /lists`

Creates a new list with the supplied parameters.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | true | The title of the list that is displayed in Affinity. |
| type | integer | true | The type of the entities (people, organizations, or opportunities) contained within the list. Each list only supports one entity type. |
| is_public | boolean | true | Set to true to make the list publicly accessible to all users in your Affinity account. Set to false to make the list private to the list's owner and additional users. |
| owner_id | integer | false | The unique ID of the internal person who should own the list. Defaults to the owner of the API key being used. See [here](https://support.affinity.co/hc/en-us/articles/360029432951-List-Level-Permissions) for permissions held by a list's owner. |
| additional_permissions | object[] | false | A list of additional internal persons and the permissions they should have on the list. Should be a list of objects with `internal_person_id` and `role_id`, where `role_id` comes from the [list-level roles](#list-level-roles) table above. See sample request to the right for expected shape. |

#### Returns

The list resource that was just created through this request.

#### Example Request

```bash
curl -X POST "https://api.affinity.co/lists" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{ "name": "My List of Organizations", "type": 1, "is_public": true, "owner_id": 38706, "additional_permissions": [ {"internal_person_id": 38701, "role_id": 0}, {"internal_person_id": 38703, "role_id": 1}, {"internal_person_id": 38900, "role_id": 0} ]}'
```

#### Example Response

```json
{
  "id": 383,
  "type": 1,
  "name": "My List of Organizations",
  "public": true,
  "owner_id": 38706,
  "creator_id": 38701,
  "list_size": 0,
  "additional_permissions": [
    {
      "internal_person_id": 38701,
      "role_id": 0
    },
    {
      "internal_person_id": 38703,
      "role_id": 1
    },
    {
      "internal_person_id": 38900,
      "role_id": 0
    }
  ]
}
```
# List Entries

## The List Entry Resource

Each list comprises a number of entries. Each list entry has a creator, a list that it belongs to, and the underlying entity it represents depending on the type of the list (people, organizations or opportunities).

Operations like adding and removing entities from a list can be accomplished using the list entry abstraction.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the list entry object. |
| list_id | integer | The unique identifier of the list on which the list entry resides. |
| creator_id | integer | The unique identifier of the user who created the list entry. If you create a list entry through the API, the user corresponding to the API token will be the creator by default. |
| entity_id | integer | The unique identifier of the entity corresponding to the list entry. |
| entity | object | Object containing entity-specific details like name, email address, domain etc. for the entity corresponding to `entity_id`. |
| created_at | datetime | The time when the list entry was created. |

#### Note

> Although list entries correspond to rows in an Affinity spreadsheet, the values associated with the entity are not stored inside the list entry resource. If you are trying to update, create, or delete a value in one of the custom columns for this list entry, please refer to the [Field Values](#field-values) section. The list entry API is only used for getting, adding, or removing entities from a list. It does not handle updating individual cells in columns.

#### Example Response

```json
{
  "id": 16367,
  "list_id": 450,
  "creator_id": 38706,
  "entity_id": 287125,
  "entity": {
    "type": 1,
    "first_name": "John",
    "last_name": "Doe",
    "primary_email": "jdoe@jdoe.com",
    "emails": ["jdoe@jdoe.com", "jdoe2@jdoe2.com"]
  },
  "created_at": "2017-01-16T16:34:03.539-08:00"
}
```
## Get All List Entries

> Example Response with Pagination

```json
{
  "list_entries": [
    {
      "id": 64608,
      "list_id": 450,
      "creator_id": 287843,
      "entity_id": 62034,
      "created_at": "2017-05-04T10:44:31.526-08:00",
      "entity": {
        "type": 0,
        "first_name": "Affinity",
        "last_name": "Team",
        "primary_email": "team@affinity.co",
        "emails": [
          "team@affinity.co"
        ],
      },
    },
    {
      "id": 53510,
      "list_id": 450,
      "creator_id": 38596,
      "entity_id": 241576,
      "created_at": "2017-02-22T15:22:21.125-08:00",
      "entity": {
        "type": 0,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "jdoe@stanford.edu",
        "emails": [
          "jdoe@stanford.edu"
        ],
      },
    },
    ...
  ],
  "next_page_token": "eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9"
}
```

`GET /lists/{list_id}/list-entries`

If no page size is specified, fetches all the list entries in the list with the supplied list id. If a page size is specified, fetches up to that number of list entries in the list with the supplied list id.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| list_id | integer | true | The unique ID of the list whose list entries are to be retrieved. |

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| page_size | integer | false | How many results to return per page. (Default is to return all results.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Returns

If the `page_size` is not passed in as a parameter, an array of all the list entry resources corresponding to the provided list will be returned. If the `page_size` is passed in as a parameter, an object with two fields: `list_entries` and `next_page_token` are returned. `list_entries` maps to an array of up to `page_size` list entries. `next_page_token` includes a token to be sent along with the next request as the `page_token` parameter to fetch the next page of results. Each list entry in the both cases includes all the attributes as specified in the [List Entry Resource](#the-list-entry-resource) section above.

#### Example Request

```bash
curl "https://api.affinity.co/lists/450/list-entries" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 64608,
    "list_id": 450,
    "creator_id": 287843,
    "entity_id": 62034,
    "created_at": "2017-05-04T10:44:31.525-08:00",
    "entity": {
      "type": 0,
      "first_name": "Affinity",
      "last_name": "Team",
      "primary_email": "team@affinity.co",
      "emails": [
        "team@affinity.co"
      ],
    },
  },
  {
    "id": 53510,
    "list_id": 450,
    "creator_id": 38596,
    "entity_id": 241576,
    "created_at": "2017-02-22T15:22:21.125-08:00",
    "entity": {
      "type": 0,
      "first_name": "John",
      "last_name": "Doe",
      "primary_email": "jdoe@stanford.edu",
      "emails": [
        "jdoe@stanford.edu"
      ],
    },
  },
  ...
]
```
## Get a Specific List Entry

`GET /lists/{list_id}/list-entries/{list_entry_id}`

Fetches a list entry with a specified id.

#### Example Request

```bash
curl "https://api.affinity.co/lists/450/list-entries/16367" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 16367,
  "list_id": 450,
  "creator_id": 38596,
  "entity_id": 241576,
  "created_at": "2017-02-22T15:22:21.125-08:00",
  "entity": {
    "type": 0,
    "first_name": "John",
    "last_name": "Doe",
    "primary_email": "jdoe@stanford.edu",
    "emails": ["jdoe@stanford.edu"]
  }
}
```

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| list_id | integer | true | The unique ID of the list that contains the specified `list_entry_id`. |
| list_entry_id | integer | true | The unique ID of the list entry object to be retrieved. |

#### Returns

The list entry object corresponding to the `list_entry_id`.

## Create a New List Entry

`POST /lists/{list_id}/list-entries`

Creates a new list entry in the list with the supplied list id.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| list_id | integer | true | The unique ID of the list whose list entries are to be retrieved. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| entity_id | integer | true | The unique ID of the person or organization to add to this list. Opportunities **cannot** be created using this endpoint. See note below. |
| creator_id | integer | false | The ID of a Person resource who should be recorded as adding the entry to the list. Must be a person who can access Affinity. If not provided the creator defaults to the owner of the API key. |

#### Notes

> - Opportunities cannot be created using this endpoint. Instead use the [`POST /opportunities`](#create-a-new-opportunity) endpoint.
> - Person and company lists can contain the same entity multiple times. Depending on your use case, before you add an entry, you may want to verify whether or not it exists in the list already.

#### Returns

The list entry resource that was just created through this request.

#### Example Request

```bash
curl -X POST "https://api.affinity.co/lists/450/list-entries" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"entity_id": 38706}'
```

#### Example Response

```json
{
  "id": 53510,
  "list_id": 450,
  "creator_id": 38596,
  "entity_id": 38706,
  "created_at": "2017-02-22T15:22:21.125-08:00",
  "entity": {
    "type": 0,
    "first_name": "John",
    "last_name": "Doe",
    "primary_email": "jdoe@stanford.edu",
    "emails": ["jdoe@stanford.edu"]
  }
}
```
## Delete a Specific List Entry

`DELETE /lists/{list_id}/list-entries/{list_entry_id}`

Deletes a list entry with a specified `list_entry_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| list_id | integer | true | The unique ID of the list that contains the specified `list_entry_id`. |
| list_entry_id | integer | true | The unique ID of the list entry object to be deleted. |

#### Returns

The JSON object `{"success": true}`.

#### Notes

> - This will also delete all the field values, if any, associated with the list entry. Such field values will only exist in fields specific to this list.
> - If the list entry belongs to an Opportunity list, then the opportunity that the list entry is associated with will also be deleted.

#### Example Request

```bash
curl "https://api.affinity.co/lists/450/list-entries/56517" \
   -u :$APIKEY \
   -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Fields

As discussed in the previous section, fields as a data model represent the "columns" in a spreadsheet. A field can be specific to a given list, or it can be global. List-specific fields appear as a column whenever that list is being viewed while global fields are displayed on all lists.

Let us consider two examples:

1. Assume you have a list called "Top Referrers", and a new list-specific field (column) called "Number of Referrals" is added to this list. In this case, the "Number of Referrals" column will only be visible on the "Top Referrers" list.
2. Now assume you have three lists of people, "Top Referrers", "Friends in Media", "BD Leads", and a person X exists on all three lists. If you want to track where all the people in these 3 lists live, you might have a field called "Location". It makes sense to make this field global - in which case it will be shared across all three lists. Hence, if person X is a top referrer and lives in San Francisco, CA, that information will automatically appear on the "Friends in Media" list as well.

By default, Affinity provides all teams with a few default global fields: For people, the global fields include Location, Job Titles, and Industries. For organizations, the global fields include Stage, Industry, Location, and more.

#### Notes

> - Global field IDs for persons are returned from [`GET /persons/fields`](#get-global-person-fields)
> - Global field IDs for organizations are returned from [`GET /organizations/fields`](#get-global-organizations-fields)
> - List-specific field IDs are also returned from [`GET /lists/{list_id}`](#get-a-specific-list)

## The Field Resource

Each field object has a unique `id`. It also has a `name`, which determines the name of the field, and `allows_multiple`, which determines whether multiple values can be added to a single cell for that field.

Affinity is extremely flexible and customizable, and a lot of that power comes from our ability to support many different value types for fields. Numbers, dates, and locations are all examples of value types, and you can search, sort, or filter all of them.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the field object. |
| name | string | The name of the field. |
| list_id | integer | The unique identifier of the list that the field object belongs to if it is specific to a list. This is `null` if the field is global. |
| allows_multiple | boolean | This determines whether multiple values can be added to a single cell for the field. |
| dropdown_options | object[] | Affinity supports pre-entered dropdown options for fields of the "Ranked Dropdown" value_type. The array is empty unless there are valid dropdown options for the field of the "Ranked Dropdown" value type. |
| value_type | integer | This field describes what values can be associated with the field. This can be one of many values, as described in the table below. |
| enrichment_source | string | The data source for the enriched field. Will appear as none for custom fields and certain list-specific fields (e.g. Status). Fields auto-created for certain integrations will also be called out here (e.g. Mailchimp). |

### Field Value Types

All the Types listed below can be referred through looking at the Affinity web app as well.

| Value | Type | Description |
| --- | --- | --- |
| 0 | Person | This type enables you to add person objects as a value. Eg: External Source, Owner, Friends |
| 1 | Organization | This type enables you to add organization objects as a value. Eg: Place of work, Co-Investors |
| 2 | Dropdown | This type allows you to add text values into a single cell. This is best used when you want to store information that is unique to a person or organization. Eg: Interests, Stage, Industry |
| 3 | Number | This type enables you to add number as a value. Eg: Deal Size, Check Size, Revenue |
| 4 | Date | This type enables you to add date as a value. Eg: Date of Event, Birthday |
| 5 | Location | This type enables you to add a smart Google Maps location as a value. Eg: Address |
| 6 | Text | This type enables you to add a long text block as a value. Eg: Summary |
| 7 | Ranked Dropdown | This type allows you to add values in a particular order as well as assign colors to them. This is the equivalent of a pick list. Eg: Status, Priority, Ranking |

#### Note

> The API currently does not support updating and modifying fields. This must be done through the web product.

#### Example Response

```json
{
  "id": 1234,
  "name": "Deal Status",
  "list_id": 11,
  "enrichment_source": "none",
  "value_type": 7,
  "allows_multiple": false,
  "track_changes": true,
  "dropdown_options": [
    {
      "id": 2863451,
      "text": "New",
      "rank": 0,
      "color": 3
    },
    {
      "id": 2863452,
      "text": "In Progress",
      "rank": 1,
      "color": 3
    },
    {
      "id": 2863453,
      "text": "Won",
      "rank": 2,
      "color": 2
    }
  ]
}
```
## Get Fields

`GET /fields`

Returns all fields based on the parameters provided.

Pass the `list_id` to only fetch fields that are specific to that list. Otherwise, all global and list-specific fields will be returned.

Pass the `value_type` to fetch fields of specific value types. Otherwise, all fields of any type will be returned.

Pass the `entity_type` to fetch fields of specific entity types. Otherwise, any fields of any entity type will be returned.

Pass the `with_modified_names` flag to return the fields such that the names have the list name prepended to them in the format `[List Name] Field Name` (i.e. `[Deals] Status`).

Pass the `exclude_dropdown_options` flag to exclude dropdown options from the response. This may be useful when the payload is too large due to too many dropdown options.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| list_id | integer | false | An unique identifier of the list whose fields are to be retrieved. |
| value_type | integer | false | The value type of the fields that are to be retrieved. |
| entity_type | integer | false | The entity type of the fields that are to be retrieved. |
| with_modified_names | boolean | false | When true, field names will return in the format `[List Name] Field Name`. |
| exclude_dropdown_options | boolean | false | When true, dropdown options will not be returned in the response. |

#### Returns

An array of all the fields requested.

#### Note

> - Results returned with `list_id: null` mean they do not belong to a specific list and thus are global fields.
> - Field endpoint does not return any Crunchbase fields.

#### Example Request

```bash
curl "https://api.affinity.co/fields?with_modified_names=true" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 1234,
    "name": "[Deals] Amount",
    "list_id": 11,
    "enrichment_source": "none",
    "value_type": 3,
    "allows_multiple": false,
    "track_changes": true,
    "dropdown_options": []
  },
  {
    "id": 5678,
    "name": "[Events] Amount",
    "list_id": 16,
    "enrichment_source": "none",
    "value_type": 3,
    "allows_multiple": false,
    "track_changes": true,
    "dropdown_options": []
  },
  {
    "id": 4321,
    "name": "[Companies] Description",
    "list_id": 18,
    "enrichment_source": "dealroom",
    "value_type": 6,
    "allows_multiple": false,
    "track_changes": false,
    "dropdown_options": []
  },
  ...
]
```
## Create Field

`POST /fields`

Creates a new field with the supplied parameters.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | true | The name of the field. |
| entity_type | integer | true | This describes what type of list this field will be associated with the field. This can be one of three values, see below for all value types. |
| value_type | integer | true | This describes what values can be associated with the field. This can be one of many values, see the [Field Resource](#the-field-resource) section for all value types. |
| list_id | integer | false | The unique identifier of the list that the field object belongs to if it is specific to a list. This is `null` if the field is global. |
| allows_multiple | boolean | false | This determines whether multiple values can be added to a single cell for the field. |
| is_list_specific | boolean | false | This determines whether the field object belongs to a specific list. If set to `true`, you must pass in the appropriate `list_id`. |
| is_required | boolean | false | This determines whether the field object is required. |

### Field Entity Types

| Parameter | Type | Description |
| --- | --- | --- |
| person | 0 | Type specifying a list of people. |
| organization | 1 | Type specifying a list of organizations. |
| opportunity | 8 | Type specifying a list of opportunities. |

#### Returns

The field resource that was just created through this request.

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
  "id": 59,
  "name": "[Deals] Amount",
  "list_id": 11,
  "enrichment_source": "none",
  "value_type": 3,
  "allows_multiple": false,
  "track_changes": false,
  "dropdown_options": []
}
```
## Delete a Field

`DELETE /fields/{id}`

Deletes an field with the specified `id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | integer | true | The unique ID of the field that needs to be deleted. |

#### Returns

`{success: true}`.

#### Example Request

```bash
curl "https://api.affinity.co/fields/1234" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Field Values

Field values are displayed in Affinity as the data in the cells of an Affinity spreadsheet.

As an example for how a field value is created:

1. Assume there exists a list of people called "Business Development Leads".
2. A custom field called "Deal Size" is created on this list. Fields are visually displayed as columns.
3. A person X is added to this list. This action creates a list entry for this person.
4. A value, 50,000, is entered in the cell corresponding to person X in the Deal Size column.
5. 50,000 is now a field value tied to the list entry corresponding to person X, and the "Deal Size" field.

#### Notes

> - By default, Affinity creates some fields for you automatically. These include Location, Industry, Job Titles, and more. See the [Default Fields](#default-fields) section for more information.
> - Opportunities cannot have global field values

## The Field Value Resource

> Example Response (Global Location Field Value)

```json
{
  "id": 250616,
  "field_id": 337,
  "list_entry_id": null,
  "entity_id": 38706,
  "created_at": "2022-10-04T08:54:24.694-04:00",
  "updated_at": null,
  "value": {
    "city": "San Francisco",
    "state": "California",
    "country": "United States",
    "continent": null,
    "street_address": null
  }
}
```

> Example Response (List Specific Dropdown Field Value)

```json
{
  "id": 177634,
  "field_id": 751,
  "list_entry_id": 605,
  "entity_id": 38706,
  "created_at": "2021-10-04T08:54:24.694-04:00",
  "updated_at": "2022-03-04T08:54:24.694-04:00",
  "value": {
    "id": 71,
    "text": "Low",
    "rank": 1,
    "color": 4
  }
}
```

Each field value object has a unique `id`.

A field value also has `field_id`, `entity_id`, and `list_entry_id` attributes that give it the appropriate associations, as noted in the example above.

Use the `created_at` and `updated_at` timestamps on field values to determine when the value(s) for a given field have last been added or changed. Please note that what might amount to an "update" in-product (e.g. for dropdown fields) might result in a newly created field value rather than an updated old one in the API.

A field value can take on many different kinds of values, depending on the `field` value type (see [Fields](#fields) section).

#### Note

> When retrieving Field Values from a specific cell in your Affinity list, it may be helpful to think about it as an XY coordinate system. The X coordinate is the List Entry or Entity and the Y coordinate is the Field ID. You will need to have both to find the appropriate Field Value ID.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the field value object. |
| field_id | integer | The unique identifier of the field the value is associated with. |
| entity_id | integer | The unique identifier of the person, organization, or opportunity object the field value is associated with. |
| list_entry_id | integer | The unique identifier of the list entry object the field value is associated with. This only exists if the field the value is associated with is list-specific. |
| value | One of many | The value attribute can take on many different types, depending on the field `value_type`. See below for reference. |
| created_at | datetime | The string representing the time when the field value was created. |
| updated_at | datetime | The string representing the last time the field value was updated. |

### Field Value Value Types

The Field Type specified below corresponds to the `value_type` of a field.

| Value Type | Type | Description |
| --- | --- | --- |
| dropdown | string | This represents a value in a dropdown field. |
| number | integer | This represents a value in a number field. |
| person | integer | This represents a value in a person field. |
| organization | integer | This represents a value in an organization field. |
| location | object | This represents a value in a location field - it's an object comprising the following keys: `street_address`, `city`, `state`, `country`, all of which take string values. |
| date | datetime | This represents a value in a date field. |
| text | string | This represents a value in a text field. |

## Get Field Values

`GET /field-values`

Returns all field values attached to a `person`, `organization`, `opportunity`, or `list_entry`.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| person_id | integer | custom* | A unique ID that represents a person object whose field values are to be retrieved. |
| organization_id | integer | custom* | A unique ID that represents an organization object whose field values are to be retrieved. |
| opportunity_id | integer | custom* | A unique ID that represents an opportunity object whose field values are to be retrieved. |
| list_entry_id | integer | custom* | A unique ID that represents a list entry object whose field values are to be retrieved. |

#### Returns

An array of all the field values associated with the supplied `person`, `organization`, `opportunity`, or `list_entry`.

#### Notes

> - Exactly one of `person_id`, `organization_id`, `opportunity_id`, or `list_entry_id` must be specified to the endpoint.
> - If a `person_id`, `organization_id`, or `opportunity_id` is specified, the endpoint returns all field values tied to these entities - including those that are associated with all list entries that exist for the given person or organization. Opportunities can only have one list entry.
> - Smart fields cannot be retrieved using the field values endpoint. Smart field values can be retrieved using the `with_interaction_dates` parameter on the [`GET /persons/{person_id}`](#get-a-specific-person) or [`GET /organizations/{organization_id}`](#get-a-specific-organization) endpoints. The people associated with smart fields can be retrieved using the `with_interaction_persons` on the [`GET /persons/{person_id}`](#get-a-specific-person) or [`GET /organizations/{organization_id}`](#get-a-specific-organization) endpoints.
> - Field values endpoint does return Crunchbase fields, but with `null` values.

#### Example Request

```bash
curl "https://api.affinity.co/field-values?person_id=38706" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 250616,
    "field_id": 337,
    "list_entry_id": null,
    "entity_id": 38706,
    "created_at": "2021-10-04T08:54:24.694-04:00",
    "updated_at": "2022-03-04T08:54:24.694-04:00",
    "value": {
      "city": "San Francisco",
      "state": "California",
      "country": "United States",
      "continent": null,
      "street_address": null
    }
  },
  {
    "id": 2634897436,
    "field_id": 768101,
    "list_entry_id": null,
    "entity_type": 0,
    "value_type": 2,
    "entity_id": 65680071,
    "created_at": "2022-10-04T08:54:24.694-04:00",
    "updated_at": null,
    "value": "Software Engineer"
  },
  {
    "id": 32760,
    "field_id": 198,
    "list_entry_id": null,
    "entity_id": 38706,
    "created_at": "2022-09-04T08:54:24.694-04:00",
    "updated_at": null,
    "value": 38659
  },
  ...
]
```
## Create a New Field Value

`POST /field-values`

Creates a new field value with the supplied parameters.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| field_id | integer | true | The unique identifier of the field (column) that the field value is associated with. |
| entity_id | integer | true | The unique identifier of the entity (person, organization, or opportunity) that the field value is associated with. |
| value | custom | true | See the [Field Value Resource](#the-field-value-resource) section for all value types. The value specified must correspond to the `value_type` of the supplied `field`. For ranked dropdown fields like the default Status field, you must supply the ID of a dropdown option rather than a string value. These IDs can be found using the `GET /fields` endpoint. |
| list_entry_id | integer | false | The unique identifier of the list entry (list row) that the field value is associated with. Only specify the `list_entry_id` if the field that the field value is associated with is list specific. |

#### Returns

The field value resource that was just created through this request.

#### Example Request

```bash
curl -X POST "https://api.affinity.co/field-values" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"field_id": 1284, "value": "Architecture", "entity_id": 38706}'
```

#### Example Response

```json
{
  "id": 20406836,
  "field_id": 1284,
  "list_entry_id": null,
  "entity_id": 38706,
  "created_at": "2022-10-04T10:37:19.418-04:00",
  "updated_at": null,
  "value": "Architecture"
}
```
## Update a Field Value

`PUT /field-values/{field_value_id}`

Updates the existing field value with `field_value_id` with the supplied parameters.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| field_value_id | integer | true | The unique ID of the field value that needs to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| value | custom | true | See the [Field Value Resource](#the-field-value-resource) section for all value types. The value specified must correspond to the `value_type` of the supplied `field`. For ranked dropdown fields like the default Status field, you must supply the ID of a dropdown option rather than a string value. These IDs can be found using the `GET /fields` endpoint. |

#### Returns

The field value object that was just updated through this request.

#### Notes

> When updating a specific field value make sure to use the field_value_id and not the `field_id`.

#### Example Request

```bash
curl -X PUT "https://api.affinity.co/field-values/20406836" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"value": "Healthcare"}'
```

#### Example Response

```json
{
  "id": 20406836,
  "field_id": 1284,
  "list_entry_id": null,
  "entity_id": 38706,
  "created_at": "2022-10-04T10:37:19.418-04:00",
  "updated_at": "2023-02-06T11:53:08.914-05:00",
  "value": "Healthcare"
}
```
## Delete a Field Value

`DELETE /field-values/{field_value_id}`

Deletes an field value with the specified `field_value_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| field_value_id | integer | true | The unique ID of the field value that needs to be deleted. |

#### Returns

`{success: true}`.

#### Example Request

```bash
curl "https://api.affinity.co/field-values/20406836" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Field Value Changes

Field value changes allow you to see historical changes to the values of fields in Affinity. This is especially useful for tracking progress through statuses (e.g. Lead --> Closed Won).

## Supported field types

Not all fields can track historical changes.

Fields that are automatically created and "enriched" by Affinity **do not** support change tracking.

Among fields that are not enriched, only the ones with the following data types support change tracking:

### Multi-valued Fields

| Value | Type |
| --- | --- |
| 0 | Person |
| 1 | Organization |
| 3 | Number |
| 5 | Location |

### Single-valued fields

| Value | Type |
| --- | --- |
| 0 | Person |
| 1 | Organization |
| 3 | Number |
| 4 | Date |
| 5 | Location |
| 7 | Ranked Dropdown |

#### Note

> You can also see if a field does so by looking at the `track_changes` attribute in the [Field Resource](#get-fields). The API will return an appropriate error if the field doesn't support historical tracking.

## The Field Value Change Resource

Each field value change object has a unique `id`.

A field value change also has `field_id`, `entity_id`, `list_entry_id` attributes that give it the appropriate associations, as noted in the example above.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the field value change object. |
| field_id | integer | The unique identifier of the field the value change is associated with. |
| entity_id | integer | The unique identifier of the person, organization, or opportunity object the field value change is associated with. |
| list_entry_id | integer | The unique identifier of the list entry object the field value change is associated with. |
| action_type | One of several | Describes the action behind this field value change. This attribute can take on several different types; see below for reference. |
| value | One of many | Represents the field's value. This attribute can take on many different types, depending on the field `value_type`. When the action type is Delete, value represents the old value; otherwise, it represents the new value. |

### Field Value Change action types

The action type specified below corresponds to the `action_type` of a field value change. This attribute filters the field value changes that are returned. For example, when an `action_type` of 0 is specified, all the field value change objects that are returned will represent when a field value has been created.

| Action Type | Type |
| --- | --- |
| 0 | Create |
| 1 | Delete |
| 2 | Update |

#### Note

> There are some extra attributes returned by this endpoint; they will be deprecated soon and should not be used.

#### Example Response

```json
{
  "id": 50822718,
  "field_id": 236333,
  "entity_id": 261131046,
  "list_entry_id": 15709964,
  "action_type": 0,
  "changer": {
    "id": 38706,
    "type": 0,
    "first_name": "Jane",
    "last_name": "Doe",
    "primary_email": "jane@gmail.com",
    "emails": ["jane@gmail.com"]
  },
  "changed_at": "2020-04-11T15:46:50.963-07:00",
  "value": {
    "id": 1607859,
    "text": "New",
    "rank": 1,
    "color": 0
  }
}
```
## Get Field Values Changes

`GET /field-value-changes`

Returns all field values changes attached to a specific field. Field value changes can be filtered by `action_type`, `person`, `organization`, `opportunity` or `list_entry` by passing in the appropriate parameter.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| field_id | integer | true | A unique ID that represents a field object whose field values changes are to be retrieved. |
| action_type | integer | false | An integer that filters field value changes that were created with this specific action type (see above). |
| person_id | integer | custom* | A unique ID that represents a person object whose field value changes are to be retrieved. |
| organization_id | integer | custom* | A unique ID that represents an organization object whose field value changes are to be retrieved. |
| opportunity_id | integer | custom* | A unique ID that represents an opportunity object whose field value changes are to be retrieved. |
| list_entry_id | integer | custom* | A unique ID that represents a list entry object whose field value changes are to be retrieved. |

#### Returns

An array of all the field values changes associated with the supplied field and `person`, `organization`, `opportunity` or `list_entry` if specified.

#### Notes

> - Exactly one of `person_id`, `organization_id`, `opportunity_id`, or `list_entry_id` must be specified to the endpoint.
> - If a `person_id`, `organization_id`, or `opportunity_id` is specified, the endpoint returns all field value changes tied to these entities.
> - If a `list_entry_id` is specified, the result is filtered by the `person_id`, `organization_id` or `opportunity_id` which is tied to the specified `list_entry_id`.

#### Example Request

```bash
curl "https://api.affinity.co/field-value-changes?field_id=236333" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 50822718,
    "field_id": 236333,
    "entity_id": 261131046,
    "list_entry_id": 15709964,
    "action_type": 0,
    "changer": {
      "id": 38706,
      "type": 0,
      "first_name": "Jane",
      "last_name": "Doe",
      "primary_email": "jane@gmail.com",
      "emails": ["jane@gmail.com"]
    },
    "changed_at": "2020-04-11T15:46:50.963-07:00",
    "value": {
      "id": 1607859,
      "text": "New",
      "rank": 1,
      "color": 0
    }
  }
]
```
# Persons

The persons API allows you to manage all the contacts of your organization. These people include anyone your team has ever been in email communications or meetings with, and all the people that your team has added to Affinity either manually or through the API. Affinity's data model also guarantees that only one person in your team's shared contact list has a given email address.

#### Notes

> - If you are looking to add or remove a person from a list, please check out the [List Entries](#list-entries) section of the API.
> - If you are looking to modify a person's field values (one of the cells on Affinity's spreadsheet), please check out the [Field Values](#field-values) section of the API.

## The Person Resource

Each person resource is assigned a unique `id` and stores the name, type, and email addresses of the person. A person resource also has access to a smart attribute called `primary_email`. The value of `primary_email` is automatically computed by Affinity's proprietary algorithms and refers to the email that is most likely to be the current active email address of a person.

The person resource `organization_ids` is a collection of unique identifiers to the person's associated organizations. Note that a person can be associated with multiple organizations. For example, say your team has talked with organizations A and B. Person X used to work at A and was your point of contact, but then changed jobs and started emailing you from a new email address (corresponding to organization B). In this case, Affinity will automatically associate person X with both organization A and organization B.

The person resource `type` indicates whether a person is internal or external to your team. Every internal person is a user of Affinity on your team, and all other people are externals.

Dates of the most recent and upcoming interactions with a person are available in the `interaction_dates` field. This data is only included when passing `with_interaction_dates=true` as a query parameter to the `/persons` or the `/persons/{person_id}` endpoints.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the person object. |
| type | integer | The type of person (see below). |
| first_name | string | The first name of the person. |
| last_name | string | The last name of the person. |
| emails | string[] | The email addresses of the person. |
| primary_email | string | The email (automatically computed) that is most likely to the current active email address of the person. |
| organization_ids | integer[] | An array of unique identifiers of organizations that the person is associated with. |
| opportunity_ids | integer[] | An array of unique identifiers of opportunities that the person is associated with. Only returned when `with_opportunities=true`. |
| current_organization_ids | integer[] | An array of unique identifiers of organizations that the person is currently associated with according to the Affinity Data: Current Organization in-app column. Only returned when `with_current_organizations=true`. |
|  |  |  |
| list_entries | ListEntry[] | An array of list entry resources associated with the person, only returned as part of the [Get a Specific Person](#get-a-specific-person) endpoint. |
| interaction_dates | object | An object with seven string date fields representing the most recent and upcoming interactions with this person: `first_email_date`, `last_email_date`, `last_event_date`, `last_chat_message_date`, `last_interacton_date`, `first_event_date` and `next_event_date`. Only returned when passing `with_interaction_dates=true`. |
| interactions | object | An object with seven fields nested underneath. Each field corresponds to one of the seven interactions, and includes nested fields for `date` and `person_ids` which indicates the internal people associated with that event. Only returned when passing `with_interaction_dates=true`. |

### Person types

| Type | Value | Description |
| --- | --- | --- |
| external | 0 | Default value. All people that your team has spoken with externally have this type. |
| internal | 1 | All people on your team that have Affinity accounts will have this type. |

#### Example Response

```json
{
  "id": 38706,
  "type": 0,
  "first_name": "John",
  "last_name": "Doe",
  "primary_email": "john@affinity.co",
  "emails": [
    "john@affinity.co",
    "jdoe@alumni.stanford.edu",
    "johnjdoe@gmail.com",
  ],
  "organization_ids": [
    1687449,
    ...
  ],
  "opportunity_ids": [
    4,
    11,
    ...
  ],
  "current_organization_ids": [1687449],
  "list_entries": [
    {
      "id": 388,
      "list_id": 26,
      "creator_id": 38603,
      "entity_id": 38706,
      "created_at": "2015-12-11T02:26:56.537-08:00",
    },
    ...
  ],
  "interaction_dates": {
    "first_email_date": "2011-11-23T08:12:45.328-08:00",
    "last_email_date": "2012-03-04T05:06:07.890-08:00",
    "last_event_date": "2011-12-11T02:26:56.537-08:00",
    "last_chat_message_date": "2011-11-01T02:26:56.537-08:00",
    "last_interaction_date": "2012-03-04T05:06:07.890-08:00",
    "next_event_date": "2019-03-04T05:06:07.890-08:00",
    "first_event_date": "2012-01-01T08:18:00.329-08:00",
  },
  "interactions": {
    "first_email": {
      "date": "2011-11-23T08:12:45.328-08:00",
      "person_ids": [
        123
      ]
    },
    "last_email": {
      "date": "2012-03-04T05:06:07.890-08:00",
      "person_ids": [
        123
      ]
    },
    "last_event": {
      "date": "2011-12-11T02:26:56.537-08:00",
      "person_ids": [
        123
      ]
    },
    "last_chat_message": {
      "date": "2011-11-01T02:26:56.537-08:00",
      "person_ids": [
        123
      ]
    },
    "last_interaction": {
      "date": "2012-03-04T05:06:07.890-08:00",
      "person_ids": [
        123,
        111
      ]
    },
    "next_event": {
      "date": "2019-03-04T05:06:07.890-08:00",
      "person_ids": [
        123,
        124,
        125
      ]
    },
    "first_event": {
      "date": "2012-01-01T08:18:00.329-08:00",
      "person_ids": [
        123
      ]
    }
  }
}
```
## Search for Persons

`GET /persons`

Searches your teams data and fetches all the persons that meet the search criteria. The search term can be part of an email address, a first name or a last name.

This result is paginated. An initial request returns an object with two fields: `persons` and `next_page_token`. `persons` contains an array of person resources. The value of `next_page_token` should be sent as the query parameter `page_token` in another request to retrieve the next page of results. While paginating through results, each request must have identical query parameters other than the changing `page_token`. Otherwise, an `Invalid page_token variable` error will be returned.

The absence of a `next_page_token` indicates that all the records have been fetched, though its presence does not necessarily indicate that there are *more* resources to be fetched. The next page may be empty (but then `next_page_token` would be `null` to confirm that there are no more resources).

Pass `with_interaction_dates=true` as a query parameter to include dates of the most recent and upcoming interactions with persons. When this parameter is included, persons with no interactions will not be returned in the response. Pass `with_interaction_persons=true` as a query parameter if `with_interaction_dates=true` to also get the internal persons associated with the interaction.

You can filter by interaction dates by providing additional query parameters like `min_last_email_date` or `max_next_event_date`. The value of these query parameters should be ISO 8601 formatted date strings.

#### Example Request

```bash
curl "https://api.affinity.co/persons?term=doe" -u :$APIKEY
```

#### Example Response

```json
{
  "persons": [
    {
      "id": 38706,
      "type": 0,
      "first_name": "John",
      "last_name": "Doe",
      "primary_email": "john@affinity.co",
      "emails": [
        "john@affinity.co",
        "jdoe@alumni.stanford.edu",
        "johnjdoe@gmail.com",
      ]
    },
    {
      "id": 624289,
      "type": 1,
      "first_name": "Jane",
      "last_name": "Doe",
      "primary_email": "jane@gmail.com",
      "emails": [
        "jane@gmail.com"
      ]
    },
    ...
  ],
  "next_page_token": "eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9"
}
```

> Example Pagination

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/persons?term=doe&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

> Example with Interaction Date

```bash
# To get the results between min_last_email_interaction_date and max_last_email_interaction_date, issue the following query:
curl "https://api.affinity.co/persons" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"min_last_email_date": "2021-01-01T00:00:00", "with_interaction_dates": true, "max_last_email_date": "2021-01-12T23:59:59"}'
```

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| term | string | false | A string used to search all the persons in your team's address book. This could be an email address, a first name or a last name. |
| with_interaction_dates | boolean | false | When true, interaction dates will be present on the returned resources. Only persons that have interactions will be returned. |
| with_interaction_persons | boolean | false | When true, persons for each interaction will be returned. Used in conjunction with `with_interaction_dates` |
| with_opportunities | boolean | false | When true, opportunity IDs will be returned for each person. |
| with_current_organizations | boolean | false | When true, the organization IDs of each person's current organizations (according to the Affinity Data: Current Organizations column) will be returned. |
| min_{interaction_type}_date | string | false | Only returns persons with the given interaction type above the given value. `interaction type` can be one of `first_email`, `last_email`, `last_interaction`, `last_event`, `first_event`, or `next_event`. This would be used with max interaction. |
| max_{interaction_type}_date | string | false | Only returns persons with the given interaction type below the given value. `interaction type` can be one of `first_email`, `last_email`, `last_interaction`, `last_event`, `first_event`, or `next_event`. This would be used with min interaction. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Returns

An object with two fields: `persons` and `next_page_token`. `persons` maps to an array of all the person resources that match the search criteria. Does not include the associated `organization_ids` or `list_entries`. `next_page_token` includes a token to be sent along with the next request as the `page_token` parameter to fetch the next page of results. When `with_interaction_dates` is passed in the returned resources will have `interaction_dates` fields.

## Get a Specific Person

`GET /persons/{person_id}`

Fetches a person with a specified `person_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| person_id | integer | true | The unique ID of the person that needs to be retrieved. |
| with_interaction_dates | boolean | false | When true, interaction dates will be present on the returned resources. |
| with_interaction_persons | boolean | false | When true, persons for each interaction will be returned. Used in conjunction with `with_interaction_dates` |
| with_opportunities | boolean | false | When true, opportunity IDs associated with this person will be returned. |
| with_current_organizations | boolean | false | When true, the IDs of this person's current organizations (according to the Affinity Data: Current Organizations column) will be returned. |

#### Returns

The person resource corresponding to the `person_id`.

#### Example Request

```bash
curl "https://api.affinity.co/persons/38706?with_opportunities=true&with_current_organizations=true" \
  -u :$APIKEY \
```

#### Example Response

```json
{
  "id": 38706,
  "type": 0,
  "first_name": "John",
  "last_name": "Doe",
  "primary_email": "john@affinity.co",
  "emails": [
    "john@affinity.co",
    "jdoe@alumni.stanford.edu",
    "johndoe@gmail.com",
  ],
  "organization_ids": [1687449],
  "opportunity_ids": [
    4,
    11,
    ...
  ],
  "current_organization_ids": [1687449],
  "list_entries": [
    {
      "id": 388,
      "list_id": 26,
      "creator_id": 38603,
      "entity_id": 38706,
      "created_at": "2015-12-11T02:26:56.537-08:00",
    },
    ...
  ],
}
```
## Create a New Person

`POST /persons`

Creates a new person with the supplied parameters.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| first_name | string | true | The first name of the person. |
| last_name | string | true | The last name of the person. |
| emails | string[] | true | The email addresses of the person. If there are no email addresses, please specify an empty array. |
| organization_ids | integer[] | false | An array of unique identifiers of organizations that the person is associated with. |

#### Returns

The person resource was newly created from this successful request.

#### Notes

> - If one of the supplied email addresses conflicts with another person object, this request will fail and an appropriate error will be returned.
> - If you are looking to add an existing person to a list, please check the [List Entries](#list-entries) section of the API.

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
  "id": 860197,
  "type": 0,
  "first_name": "Alice",
  "last_name": "Doe",
  "primary_email": "alice@affinity.co",
  "emails": ["alice@affinity.co"],
  "organization_ids": [1687449]
}
```
## Update a person

`PUT /persons/{person_id}`

Updates an existing person with `person_id` with the supplied parameters. Only attributes that need to be changed must be passed in.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| person_id | integer | true | The unique ID of the person that needs to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| first_name | string | false | The first name of the person. |
| last_name | string | false | The last name of the person. |
| emails | string[] | false | The email addresses of the person. If there are no email addresses, please specify an empty array. |
| organization_ids | integer[] | false | An array of unique identifiers of organizations that the person is associated with |

#### Returns

The person object that was just updated through this request.

#### Note

> - If you are looking to add an existing person to a list, please check the [List Entries](#list-entries) section of the API.
> - If you are trying to add a new email or organization to a person, the existing values for `emails` and `organization_ids` must also be supplied as parameters.

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
  "id": 860197,
  "type": 0,
  "first_name": "Allison",
  "last_name": "Doe",
  "primary_email": "alice@affinity.co",
  "emails": ["alice@affinity.co", "allison@example.com", "allison@gmail.com"],
  "organization_ids": [1687449]
}
```
## Delete a Person

`DELETE /persons/{person_id}`

Deletes a person with a specified `person_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| person_id | integer | true | The unique ID of the person that needs to be deleted. |

#### Returns

`{success: true}`.

#### Note

> This will also delete all the field values, if any, associated with the person. Such field values exist linked to either global or list-specific fields.

#### Example Request

```bash
curl "https://api.affinity.co/persons/860197" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
## Get Global Person Fields

`GET /persons/fields`

Fetches an array of all the global fields that exist on people. If you aren't sure about what fields are, please read the [Fields](#fields) section first.

#### Example Request

```bash
curl "https://api.affinity.co/persons/fields" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 125,
    "name": "Use Case",
    "value_type": 2,
    "allows_multiple": true,
    "dropdown_options": []
  },
  {
    "id": 198,
    "name": "Referrers",
    "value_type": 0,
    "allows_multiple": true,
    "dropdown_options": []
  },
  {
    "id": 1615,
    "name": "Address",
    "value_type": 5,
    "allows_multiple": false,
    "dropdown_options": []
  },
  ...
]
```

### Parameters

None.

#### Returns

An array of the global fields that exist on people for your team.

# Organizations

An organization in Affinity represents an external company that your team is in touch with- this could be an organization you're trying to invest in, sell to, or establish a relationship with.

An organization has many people associated with it - these are your team's points of contacts at that organization. Just like people, organizations can be added to multiple lists and can be assigned field values.

To make the data quality as good as possible, we have our own proprietary database of organizations that we have developed through third-party partnerships and web scraping. We use this database to minimize data entry for you as you use Affinity's CRM products.

#### Notes

> - If you are looking to add or remove an organization from a list, please check out the [List Entries](#list-entries) section of the API.
> - If you are looking to modify a field value (one of the cells on Affinity's spreadsheet), please check out the [Field Values](#field-values) section of the API.

## The Organization Resource

Each organization object has a unique `id`. It also has a `name`, `domain` (the website of the organization), and `persons` associated with it. The `domain` is an important attribute from an automation perspective, as it helps Affinity automatically link all the appropriate person objects to the organization.

Each organization also has a flag determining whether it's `global` or not. As mentioned above, Affinity maintains its own database of global organizations that each customer has access to. Note that you cannot change the name or the domain of a `global` organization. You also cannot delete a `global` organization.

Of course, if an organization is manually created by your team, all fields can be modified and the organization can be deleted.

Dates of the most recent and upcoming interactions with an organization are available in the `interaction_dates` field. This data is only included when passing `with_interaction_dates=true` as a query parameter to the [`GET /organizations`](#search-for-organizations) or the [`GET /organizations/{organization_id}`](#get-a-specific-organization) endpoints.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the organization object. |
| name | string | The name of the organization. |
| domain | string | The website name of the organization. This is used by Affinity to automatically associate person objects with an organization. |
| domains | string[] | An array of all the websites associated with the organization. These are also used to automatically associate person objects with an organization. |
| person_ids | integer[] | An array of unique identifiers of people that are associated with the organization |
| opportunity_ids | integer[] | An array of unique identifiers of opportunities that are associated with the organization |
| global | boolean | Returns whether this organization is a part of Affinity's global dataset of organizations. This is always false if the organization was created by you. |
| list_entries | ListEntry[] | An array of list entry resources associated with the organization, only returned as part of the [Get a specific organization](#get-a-specific-organization) endpoint. |
| interaction_dates | object | An object with seven string date fields representing the most recent and upcoming interactions with this organization: `first_email_date`, `last_email_date`, `last_event_date`, `last_chat_message_date`, `last_interacton_date`, `first_event_date`, and `next_event_date`. Only returned when passing `with_interaction_dates=true`. |
| interactions | object | An object with seven fields nested underneath. Each field corresponds to one of the seven interactions, and includes nested fields for `date` and `person_ids` which indicates the internal people associated with that event (people only returned if passing `with_interaction_persons=true`). Only returned when passing `with_interaction_dates=true`. |

#### Example Response

```json
{
  "id": 64779194,
  "name": "Affinity",
  "domain": "affinity.co",
  "domains": ["affinity.co"],
  "global": false,
  "person_ids": [
    89734,
    117270,
    138123,
    274492,
    304848,
    ...],
  "opportunity_ids": [
    4,
    11,
    ...
  ],
  "list_entries": [
    {
      "id": 389,
      "list_id": 26,
      "creator_id": 38603,
      "entity_id": 64779194,
      "created_at": "2015-12-11T02:26:56.537-08:00",
    },
    ...
  ],
  "interaction_dates": {
    "first_email_date": "2011-11-23T08:12:45.328-08:00",
    "last_email_date": "2012-03-04T05:06:07.890-08:00",
    "last_event_date": "2011-12-11T02:26:56.537-08:00",
    "last_chat_message_date": "2011-11-01T02:26:56.537-08:00",
    "last_interaction_date": "2012-03-04T05:06:07.890-08:00",
    "next_event_date": "2019-03-04T05:06:07.890-08:00",
    "first_event_date": "2012-01-01T08:18:00.329-08:00",
  },
  "interactions": {
    "first_email": {
      "date": "2011-11-23T08:12:45.328-08:00",
      "person_ids": [
        123
      ]
    },
    "last_email": {
      "date": "2012-03-04T05:06:07.890-08:00",
      "person_ids": [
        123
      ]
    },
    "last_event": {
      "date": "2011-12-11T02:26:56.537-08:00",
      "person_ids": [
        123
      ]
    },
    "last_chat_message": {
      "date": "2011-11-01T02:26:56.537-08:00",
      "person_ids": [
        123
      ]
    },
    "last_interaction": {
      "date": "2012-03-04T05:06:07.890-08:00",
      "person_ids": [
        123,
        111
      ]
    },
    "next_event": {
      "date": "2019-03-04T05:06:07.890-08:00",
      "person_ids": [
        123,
        124,
        125
      ]
    },
    "first_event": {
      "date": "2012-01-01T08:18:00.329-08:00",
      "person_ids": [
        123
      ]
    }
  }
}
```
## Search for Organizations

`GET /organizations`

Searches your team's data and fetches all the organizations that meet the search criteria. The search term can be a part of an organization's name or domain.

This result is paginated. An initial request returns an object with two fields: `organizations` and `next_page_token`. `organizations` contains an array of organization resources. The value of `next_page_token` should be sent as the query parameter `page_token` in another request to retrieve the next page of results. While paginating through results, each request must have identical query parameters other than the changing `page_token`. Otherwise, an `Invalid page_token variable` error will be returned.

The absence of a `next_page_token` indicates that all the records have been fetched, though its presence does not necessarily indicate that there are *more* resources to be fetched. The next page may be empty (but then `next_page_token` would be `null` to confirm that there are no more resources).

Pass `with_interaction_dates=true` as a query parameter to include dates of the most recent and upcoming interactions with organizations. When this parameter is included, organizations with no interactions will not be returned in the response. Pass `with_interaction_persons=true` as a query parameter if `with_interaction_dates=true` to also get the internal persons associated with the interaction.

You can filter by interaction dates by providing additional query parameters like `min_last_email_date` or `max_next_event_date`. The value of these query parameters should be ISO 8601 formatted date strings. The interaction dates are stored with timestamps, so the `{min,max}_<interaction>_date` parameter can include or exclude timestamps to explicitly filter the dataset. If a timestamp is not provided, the system will use the default value of `00:00:00`.

#### Example Request

```bash
curl "https://api.affinity.co/organizations?term=affinity" -u :$APIKEY
```

#### Example Response

```json
{
  "organizations": [
    {
      "id": 64779194,
      "name": "Affinity",
      "domain": "affinity.co",
      "domains": ["affinity.co"],
      "global": false
    },
    {
      "id": 1513682,
      "name": "Brand Affinity Technologies",
      "domain": "brandaffinity.net",
      "domains": ["brandaffinity.net"],
      "global": true
    },
    ...
  ],
  "next_page_token": "eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9",
}
```

> Example Pagination

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/organizations" \
  -u :$APIKEY \
  -d page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9
```

> Example with Interaction Date

```bash
# To get the results between min_last_email_interaction_date and max_last_email_interaction_date, issue the following query:
curl "https://api.affinity.co/organizations" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"min_last_email_date": "2021-01-01T00:00:00", "with_interaction_dates": true, "max_last_email_date": "2021-01-12T23:59:59"}'
```

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| term | string | false | A string used to search all the organizations in your team's address book. This could be a name or a domain name. |
| with_interaction_dates | boolean | false | When true, interaction dates will be present on the returned resources. Only organizations that have interactions will be returned. |
| with_interaction_persons | boolean | false | When true, persons for each interaction will be returned. Used in conjunction with `with_interaction_dates`. |
| with_opportunities | boolean | false | When true, opportunity IDs associated with this organization will be returned. |
| min_{interaction_type}_date | string | false | Only returns organizations with the given interaction type above the given value. `interaction type` can be one of `first_email`, `last_email`, `last_interaction`, `last_event`, `first_event`, or `next_event`. This would be used with max interaction. |
| max_{interaction_type}_date | string | false | Only returns organizations with the given interaction type below the given value. `interaction type` can be one of `first_email`, `last_email`, `last_interaction`, `last_event`, `first_event`, or `next_event`. This would be used with min interaction. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Returns

An object with two fields: `organizations` and `next_page_token`. `organizations` maps to an array of all the organization resources that match the search criteria. `next_page_token` includes a token to be sent along with the next request as the `page_token` parameter to fetch the next page of results. When `with_interaction_dates` is passed in the returned resources will have `interaction_dates` fields.

#### Note

> When only a search term is supplied, Affinity will search organization resources that are also outside of your instance.

## Get a Specific Organization

`GET /organizations/{organization_id}`

Fetches an organization with a specified `organization_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| organization_id | integer | true | The unique ID of the organization that needs to be retrieved. |
| with_interaction_dates | boolean | false | When true, interaction dates will be present on the returned resources. |
| with_interaction_persons | boolean | false | When true, persons for each interaction will be returned. Used in conjunction with `with_interaction_dates` |
| with_opportunities | boolean | false | When true, opportunity IDs associated with this organization will be returned. |

#### Returns

The organization object corresponding to the `organization_id`.

#### Example Request

```bash

#### Example Response

```json
{
  "id": 64779194,
  "name": "Affinity",
  "domain": "affinity.co",
  "domains": ["affinity.co"],
  "global": false,
  "person_ids": [
    89734,
    117270,
    138123,
    274492,
    304848,
    ...
  ],
  "opportunity_ids": [
    4,
    11,
    ...
  ],
  "list_entries": [
    {
      "id": 389,
      "list_id": 26,
      "creator_id": 38603,
      "entity_id": 64779194,
      "created_at": "2015-12-11T02:26:56.537-08:00",
    },
    ...
  ],
}
```
# Returns the organization with the specified `organization_id`.
curl "https://api.affinity.co/organizations/120611418" -u :$APIKEY
```

## Create a New Organization

`POST /organizations`

Creates a new organization with the supplied parameters.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | true | The name of the organization. |
| domain | string | false | The domain name of the organization. |
| person_ids | integer[] | false | An array of unique identifiers of persons that the new organization will be associated with. |

#### Returns

The organization resource that was just created by a successful request.

#### Notes

> If you are looking to add an existing organization to a list, please check the [List Entries](#list-entries) section of the API.

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
  "id": 120611418,
  "name": "Acme Corporation",
  "domain": "acme.co",
  "domains": ["acme.co"],
  "global": false,
  "person_ids": [38706]
}
```
## Update an Organization

`PUT /organizations/{organization_id}`

Updates an existing organization with `organization_id` with the supplied parameters.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| organization_id | integer | true | The unique ID of the organization to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | false | The name of the organization. |
| domain | string | false | The domain name of the organization. |
| person_ids | integer[] | false | An array of unique identifiers of persons that the organization will be associated with. |

#### Returns

The organization resource that was just updated through a successful request.

#### Notes

> - If you are looking to add an existing organization to a list, please check the [List Entries](#list-entries) section of the API.
> - If you are trying to add a person to an organization, the existing values for `person_ids` must also be passed into the endpoint.

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
  "id": 120611418,
  "name": "Acme Corp.",
  "domain": "acme.co",
  "domains": ["acme.co"],
  "global": false,
  "person_ids": [38706, 89734]
}
```
## Delete an Organization

`DELETE /organizations/{organization_id}`

Deletes an organization with a specified `organization_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| organization_id | integer | true | The unique ID of the organization that needs to be deleted. |

#### Returns

`{success: true}`.

#### Notes

> - An appropriate error will be returned if you are trying to delete a `global` organization.
> - This will also delete all the field values, if any, associated with the organization. Such field values exist linked to either global or list-specific fields.

#### Example Request

```bash
curl "https://api.affinity.co/organizations/120611418" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
## Get Global Organizations Fields

`GET /organizations/fields`

Fetches an array of all the global fields that exist on organizations. If you aren't sure about what fields are, please read the [Fields](#fields) section first.

### Parameters

None.

#### Returns

An array of the fields that exist on all organizations for your team.

#### Example Request

```bash
curl "https://api.affinity.co/organizations/fields" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 662,
    "name": "Potential Users",
    "value_type": 3,
    "allows_multiple": false,
    "dropdown_options": []
  },
  {
    "id": 700,
    "name": "Leads",
    "value_type": 0,
    "allows_multiple": true,
    "dropdown_options": []
  },
  {
    "id": 2988,
    "name": "Last Funding Date",
    "value_type": 4,
    "allows_multiple": false,
    "dropdown_options": []
  },
  ...
]
```
# Opportunities

An opportunity in Affinity represents a potential future sale or deal for your team. It can have multiple people - your team's main points of contacts for the opportunity - and organization(s) associated with it. Opportunities are generally used to track the progress of and revenue generated from sales and deals in your pipeline with a specific organization.

Unlike people and organizations, an opportunity can only belong to a single list and, thus, does not have global fields. This list must be provided at the creation of the opportunity. If the list or list entry containing the opportunity gets deleted, then the opportunity subsequently gets deleted. If a user does not have permission to access a list with opportunities, the user cannot view any of those opportunities.

#### Notes

> - If you are looking to remove an opportunity from a list, note that deleting an opportunity is the same as removing an opportunity from a list because an opportunity can only exist on a single list with a single list entry.
> - If you are looking to modify a field value (one of the cells on Affinity's spreadsheet), please check out the [Field Values](#field-values) section of the API.

## The Opportunity Resource

Each opportunity object has a unique `id`. It also has a `name`, `persons_ids` and `organization_ids` associated with it, and an array of `list_entries`. An important attribute to note is `list_entries`. Because an opportunity can only belong to a single list, `list_entries` can only have one list entry.

Of course, all fields can be modified and the opportunity can be deleted.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the opportunity object. |
| name | string | The name of the opportunity (see below). |
| person_ids | number[] | An array of unique identifiers for persons that are associated with the opportunity |
| organization_ids | number[] | An array of unique identifiers for organizations that are associated with the opportunity |
| list_entries | ListEntry[] | An array of list entry resources associated with the opportunity (at most 1 list entry). If the user corresponding to the API key does not have access to the list, this will be empty. |

#### Example Response

```json
{
  "id": 117,
  "name": "Affinity Opportunity",
  "person_ids": [38706],
  "organization_ids": [21442],
  "list_entries": [
    {
      "id": 442313,
      "creator_id": 38706,
      "list_id": 4974,
      "entity_id": 117,
      "entity_type": 8,
      "created_at": "2018-03-03T23:02:46.412-08:00"
    }
  ]
}
```
## Search for Opportunities

`GET /opportunities`

Searches your team's data and fetches all the opportunities that meet the search criteria. The search term can be a part of an opportunity's name.

This result is paginated. An initial request returns an object with two fields: `opportunities` and `next_page_token`. `opportunities` contains an array of opportunity resources. The value of `next_page_token` should be sent as the query parameter `page_token` in another request to retrieve the next page of results. While paginating through results, each request must have identical query parameters other than the changing `page_token`. Otherwise, an `Invalid page_token variable` error will be returned.

The absence of a `next_page_token` indicates that all the records have been fetched, though its presence does not necessarily indicate that there are *more* resources to be fetched. The next page may be empty (but then `next_page_token` would be `null` to confirm that there are no more resources).

#### Example Request

```bash
curl "https://api.affinity.co/opportunities?term=affinity" -u :$APIKEY
```

#### Example Response

```json
{
  "opportunities": [
    {
      "id": 121,
      "name": "Affinity Opportunity",
      "person_ids": [3526824],
      "organization_ids": [128367168],
      "list_entries": [
        {
          "id": 442313,
          "creator_id": 1124736,
          "list_id": 4974,
          "entity_id": 121,
          "entity_type": 8,
          "created_at": "2018-03-03T23:02:46.412-08:00"
        },
      ],
    },
    {
      "id": 150,
      "name": "Affinity Opportunity 2",
      "person_ids": [5326214],
      "organization_ids": [128367168],
      "list_entries": [
        {
          "id": 442421,
          "creator_id": 1124736,
          "list_id": 4974,
          "entity_id": 150,
          "entity_type": 8,
          "created_at": "2018-03-08T23:02:46.412-08:00"
        },
      ],
    },
    ...
  ],
  "next_page_token": "eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9",
}
```

> Example pagination

```bash
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/opportunities?term=affinity&page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| term | string | false | A string used to search all the opportunities in your team's database. This could be part of a name. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Returns

An object with two fields: `opportunities` and `next_page_token`. `opportunities` maps to an array of all the opportunity resources that match the search criteria. `next_page_token` includes a token to be sent along with the next request as the `page_token` parameter to fetch the next page of results.

## Get a Specific Opportunity

`GET /opportunities/{opportunity_id}`

Fetches an opportunity with a specified `opportunity_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| opportunity_id | integer | true | The unique ID of the opportunity that needs to be retrieved. |

#### Returns

The opportunity object corresponding to the `opportunity_id`.

#### Example Request

```bash
curl "https://api.affinity.co/opportunities/117" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 117,
  "name": "Affinity Opportunity",
  "person_ids": [3526824],
  "organization_ids": [128367168],
  "list_entries": [
    {
      "id": 442313,
      "creator_id": 1124736,
      "list_id": 4974,
      "entity_id": 117,
      "entity_type": 8,
      "created_at": "2018-03-03T23:02:46.412-08:00"
    },
  ],
}
```
## Create a New Opportunity

`POST /opportunities`

Creates a new opportunity with the supplied parameters.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | true | The name of the opportunity. |
| list_id | integer | true | An unique identifier of the list that the new opportunity will be associated with. This list must be of type opportunity. |
| person_ids | integer[] | false | An array of unique identifiers of persons that the new opportunity will be associated with. |
| organization_ids | integer[] | false | An array of unique identifiers of organizations that the new opportunity will be associated with. |

#### Returns

The opportunity resource that was just created by a successful request (without `person_ids` and `organization_ids`).

#### Example Request

```bash
curl -X POST "https://api.affinity.co/opportunities" \
   -u :$APIKEY \
   -H "Content-Type: application/json" \
   -d '{"name": "Penny Opportunity", "list_id": 6645, "person_ids": [38706], "organization_ids": [21442]}'
```

#### Example Response

```json
{
  "id": 120611418,
  "name": "Penny Opportunity",
  "person_ids": [38706],
  "organization_ids": [21442],
  "list_entries": [
    {
      "id": 999886,
      "creator_id": 1127776,
      "list_id": 6645,
      "entity_id": 50,
      "entity_type": 8,
      "created_at": "2018-03-07T16:32:35.794-08:00"
    }
  ]
}
```
## Update an Opportunity

`PUT /opportunities/{opportunity_id}`

Updates an existing opportunity with `opportunity_id` with the supplied parameters.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| opportunity_id | integer | true | The unique ID of the opportunity to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| name | string | false | The name of the opportunity. |
| person_ids | integer[] | false | An array of unique identifiers of persons that the opportunity will be associated with. |
| organization_ids | integer[] | false | An array of unique identifiers of organizations that the opportunity will be associated with. |

#### Returns

The opportunity resource that was just updated through a successful request.

#### Notes

> - If you are trying to add a person to an opportunity, the existing values for `person_ids` must also be passed into the endpoint.
> - If you are trying to add an organization to an opportunity, the existing values for `organization_ids` must also be passed into the endpoint.

#### Example Request

```bash

#### Example Response

```json
{
  "id": 120611418,
  "name": "Penny Opp",
  "person_ids": [38706, 89734],
  "organization_ids": [21442],
  "list_entries": [
    {
      "id": 999886,
      "creator_id": 1127776,
      "list_id": 6645,
      "entity_id": 50,
      "entity_type": 8,
      "created_at": "2018-03-07T16:32:35.794-08:00"
    }
  ]
}
```
# Updates the opportunity with the specified `opportunity_id`.
curl -X PUT "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"name": "Penny Opportunity", "person_ids": [38706, 89734]}'
```

## Delete an Opportunity

`DELETE /opportunities/{opportunity_id}`

Deletes an opportunity with a specified `opportunity_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| opportunity_id | integer | true | The unique ID of the opportunity that needs to be deleted. |

#### Returns

`{success: true}`.

#### Note

> This will also delete all the field values, if any, associated with the opportunity.

#### Example Request

```bash
curl "https://api.affinity.co/opportunities/120611418" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Interactions

The interactions API allows you to manage interactions.

## The Interactions Resource

Different types of interactions have different interaction resources. Note the combination of ID and type for an interaction is unique.

#### Example Response

```json
# Meeting/Call type
{
    "date": "2022-02-22T11:15:29.758-08:00",
    "id": 3007,
    "attendees": [
        "john@affinity.co",
        "yen@alice.com"
    ],
    "start_time": "2022-02-22T11:15:29.758-08:00",
    "end_time": null,
    "updated_at": null,
    "manual_creator_id": 2,
    "title": "Manually logged event",
    "type": 0,
    "notes": [
        7
    ],
    "persons": [
        {
            "id": 443,
            "type": 1,
            "first_name": "John",
            "last_name": "Doe",
            "primary_email": "john@affinity.co",
            "emails": [
                "john@affinity.co"
            ]
        },
        {
            "id": 2021,
            "type": 0,
            "first_name": "Alice",
            "last_name": "Yen",
            "primary_email": "yen@alice.com",
            "emails": [
                "yen@alice.com"
            ]
        }
    ]
}

# Chat message type
{
    "id": 7267,
    "date": "2022-02-22T11:50:20.126-08:00",
    "direction": 0,
    "manual_creator_id": 443,
    "persons": [
        {
            "id": 443,
            "type": 1,
            "first_name": "John",
            "last_name": "Doe",
            "primary_email": "john@affinity.co",
            "emails": [
                "john@affinity.co"
            ]
        },
        {
            "id": 2021,
            "type": 0,
            "first_name": "Alice",
            "last_name": "Yen",
            "primary_email": "yen@alice.com",
            "emails": [
                "yen@alice.com"
            ]
        }
    ],
    "type": 2,
    "notes": [
        7462534
    ]
}

# Email type
{
    "date": "2021-02-04T09:43:39.717-08:00",
    "id": 417,
    "subject": "John <-> Alice",
    "type": 3,
    "from": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "to": [
        {
            "id": 2021,
            "type": 0,
            "first_name": "Alice",
            "last_name": "Yen",
            "primary_email": "yen@alice.com",
            "emails": [
                "yen@alice.com"
            ]
        }
    ],
    "cc": [],
    "direction": 0
}
```

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The identifier of the interaction. Note the ID is not unique across different types of interactions. |
| manual_creator_id | integer | The unique identifier of the person object who created the interaction. |
| persons | object[] | The list of persons who are associated with the interaction. |
| type | integer | The type of interaction. This can be one of many values, as described in the table below. |
| logging_type | integer | The logging type of interaction. |
| attendees | string[] | The list of person emails that attended the event. |
| date | datetime | The time when the interaction happens. |
| start_time | datetime | The time when event starts. |
| end_time | datetime | The time when event ends. |
| title | string | The title of event. |
| notes | integer[] | The list of note IDs that are associated with the event. |
| direction | integer | The direction of the interaction. Only relevant for `type == 2` and `type == 3`. This can be one of two values, as described in the table below. |

### Interactions Types

| Type | Value | Description |
| --- | --- | --- |
| Meeting | 0 | Type specifying a meeting interaction. |
| Call | 1 | Type specifying a call interaction. |
| Chat message | 2 | Type specifying a chat message interaction. |
| Email | 3 | Type specifying a email interaction. |

### Direction Types

| Type | Value | Description |
| --- | --- | --- |
| Sent | 0 | The interaction is sent by an internal person. |
| Received | 1 | The interaction is sent by an external person. |

### Logging Types

| Type | Value | Description |
| --- | --- | --- |
| All | 0 | Type specifying both automatically logged interactions and manually logged interactions. |
| Manual | 1 | Type specifying only manually logged interactions |

## Get All Interactions

`GET /interactions`

Returns all interactions that meet the query parameters.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | integer | true | The type of interactions to be retrieved. |
| logging_type | integer | false | The logging type of interactions to be retrieved. |
| person_id | integer | custom* | A unique identifier that represents an external Person that was involved in the interactions. |
| organization_id | integer | custom* | A unique identifier that represents an Organization that was involved in the interactions. |
| opportunity_id | integer | custom* | A unique identifier that represents an Opportunity that was involved in the interactions. |
| internal_person_id | integer | false | A unique identifier that represents an internal person that was involved in the interactions.Thi parameter cannot be used to find all of an internal person's interactions. It only filters down the set of interactions related to the given external person, organization, or opportunity -- to the interactions in which the given internal person was involved. |
| direction | integer | false | The direction of the interactions. Only applies to chat message and email. |
| start_time | string | true | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the start of the time range for the interactions to be retrieved. Must be before `end_time`. Date range must not exceed one year. |
| end_time | string | true | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the end of the time range for the interactions to be retrieved. Must be after `start_time`. Date range must not exceed one year. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 100.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Notes

> - One `person_id`, `organization_id` or `opportunity_id` must be specified per request.
> - Only one `type` of interaction can be specified per request.
> - `start_time` and `end_time` must be within a single one-year window when querying interactions.
> - An error will be returned if an internal person is used in the `person_id` parameter.

#### Returns

An array of all the interactions filtered by query parameters. `next_page_token` includes a token to be sent along with the next request as the `page_token` parameter to fetch the next page of results.

#### Note

> Interactions in the API response may not be visible on a CRM profile page if they have the exact same timestamp as another interaction.

#### Example Request

```bash
curl "https://api.affinity.co/interactions?organization_id=1609909&type=3&start_time=2021-01-01T07:00:00Z&end_time=2021-02-25T21:00:00Z&" -u :$APIKEY
```

#### Example Response

```json
{
  "emails": [
    {
      "date": "2021-02-04T09:43:39.717-08:00",
      "id": 417,
      "subject": "John <-> Alice",
      "type": 3,
      "from": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": ["john@affinity.co"]
      },
      "to": [
        {
          "id": 2021,
          "type": 0,
          "first_name": "Alice",
          "last_name": "Yen",
          "primary_email": "yen@alice.com",
          "emails": ["yen@alice.com"]
        }
      ],
      "cc": [],
      "direction": 0
    },
    {
      "date": "2021-02-02T12:55:19.801-08:00",
      "id": 265,
      "subject": "Alfred <-> Alice",
      "type": 3,
      "from": {
        "id": 1012,
        "type": 1,
        "first_name": "Alfred",
        "last_name": "Hickey",
        "primary_email": "alfredhickeyshmcneax@affinity.co",
        "emails": ["alfredhickeyshmcneax@affinity.co"]
      },
      "to": [
        {
          "id": 2021,
          "type": 0,
          "first_name": "Alice",
          "last_name": "Yen",
          "primary_email": "yen@alice.com",
          "emails": ["yen@alice.com"]
        }
      ],
      "cc": [],
      "direction": 0
    }
  ],
  "next_page_token": "eyJwYXJhbXMiOnsiY29tcGxldGVyX2lkIjpudWxsLCJvd25lcl9pZCI6bnVsbCwiY3JlYXRvcl9"
}
```
## Get a Specific Interaction

#### Example Request

```bash
# Returns the interactions with the specified `id`
curl "https://api.affinity.co/interactions/15326?type=2" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 7267,
  "date": "2022-02-22T11:50:20.126-08:00",
  "direction": 0,
  "manual_creator_id": 64056952,
  "persons": [
    {
      "id": 443,
      "type": 1,
      "first_name": "John",
      "last_name": "Doe",
      "primary_email": "john@affinity.co",
      "emails": ["john@affinity.co"]
    },
    {
      "id": 2021,
      "type": 0,
      "first_name": "Alice",
      "last_name": "Yen",
      "primary_email": "yen@alice.com",
      "emails": ["yen@alice.com"]
    }
  ],
  "type": 2,
  "notes": [7462534]
}
```

`GET /interactions/{id}`

Gets the details for a specific interaction given the existing ID and type.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | integer | true | The identifier of the interaction object to be retrieved. |
| type | integer | true | The type of interaction to be retrieved. |

#### Returns

The details of the interaction corresponding to the ID and type specified in the path parameter. An appropriate error is returned if an invalid ID and type are supplied.

## Create a New Interaction

`POST /interactions`

Creates a new interaction with the supplied parameters.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | integer | true | The type of interaction to be created. Only meetings (`type == 0`), calls (`type == 1`) and chat messages (`type == 2`) are supported. |
| person_ids | integer[] | true | The list of person IDs that are associated with the event. At least one internal person ID must be included (see [Person Resource](#the-person-resource) for more details on internal persons). |
| content | string | true | The string containing the content of the new interaction. |
| direction | integer | false | The direction of the chat message to be created. Only applies to chat messages (`type == 2`). |
| date | string | true | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the date time the interaction occurred. |

#### Returns

The interaction created through this request.

#### Note

> When creating an interaction using the API, the user corresponding to the API token will be the creator by default.

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
  "date": "2021-02-07T10:56:29.546-08:00",
  "id": 3007,
  "attendees": ["john@affinity.co", "yen@alice.com"],
  "start_time": "2021-02-07T10:56:29.546-08:00",
  "end_time": null,
  "updated_at": null,
  "manual_creator_id": 443,
  "title": "Manually logged event",
  "type": 0,
  "notes": [7],
  "persons": [
    {
      "id": 443,
      "type": 1,
      "first_name": "John",
      "last_name": "Doe",
      "primary_email": "john@affinity.co",
      "emails": ["john@affinity.co"]
    },
    {
      "id": 2021,
      "type": 0,
      "first_name": "Alice",
      "last_name": "Yen",
      "primary_email": "yen@alice.com",
      "emails": ["yen@alice.com"]
    }
  ]
}
```
## Update an Interaction

`PUT /interactions/{id}`

Updates the content of an existing interaction with the supplied parameters.

#### Note

> Updating the content of an interaction using the API is not supported when mentioned IDs are in the content.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | integer | true | The ID of the interaction to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| type | integer | true | The type of interaction to be updated. |
| person_ids | integer[] | true | The list of person IDs that are associated with the event. |
| content | string | false | The string containing the content of the interaction. |
| date | string | false | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the date time the interaction occurred. |

#### Returns

The interaction object that was just updated through this request.

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
  "date": "2022-02-07T10:56:29.546-08:00",
  "id": 3007,
  "attendees": ["john@affinity.co", "yen@alice.com"],
  "start_time": "2022-02-07T10:56:29.546-08:00",
  "end_time": null,
  "updated_at": null,
  "manual_creator_id": 443,
  "title": "Manually logged event",
  "type": 0,
  "notes": [7],
  "persons": [
    {
      "id": 443,
      "type": 1,
      "first_name": "John",
      "last_name": "Doe",
      "primary_email": "john@affinity.co",
      "emails": ["john@affinity.co"]
    },
    {
      "id": 2021,
      "type": 0,
      "first_name": "Alice",
      "last_name": "Yen",
      "primary_email": "yen@alice.com",
      "emails": ["yen@alice.com"]
    }
  ]
}
```
## Delete an Interaction

`DELETE /interactions/{id}`

Deletes the interaction with the specified `id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | integer | true | The unique ID of the interaction to be deleted. |
| type | integer | true | The type of interaction to be deleted. |

#### Returns

`{success: true}`.

#### Example Request

```bash
curl "https://api.affinity.co/interactions/22984?type=0" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Relationship Strengths

Affinity calculates relationship strengths between internal and external people based on previous interactions (emails, logged calls, calendar events).

A higher numeric value means that the relationship strength between the two people is higher. Emails, calls, and meetings don't tell the whole story of a relationship, so treat the strength as an estimate.

Relationship strengths are usually recalculated daily.

## The Relationship Strength Resource

The relationship strength resource specifies the two [Persons](#persons) the relationship strength is about, along with the actual value.

There may be at most one resource for every (internal, external) pair. If an internal and external person have no previous interactions, there may be no relationship strength resource for the pair.

| Attribute | Type | Description |
| --- | --- | --- |
| internal_id | integer | The internal person associated with this relationship strength. |
| external_id | integer | The external person associated with this relationship strength. |
| strength | float | The actual relationship strength. This is currently a number between 0 and 1, but may change in the future. |

#### Example Response

```json
{
  "external_id": 1234,
  "internal_id": 2345,
  "strength": 0.5
}
```
## Get Relationship Strength

`GET /relationships-strengths`



### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| internal_id | integer | false | The internal person associated with this relationship strength. |
| external_id | integer | true | The external person associated with this relationship strength. |

#### Returns

An array of the relationship strengths matching the criteria.

If an `internal_id` is given, returns the relationship strength between the given internal and external person. The returned list will have a length of 1 or 0 (if no relationship strength is available between the two people).

If no `internal_id` is given, returns the relationship strengths between all internal people and the given external person. The results are not guaranteed to be sorted in any way.

#### Example Request

```bash
# Returns relationship strengths matching the provided identifiers.
curl "https://api.affinity.co/relationships-strengths?external_id=1234&internal_id=2345" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "internal_id": 1234,
    "external_id": 2345,
    "strength": 0.5
  }
]
```

# Notes

Just like field values, notes are used to keep track of state on an entity. They could be notes manually taken from due diligence, a meeting, or a call. Or, notes could be used to store logged activity from a prospect's visit to your website.

## The Note Resource

A note object contains `content`, which is a string containing the note body. In addition, a note can be associated with multiple people, organizations, or opportunities. Each person, organization, or opportunity will display linked notes on their profiles.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the note object. |
| creator_id | integer | The unique identifier of the person object who created the note. |
| person_ids | integer[] | An array containing the unique identifiers for all the persons relevant to the note. This is the union of `associated_person_ids` and `interaction_person_ids`. |
| associated_person_ids | integer[] | An array containing the unique identifiers for the persons directly associated with the note. |
| interaction_person_ids | integer[] | An array containing the unique identifiers for the persons on the interaction the note is attached to, if any. This will be an empty array if there is no such interaction or there aren't any attendees. |
| interaction_id | integer | The unique identifier of the interaction the note is attached to, if any. |
| interaction_type | integer | The type of the interaction the note is attached to, if any. |
| is_meeting | boolean | True if the note is attached to a meeting or a call. |
| mentioned_person_ids | integer[] | An array containing the unique identifiers for the persons who are @ mentioned in the note. If there are no mentioned persons, this will be an empty array. |
| organization_ids | integer[] | An array of unique identifiers of organization objects that are associated with the note. |
| opportunity_ids | integer[] | An array of unique identifiers of opportunity objects that are associated with the note. |
| parent_id | integer | The unique identifier of the note that this note is a reply to. If this field is `null`, the note is not a reply. Note replies will never have values for `opportunity_ids`, `person_ids`, and `organization_ids`. Only the parent note is associated with an entity. You can fetch the parent note resource to identify the root entity. |
| content | string | The string containing the content of the note. |
| type | integer | The type of the note. The supported types for new note creation via API are 0 and 2, which represent plain text and HTML notes, respectively. Notes with type 3 are AI meeting summaries generated by [Affinity Notetaker](https://support.affinity.co/hc/en-us/articles/19495299764365-How-to-set-up-use-Affinity-Notetaker), and can only be created by the system. Users may also encounter existing notes with type 1, which represents notes created directly from email messages (this creation method is now deprecated). |
| created_at | datetime | The string representing the time when the note was created. |
| updated_at | datetime | The string representing the last time the note was updated. |

### Formatting `content` as HTML

> Example `content` payload

```html
<p>
  This is normal text. <strong> But this is bold! </strong>
  <span style="color: rgb(255, 0, 0);"> And this is red! </span>
</p>
```

If you would like to format your notes, create them with `type` equal to `2`, as described in [Create a New Note](#create-a-new-note). All currently supported formatting options are described below.

| Style | Formatting | Example |
| --- | --- | --- |
| Paragraph | `<p>` element | `<p>I am a paragraph!</p>` |
| Bold | `<strong>` element | `<p><strong>This text is bold</strong></p>` |
| Italics | `<em>` element | `<p><em>This text is italicized</em></p>` |
| Underlined | `<u>` element | `<p><u>This text is underlined</u></p>` |
| Ordered lists | `<ol>` + `<li>` elements | `<ol><li>First item</li><li>Second item</li></ol>` |
| Unordered lists | `<ul>` + `<li>` elements | `<ul><li>An item</li><li>Another item</li></ul>` |
| Background color | `background-color` inline style | `<p><span style="background-color: rgb(255, 0, 0);"> The background is red</span></p>` |
| Font color | `color` inline style | `<p><span style="color: rgb(255, 0, 0);"> The text color is red</span></p>` |

#### Example Response

```json
{
  "id": 22984,
  "creator_id": 860197,
  "person_ids": [38708, 24809, 89203, 97304],
  "associated_person_ids": [38708, 24809],
  "interaction_person_ids": [89203, 97304],
  "interaction_id": 114,
  "interaction_type": 0,
  "is_meeting": true,
  "mentioned_person_ids": [49817, 78624],
  "organization_ids": [64779194],
  "opportunity_ids": [117],
  "parent_id": null,
  "content": "Had a lunch meeting with Jane and John today. They are looking to invest.",
  "type": 0,
  "created_at": "2017-03-28T00:38:41.275-08:00",
  "updated_at": "2017-04-03T00:22:25.612-08:00"
}
```
## Get All Notes

`GET /notes`

Returns all notes attached to a `person`, `organization`, `opportunity`.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| person_id | integer | false | A unique identifier that represents a Person that was either directly attached to the retrieved notes or attended an interaction that the retrieved notes were taken on. |
| organization_id | integer | false | A unique identifier that represents an Organization that was directly attached to the retrieved notes. |
| opportunity_id | integer | false | A unique identifier that represents an Opportunity that was directly attached to retrieved notes. |
| creator_id | integer | false | A unique identifier that represents an Affinity user whose created notes should be retrieved. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Returns

An array of all the note resources available to you.

#### Example Request

```bash
curl "https://api.affinity.co/notes" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 22984,
    "creator_id": 860197,
    "person_ids": [38706,89734],
    "is_meeting": false,
    "mentioned_person_ids": [49817, 78624],
    "organization_ids": [64779194],
    "opportunity_ids": [117],
    "parent_id":  null,
    "content": "Had a lunch meeting with Jane ... ",
    "type": 0,
    "created_at": "2017-03-28T00:38:41.275-08:00",
    "updated_at": "2017-04-03T00:22:25.612-08:00"
  },
  {
    "id": 22983,
    "creator_id": 860196,
    "person_ids": [],
    "is_meeting": false,
    "mentioned_person_ids": [7237],
    "organization_ids": [64779194],
    "opportunity_ids": [115],
    "parent_id":  null,
    "content": "Had a **lunch meeting** @ Google ... ",
    "type": 2,
    "created_at": "2017-03-28T00:38:41.275-08:00",
    "updated_at": null
  },
  ...
]
```
## Get a Specific Note

#### Example Request

```bash
# Returns the note with the specified `note_id`
curl "https://api.affinity.co/notes/22984" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 22984,
  "creator_id": 860197,
  "person_ids": [38708, 24809, 89203, 97304],
  "associated_person_ids": [38708, 24809],
  "interaction_person_ids": [89203, 97304],
  "interaction_id": 114,
  "interaction_type": 0,
  "is_meeting": true,
  "mentioned_person_ids": [49817, 78624],
  "organization_ids": [64779194],
  "opportunity_ids": [117],
  "parent_id":  null,
  "content": "Had a lunch meeting with Jane ... ",
  "type": 0,
  "created_at": "2017-03-28T00:38:41.275-08:00",
  "updated_at": "2017-04-03T00:22:25.612-08:00",
},
```

`GET /notes/{note_id}`

Gets the details for a specific note given the existing note id.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| note_id | integer | true | The unique identifier of the note object to be retrieved. |

#### Returns

The details of the note resource corresponding to the note ID specified in the path parameter. An appropriate error is returned if an invalid note is supplied.

## Create a New Note

> Example Request (JSON)

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "content": "Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."}'
```

> Example Request (Form)

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&content=Had a lunch meeting with Jane and John today. They want to invest in Acme Corp."
```

#### Example Response

```json
{
  "id": 22985,
  "creator_id": 860197,
  "person_ids": [38708, 24809, 89203, 97304],
  "associated_person_ids": [38708, 24809],
  "interaction_person_ids": [89203, 97304],
  "interaction_id": 114,
  "interaction_type": 0,
  "is_meeting": true,
  "mentioned_person_ids": [],
  "organization_ids": [64779194],
  "opportunity_ids": [117],
  "parent_id": null,
  "content": "Had a lunch meeting with Jane ... ",
  "type": 0,
  "created_at": "2017-03-28T00:38:41.275-08:00",
  "updated_at": null
}
```

> Example Request Creating An HTML-Type Note (JSON)

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [38706, 624289], "organization_ids": [120611418], "opportunity_ids": [167], "type": 2, "content": "Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."}'
```

> Example Request Creating An HTML-Type Note (Form)

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "person_ids[]=38706&person_ids[]=624289&organization_ids[]=120611418&opportunity_ids[]=167&type=2&content=Had a <strong>lunch meeting<strong> with Jane and John today. They want to invest in Acme Corp."
```

#### Example Response

```json
{
  "id": 22986,
  "creator_id": 860197,
  "person_ids": [38708, 24809, 89203, 97304],
  "associated_person_ids": [38708, 24809],
  "interaction_person_ids": [89203, 97304],
  "interaction_id": 114,
  "interaction_type": 0,
  "is_meeting": true,
  "mentioned_person_ids": [],
  "organization_ids": [64779194],
  "opportunity_ids": [117],
  "parent_id": null,
  "content": "Had a **lunch meeting** with Jane ... ",
  "type": 2,
  "created_at": "2017-03-28T00:38:41.275-08:00",
  "updated_at": null
}
```

> Example Request with parent_id

```bash
curl -X POST "https://api.affinity.co/notes" \
  -u :$APIKEY \
  -H "Content-Type: application/json" \
  -d '{"person_ids": [38706], "organization_ids": [120611418], "parent_id": 22984, "content": "This is a <strong> reply </strong>to the previous note.", "type":2}'
```

#### Example Response

```json
{
  "id": 22987,
  "creator_id": 860197,
  "person_ids": [],
  "associated_person_ids": [],
  "interaction_person_ids": [],
  "interaction_id": null,
  "interaction_type": null,
  "is_meeting": false,
  "mentioned_person_ids": [],
  "organization_ids": [],
  "opportunity_ids": [],
  "parent_id": 22984,
  "content": "This is a reply to the previous note. Because a parent_id was supplied, the supplied person_ids, organization_ids, and opportunity_ids were ignored.",
  "type": 2,
  "created_at": "2017-03-29T00:38:41.275-08:00",
  "updated_at": null
}
```

`POST /notes`

Creates a new note with the supplied parameters.

Set the `type` parameter to 2 to create an HTML note. See [here](https://support.affinity.co/hc/en-us/articles/360016292631-Rich-text-formatting-for-notes-within-Affinity) for more information on the sorts of rich text formatting we support in notes. Please note that `<a>` tags aren't currently clickable inside the Affinity web app -- though full links are.

It is possible to create a **reply** to an existing note by setting `parent_id`. The parent note should not have a `parent_id` itself. It is possible for a single parent note to have multiple reply notes -- They just get displayed in order of creation. `opportunity_ids`, `person_ids`, and `organization_ids` will be ignored when a `parent_id` is provided.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| content | string | true | The string containing the content of the new note. See [formatting options](#formatting-content-as-html) for HTML support. |
| person_ids | integer[] | custom* | An array of unique identifiers of person objects that are associated with the new note. |
| organization_ids | integer[] | custom* | An array of unique identifiers of organization objects that are associated with the new note. |
| opportunity_ids | integer[] | custom* | An array of unique identifiers of opportunity objects that are associated with the new note. |
| type | integer | false | The type of the new note. Defaults to 0. The types 0 and 2 represent plain text and HTML notes, respectively. If submitting as HTML, see the [formatting options](#formatting-content-as-html). |
| parent_id | integer | custom* | The unique identifier of the note to which the newly created note should reply. See comments above. |
| creator_id | integer | false | The ID of a Person resource who should be recorded as the author of the note. Must be a person who can access Affinity. If not provided the creator defaults to the owner of the API key. |
| created_at | datetime | false | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the creation time to be recorded for the note. If not provided, defaults to the current time. Does not support times in the future. |

#### Returns

The note resource created through this request.

#### Note

> At least one `person_id`, `organization_id`, `opportunity_id`, or `parent_id` must be specified to the endpoint.

#### Note

> When creating a note using the API, the user corresponding to the API token will be the creator by default.

#### Note

> To ensure that `content` gets encoded properly, it is recommended to submit as either `application/json` or `application/x-www-form-urlencoded` instead of query parameters.

## Update a Note

`PUT /notes/{notes_id}`

Updates the content of an existing note with `note_id` with the supplied `content` parameter.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| note_id | integer | true | The unique ID of the note that needs to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| content | string | true | The new content of the note. |

#### Returns

The note object that was just updated through this request.

#### Note

> You cannot update the content of a note that has mentions. You also cannot update the content of a note associated with an email. You cannot update the type of a note.

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
  "id": 22984,
  "creator_id": 860197,
  "person_ids": [38708, 24809, 89203, 97304],
  "associated_person_ids": [38708, 24809],
  "interaction_person_ids": [89203, 97304],
  "interaction_id": 114,
  "interaction_type": 0,
  "is_meeting": true,
  "mentioned_person_ids": [49817, 78624],
  "organization_ids": [64779194],
  "opportunity_ids": [117],
  "parent_id": null,
  "content": "Had another meeting with Jane ... ",
  "type": 0,
  "created_at": "2017-03-28T00:38:41.275-08:00",
  "updated_at": "2017-04-03T00:22:25.612-08:00"
}
```
## Delete a Note

`DELETE /notes/{note_id}`

Deletes a note with a specified `note_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| note_id | integer | true | The unique ID of the note that needs to be deleted. |

#### Returns

`{success: true}`.

#### Note

> An appropriate error will be returned if you are not the creator of the note you are trying to delete.

#### Example Request

```bash
curl "https://api.affinity.co/notes/22984" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Entity Files

Entity files are files uploaded to a relevant entity. Possible files, for example, would be a pitch deck for an opportunity or a physical mail correspondence for a person.

## The Entity File Resource

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the entity file object. |
| name | string | The name of the file. |
| size | string | The size of the file in bytes. |
| person_id | integer | The unique identifier of the person corresponding to the entity file. |
| organization_id | integer | The unique identifier of the organization corresponding to the entity file. |
| opportunity_id | integer | The unique identifier of the opportunity corresponding to the entity file. |
| uploader_id | integer | The unique identifier of the user who created the entity file. |
| created_at | datetime | The time when the entity file was created. |

#### Example Response

```json
{
  "id": 43212,
  "name": "JohnDoeFriends.csv",
  "size": 993,
  "person_id": 10,
  "organization_id": null,
  "opportunity_id": null,
  "created_at": "2011-01-25T09:59:35.288-08:00",
  "uploader_id": 10
}
```
## Get All Files

> Example pagination

```bash

#### Example Request

```bash
curl "https://api.affinity.co/entity-files" -u :$APIKEY
```

#### Example Response

```json
{
    "entity_files": [
        {
            "id": 43212,
            "name": "JohnDoeFriends.csv",
            "size": 993,
            "person_id": 142,
            "organization_id": null,
            "opportunity_id": null,
            "created_at": "2011-01-25T09:59:35.288-08:00",
            "uploader_id": 10
        },
        {
            "id": 131,
            "name": "Import.csv",
            "size": 227224,
            "person_id": 38654,
            "organization_id": null,
            "opportunity_id": null,
            "created_at": "2019-01-13T12:52:51.539-08:00",
            "uploader_id": 101
        },
        ...
    ],
    "next_page_token": "eyJwYXJhbXMiOnt9LCJwYWdlX3NpemUiOjUwMCwib2Zmc2V0Ijo1MDB9",
}
```
# To get the second page of results, issue the following query:
curl "https://api.affinity.co/entity-files?page_token=eyJwYXJhbXMiOnsidGVybSI6IiJ9LCJwYWdlX3NpemUiOjUsIm9mZnNldCI6MTB9" -u :$APIKEY
```

`GET /entity-files`

Returns all entity files within your organization. This result will be an object with two fields: `entity_files` and `next_page_token`. `entity_files` maps to an array of all the entity file resources. The value of `next_page_token` should be sent as the query parameter `page_token` in another request to retrieve the next page of results. While paginating through results, each request must have identical query parameters other than the changing `page_token`. Otherwise, an `Invalid page_token variable` error will be returned.

The absence of a `next_page_token` indicates that all the records have been fetched, though its presence does not necessarily indicate that there are *more* resources to be fetched. The next page may be empty (but then `next_page_token` would be `null` to confirm that there are no more resources).

Can optionally be filtered to return only entity files associated with a specific `person`, `organization`, or `opportunity`.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |
| person_id | integer | false | A unique ID that represents a Person whose associated files should be retrieved. |
| organization_id | integer | false | A unique ID that represents an Organization whose associated files should be retrieved. |
| opportunity_id | integer | false | A unique ID that represents an Opportunity whose associated files should be retrieved. |

#### Returns

An object with two fields: `entity_files` and `next_page_token`. `entity_files` maps to an array of all the entity file resources. See description for more details on pagination.

## Get a Specific File

`GET /entity-files/{entity_file_id}`

Fetches an entity with a specified `entity_file_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| entity_file_id | integer | true | The unique ID of the entity file that needs to be retrieved. |

#### Returns

The entity file resource corresponding to the `entity_file_id`.

#### Example Request

```bash
curl "https://api.affinity.co/entity-files/43212" -u :$APIKEY
```

#### Example Response

```json
{
  "id": 43212,
  "name": "GoogleFriends.csv",
  "size": 993,
  "person_id": null,
  "organization_id": 10,
  "opportunity_id": null,
  "created_at": "2011-01-25T09:59:35.288-08:00",
  "uploader_id": 10
}
```
## Download File

`GET /entity-files/download/{entity_file_id}`

Downloads an entity file with a specified `entity_file_id`

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| entity_file_id | integer | true | The unique ID of the entity file that needs to be downloaded. |

#### Returns

The actual entity file corresponding to the `entity_file_id`.

#### Notes

> The download location of entity files is provided via a redirect from our endpoint and requires the `-L` flag.

#### Example Request

```bash
curl "https://api.affinity.co/entity-files/download/12345" \
  -u :$APIKEY \
  -L \
  -o Downloads/file.png
```
## Upload Files

#### Example Request

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

#### Example Response

```json
{ "success": true }
```

`POST /entity-files`

Uploads files attached to the entity with the given id.

The file will display on the entity's profile, provided that the entity is not a person internal to the user's organization.

### Form Data Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| file | File | false | A singular file to be uploaded, formatted as form data (multipart/form-data). |
| files | File[] | false | An array of files to be uploaded, formatted as form data (multipart/form-data). |
| person_id | integer | false | The unique identifier of the person object to attach the file(s) to. |
| organization_id | integer | false | The unique identifier of the organization object to attach the file(s) to. |
| opportunity_id | integer | false | The unique identifier of the opportunity object to attach the file(s) to. |

#### Returns

`{"success": true}`

#### Notes

> - Files must be attached to a single entity, specified using one of the three entity ID parameters (`person_id`, `organization_id`, and `opportunity_id`).
> - At least one file must be uploaded using the `file` or `files` parameters.

# Reminders

The reminders API allows you to manage reminders.

## The Reminder Resource

A reminder object contains `content`, which is a string containing the reminder content. In addition, a person, organization or opportunity can be tagged to the reminder.

#### Example Response

```json
{
    "id": 15326,
    "type": 1,
    "created_at": "2021-11-18T14:34:53.218-08:00",
    "completed_at": null,
    "content": "Reply email to Alice",
    "due_date": "2021-12-18T14:34:53.217-08:00",
    "reset_type": 1,
    "reminder_days": 30,
    "status": 2,
    "creator": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "owner": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "completer": null,
    "person": {
        "id": 2021,
        "type": 0,
        "first_name": "Alice",
        "last_name": "Yen",
        "primary_email": "yen@alice.com",
        "emails": [
            "yen@alice.com"
        ]
    },
    "organization": null,
    "opportunity": null
}
```

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the reminder object. |
| creator | object | The person object who created the reminder. |
| person | object | The person object tagged in the reminder. |
| organization | object | The organization object tagged in the reminder. |
| opportunity | object | The opportunity object tagged in the reminder. |
| owner | object | The person object who was assigned to the reminder. |
| completer | object | The person object who completed the reminder. |
| type | integer | The type of reminder. |
| reset_type | integer | The reset type of the recurring reminder. |
| status | integer | Current status of the reminder. |
| created_at | datetime | The time when the reminder was created. |
| content | string | The string containing the content of the reminder. |
| due_date | datetime | The due date of the reminder. |
| completed_at | datetime | The time when the reminder was completed. |
| reminder_days | integer | When a recurring reminder is completed or reset, the number of days before the reminder is due again. |

### Reminder Types

| Type | Value | Description |
| --- | --- | --- |
| One-time | 0 | Type specifying a one time reminder. |
| Recurring | 1 | Type specifying a recurring reminder. |

### Reminder Reset Types

| Type | Value | Description |
| --- | --- | --- |
| Interaction | 0 | Recurring reminder that can be reset by email or meeting. |
| Email | 1 | Recurring reminder that can be reset by an email. |
| Meeting | 2 | Recurring reminder that can be reset by a meeting. |

### Reminder Status Types

| Type | Value | Description |
| --- | --- | --- |
| Completed | 0 | Reminder that has been marked as completed. |
| Active | 1 | Reminder that has not been completed and is not past due. |
| Overdue | 2 | Reminder that has not been completed and is past due. |

## Get All Reminders

`GET /reminders`

Returns all reminders that meet the query parameters.

### Query Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| person_id | integer | false | A unique identifier that represents a Person that was directly attached to the retrieved reminders. |
| organization_id | integer | false | A unique identifier that represents an Organization that was directly attached to the retrieved reminders. |
| opportunity_id | integer | false | A unique identifier that represents an Opportunity that was directly attached to the retrieved reminders. |
| creator_id | integer | false | A unique identifier that represents an internal person whose created reminders should be retrieved. |
| owner_id | integer | false | A unique identifier that represents an internal person that was assigned to the retrieved reminders. |
| completer_id | integer | false | A unique identifier that represents an internal person whose completed reminders should be retrieved. |
| type | integer | false | The type of reminders to be retrieved. |
| reset_type | integer | false | The reset type of reminders to be retrieved. Required when `type == 1`. |
| status | integer | false | The status of reminders to be retrieved. |
| due_before | string | false | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the date that reminders to be retrieved are due before. |
| due_after | string | false | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the date that reminders to be retrieved are due after. |
| page_size | number | false | How many results to return per page. (Default is the maximum value of 500.) |
| page_token | string | false | The `next_page_token` from the previous response required to retrieve the next page of results. |

#### Returns

An array of all the reminders filtered by query parameters. `next_page_token` includes a token to be sent along with the next request as the `page_token` parameter to fetch the next page of results.

#### Example Request

```bash
curl "https://api.affinity.co/reminders?page_size=2&status=2" -u :$APIKEY
```

#### Example Response

```json
{
    "reminders": [
        {
            "id": 15562,
            "type": 1,
            "created_at": "2021-11-22T09:31:52.415-08:00",
            "completed_at": null,
            "content": "Recurring reminder",
            "due_date": "2021-12-22T09:31:52.415-08:00",
            "reset_type": 0,
            "reminder_days": 30,
            "status": 2,
            "creator": {
                "id": 443,
                "type": 1,
                "first_name": "John",
                "last_name": "Doe",
                "primary_email": "john@affinity.co",
                "emails": [
                    "john@affinity.co"
                ]
            },
            "owner": {
                "id": 443,
                "type": 1,
                "first_name": "John",
                "last_name": "Doe",
                "primary_email": "john@affinity.co",
                "emails": [
                    "john@affinity.co"
                ]
            },
            "completer": null,
            "person": null,
            "organization": {
                "id": 4904,
                "name": "organization",
                "domain": null,
                "domains": [],
                "crunchbase_uuid": null,
                "global": false
            },
            "opportunity": null
        },
        {
            "id": 15326,
            "type": 1,
            "created_at": "2021-11-18T14:34:53.218-08:00",
            "completed_at": null,
            "content": "Reply email to Alice",
            "due_date": "2021-12-18T14:34:53.217-08:00",
            "reset_type": 1,
            "reminder_days": 30,
            "status": 2,
            "creator": {
                "id": 443,
                "type": 1,
                "first_name": "John",
                "last_name": "Doe",
                "primary_email": "john@affinity.co",
                "emails": [
                    "john@affinity.co"
                ]
            },
            "owner": {
                "id": 443,
                "type": 1,
                "first_name": "John",
                "last_name": "Doe",
                "primary_email": "john@affinity.co",
                "emails": [
                    "john@affinity.co"
                ]
            },
            "completer": null,
            "person": {
                "id": 2021,
                "type": 0,
                "first_name": "Alice",
                "last_name": "Yen",
                "primary_email": "yen@alice.com",
                "emails": [
                    "yen@alice.com"
                ]
            },
            "organization": null,
            "opportunity": null
        }
    ],
    "next_page_token": "eyJwYXJhbXMiOnsiY29tcGxldGVyX2lkIjpudWxsLCJvd25lcl9pZCI6bnVsbCwiY3JlYXRvcl9"
}
```
## Get a Specific Reminder

#### Example Request

```bash
# Returns the reminder with the specified `reminder_id`
curl "https://api.affinity.co/reminders/15326" -u :$APIKEY
```

#### Example Response

```json
{
    "id": 15326,
    "type": 1,
    "created_at": "2021-11-18T14:34:53.218-08:00",
    "completed_at": null,
    "content": "Reply email to Alice",
    "due_date": "2021-12-18T14:34:53.217-08:00",
    "reset_type": 1,
    "reminder_days": 30,
    "status": 2,
    "creator": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "owner": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "completer": null,
    "person": {
        "id": 2021,
        "type": 0,
        "first_name": "Alice",
        "last_name": "Yen",
        "primary_email": "yen@alice.com",
        "emails": [
            "yen@alice.com"
        ]
    },
    "organization": null,
    "opportunity": null
}
```

`GET /reminders/{reminder_id}`

Gets the details for a specific reminder given the existing reminder id.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| reminder_id | integer | true | The unique identifier of the reminder object to be retrieved. |

#### Returns

The details of the reminder corresponding to the reminder ID specified in the path parameter. An appropriate error is returned if an invalid reminder ID is supplied.

## Create a New Reminder

`POST /reminders`

Creates a new reminder with the supplied parameters.

### Body Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| owner_id | integer | true | A unique identifier that represents an internal person that is assigned to the reminder. |
| content | string | false | The string containing the content of the new reminder. |
| type | integer | true | The type of reminder to be created. |
| reset_type | integer | false | The reset type of reminder to be created. Required when `type == 1`. |
| person_id | integer | false | A unique identifier that represents a Person that is tagged in the reminder to be created. |
| organization_id | integer | false | A unique identifier that represents an Organization that is tagged in the reminder to be created. |
| opportunity_id | integer | false | A unique identifier that represents an Opportunity that is tagged in the reminder to be created. |
| due_date | string | false | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the due date of the reminder to be created. Required when `type == 0`. |
| reminder_days | integer | false | When a recurring reminder is completed or reset, the number of days before the reminder is due again. Required when `type == 1`. |
| is_completed | integer | false | Indicator if the reminder has been completed. |

Note that at most one of `person_id`, `organization_id` or `opportunity_id` can be specified.

One-time reminders (`type = 0`) require a `due_date`. Recurring reminders (`type = 1`) require `reset_type` and `reminder_days`.

#### Returns

The reminder created through this request.

#### Note

> When creating a reminder using the API, the user corresponding to the API token will be the creator by default.

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
    "id": 15385,
    "type": 0,
    "created_at": "2022-02-01T09:36:07.316-08:00",
    "completed_at": null,
    "content": "Create reminder from external API",
    "due_date": "2021-11-30T00:00:00.000-08:00",
    "reset_type": null,
    "reminder_days": null,
    "status": 2,
    "creator": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "owner": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "completer": null,
    "person": {
        "id": 2021,
        "type": 0,
        "first_name": "Alice",
        "last_name": "Yen",
        "primary_email": "yen@alice.com",
        "emails": [
            "yen@alice.com"
        ]
    },
    "organization": null,
    "opportunity": null
}
```
## Update a Reminder

`PUT /reminders/{reminder_id}`

Updates the content of an existing reminder with `reminder_id` with the supplied parameters.

### Body Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| reminder_id | integer | true | The unique ID of the reminder to be updated. |

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| owner_id | integer | false | A unique identifier that represents an internal person that is assigned to the reminder. |
| content | string | false | The string containing the content of the new reminder. |
| type | integer | false | The type of reminder to be updated. |
| reset_type | integer | false | The reset type of reminder to be updated. Required when `type == 1`. |
| due_date | string | false | A string (formatted according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)) representing the due date of the reminder to be updated. Required when `type == 0`. |
| reminder_days | integer | false | When a recurring reminder is completed or reset, the number of days before the reminder is due again. Required when `type == 1`. |
| is_completed | integer | false | Indicator if the reminder has been completed. |

#### Returns

The reminder object that was just updated through this request.

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
    "id": 15385,
    "type": 1,
    "created_at": "2022-02-01T09:36:07.316-08:00",
    "completed_at": null,
    "content": "Create reminder from external API",
    "due_date": "2021-11-30T00:00:00.000-08:00",
    "reset_type": 0,
    "reminder_days": 70,
    "status": 2,
    "creator": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "owner": {
        "id": 443,
        "type": 1,
        "first_name": "John",
        "last_name": "Doe",
        "primary_email": "john@affinity.co",
        "emails": [
            "john@affinity.co"
        ]
    },
    "completer": null,
    "person": {
        "id": 2021,
        "type": 0,
        "first_name": "Alice",
        "last_name": "Yen",
        "primary_email": "yen@alice.com",
        "emails": [
            "yen@alice.com"
        ]
    },
    "organization": null,
    "opportunity": null
}
```
## Delete a Reminder

`DELETE /reminders/{reminder_id}`

Deletes the reminder with the specified `reminder_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| reminder_id | integer | true | The unique ID of the reminder to be deleted. |

#### Returns

`{success: true}`.

#### Example Request

```bash
curl "https://api.affinity.co/reminders/22984" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Webhooks

Webhooks allow you to be notified of events that happen on your Affinity instance. For example, your app can be notified when a list is created, a field value is updated, a person is deleted, and more. These events will fire immediately after the corresponding action takes place.

## The Webhook Subscription Resource

Each webhook subscription object has a unique `id`. It also has a `webhook_url` and `subscriptions` associated with it.

| Attribute | Type | Description |
| --- | --- | --- |
| id | integer | The unique identifier of the webhook subscription object. |
| webhook_url | string | The URL to which the webhooks are sent to. |
| subscriptions | string[] | An array of webhook events that are enabled for that endpoint. An empty array indicates subscription to all webhook events. See [below](#supported-webhook-events) for the complete list of supported webhook events. |
| disabled | boolean | If the subscription is disabled, this is true. Otherwise, this is false by default. A subscription may be disabled manually via API or automatically if we are not able to process it. |
| created_by | integer | The unique identifier of the user who created the webhook subscription. |

#### Note

> If webhooks cannot be delivered as the result of a timeout or a connectivity issue with the webhook URL, Affinity will retry the delivery with an exponential backoff for up to 10 hours. If Affinity is still unable to deliver webhooks at that point, the webhook subscription will be disabled and an email notification will be sent to the Affinity admin and technical contacts.

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
## Supported Webhook Events

> Example Responses

```json
{
  "type": "list_entry.created",
  "body": {
    "id": 388,
    "list_id": 26,
    "creator_id": 38603,
    "entity_id": 38706,
    "entity_type": 0,
    "created_at": "2021-09-08T09:55:50.321-07:00",
    "entity": {
      "id": 70796737,
      "type": 0,
      "first_name": "John",
      "last_name": "Doe",
      "primary_email": "john@affinity.co",
      "emails": ["john@affinity.co"]
    }
  },
  "sent_at": 1631120151
}
```

| Object Type | Events |
| --- | --- |
| List | `list.created`, `list.updated`, `list.deleted` |
| List Entry | `list_entry.created`, `list_entry.deleted` |
| Note | `note.created`, `note.updated`, `note.deleted` |
| Field | `field.created`, `field.updated`, `field.deleted` |
| Field Value | `field_value.created`, `field_value.updated`, `field_value.deleted` |
| Person | `person.created`, `person.updated`, `person.deleted` |
| Organization | `organization.created`, `organization.updated`, `organization.deleted`, `organization.merged` |
| Opportunity | `opportunity.created`, `opportunity.updated`, `opportunity.deleted` |
| Entity File | `file.created`, `file.deleted` |
| Reminder | `reminder.created`, `reminder.updated`, `reminder.deleted` |

#### Note

> - The Field Value webhook events do not include enrichment events; updates to enrichment field values are not supported.
> - Examples of our webhook responses can be found in the [Help Center](https://support.affinity.co/s/article/Types-of-webhooks-available-with-Affinity-s-API).
> - Field webhooks are not fired for Crunchbase fields.
> - Field value webhooks are fired with `null` values for Crunchbase fields.

## Get All Webhook Subscriptions

`GET /webhook`

Returns all of your organization's webhook subscriptions.

#### Example Request

```bash
curl "https://api.affinity.co/webhook" -u :$APIKEY
```

#### Example Response

```json
[
  {
    "id": 1234,
    "webhook_url": "https://hooks.example.com/webhook-create",
    "subscriptions": [
      "list.created",
      "person.created",
      "organization.created",
      "opportunity.created"
    ],
    "disabled": false,
    "created_by": 5678
  },
  {
    "id": 2345,
    "webhook_url": "https://hooks.example.com/webhook-all",
    "subscriptions": [],
    "disabled": true,
    "created_by": 5678
  }
]
```
## Get a Specific Webhook Subscription

`GET /webhook/{webhook_subscription_id}`

Gets the details for a specific webhook subscription given the specified `webhook_subscription_id`.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| webhook_subscription_id | integer | true | The unique ID of the webhook subscription that needs to be retrieved. |

#### Returns

The webhook subscription object corresponding to the `webhook_subscription_id`.

#### Example Request

```bash
curl "https://api.affinity.co/webhook/1234" -u :$APIKEY
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
## Create a New Webhook Subscription

`POST /webhook/subscribe`

Creates a new webhook subscription with the supplied parameters. If the endpoint returns an invalid response, the webhook creation will fail.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| webhook_url | string | true | The URL to which the webhooks will be sent to. |
| subscriptions | string[] | false | An array of webhook events that will be enabled for that endpoint. Leave out this parameter or pass an empty array to subscribe to all webhook events. You can find the complete list of supported webhook events [here](#supported-webhook-events). |

#### Returns

The webhook subscription object that was just created from this successful request per organization.

#### Note

> There is a limit of three webhook subscriptions per Affinity instance.

#### Example Request

```bash
curl -X POST "https://api.affinity.co/webhook/subscribe" \
  -u :$APIKEY \
  -d webhook_url="https://hooks.example.com/webhook"
```

#### Example Response

```json
{
  "id": 1234,
  "webhook_url": "https://hooks.example.com/webhook",
  "subscriptions": [],
  "disabled": false,
  "created_by": 5678
}
```
## Update a Webhook Subscription

`PUT /webhook/{webhook_subscription_id}`

Update webhook subscription with the supplied parameters. A webhook subscription can only be updated by its creator. If the endpoint returns an invalid response, the webhook update will fail.

### Payload Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| webhook_url | string | false | The URL to which the webhooks will be sent to. |
| subscriptions | string[] | false | An array of webhook events that will be enabled for that endpoint. Leave out this parameter or pass an empty array to subscribe to all webhook events. You can find the complete list of supported webhook events [here](#supported-webhook-events). |
| disabled | boolean | false | Change the status of a subscription. To enable a subscription, provide the value as `false`. Otherwise, provide the value as `true.` |

#### Returns

The webhook subscription object that was just updated from this successful request.

#### Example Request

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -d webhook_url="https://hooks.example.com/webhook" \
  -d disabled=true \
  -X "PUT"
```

#### Example Response

```json
{
  "id": 1234,
  "webhook_url": "https://hooks.example.com/webhook",
  "subscriptions": [],
  "disabled": true,
  "created_by": 5678
}
```
## Delete a Specific Webhook Subscription

`DELETE /webhook/{webhook_subscription_id}`

Deletes a webhook subscription with a specified `webhook_subscription_id`. A webhook subscription can only be deleted by its creator, or an admin.

### Path Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| webhook_subscription_id | integer | true | The unique ID of the webhook subscription that needs to be deleted. |

#### Returns

`{success: true}`.

#### Example Request

```bash
curl "https://api.affinity.co/webhook/1234" \
  -u :$APIKEY \
  -X "DELETE"
```

#### Example Response

```json
{ "success": true }
```
# Whoami

The Whoami API gives the user metadata about the user's authentication and Affinity instance information, including the instance subdomain. This can be used for linking back to the user's Affinity instance.

#### Example Request

```bash
# Returns the authenticated user.
curl "https://api.affinity.co/auth/whoami" -u :$APIKEY
```

## The Whoami Resource

Querying the Whoami endpoint will give information about the user, Affinity instance, and authentication method.

#### Example Response

```json
{
    "tenant": {
        "id": 1,
        "name": "Affinity",
        "subdomain": "affinity"
    },
    "user": {
        "id": 2,
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@affinity.co"
    },
    "grant": {
        "type": "api_key",
        "scope": "external_api",
        "createdAt": "2020-12-14T09:00:00.000-05:00"
    }
}
```

| Attribute | Type | Description |
| --- | --- | --- |
| tenant | object | Information about the Affinity instance the user belongs to. |
| user | object | Data about the user whose api key was used for the endpoint. |
| grant | object | Data about the type of authentication and metadata about the api key. |

## Get Whoami

`GET /auth/whoami`

Gets information about the user sending the request, and their affiliate company.

There are no query or path parameters for this method. The information needed is contained within the API key.

#### Returns

JSON body of data including tenant, user, and grant information.

#### Example Request

```bash
curl "https://api.affinity.co/auth/whoami" -u :$API_KEY
```

#### Example Response

```json
{
    "tenant": {
        "id": 1,
        "name": "Affinity",
        "subdomain": "affinity"
    },
    "user": {
        "id": 2,
        "firstName": "John",
        "lastName": "Doe",
        "email": "john@affinity.co"
    },
    "grant": {
        "type": "api_key",
        "scope": "external_api",
        "createdAt": "2020-12-14T09:00:00.000-05:00"
    }
}
```
# Rate Limit

The rate limit endpoint allows you to see your monthly account-level and per minute user-level API limits and usage. The monthly account-level call limit resets at the end of each calendar month.

#### Example Request

```bash
# Returns the current rate limit status.
curl "https://api.affinity.co/rate-limit" -u :$APIKEY
```

## The Rate Limit Resource

The rate limit resource includes information about account (AKA organization)-level and API key-level rate limits and usage.

#### Example Response

```json
{
    "rate": {
        "org_monthly": {
            "limit": 40000,
            "remaining": 39993,
            "reset": 2124845,
            "used": 7
        },
        "api_key_per_minute": {
            "limit": 900,
            "remaining": 900,
            "reset": 0,
            "used": 0
        }
    }
}
```

| Attribute | Type | Description |
| --- | --- | --- |
| rate | object | Type of rate limit. |
| org_monthly | object | Monthly rate limit per organization. |
| api_key_per_minute | object | Per minute rate limit per API key. |
| limit | integer | The maximum number of calls for each period. |
| remaining | integer | The number of calls remaining before reset. |
| reset | integer | Time in seconds until call count resets. |
| used | integer | The number of calls that have been used. |

#### Note

> - `/rate-limit` and `/auth/whoami` endpoints are exempt from organization-level monthly rate limits.

## Get Rate Limit Information

`GET /rate-limit`

Querying the rate limit endpoint will yield information about account (AKA organization)-level and API key-level rate limits and usage.

#### Returns

The rate limit resource, a JSON body of data including limits, calls remaining, seconds until reset and call count.

#### Example Request

```bash
curl "https://api.affinity.co/rate-limit" -u :$API_KEY
```

#### Example Response

```json
{
    "rate": {
        "org_monthly": {
            "limit": 40000,
            "remaining": 39993,
            "reset": 2124845,
            "used": 7
        },
        "api_key_per_minute": {
            "limit": 900,
            "remaining": 900,
            "reset": 0,
            "used": 0
        }
    }
}
```
# Changelog

**2025-11-05**

- Added support for bearer authentication

**2024-07-17**

- At least one associated person, company, opportunity, or parent note must be specified when
  [creating a note](#create-a-new-note)
  .

**2024-05-01**

- `/interactions`
  now restricts the duration between
  `start_time`
  and
  `end_time`
  to a maximum of one year
- `/interactions`
  now ensures that the provided
  `start_time`
  is before the provided
  `end_time`
  year
- `/interactions`
  now has a maximum
  `page_size`
  of 100.

**2023-08-07**

- Added
  `associated_person_ids`
  ,
  `interaction_person_ids`
  ,
  `interaction_id`
  , and
  `interaction_type`
  to
  [the note resource](#the-note-resource)
  . The
  `person_ids`
  ,
  `associated_person_ids`
  , and
  `interaction_person_ids`
  properties on a note should now reflect the various ways a note can be tied to a person.

**2023-07-27**

- datetime values in webhook bodies and API responses are ISO 8601-formatted date strings. For example:
  `"2023-06-21T16:00:28.315-07:00"`
  .

**2023-07-17**

- Add information about
  [notes with `type` 1](#the-note-resource)
  .

**2023-07-03**

- Updated API access information for Professional tier customers.

**2023-06-13**

- The
  `created_at`
  parameter on the
  [POST endpoint for notes](#create-a-new-note)
  no longer accepts timestamps in the future.

**2023-05-17**

- Added
  [403 error code](#requests-amp-responses)
  for permissions-related errors.

**2023-03-27**

- Added the ability to
  [create a List](#create-a-new-list)
  .
- Updated
  [Postman collection](#useful-resources)
  to help developers get started.
- Added
  [documentation](#formatting-content-as-html)
  on formatting options for HTML notes.

**2023-03-09**

- Account for chat messages when returning interaction info on the GET endpoints for
  [Persons](#persons)
  and
  [Organizations](#organizations)
  .

**2023-02-28**

- Added the ability to
  [create HTML notes](#create-a-new-note)
  .
- Added the ability to
  [create a note within a thread](#create-a-new-note)
  .

**2023-02-10**

- Added
  [Rate Limit Headers](#rate-limit-headers)
  section to the
  [Rate Limits](#rate-limits)
  documentation.

**2023-02-08**

- Added
  `created_at`
  and
  `updated_at`
  timestamps to
  [Field Values](#field-values)
  .
- Added an
  `updated_at`
  timestamp to
  [Notes](#notes)
  .

**2023-02-07**

- Added the ability to retrieve Current Organization column data on
  [Persons](#persons)
  .

**2022-09-06**

- Added
  [Rate Limit](#rate-limit)
  endpoint and documentation. Moved from a daily to a per minute per user limit. Monthly per account limits remain the same.

**2022-09-02**

- Added
  `entity_type`
  and
  `exclude_dropdown_options`
  documentation to
  [Fields](#fields)
  .

**2022-05-05**

- Added
  `enrichment_source`
  documentation to
  [Fields](#fields)
  .

**2022-04-11**

- Added
  [Partner With Us](#partner-with-us)
  section.

**2022-03-21**

- Added
  `opportunity_ids`
  fields to person and organization responses.

**2022-02-23**

- Added
  [Interactions API](#interactions)
  documentation.

**2022-02-17**

- Updated
  [GET entity files](#get-all-files)
  and entity file webhooks to exclude non-user uploaded files.

**2022-02-03**

- Added
  [Whoami API](#whoami)
  documentation.

**2022-02-01**

- Added
  [Reminder API](#reminders)
  documentation.
- Added
  [Reminder webhook](/#webhooks)
  events.

**2022-01-28**

- Added
  `organization.merged`
  event to
  [Webhooks](#webhooks)
  .
- Added
  `mentioned_person_ids`
  and
  `is_meeting`
  fields to
  [Notes](#notes)
  .

**2021-11-22**

- Added link out to
  [Help Center](https://support.affinity.co/s/article/Types-of-webhooks-available-with-Affinity-s-API)
  for webhook responses

**2021-11-19**

- Updated
  [GET field values changes](#get-field-values-changes)
  to be filterable by
  `action_type`
  ,
  `person`
  ,
  `organization`
  ,
  `opportunity`
  or
  `list_entry`
  by passing in the appropriate parameter.

**2021-10-15**

- Minor content updates

**2021-10-04**

- Updates to Example Responses.
- Responsive tweaks.

**2021-09-07**

- Revamped API documentation
  - Added
    [Common Use Cases](#common-use-cases)
    section.
  - Added
    [Rate Limits](#rate-limits)
    section.
  - Updates to
    `PUT`
    and
    `POST`
    cURL examples.

**2021-08-18**

- Fixed typo in the API docs where
  `entity_id`
  and
  `creator_id`
  was in path paramaters when they should be inside the payload parameters for
  [Create a New List Entry](#create-a-new-list-entry)
  .

**2021-07-28**

- Fixed typo in Relationship Strength section.

**2021-05-05**

- Updated API rate limit information.
