# Affinity API v2 Documentation (Auto-synced)

> **⚠️ IMPORTANT DISCLAIMER**
>
> **This is an UNOFFICIAL markdown copy of the Affinity API v2 documentation.** The official and authoritative documentation is maintained by Affinity at:
>
> **📚 Official Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)
>
> **Always refer to the official Affinity documentation for the most up-to-date and accurate information.**

---

## About This Document

This markdown version of the Affinity API v2 documentation was generated automatically to provide:

- **Better compatibility with AI coding assistants**
- **Offline access**
- **Text-based search**
- **Version control**
- **Direct raw access**

**Source:** Extracted from the live Affinity API documentation at https://developer.affinity.co/

> **Note:** The live site renders dynamic multi-language request/response samples in-browser. Because those snippets are generated at runtime and are not embedded in the OpenAPI payload, they cannot be mirrored here. Refer to https://developer.affinity.co/ for the full interactive samples.

**Documentation Version:** This copy is based on the official documentation as it appeared on **November 05, 2025 at 18:08:51 UTC** (Last updated: 11/05/2025 18:08:51 UTC).
**Snapshot:** `tmp/v2/developer_affinity_co.html`

> **⚠️ Use at Your Own Risk**
>
> While every effort is made to ensure accuracy, this is an unofficial copy and may contain errors or outdated information.

## Contact & Support

- **Affinity Support:** [support@affinity.co](mailto:support@affinity.co)
- **Official v2 Documentation:** [https://developer.affinity.co/](https://developer.affinity.co/)
- **Official v1 Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)

---

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Authentication](#authentication)
  - [Permissions](#permissions)
    - [Overall Requirements](#overall-requirements)
    - [Resource-Level Permissions](#resource-level-permissions)
    - [Endpoint-Level Permissions](#endpoint-level-permissions)
  - [Rate Limits](#rate-limits)
    - [Per-Minute Limits (User-Level)](#per-minute-limits-user-level)
    - [Concurrent Request Limits (Account-Level)](#concurrent-request-limits-account-level)
    - [Monthly Plan Tier Limits (Account-Level)](#monthly-plan-tier-limits-account-level)
    - [Rate Limit Headers](#rate-limit-headers)
  - [Pagination](#pagination)
  - [Filtering](#filtering)
    - [Rules](#rules)
    - [Grammar](#grammar)
      - [Simple Types](#simple-types)
      - [Collections (all types)](#collections-all-types)
  - [Error Codes](#error-codes)
  - [Beta Endpoints](#beta-endpoints)
- [Data Model](#data-model)
  - [The Basics](#the-basics)
  - [Working with Field Data](#working-with-field-data)
    - [Field Types and IDs](#field-types-and-ids)
    - [Field Value Types](#field-value-types)
    - [Retrieving Field Data](#retrieving-field-data)
    - [Specifying Desired Fields (Field Selection)](#specifying-desired-fields-field-selection)
    - [Saved Views](#saved-views)
    - [Partner Data Restrictions](#partner-data-restrictions)
  - [Nested Associations](#nested-associations)
- [User Guides](#user-guides)
  - [A Tour of Our GET Endpoints](#a-tour-of-our-get-endpoints)
- [Changelog](#changelog)
  - [September 25th, 2025](#september-25th-2025)
  - [July 30th, 2025](#july-30th-2025)
  - [May 14th, 2025](#may-14th-2025)
  - [April 9th, 2025](#april-9th-2025)
  - [March 31st, 2025](#march-31st-2025)
  - [February 28th, 2025](#february-28th-2025)
  - [January 17th, 2025](#january-17th-2025)
  - [January 15th, 2025](#january-15th-2025)
  - [December 3rd, 2024](#december-3rd-2024)
  - [September 25th, 2024](#september-25th-2024)
  - [August 5, 2024](#august-5-2024)
  - [July 24, 2024](#july-24-2024)
  - [March 25, 2024](#march-25-2024)
  - [January 4, 2023](#january-4-2023)
  - [December 12, 2023](#december-12-2023)
  - [auth](#auth)
    - [Get current user](#get-current-user)
      - [Example Request](#example-request)
      - [Responses](#responses)
  - [calls](#calls)
    - [Get metadata on all Calls](#get-metadata-on-all-calls)
      - [Query Parameters](#query-parameters)
      - [Example Request](#example-request-1)
      - [Responses](#responses-1)
  - [chatMessages](#chatmessages)
    - [Get metadata on all Chat Messages](#get-metadata-on-all-chat-messages)
      - [Query Parameters](#query-parameters-1)
      - [Example Request](#example-request-2)
      - [Responses](#responses-2)
  - [companies](#companies)
    - [Get all Companies](#get-all-companies)
      - [Query Parameters](#query-parameters-2)
      - [Example Request](#example-request-3)
      - [Responses](#responses-3)
    - [Get metadata on Company Fields](#get-metadata-on-company-fields)
      - [Query Parameters](#query-parameters-3)
      - [Example Request](#example-request-4)
      - [Responses](#responses-4)
    - [Get a single Company](#get-a-single-company)
      - [Path Parameters](#path-parameters)
      - [Query Parameters](#query-parameters-4)
      - [Example Request](#example-request-5)
      - [Responses](#responses-5)
    - [Get a Company's List Entries](#get-a-companys-list-entries)
      - [Path Parameters](#path-parameters-1)
      - [Query Parameters](#query-parameters-5)
      - [Example Request](#example-request-6)
      - [Responses](#responses-6)
    - [Get a Company's Lists](#get-a-companys-lists)
      - [Path Parameters](#path-parameters-2)
      - [Query Parameters](#query-parameters-6)
      - [Example Request](#example-request-7)
      - [Responses](#responses-7)
    - [Get Notes for a Company](#get-notes-for-a-company)
      - [Path Parameters](#path-parameters-3)
      - [Query Parameters](#query-parameters-7)
      - [Example Request](#example-request-8)
      - [Responses](#responses-8)
  - [companyMerges](#companymerges)
    - [Get All Company Merges](#get-all-company-merges)
      - [Query Parameters](#query-parameters-8)
      - [Example Request](#example-request-9)
      - [Responses](#responses-9)
    - [Initiate Company Merge](#initiate-company-merge)
      - [Request Body](#request-body)
      - [Example Request](#example-request-10)
      - [Responses](#responses-10)
    - [Get Company Merge](#get-company-merge)
      - [Path Parameters](#path-parameters-4)
      - [Example Request](#example-request-11)
      - [Responses](#responses-11)
    - [Get All Company Merge Tasks](#get-all-company-merge-tasks)
      - [Query Parameters](#query-parameters-9)
      - [Example Request](#example-request-12)
      - [Responses](#responses-12)
    - [Get Company Merge Task](#get-company-merge-task)
      - [Path Parameters](#path-parameters-5)
      - [Example Request](#example-request-13)
      - [Responses](#responses-13)
  - [emails](#emails)
    - [Get metadata on all Emails](#get-metadata-on-all-emails)
      - [Query Parameters](#query-parameters-10)
      - [Example Request](#example-request-14)
      - [Responses](#responses-14)
  - [lists](#lists)
    - [Get metadata on all Lists](#get-metadata-on-all-lists)
      - [Query Parameters](#query-parameters-11)
      - [Example Request](#example-request-15)
      - [Responses](#responses-15)
    - [Get metadata on a single List](#get-metadata-on-a-single-list)
      - [Path Parameters](#path-parameters-6)
      - [Example Request](#example-request-16)
      - [Responses](#responses-16)
    - [Get metadata on a single List's Fields](#get-metadata-on-a-single-lists-fields)
      - [Path Parameters](#path-parameters-7)
      - [Query Parameters](#query-parameters-12)
      - [Example Request](#example-request-17)
      - [Responses](#responses-17)
    - [Get all List Entries on a List](#get-all-list-entries-on-a-list)
      - [Path Parameters](#path-parameters-8)
      - [Query Parameters](#query-parameters-13)
      - [Example Request](#example-request-18)
      - [Responses](#responses-18)
    - [Get a single List Entry on a List](#get-a-single-list-entry-on-a-list)
      - [Path Parameters](#path-parameters-9)
      - [Query Parameters](#query-parameters-14)
      - [Example Request](#example-request-19)
      - [Responses](#responses-19)
    - [Get field values on a single List Entry](#get-field-values-on-a-single-list-entry)
      - [Path Parameters](#path-parameters-10)
      - [Query Parameters](#query-parameters-15)
      - [Example Request](#example-request-20)
      - [Responses](#responses-20)
    - [Perform batch operations on a list entry's fields](#perform-batch-operations-on-a-list-entrys-fields)
      - [Path Parameters](#path-parameters-11)
      - [Request Body](#request-body-1)
      - [Example Request](#example-request-21)
      - [Responses](#responses-21)
    - [Get a single field value](#get-a-single-field-value)
      - [Path Parameters](#path-parameters-12)
      - [Example Request](#example-request-22)
      - [Responses](#responses-22)
    - [Update a single field value on a List Entry](#update-a-single-field-value-on-a-list-entry)
      - [Path Parameters](#path-parameters-13)
      - [Request Body](#request-body-2)
      - [Example Request](#example-request-23)
      - [Responses](#responses-23)
    - [Get metadata on Saved Views](#get-metadata-on-saved-views)
      - [Path Parameters](#path-parameters-14)
      - [Query Parameters](#query-parameters-16)
      - [Example Request](#example-request-24)
      - [Responses](#responses-24)
    - [Get metadata on a single Saved View](#get-metadata-on-a-single-saved-view)
      - [Path Parameters](#path-parameters-15)
      - [Example Request](#example-request-25)
      - [Responses](#responses-25)
    - [Get all List Entries on a Saved View](#get-all-list-entries-on-a-saved-view)
      - [Path Parameters](#path-parameters-16)
      - [Query Parameters](#query-parameters-17)
      - [Example Request](#example-request-26)
      - [Responses](#responses-26)
  - [meetings](#meetings)
    - [Get metadata on all Meetings](#get-metadata-on-all-meetings)
      - [Query Parameters](#query-parameters-18)
      - [Example Request](#example-request-27)
      - [Responses](#responses-27)
  - [notes](#notes)
    - [Get all Notes](#get-all-notes)
      - [Query Parameters](#query-parameters-19)
      - [Example Request](#example-request-28)
      - [Responses](#responses-28)
    - [Get a single Note](#get-a-single-note)
      - [Path Parameters](#path-parameters-17)
      - [Query Parameters](#query-parameters-20)
      - [Example Request](#example-request-29)
      - [Responses](#responses-29)
    - [Get Companies attached to a Note](#get-companies-attached-to-a-note)
      - [Path Parameters](#path-parameters-18)
      - [Query Parameters](#query-parameters-21)
      - [Example Request](#example-request-30)
      - [Responses](#responses-30)
    - [Get Opportunities attached to a Note](#get-opportunities-attached-to-a-note)
      - [Path Parameters](#path-parameters-19)
      - [Query Parameters](#query-parameters-22)
      - [Example Request](#example-request-31)
      - [Responses](#responses-31)
    - [Get Persons attached to a Note](#get-persons-attached-to-a-note)
      - [Path Parameters](#path-parameters-20)
      - [Query Parameters](#query-parameters-23)
      - [Example Request](#example-request-32)
      - [Responses](#responses-32)
    - [Get replies for a Note](#get-replies-for-a-note)
      - [Path Parameters](#path-parameters-21)
      - [Query Parameters](#query-parameters-24)
      - [Example Request](#example-request-33)
      - [Responses](#responses-33)
  - [opportunities](#opportunities)
    - [Get all Opportunities](#get-all-opportunities)
      - [Query Parameters](#query-parameters-25)
      - [Example Request](#example-request-34)
      - [Responses](#responses-34)
    - [Get a single Opportunity](#get-a-single-opportunity)
      - [Path Parameters](#path-parameters-22)
      - [Example Request](#example-request-35)
      - [Responses](#responses-35)
    - [Get Notes for an Opportunity](#get-notes-for-an-opportunity)
      - [Path Parameters](#path-parameters-23)
      - [Query Parameters](#query-parameters-26)
      - [Example Request](#example-request-36)
      - [Responses](#responses-36)
  - [personMerges](#personmerges)
    - [Get All Person Merges](#get-all-person-merges)
      - [Query Parameters](#query-parameters-27)
      - [Example Request](#example-request-37)
      - [Responses](#responses-37)
    - [Initiate Person Merge](#initiate-person-merge)
      - [Request Body](#request-body-3)
      - [Example Request](#example-request-38)
      - [Responses](#responses-38)
    - [Get Person Merge](#get-person-merge)
      - [Path Parameters](#path-parameters-24)
      - [Example Request](#example-request-39)
      - [Responses](#responses-39)
    - [Get All Person Merge Tasks](#get-all-person-merge-tasks)
      - [Query Parameters](#query-parameters-28)
      - [Example Request](#example-request-40)
      - [Responses](#responses-40)
    - [Get Person Merge Task](#get-person-merge-task)
      - [Path Parameters](#path-parameters-25)
      - [Example Request](#example-request-41)
      - [Responses](#responses-41)
  - [persons](#persons)
    - [Get all Persons](#get-all-persons)
      - [Query Parameters](#query-parameters-29)
      - [Example Request](#example-request-42)
      - [Responses](#responses-42)
    - [Get metadata on Person Fields](#get-metadata-on-person-fields)
      - [Query Parameters](#query-parameters-30)
      - [Example Request](#example-request-43)
      - [Responses](#responses-43)
    - [Get a single Person](#get-a-single-person)
      - [Path Parameters](#path-parameters-26)
      - [Query Parameters](#query-parameters-31)
      - [Example Request](#example-request-44)
      - [Responses](#responses-44)
    - [Get a Person's List Entries](#get-a-persons-list-entries)
      - [Path Parameters](#path-parameters-27)
      - [Query Parameters](#query-parameters-32)
      - [Example Request](#example-request-45)
      - [Responses](#responses-45)
    - [Get a Person's Lists](#get-a-persons-lists)
      - [Path Parameters](#path-parameters-28)
      - [Query Parameters](#query-parameters-33)
      - [Example Request](#example-request-46)
      - [Responses](#responses-46)
    - [Get Notes for a Person](#get-notes-for-a-person)
      - [Path Parameters](#path-parameters-29)
      - [Query Parameters](#query-parameters-34)
      - [Example Request](#example-request-47)
      - [Responses](#responses-47)
  - [Schema Reference](#schema-reference)
    - [Attendee](#attendee)
    - [AttendeesPreview](#attendeespreview)
    - [AuthenticationError](#authenticationerror)
    - [AuthorizationError](#authorizationerror)
    - [AuthorizationErrors](#authorizationerrors)
    - [BadRequestError](#badrequesterror)
    - [ChatMessage](#chatmessage)
    - [CompaniesValue](#companiesvalue)
    - [CompaniesValueUpdate](#companiesvalueupdate)
    - [Company](#company)
    - [CompanyData](#companydata)
    - [CompanyDataPaged](#companydatapaged)
    - [CompanyListEntry](#companylistentry)
    - [CompanyMergeRequest](#companymergerequest)
    - [CompanyMergeResponse](#companymergeresponse)
    - [CompanyMergeState](#companymergestate)
    - [CompanyMergeStatePaged](#companymergestatepaged)
    - [CompanyMergeTask](#companymergetask)
    - [CompanyMergeTaskPaged](#companymergetaskpaged)
    - [CompanyPaged](#companypaged)
    - [CompanyReference](#companyreference)
    - [CompanyValue](#companyvalue)
    - [CompanyValueUpdate](#companyvalueupdate)
    - [ConflictError](#conflicterror)
    - [DateValue](#datevalue)
    - [Dropdown](#dropdown)
    - [DropdownReference](#dropdownreference)
    - [DropdownValue](#dropdownvalue)
    - [DropdownValueUpdate](#dropdownvalueupdate)
    - [DropdownsValue](#dropdownsvalue)
    - [DropdownsValueUpdate](#dropdownsvalueupdate)
    - [Email](#email)
    - [Error](#error)
    - [Errors](#errors)
    - [Field](#field)
    - [FieldMetadata](#fieldmetadata)
    - [FieldMetadataPaged](#fieldmetadatapaged)
    - [FieldPaged](#fieldpaged)
    - [FieldUpdate](#fieldupdate)
    - [FieldValue](#fieldvalue)
    - [FieldValueUpdate](#fieldvalueupdate)
    - [FloatValue](#floatvalue)
    - [FloatsValue](#floatsvalue)
    - [FormulaNumber](#formulanumber)
    - [FormulaValue](#formulavalue)
    - [Grant](#grant)
    - [Interaction](#interaction)
    - [InteractionValue](#interactionvalue)
    - [List](#list)
    - [ListEntry](#listentry)
    - [ListEntryBatchOperationRequest](#listentrybatchoperationrequest)
    - [ListEntryBatchOperationResponse](#listentrybatchoperationresponse)
    - [ListEntryBatchOperationUpdateFields](#listentrybatchoperationupdatefields)
    - [ListEntryBatchOperations](#listentrybatchoperations)
    - [ListEntryPaged](#listentrypaged)
    - [ListEntryWithEntity](#listentrywithentity)
    - [ListEntryWithEntityPaged](#listentrywithentitypaged)
    - [ListPaged](#listpaged)
    - [ListWithType](#listwithtype)
    - [ListWithTypePaged](#listwithtypepaged)
    - [Location](#location)
    - [LocationValue](#locationvalue)
    - [LocationsValue](#locationsvalue)
    - [Meeting](#meeting)
    - [MethodNotAllowedError](#methodnotallowederror)
    - [NotAcceptableError](#notacceptableerror)
    - [NotFoundError](#notfounderror)
    - [NotFoundErrors](#notfounderrors)
    - [NotImplementedError](#notimplementederror)
    - [Opportunity](#opportunity)
    - [OpportunityListEntry](#opportunitylistentry)
    - [OpportunityPaged](#opportunitypaged)
    - [OpportunityWithFields](#opportunitywithfields)
    - [Pagination](#pagination-1)
    - [PaginationWithTotalCount](#paginationwithtotalcount)
    - [Person](#person)
    - [PersonData](#persondata)
    - [PersonDataPaged](#persondatapaged)
    - [PersonDataPreview](#persondatapreview)
    - [PersonListEntry](#personlistentry)
    - [PersonMergeRequest](#personmergerequest)
    - [PersonMergeResponse](#personmergeresponse)
    - [PersonMergeState](#personmergestate)
    - [PersonMergeStatePaged](#personmergestatepaged)
    - [PersonMergeTask](#personmergetask)
    - [PersonMergeTaskPaged](#personmergetaskpaged)
    - [PersonPaged](#personpaged)
    - [PersonReference](#personreference)
    - [PersonValue](#personvalue)
    - [PersonValueUpdate](#personvalueupdate)
    - [PersonsValue](#personsvalue)
    - [PersonsValueUpdate](#personsvalueupdate)
    - [PhoneCall](#phonecall)
    - [RankedDropdown](#rankeddropdown)
    - [RankedDropdownReference](#rankeddropdownreference)
    - [RankedDropdownValue](#rankeddropdownvalue)
    - [RankedDropdownValueUpdate](#rankeddropdownvalueupdate)
    - [RateLimitError](#ratelimiterror)
    - [SavedView](#savedview)
    - [SavedViewPaged](#savedviewpaged)
    - [ServerError](#servererror)
    - [Tenant](#tenant)
    - [TextValue](#textvalue)
    - [TextsValue](#textsvalue)
    - [UnprocessableEntityError](#unprocessableentityerror)
    - [UnsupportedMediaTypeError](#unsupportedmediatypeerror)
    - [User](#user)
    - [ValidationError](#validationerror)
    - [WhoAmI](#whoami)
    - [interactions.Call](#interactionscall)
    - [interactions.CallPaged](#interactionscallpaged)
    - [interactions.ChatMessage](#interactionschatmessage)
    - [interactions.ChatMessagePaged](#interactionschatmessagepaged)
    - [interactions.Email](#interactionsemail)
    - [interactions.EmailPaged](#interactionsemailpaged)
    - [interactions.Meeting](#interactionsmeeting)
    - [interactions.MeetingPaged](#interactionsmeetingpaged)
    - [notes.AiNotetakerReplyNote](#notesainotetakerreplynote)
    - [notes.AiNotetakerRootNote](#notesainotetakerrootnote)
    - [notes.BaseNote](#notesbasenote)
    - [notes.BaseReply](#notesbasereply)
    - [notes.BaseRootNote](#notesbaserootnote)
    - [notes.CallInteraction](#notescallinteraction)
    - [notes.ChatMessageInteraction](#noteschatmessageinteraction)
    - [notes.CompaniesPreview](#notescompaniespreview)
    - [notes.Content](#notescontent)
    - [notes.EmailInteraction](#notesemailinteraction)
    - [notes.EntitiesNote](#notesentitiesnote)
    - [notes.Interaction](#notesinteraction)
    - [notes.InteractionNote](#notesinteractionnote)
    - [notes.MeetingInteraction](#notesmeetinginteraction)
    - [notes.Mention](#notesmention)
    - [notes.Note](#notesnote)
    - [notes.NotesPaged](#notesnotespaged)
    - [notes.OpportunitiesPreview](#notesopportunitiespreview)
    - [notes.PermissionSettings](#notespermissionsettings)
    - [notes.PersonMention](#notespersonmention)
    - [notes.PersonsPreview](#notespersonspreview)
    - [notes.RepliesPaged](#notesrepliespaged)
    - [notes.Reply](#notesreply)
    - [notes.UserReplyNote](#notesuserreplynote)
  - [Error Reference](#error-reference)

# Introduction

Welcome to Affinity API v2! This API provides a RESTful interface for building internal apps,
automated workflows, 3rd party integrations, and for connecting Affinity to the rest of your tech
stack.

The legacy Affinity v1 API can be found at [api-docs.affinity.co](https://api-docs.affinity.co/).
The v2 API is not at feature parity with v1 - we are continuing to develop new v2 APIs to support
all v1 functionality over time.

**The Affinity APIs are only available on select license types.** See
[this Help Center article](https://support.affinity.co/hc/en-us/articles/5563700459533-Getting-started-with-the-Affinity-API-FAQs)
or contact your Customer Success Manager for more information.

# Getting Started

All Affinity API endpoints use the base URL `https://api.affinity.co`. All v2 endpoint paths start
with `/v2`. Requests must be sent over HTTPS.

The first few sections of these docs cover general information on the API. Each subsequent section
covers a set of API endpoints.

Each endpoint is documented with its accepted request parameters, expected response shapes, and a
sample request and response. The shape of a given response can vary depending on what "type" of
object or data is being returned. When this is the case, the response documentation will include a
dropdown that can be used to select the "type" for which to display the response shape.

## Authentication

Affinity API v2 uses API keys and **bearer authentication** (this is an important difference from
Affinity API v1's use of basic authentication).

To generate an API key, navigate to the Settings page in the Affinity web app. You will need the
"Generate an API key" role-based permission controlled by your Affinity admin. See
[this Help Center article](https://support.affinity.co/hc/en-us/articles/360032633992-How-to-obtain-your-API-Key)
for full instructions on API key generation, and
[this article](https://support.affinity.co/hc/en-us/articles/360015976732-Account-Level-Permissions)
for more information on role-based permissions in Affinity.

Provide your API key as your bearer authentication token to start making calls to Affinity API v2.

We support one API key per user in your Affinity account. Your API key is able to read data and
perform actions in Affinity on your behalf, so keep it safe as you would a password.

## Permissions

### Overall Requirements

You must have the "Generate an API key" permission to be able to work with the Affinity API. Most
users in Affinity have this by default — Contact your Affinity admin if you are not able to generate
an API key, and see
[this article](https://support.affinity.co/hc/en-us/articles/360015976732-Account-Level-Permissions)
for more information on role-based permissions in Affinity.

### Resource-Level Permissions

The Affinity API respects sharing permissions that are set in-product. For example, if a given user
does not have access to a list, note, or interaction in-product, they will not be able to see or
modify it via API.

### Endpoint-Level Permissions

Many API endpoints require endpoint-specific permissions in-product. These permissions, along with
the "Generate an API key" permission, are managed by your Affinity admin in the Settings page. In
the description of each endpoint you will see the required permissions needed.

## Rate Limits

The Affinity API sets a limit on the number of calls that a user can make per minute, and that all
the users on an account can make per month. It also sets a reasonable limit on the number of
concurrent requests it will support from an account at one time.

Requests to **both** Affinity API versions will count toward the one pool of requests allowed for a
user or account. Once a per-minute, monthly, or concurrent rate limit is hit, subsequent requests
will return an error code of 429. **We highly recommend designing your application to handle 429
errors.**

### Per-Minute Limits (User-Level)

To help protect our systems, API requests will be halted at **900 per user, per minute.** We may
also lower this limit on a temporary basis to manage API availability.

### Concurrent Request Limits (Account-Level)

To protect our systems and manage availability across customers, we set a reasonable limit on
concurrent requests at the account level. Customers should not expect to hit this limit unless they
are hitting the API with heavy operations from many concurrent threads at once.

### Monthly Plan Tier Limits (Account-Level)

The overall number of requests you can make per month will depend on your account's plan tier.
**This monthly account-level limit resets at the end of each calendar month.** Current rate limits
by plan tier are:

| Plan Tier  | Calls Per Month |
| ---------- | --------------- |
| Essentials | None            |
| Scale      | 100k            |
| Advanced   | 100k            |
| Enterprise | Unlimited\*     |

\*Per-Minute and Concurrent Request Limits still apply.

### Rate Limit Headers

All API calls will return the following response headers with information about per-minute and
monthly limits:

| Header                           | Description                                             |
| -------------------------------- | ------------------------------------------------------- |
| X-Ratelimit-Limit-User           | Number of requests allowed per minute for the user      |
| X-Ratelimit-Limit-User-Remaining | Number of requests remaining for the user               |
| X-Ratelimit-Limit-User-Reset     | Time in seconds before the limit resets for the user    |
| X-Ratelimit-Limit-Org            | Number of requests allowed per month for the account    |
| X-Ratelimit-Limit-Org-Remaining  | Number of requests remaining for the account            |
| X-Ratelimit-Limit-Org-Reset      | Time in seconds before the limit resets for the account |

## Pagination

When an endpoint is expected to return multiple results, we break the results into pages to make
them easier to handle. To cycle forward through multiple pages of data, look for the `nextUrl`
property in the `pagination` portion of an API response, and use it for your next request. See
endpoint documentation for more information.

## Filtering

Some endpoints support a filtering language for flexible and powerful queries. This allows for the
creation of complex filter expressions using different operators and boolean logic in a single
filter string. The description of each endpoint will contain information on which filter properties
and operators are supported.

### Rules

- Spaces are insignificant by default. For example, `field = hello` and `field=hello` are both
  valid.
- If spaces are significant, they need to be inside double quotes, for example,
  `field = "hello world"`
- Special characters need to be escaped with a backslash: `field="hello\" world"` <br> Full list of
  special characters: `\ * ~ ! & = > < $ ^ | " ' ( ) ] [ /`
- Use `&` and `|` for boolean operations: `foo = 1 | baz = 2 & bar = 3`. Boolean Algebra Logic is
  assumed: `&` takes precedence over `|`. When evaluating the condition above, `baz = 2 & bar = 3`
  will be computed first, and then the result will be `or`'ed with `foo=1`
- Parentheses can be used to specify the order of operations. In the example above, to make sure
  that `foo = 1 | baz = 2` is evaluated first, parentheses must be placed
  `(foo = 1 | baz = 2) & bar = 3`

### Grammar

#### Simple Types

| Definition               | Property Type                                        | Operator | Example                                                                                   |
| ------------------------ | ---------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------- |
| exact match              | all                                                  | =        | content = "hello world" <br> content=hello                                                |
| starts with              | text                                                 | =^       | content =^ he                                                                             |
| ends with                | text                                                 | =$       | content =$ llo                                                                            |
| contains                 | text                                                 | =~       | content =~ lo                                                                             |
| greater than             | int32, int64, float, double, decimal, date, datetime | \>       | count > 1                                                                                 |
| greater than or equal to | int32, int64, float, double, decimal, date, datetime | \>=      | content >= 1                                                                              |
| less than                | int32, int64, float, double, decimal, date, datetime | \<       | count < 1                                                                                 |
| less than or equal to    | int32, int64, float, double, decimal, date, datetime | \<=      | content <= 1                                                                              |
| is NULL                  | all                                                  | != \*    | content != \*                                                                             |
| is not NULL              | all                                                  | =\*      | content = \*                                                                              |
| is empty                 | text                                                 | =""      | content = ""                                                                              |
| negation                 | all                                                  | !        | content != "hello world" <br> !(content = "hello world") <br> !(content =^ "hello world") |

#### Collections (all types)

| Definition                | Operator | Example                              |
| ------------------------- | -------- | ------------------------------------ |
| exact match with ordering | =        | industries = [Healthcare,Fintech]    |
| contains all              | =~       | industries =~ [Healthcare,Fintech]   |
| empty                     | =[]      | industries =[]                       |
| negation                  | !        | !(industries = [Healthcare,Fintech]) |

## Error Codes

Here is a list of the error codes the API will return if something goes wrong (see endpoint
documentation for endpoint-specific errors):

| Error Code | Meaning                                                                                                                                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 400        | Bad Request — See endpoint documentation for more information.                                                                                                                                              |
| 401        | Unauthorized — Your API key is invalid.                                                                                                                                                                     |
| 403        | Forbidden — Insufficient rights to a resource.                                                                                                                                                              |
| 404        | Not Found — Requested resource does not exist. See endpoint documentation for more information.                                                                                                             |
| 405        | Method Not Allowed — The method being used is not supported for this resource.                                                                                                                              |
| 422        | Unprocessable Entity — Malformed parameters supplied. This can also happen in cases the parameters supplied logically cannot complete the request. In this case, an appropriate error message is delivered. |
| 429        | Too Many Requests — You have exceeded the rate limit.                                                                                                                                                       |
| 500        | Internal Server Error — We had a problem with our server. Try again later.                                                                                                                                  |
| 503        | Service Unavailable — This shouldn't generally happen. Contact us if you encounter this error.                                                                                                              |

## Beta Endpoints

You'll notice in our documentation that some endpoints will be marked as BETA. These endpoints are
newly released and will eventually progress to General Availability (GA). While an endpoint is in
BETA there are some important things to consider:

- The development of this endpoint may still be in progress. This means new capabilities, request
  parameters, response data, and performance improvements may be adjusted over time. Because of
  this, breaking changes may occur to the endpoint WITHOUT notice or versioning.
- As this is an early release, bug fixes may still be ongoing as well, and we encourage you to
  report bugs to [support@affinity.co](mailto:support@affinity.co).
- In addition, your feedback around the capabilities of the endpoint are highly valuable, please
  reach out to your CSM to provide feedback to our product team.

# Data Model

## The Basics

The three top-level objects in Affinity are **Persons, Companies, and Opportunities**. (Note:
Companies are called Organizations in the Affinity web app.) These have profiles in the Affinity web
app and can be added to Lists.

A **List** is a spreadsheet-like collection of rows tied to Persons, Companies, or Opportunities.

- Each row on a List is a **List Entry**. A List Entry contains data and metadata about a given
  Person, Company, or Opportunity in the context of a List. This includes list-specific field data,
  and information about who added the row to the List and when.
- A given entity can be added to a List more than once. These List Entries can have different
  List-specific field data and List Entry-level metadata.

Each column on a List maps to a **Field**. Fields show up within Affinity profile pages, extensions,
and integrations. There are two categories of fields:

- **List-specific fields** are scoped to a single List. In the API, their data can only be accessed
  through the List Entry resource.
- **Global fields** belong to entities directly. These can include default fields, fields created by
  you, enrichment fields, or relationship intelligence fields. They can be accessed through the
  Person/Company/Opportunity resources and the List Entry resource.

## Working with Field Data

### Field Types and IDs

Here is a deeper look at the types of Fields in Affinity, differentiated by the scope and source of
their data:

| Field&nbsp;Type             | Description                                                                                                                                                  | Example Fields                                                                                                                                              | Field ID Pattern                                                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `enriched`                  | Firmographic, funding, and people Fields populated by Affinity. These can be "Affinity Data" Fields or come from distinct data partners.                     | "Affinity Data: Description", "Dealroom: Number of Employees"                                                                                               | A string representing the enrichment source, followed by the field name, e.g. `affinity-data-description` or `dealroom-number-of-employees`. |
| `list`                      | Fields that are specific to the context of a given list. These can only be accessed through `*/list-entries` endpoints in this version of the API.           | Default "Status" and "Amount" columns, custom columns that pertain to a given List of deals or founders                                                     | `field-`, followed by a unique integer, e.g. `field-1234`                                                                                    |
| `global`                    | Fields that persist across an Affinity account and are not list-specific.                                                                                    | "My Firm's Founder Scoring Column"                                                                                                                          | `field-`, followed by a unique integer, e.g. `field-1234`                                                                                    |
| `relationship-intelligence` | Fields populated by Affinity from users' email and calendar data that provide insight into your firm's relationship with a given Person/Company/Opportunity. | "Source of Introduction", "First Email", "Last Email", "First Event", "Last Event", "Next Event", "First Chat Message", "Last Chat Message", "Last Contact" | A string similar to the field's name in-product, e.g. `source-of-introduction`                                                               |

### Field Value Types

Field data can take a variety of shapes. These value types are described in the Affinity Help Center
[creating columns in lists](https://support.affinity.co/hc/en-us/articles/115001608232-How-to-create-a-new-column-in-a-list).
Here is a list of the same value types, as represented in this API. Notice how array types end with
`-multi`:

| Single Type         | Array Type                |
| ------------------- | ------------------------- |
| `text`              | Not supported in Affinity |
| `number`            | `number-multi`            |
| `datetime`          | Not supported in Affinity |
| `location`          | `location-multi`          |
| `dropdown`          | `dropdown-multi`          |
| `ranked-dropdown`   | Not supported in Affinity |
| `person`            | `person-multi`            |
| `company`           | `company-multi`           |
| `filterable-text`\* | `filterable-text-multi`\* |

\*Note that `filterable-text` and `filterable-text-multi` are special types that operate similarly
to `dropdown` and `dropdown-multi`. They are reserved for Affinity-populated Fields, and users
cannot create Fields with these types.

When an array-typed value has no data in it, the API will return `null` (rather than an empty
array).

### Retrieving Field Data

To retrieve field data on companies, persons, or opportunities, call GET `/v2/companies`, GET
`/v2/persons`, or one of our GET `*/list-entries` endpoints. (Note that Opportunities only have
list-specific Fields, so all their field data will live on the `*/list-entries` endpoints.) For most
of these endpoints, you will need to specify the Fields for which you want data returned via the
`fieldIds` or `fieldTypes` parameter — Otherwise, entities will be returned without any field data
attached.

The GET `/v2/companies` and `/v2/persons` endpoints can return entities with enriched, global, and
relationship intelligence field data attached, but do not support list-specific field data. **To get
comprehensive field data including list-specific field data on Companies and Persons, use the GET
`*/list-entries` endpoints.**

### Specifying Desired Fields (Field Selection)

As mentioned above, you will need to specify the Fields (either by ID or by Type) for which you want
data returned when using the following endpoints:

- GET `/v2/companies`
- GET `/v2/companies/{id}`
- GET `/v2/persons`
- GET `/v2/persons/{id}`
- GET `/v2/lists/{listId}/list-entries`

Each of these endpoints has a `fieldIds` parameter that accepts an array of Field IDs, and a
`fieldTypes` parameter that accepts an array of Field Types. Use the GET `*/fields` endpoints to get
Field IDs, Field Types, and other Field-level metadata:

- Call GET `/v2/companies/fields` and `/v2/persons/fields` to get a list of the enriched, global,
  and relationship intelligence (AKA non-list-specific) Fields that exist on Companies and Persons,
  respectively. These are the Fields whose values are available to pull via GET `/v2/companies`, GET
  `/v2/companies/{id}`, GET `/v2/persons`, and `/v2/persons/{id}`.
- Call GET `/v2/lists/{listId}/fields` to get a list of the enriched, global, relationship
  intelligence, **and list-specific** Fields for a given List. These are the Fields whose values are
  available to pull via GET `/v2/lists/{listId}/list-entries`.

The following endpoints don't require field selection:

- GET `/v2/lists/{listId}/saved-views/{viewId}/list-entries` — See below. This endpoint returns just
  the field data that has been pulled into the given Saved View via UI.
- GET `/v2/companies/{id}/list-entries` and GET `/v2/persons/{id}/list-entries` — These endpoints
  return comprehensive field data for the given person or company in the context of each List Entry.

### Saved Views

A Saved View allows a user to configure the Fields they want to see in the UI for a given List, and
set filters and sorts on the rows on that List. A List can have multiple Saved Views. In the context
of this API, Saved Views can be useful for specifying the exact Fields for which data is needed. The
`*/saved-views/{viewId}/list-entries` endpoint also respects the filters that have been set on the
given Saved View in the Affinity web app. (It does not, however, respect sorts just yet.)

### Partner Data Restrictions

This API supports pulling data from
[Affinity Data](https://support.affinity.co/hc/en-us/articles/360058255052-Affinity-Data) fields and
select
[Dealroom fields](https://support.affinity.co/hc/en-us/articles/6106558518797-Dealroom-co-data-in-Affinity#h_01G2N22SVH7TJR3DJV3NQDE9HQ).
Due the agreements we have with some of our data partners, the API does not expose data from the
following sources:

- Crunchbase, including Crunchbase UUID
- Pitchbook
- [Dealroom "exclusive" fields](https://support.affinity.co/hc/en-us/articles/6106558518797-Dealroom-co-data-in-Affinity#h_01G2N22YEAZJ5TC1X9ENKZFWF5)

## Nested Associations

Some GET endpoints return "association" data under `fields`. For example, the Persons GET endpoints
return data about which Companies a Person is associated with in Affinity. The Opportunities GET
endpoints return similar data about associated Companies and Persons. The List Entries GET endpoints
also return this data for Person and Opportunity List Entries.

The API truncates these nested arrays of Persons or Companies **at 100 entries**. For example, if an
Opportunity is associated with 200 Persons in Affinity, only 100 of those Persons will be returned
by the GET `/opportunities` or `/opportunities/{id}` endpoint.

# User Guides

## A Tour of Our GET Endpoints

| Desired Data                                                | Relevant Endpoints                                                                                                                                                                                                                                                                                                                                    | Notes                                                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Company/Person/Opportunity rows from a List                 | Grab the List's ID from its URL in the Affinity web app, then hit GET `/v2/lists/{listId}/list-entries`                                                                                                                                                                                                                                               | Data returned will be restricted to the rows on the requested List                        |
| Company/Person/Opportunity rows from a Saved View           | In the Affinity web app, navigate to a List and [create a Saved View](https://support.affinity.co/hc/en-us/articles/115001508572-How-to-leverage-saved-views-within-a-list) with the desired field data and filters on it. Grab the List and Saved View IDs from the web app URL, then hit GET `/v2/lists/{listId}/saved-views/{viewId}/list-entries` | Data returned will be restricted to the rows and columns on the requested Saved View      |
| Full rolodex of Companies or Persons in Affinity            | GET `/v2/companies`, GET `/v2/persons`                                                                                                                                                                                                                                                                                                                | Data from list-specific Fields will not be returned                                       |
| All the rows for a given Company or Person across all Lists | GET `/v2/companies/{id}/list-entries`, GET `/v2/persons/{id}/list-entries`                                                                                                                                                                                                                                                                            |                                                                                           |
| Metadata on Fields, including Field IDs                     | GET `/v2/companies/fields`, GET `/v2/persons/fields`, GET `/v2/lists/{listId}/fields`                                                                                                                                                                                                                                                                 | Metadata on list-specific Fields will only be returned by GET `/v2/lists/{listId}/fields` |
| Metadata on Lists or Saved Views                            | GET `/v2/lists`, GET `/v2/lists/{listId}/saved-views`                                                                                                                                                                                                                                                                                                 |                                                                                           |
| Opportunity data                                            | GET `/v2/opportunities` will only return Opportunity names and List IDs. For comprehensive Opportunity data, hit GET `/v2/lists/{listId}/list-entries` for an Opportunity List                                                                                                                                                                        |                                                                                           |

Tip: The ID for a List, Saved View, Person, Company, or Opportunity can always be found in its
Affinity web app URL.

# Changelog

## September 25th, 2025

- Added the following endpoints in BETA:

| Method | URL                                 | Summary                      |
| ------ | ----------------------------------- | ---------------------------- |
| GET    | `/v2/company-merges`                | Get All Company Merge status |
| POST   | `/v2/company-merges`                | Initiate Company Merge       |
| GET    | `/v2/company-merges/{mergeId}`      | Get Company Merge status     |
| GET    | `/v2/tasks/company-merges`          | Get All Company Merge Tasks  |
| GET    | `/v2/tasks/company-merges/{taskId}` | Get Company Merge Task       |

## July 30th, 2025

- Added the following endpoints in BETA:

| Method | URL                                | Summary                     |
| ------ | ---------------------------------- | --------------------------- |
| GET    | `/v2/person-merges`                | Get All Person Merge status |
| POST   | `/v2/person-merges`                | Initiate Person Merge       |
| GET    | `/v2/person-merges/{mergeId}`      | Get Person Merge status     |
| GET    | `/v2/tasks/person-merges`          | Get All Person Merge Tasks  |
| GET    | `/v2/tasks/person-merges/{taskId}` | Get Person Merge Task       |

## May 14th, 2025

- Renamed all path parameters named simply "id" to a more descriptive name (eg. "personId"). This
  will not have any effect on the API at runtime, but may impact code relying on the OpenAPI spec
  doing type generation.

## April 9th, 2025

- The following endpoints are no longer in BETA:

| Method | URL                                                              | Summary                                           |
| ------ | ---------------------------------------------------------------- | ------------------------------------------------- |
| GET    | `/v2/lists/{listId}/list-entries/{listEntryId}`                  | Get a single List Entry on a List                 |
| GET    | `/v2/lists/{listId}/list-entries/{listEntryId}/fields`           | Get field values on a single List Entry           |
| PATCH  | `/v2/lists/{listId}/list-entries/{listEntryId}/fields`           | Perform batch operations on a list entry's fields |
| GET    | `/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}` | Get a single field value                          |
| POST   | `/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}` | Update a single field value on a List Entry       |

## March 31st, 2025

- The following beta endpoints now support updating association fields.

| Method | URL                                                              | Summary                                           |
| ------ | ---------------------------------------------------------------- | ------------------------------------------------- |
| PATCH  | `/v2/lists/{listId}/list-entries/{listEntryId}/fields`           | Perform batch operations on a list entry's fields |
| POST   | `/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}` | Update a single field value on a List Entry       |

## February 28th, 2025

- Added the following endpoints in BETA:

| Method | URL                                                              | Summary                                           |
| ------ | ---------------------------------------------------------------- | ------------------------------------------------- |
| GET    | `/v2/lists/{listId}/list-entries/{listEntryId}`                  | Get a single List Entry on a List                 |
| GET    | `/v2/lists/{listId}/list-entries/{listEntryId}/fields`           | Get field values on a single List Entry           |
| PATCH  | `/v2/lists/{listId}/list-entries/{listEntryId}/fields`           | Perform batch operations on a list entry's fields |
| GET    | `/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}` | Get a single field value                          |
| POST   | `/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}` | Update a single field value on a List Entry       |

## January 17th, 2025

- Document `X-Ratelimit` headers in the schema for all endpoints.

## January 15th, 2025

- Add default responses to all endpoints to document all possible error codes that can be returned
  by the API.
- Updated 400 error responses to correctly include the `bad-request` error code as a possible error.

## December 3rd, 2024

- Properly document `listId` property on `CompanyListEntry`, `PersonListEntry`, and
  `OpportunityListEntry` schemas.

## September 25th, 2024

- Upgrade schema to OpenAPI 3.1

## August 5, 2024

- Correct `opp` to `opportunity` to match documentation for the `List` `type` property.

## July 24, 2024

- More accurate documentation for response properties that are enums — Enums with `null` as a
  possible value will have it listed as one.

## March 25, 2024

- Added the ability to retrieve the date and other details of your firm's "First Email", "Last
  Email", "First Event", "Last Event", "Next Event", "First Chat Message", "Last Chat Message", and
  "Last Contact" with a given entity. Use these timestamps to add relationship context to your
  applications, and to identify founders and companies that need investors' attention.
- Endpoints that previously required a `fieldIds` parameter to return field data, now accept either
  `fieldIds` or `fieldTypes`, and will return field data accordingly. See the
  [Specifying Desired Fields (Field Selection)](#section/Data-Model/Working-with-Field-Data) section
  of these docs for more information. The new `fieldTypes` parameter should make field data
  retrieval easier for users looking to pull data from many similar Fields at a time.

## January 4, 2023

- Most endpoints that return field data now require the user to use the `fieldIds` parameter to
  specify which Fields they want data for. Without `fieldIds` specified, these endpoints will return
  basic entity data but not field data.

## December 12, 2023

- Added the ability to retrieve metadata (e.g. ID, name, type, enrichment source, and data type) on
  Fields. See the [Retrieving Field Metadata](#section/Data-Model/Working-with-Field-Data) section
  of these docs for more information.

## auth

Operations about auths

### Get current user
`GET /v2/auth/whoami`

- **Tag:** auth · **OperationId:** v2_auth_whoami__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns information about the authenticated user, their current organization, and API key permissions.
Use this endpoint to verify your authentication and understand your available API access levels.

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/auth/whoami' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: WhoAmI
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `tenant` | `object` | Yes |  |
| `user` | `object` | Yes |  |
| `grant` | `object` | Yes |  |

**`tenant` details** — See [Tenant](#tenant)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The tenant's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the tenant |
| `subdomain` | `string<hostname>` | Yes | The tenant's subdomain under affinity.co |

**`user` details** — See [User](#user)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The user's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The user's first name |
| `lastName` | `string/null` | Yes | The user's last name |
| `emailAddress` | `string<email>` | Yes | The user's email address |

**`grant` details** — See [Grant](#grant)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `api-key`, `access-token`)` | Yes | The type of grant used to authenticate |
| `scopes` | `array<string>` | Yes | The scopes available to the current grant |
| `createdAt` | `string<date-time>` | Yes | When the grant was created |

**`scopes` details** — The scopes available to the current grant

**Items**

Example

```json
{
  "grant": {
    "createdAt": "2023-01-01T00:00:00Z",
    "scopes": [
      "api"
    ],
    "type": "api-key"
  },
  "tenant": {
    "id": 1,
    "name": "Contoso Ltd.",
    "subdomain": "contoso"
  },
  "user": {
    "emailAddress": "john.smith@contoso.com",
    "firstName": "John",
    "id": 1,
    "lastName": "Smith"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## calls

Operations about calls

### Get metadata on all Calls
`GET /v2/calls`

- **Tag:** calls · **OperationId:** v2_calls__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all calls in Affinity. Returns basic information about the call interaction
and its participants. Will only return calls that the current authenticated user has
permission to see.

You can filter calls using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                     |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|----------------------------------|
| `id`                        | Unique identifier for Calls                                     | `int64`    | `=`                                  | `id=1`                           |
| `startTime`                 | Start time of when the Call was held                            | `datetime` | `>`, `<`, `>=`, `<=`                 | `sentAt>2025-01-01T01:00:00Z`    |
| `createdAt`                 | When the Call was created in Affinity                           | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt`                 | When the Call was updated in Affinity                           | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-01-01T01:00:00Z`|

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/calls' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: interactions.CallPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Call results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.Call](#interactionscall)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The call's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, calls can only be logged as 'manual'. |
| `title` | `string/null` | Yes | The call's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the call starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the call ends |
| `allDay` | `boolean` | Yes | Whether the call is all day |
| `creator` | `oneOf` | Yes | The person who created the call |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the call was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the call was updated |
| `attendeesPreview` | `object` | Yes | A preview of the attendees in the call (Constraints: stability `beta`) |

**`attendeesPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## chatMessages

Operations about chat messages

### Get metadata on all Chat Messages
`GET /v2/chat-messages`

- **Tag:** chatMessages · **OperationId:** v2_chat-messages__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all chat messages in Affinity. Returns basic information about the chat message
interaction and its participants. Will only return chat messages that the current authenticated
user has permission to see.

You can filter chat messages using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                     |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|----------------------------------|
| `id`                        | Unique identifier for Chat Messages                             | `int64`    | `=`                                  | `id=1`                           |
| `sentAt`                    | When the Chat Message was sent at                               | `datetime` | `>`, `<`, `>=`, `<=`                 | `sentAt>2025-01-01T01:00:00Z`    |
| `createdAt`                 | When the Chat Message was created in Affinity                   | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt`                 | When the Chat Message was updated in Affinity                   | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-01-01T01:00:00Z`|

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/chat-messages' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: interactions.ChatMessagePaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ChatMessage results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.ChatMessage](#interactionschatmessage)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The chat message's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the chat message was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, chat messages can only be logged as 'manual'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the chat message |
| `creator` | `object` | Yes | The creator of the chat message |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the chat message was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the chat message was updated |
| `participantsPreview` | `object` | Yes | A preview of the participants who are in the chat message (Constraints: stability `beta`) |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`participantsPreview` details** — See [interactions.PersonDataPreview](#interactionspersondatapreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of persons |
| `totalCount` | `integer<int64>` | Yes | The total count of persons (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## companies

Operations about companies

### Get all Companies
`GET /v2/companies`

- **Tag:** companies · **OperationId:** v2_companies__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through Companies in Affinity.
Returns basic information and non-list-specific field data on each Company.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/companies/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Companies will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export All Organizations directory" [permission](#section/Getting-Started/Permissions).

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `ids` | `array<integer<int64>>` | No | Company IDs |
| `fieldIds` | `array<string>` | No | Field IDs for which to return field data |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | Field Types for which to return field data |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Company results |
| `pagination` | `object` | Yes |  |

**`data` details** — Company model See [Company](#company)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "domain": "acme.co",
      "domains": [
        "acme.co"
      ],
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-description",
          "name": "Description",
          "type": "enriched",
          "value": {
            "data": "A leading provider of innovative solutions",
            "type": "text"
          }
        }
      ],
      "id": 1,
      "isGlobal": true,
      "name": "Acme"
    },
    {
      "domain": "umbrella.co",
      "domains": [
        "umbrella.co"
      ],
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "Raccoon City",
              "continent": "North America",
              "country": "United States",
              "state": "Ohio",
              "streetAddress": "200 Corporate Blvd"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-description",
          "name": "Description",
          "type": "enriched",
          "value": {
            "data": "Pharmaceutical and biotechnology company",
            "type": "text"
          }
        }
      ],
      "id": 2,
      "isGlobal": true,
      "name": "Umbrella Corporation"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get metadata on Company Fields
`GET /v2/companies/fields`

- **Tag:** companies · **OperationId:** v2_companies_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns metadata on non-list-specific Company Fields.

Use the returned Field IDs to request field data from the GET `/v2/companies` and GET `/v2/companies/{id}` endpoints.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldMetadataPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of FieldMetadata results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [FieldMetadata](#fieldmetadata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `valueType` | `string (enum: `person`, `person-multi`, `company`, `company-multi`, `filterable-text`, …)` | Yes | The type of the data in this Field |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a single Company
`GET /v2/companies/{companyId}`

- **Tag:** companies · **OperationId:** v2_companies_companyId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns basic information and non-list-specific field data on the requested Company.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/companies/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Companies will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export All Organizations directory" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldIds` | `array<string>` | No | Field IDs for which to return field data |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | Field Types for which to return field data |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: Company
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

Example

```json
{
  "domain": "acme.co",
  "domains": [
    "acme.co"
  ],
  "fields": [
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "name": "Location",
      "type": "enriched",
      "value": {
        "data": {
          "city": "San Francisco",
          "continent": "North America",
          "country": "United States",
          "state": "California",
          "streetAddress": "1 Main Street"
        },
        "type": "location"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-description",
      "name": "Description",
      "type": "enriched",
      "value": {
        "data": "A leading provider of innovative solutions",
        "type": "text"
      }
    }
  ],
  "id": 1,
  "isGlobal": true,
  "name": "Acme"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a Company's List Entries
`GET /v2/companies/{companyId}/list-entries`

- **Tag:** companies · **OperationId:** v2_companies_companyId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) for the given Company across all Lists.
Each List Entry includes field data for the Company, including list-specific field data.
Each List Entry also includes metadata about its creation, i.e., when it was added to the List and by whom.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/list-entries' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListEntryPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ListEntry results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [ListEntry](#listentry)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | Yes | The fields associated with the list entry |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        }
      ],
      "id": 1,
      "listId": 1
    },
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        }
      ],
      "id": 1,
      "listId": 1
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a Company's Lists
`GET /v2/companies/{companyId}/lists`

- **Tag:** companies · **OperationId:** v2_companies_companyId_lists__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Lists where the given Company appears as an entry and that you have access to view.
Returns basic List information for each List that contains this Company.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/lists' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of List results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [List](#list)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "creatorId": 1,
      "id": 1,
      "isPublic": false,
      "name": "All companies",
      "ownerId": 1
    },
    {
      "creatorId": 1,
      "id": 1,
      "isPublic": false,
      "name": "All companies",
      "ownerId": 1
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Notes for a Company
`GET /v2/companies/{companyId}/notes`

- **Tag:** companies · **OperationId:** v2_companies_companyId_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns relevant notes for a given company which includes directly attached notes and notes attached to persons on this company.

You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                    |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|---------------------------------|
| `creator.id`                | Filter notes by the creator of the note                         | `int32`    | `=`                                  | `creator.id=1`                  |
| `createdAt`                 | Filter notes by when it was created                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt`                 | Filter notes by when it was updated                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-02-03T10:48:24Z`|

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company's ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/notes' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: notes.NotesPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note objects |
| `pagination` | `object` | Yes |  |

**`data` details** — Note model See [notes.Note](#notesnote)

**Items**

**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## companyMerges

Operations about company merges

### Get All Company Merges
`GET /v2/company-merges`

- **Tag:** companyMerges · **OperationId:** v2_company-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated company merges for the organization.

Returns all company merges initiated by users in your organization, including their current
status, the companies involved, and merge details. You can filter company merges using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| Property | Type | Operators | Values | Examples |
|----------|------|-----------|--------|----------|
| `status` | `enum` | `=` | `in-progress`, `success`, `failed` | `status=failed` |
| `taskId` | `string` | `=` | | `taskId=789e0123-e45b-67c8-d901-234567890123` |

Company merges are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and
organization admin role.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter company merges using Affinity Filtering Language |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/company-merges' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyMergeStatePaged
*Type:* object
Paginated list of company merge states
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of company merge states |
| `pagination` | `object` | Yes |  |

**`data` details** — Entity representing the state of an individual company merge See [CompanyMergeState](#companymergestate)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryCompanyId` | `integer<int64>` | Yes | ID of the primary company that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | ID of the duplicate company that was merged into the primary company (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: merges-list

```json
{
  "data": [
    {
      "completedAt": "2025-06-03T10:32:15Z",
      "duplicateCompanyId": 67890,
      "errorMessage": null,
      "id": 12,
      "primaryCompanyId": 12345,
      "startedAt": "2025-06-03T10:30:00Z",
      "status": "success",
      "taskId": "789e0123-e45b-67c8-d901-234567890123"
    },
    {
      "completedAt": "2025-06-03T09:16:30Z",
      "duplicateCompanyId": 98765,
      "errorMessage": "Primary company not found",
      "id": 13,
      "primaryCompanyId": 54321,
      "startedAt": "2025-06-03T09:15:00Z",
      "status": "failed",
      "taskId": "456e7890-1234-5678-9012-345678901234"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/companies/merge?cursor=eyJpZCI6NDU2ZTc4OTAtZTEyYi0zNGM1LWQ2NzgtOTAxMjM0NTY3ODkwfQ==",
    "prevUrl": null
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Initiate Company Merge
`POST /v2/company-merges`

- **Tag:** companyMerges · **OperationId:** v2_company-merges__POST · **Stability:** `beta` · **Auth:** bearerAuth

Initiate a company merge to combine a duplicate company profile into a primary company profile.

This is an asynchronous process that will merge all data from the duplicate company into the primary company. Once the merge is initiated, you can track its progress using the returned [task URL](#tag/companyMerges/operation/v2_tasks_company-merges_taskId__GET).

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and organization admin role.

#### Request Body

**Media type:** `application/json`
Request body for initiating a company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `primaryCompanyId` | `integer<int64>` | Yes | The ID of the company profile that will be kept after the merge. All data from the duplicate company will be merged into this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | The ID of the company profile that will be merged and then deleted. All data from this company will be transferred to the primary company. (Constraints: ≥ 1; ≤ 9007199254740991) |

Example: merge-companies
```json
{
  "duplicateCompanyId": 67890,
  "primaryCompanyId": 12345
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/company-merges' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"primaryCompanyId":12345,"duplicateCompanyId":67890}'
```

#### Responses

##### 202 — application/json

Accepted

**Response schema (`application/json`):**
###### Schema: CompanyMergeResponse
*Type:* object
Response body for initiating a company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `taskUrl` | `string<uri>` | Yes | URL to check the status of the merge task |

Example: merge-initiated

```json
{
  "taskUrl": "https://api.affinity.co/v2/tasks/company-merges/123e4567-e89b-12d3-a456-426614174000"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Company Merge
`GET /v2/company-merges/{mergeId}`

- **Tag:** companyMerges · **OperationId:** v2_company-merges_mergeId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific company merge.

Returns information about the company merge including its current status, the companies involved, timestamps, and any error information if the merge failed.

The `mergeId` can be obtained from the response of the [Get All Company Merges](#tag/companyMerges/operation/v2_company-merges__GET) endpoint, or by filtering company merges by task ID using `/v2/company-merges?filter=taskId={taskId}` after initiating a merge.

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and organization admin role.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `mergeId` | `integer<int64>` | Yes | Company merge ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/company-merges/{mergeId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyMergeState
*Type:* object
Entity representing the state of an individual company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryCompanyId` | `integer<int64>` | Yes | ID of the primary company that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | ID of the duplicate company that was merged into the primary company (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |

Example: completed-merge

```json
{
  "completedAt": "2025-06-03T10:32:15Z",
  "duplicateCompanyId": 67890,
  "errorMessage": null,
  "id": 12345,
  "primaryCompanyId": 12345,
  "startedAt": "2025-06-03T10:30:00Z",
  "status": "success",
  "taskId": "1ac19acd-674c-49a0-819a-cd674cc9a042"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get All Company Merge Tasks
`GET /v2/tasks/company-merges`

- **Tag:** companyMerges · **OperationId:** v2_tasks_company-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated company merge tasks for the organization.

Returns all merge tasks initiated by users in your organization, including their current status,
the companies involved, and task details.

You can filter tasks using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| Property | Type | Operators | Values | Examples |
|----------|------|-----------|--------|----------|
| `status` | `enum` | `=` | `in-progress`, `success`, `failed` | `status=failed` |

Tasks are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and
organization admin role.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter tasks using Affinity Filtering Language |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/tasks/company-merges' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyMergeTaskPaged
*Type:* object
Paginated list of company merge tasks
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of company merge tasks |
| `pagination` | `object` | Yes |  |

**`data` details** — Company merge task details and status for batch operations See [CompanyMergeTask](#companymergetask)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: tasks-list

```json
{
  "data": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "resultsSummary": {
        "failed": 0,
        "inProgress": 0,
        "success": 1,
        "total": 1
      },
      "status": "success"
    },
    {
      "id": "456e7890-e12b-34c5-d678-901234567890",
      "resultsSummary": {
        "failed": 1,
        "inProgress": 0,
        "success": 0,
        "total": 1
      },
      "status": "failed"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/tasks/company-merges?cursor=eyJpZCI6NDU2ZTc4OTAtZTEyYi0zNGM1LWQ2NzgtOTAxMjM0NTY3ODkwfQ==",
    "prevUrl": null
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Company Merge Task
`GET /v2/tasks/company-merges/{taskId}`

- **Tag:** companyMerges · **OperationId:** v2_tasks_company-merges_taskId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific task for company merges.

Returns information about the company merges for a specific task including its overall status,
number of merges in-progress, completed, and failed.

Detailed information about individual merges for this task can be found by querying:
`/v2/company-merges?filter=taskId={taskId}` See [Company
Merges](#tag/companyMerges/operation/v2_company-merges__GET) for more details.

Task statuses:

- `in-progress`: The merge task is currently being processed.
- `success`: The merge task completed successfully.
- `failed`: The merge task failed.

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and
organization admin role.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | `string<uuid>` | Yes | Company merge task ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/tasks/company-merges/{taskId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyMergeTask
*Type:* object
Company merge task details and status for batch operations
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |

Example: task-in-progress

```json
{
  "id": "456e7890-e12b-34c5-d678-901234567890",
  "resultsSummary": {
    "failed": 0,
    "inProgress": 1,
    "success": 0,
    "total": 1
  },
  "status": "in-progress"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## emails

Operations about emails

### Get metadata on all Emails
`GET /v2/emails`

- **Tag:** emails · **OperationId:** v2_emails__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all emails in Affinity. Returns basic information about the email interaction
and its participants. Will only return emails or subject lines that the current authenticated
user has permission to see.

You can filter emails using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                     |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|----------------------------------|
| `id`                        | Unique identifier for Emails                                    | `int64`    | `=`                                  | `id=1`                           |
| `sentAt`                    | When the Email was sent at                                      | `datetime` | `>`, `<`, `>=`, `<=`                 | `sentAt>2025-01-01T01:00:00Z` |
| `createdAt`                 | When the Email was created in Affinity                          | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt`                 | When the Email was updated in Affinity                          | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-01-01T01:00:00Z`|

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/emails' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: interactions.EmailPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Email results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.Email](#interactionsemail)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the email was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, emails can only be logged as 'automated'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the email: 'sent' if the email was sent by an internal user and  'received' if the email was sent to an internal user. |
| `subject` | `string/null` | Yes | The email's subject |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the email was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the email was updated |
| `from` | `object` | Yes | The participant who sent the email |
| `toParticipantsPreview` | `object` | Yes | A preview of the participants in the 'To' field of the email (Constraints: stability `beta`) |
| `ccParticipantsPreview` | `object` | Yes | A preview of the participants who are cc'ed in the email (Constraints: stability `beta`) |

**`from` details** — See [Attendee](#attendee)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`toParticipantsPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`ccParticipantsPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## lists

Operations about lists

### Get metadata on all Lists
`GET /v2/lists`

- **Tag:** lists · **OperationId:** v2_lists__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Lists in your organization that you have access to view.
Returns basic information about each List, including name, owner, and privacy settings.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListWithTypePaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ListWithType results |
| `pagination` | `object` | Yes |  |

**`data` details** — ListWithType model See [ListWithType](#listwithtype)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for this list |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: success

```json
{
  "data": [
    {
      "creatorId": 1,
      "id": 1,
      "isPublic": false,
      "name": "My Companies",
      "ownerId": 1,
      "type": "company"
    },
    {
      "creatorId": 1,
      "id": 2,
      "isPublic": false,
      "name": "My Persons",
      "ownerId": 1,
      "type": "person"
    },
    {
      "creatorId": 1,
      "id": 3,
      "isPublic": false,
      "name": "My Opportunities",
      "ownerId": 1,
      "type": "opportunity"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/lists?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/lists?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get metadata on a single List
`GET /v2/lists/{listId}`

- **Tag:** lists · **OperationId:** v2_lists_listId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve detailed information about a specific List you have access to view.
Returns List configuration including name, owner, privacy settings, and creation details.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListWithType
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for this list |

Example: company-list

```json
{
  "creatorId": 1,
  "id": 1,
  "isPublic": false,
  "name": "My Companies",
  "ownerId": 1,
  "type": "company"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get metadata on a single List's Fields
`GET /v2/lists/{listId}/fields`

- **Tag:** lists · **OperationId:** v2_lists_listId_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns metadata on the Fields available on a single List.

Use the returned Field IDs to request field data from the GET `/v2/lists/{listId}/list-entries` endpoint.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldMetadataPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of FieldMetadata results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [FieldMetadata](#fieldmetadata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `valueType` | `string (enum: `person`, `person-multi`, `company`, `company-multi`, `filterable-text`, …)` | Yes | The type of the data in this Field |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: company-list

```json
{
  "data": [
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-description",
      "name": "Description",
      "type": "enriched",
      "valueType": "text"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-industry",
      "name": "Industry",
      "type": "enriched",
      "valueType": "filterable-text-multi"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-investment-stage",
      "name": "Investment Stage",
      "type": "enriched",
      "valueType": "filterable-text"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-investors",
      "name": "Investors",
      "type": "enriched",
      "valueType": "filterable-text-multi"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-amount",
      "name": "Last Funding Amount (USD)",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-date",
      "name": "Last Funding Date",
      "type": "enriched",
      "valueType": "datetime"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-linkedin-url",
      "name": "LinkedIn URL",
      "type": "enriched",
      "valueType": "text"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "name": "Location",
      "type": "enriched",
      "valueType": "location"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-number-of-employees",
      "name": "Number of Employees",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-total-funding-amount",
      "name": "Total Funding Amount (USD)",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-year-founded",
      "name": "Year Founded",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "enrichmentSource": null,
      "id": "field-1",
      "name": "Custom global field",
      "type": "global",
      "valueType": "text"
    },
    {
      "enrichmentSource": null,
      "id": "field-2",
      "name": "Custom list field",
      "type": "list",
      "valueType": "text"
    },
    {
      "enrichmentSource": null,
      "id": "first-chat-message",
      "name": "First Chat Message",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "first-email",
      "name": "First Email",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "first-event",
      "name": "First Event",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "last-chat-message",
      "name": "Last Chat Message",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "last-contact",
      "name": "Last Contact",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "last-email",
      "name": "Last Email",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "last-event",
      "name": "Last Event",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "next-event",
      "name": "Next Event",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "enrichmentSource": null,
      "id": "source-of-introduction",
      "name": "Source of Introduction",
      "type": "relationship-intelligence",
      "valueType": "person"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/lists/1/fields?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/lists/1/fields?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get all List Entries on a List
`GET /v2/lists/{listId}/list-entries`

- **Tag:** lists · **OperationId:** v2_lists_listId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) on a given List.
Returns basic information and field data, including list-specific
field data, on each Company, Person, or Opportunity on the List.
List Entries also include metadata about their creation,
i.e., when they were added to the List and by whom.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/lists/{listId}/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, List Entries will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `fieldIds` | `array<string>` | No | Field IDs for which to return field data |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)>` | No | Field Types for which to return field data |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/list-entries' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListEntryWithEntityPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array/null` | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: company-list-enriched

```json
{
  "data": [
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "entity": {
        "domain": "acme.co",
        "domains": [
          "acme.co"
        ],
        "fields": [
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-description",
            "name": "Description",
            "type": "enriched",
            "value": {
              "data": "Acme is a mega-corporation that manufactures everything from anvils to earthquake pills.",
              "type": "text"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-industry",
            "name": "Industry",
            "type": "enriched",
            "value": {
              "data": [
                "Aerospace",
                "Construction",
                "Consumer Goods"
              ],
              "type": "filterable-text-multi"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-investment-stage",
            "name": "Investment Stage",
            "type": "enriched",
            "value": {
              "data": "Public Markets",
              "type": "filterable-text"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-investors",
            "name": "Investors",
            "type": "enriched",
            "value": {
              "data": [
                "Marvin Acme",
                "Yosemite Sam"
              ],
              "type": "filterable-text-multi"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-last-funding-amount",
            "name": "Last Funding Amount (USD)",
            "type": "enriched",
            "value": {
              "data": 100000000,
              "type": "number"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-last-funding-date",
            "name": "Last Funding Date",
            "type": "enriched",
            "value": {
              "data": "2023-01-01T00:00:00Z",
              "type": "datetime"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-linkedin-url",
            "name": "LinkedIn URL",
            "type": "enriched",
            "value": {
              "data": "https://linkedin.com/company/acme",
              "type": "text"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-location",
            "name": "Location",
            "type": "enriched",
            "value": {
              "data": {
                "city": "Fairfield",
                "continent": null,
                "country": "United States",
                "state": "New Jersey",
                "streetAddress": null
              },
              "type": "location"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-number-of-employees",
            "name": "Number of Employees",
            "type": "enriched",
            "value": {
              "data": 3990,
              "type": "number"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-total-funding-amount",
            "name": "Total Funding Amount (USD)",
            "type": "enriched",
            "value": {
              "data": 90000000,
              "type": "number"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-year-founded",
            "name": "Year Founded",
            "type": "enriched",
            "value": {
              "data": 1952,
              "type": "number"
            }
          }
        ],
        "id": 1,
        "isGlobal": true,
        "name": "Acme"
      },
      "id": 1,
      "listId": 1,
      "type": "company"
    },
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "entity": {
        "domain": "umbrella.co",
        "domains": [
          "umbrella.co"
        ],
        "fields": [
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-description",
            "name": "Description",
            "type": "enriched",
            "value": {
              "data": "The Umbrella Corporation is a multinational conglomerate with subsidiaries active in a variety of industries.",
              "type": "text"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-industry",
            "name": "Industry",
            "type": "enriched",
            "value": {
              "data": [
                "Cosmetics",
                "Chemical",
                "Consumer Goods",
                "Food Products",
                "Machinery Manufacturing",
                "Pharmaceuticals",
                "Transportation",
                "Tourism"
              ],
              "type": "filterable-text-multi"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-investment-stage",
            "name": "Investment Stage",
            "type": "enriched",
            "value": {
              "data": "Public Markets",
              "type": "filterable-text"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-investors",
            "name": "Investors",
            "type": "enriched",
            "value": {
              "data": [
                "Oswell E. Spencer",
                "Albert Wesker"
              ],
              "type": "filterable-text-multi"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-last-funding-amount",
            "name": "Last Funding Amount (USD)",
            "type": "enriched",
            "value": {
              "data": 100000000,
              "type": "number"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-last-funding-date",
            "name": "Last Funding Date",
            "type": "enriched",
            "value": {
              "data": "2023-01-01T00:00:00Z",
              "type": "datetime"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-linkedin-url",
            "name": "LinkedIn URL",
            "type": "enriched",
            "value": {
              "data": "https://linkedin.com/company/umbrella",
              "type": "text"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-location",
            "name": "Location",
            "type": "enriched",
            "value": {
              "data": {
                "city": "Chicago",
                "continent": null,
                "country": "United States",
                "state": "Illinois",
                "streetAddress": null
              },
              "type": "location"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-number-of-employees",
            "name": "Number of Employees",
            "type": "enriched",
            "value": {
              "data": 12000,
              "type": "number"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-total-funding-amount",
            "name": "Total Funding Amount (USD)",
            "type": "enriched",
            "value": {
              "data": 60000000,
              "type": "number"
            }
          },
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-year-founded",
            "name": "Year Founded",
            "type": "enriched",
            "value": {
              "data": 1968,
              "type": "number"
            }
          }
        ],
        "id": 2,
        "isGlobal": true,
        "name": "Umbrella Corporation"
      },
      "id": 2,
      "listId": 1,
      "type": "company"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/lists/1/list-entries?fieldTypes=enriched&cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/lists/1/list-entries?fieldTypes=enriched&cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a single List Entry on a List
`GET /v2/lists/{listId}/list-entries/{listEntryId}`

- **Tag:** lists · **OperationId:** v2_lists_listId_list-entries_listEntryId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve a single list entry.
Returns basic information and field data, including list-specific field data.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/lists/{listId}/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, the List Entry will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldIds` | `array<string>` | No | Field IDs for which to return field data |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)>` | No | Field Types for which to return field data |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListEntryWithEntity
*Type:* oneOf
**Variant:** CompanyListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes | Company model |

**`entity` details** — See [Company](#company)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
**Variant:** OpportunityListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes |  |

**`entity` details** — See [OpportunityWithFields](#opportunitywithfields)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | No | The fields associated with the opportunity |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
**Variant:** PersonListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes | Person model |

**`entity` details** — See [Person](#person)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

Example: company-list-enriched

```json
{
  "createdAt": "2023-01-01T00:00:00Z",
  "creatorId": 1,
  "entity": {
    "domain": "acme.co",
    "domains": [
      "acme.co"
    ],
    "fields": [
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-description",
        "name": "Description",
        "type": "enriched",
        "value": {
          "data": "Acme is a mega-corporation that manufactures everything from anvils to earthquake pills.",
          "type": "text"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-industry",
        "name": "Industry",
        "type": "enriched",
        "value": {
          "data": [
            "Aerospace",
            "Construction",
            "Consumer Goods"
          ],
          "type": "filterable-text-multi"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-investment-stage",
        "name": "Investment Stage",
        "type": "enriched",
        "value": {
          "data": "Public Markets",
          "type": "filterable-text"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-investors",
        "name": "Investors",
        "type": "enriched",
        "value": {
          "data": [
            "Marvin Acme",
            "Yosemite Sam"
          ],
          "type": "filterable-text-multi"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-last-funding-amount",
        "name": "Last Funding Amount (USD)",
        "type": "enriched",
        "value": {
          "data": 100000000,
          "type": "number"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-last-funding-date",
        "name": "Last Funding Date",
        "type": "enriched",
        "value": {
          "data": "2023-01-01T00:00:00Z",
          "type": "datetime"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-linkedin-url",
        "name": "LinkedIn URL",
        "type": "enriched",
        "value": {
          "data": "https://linkedin.com/company/acme",
          "type": "text"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-location",
        "name": "Location",
        "type": "enriched",
        "value": {
          "data": {
            "city": "Fairfield",
            "continent": null,
            "country": "United States",
            "state": "New Jersey",
            "streetAddress": null
          },
          "type": "location"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-number-of-employees",
        "name": "Number of Employees",
        "type": "enriched",
        "value": {
          "data": 3990,
          "type": "number"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-total-funding-amount",
        "name": "Total Funding Amount (USD)",
        "type": "enriched",
        "value": {
          "data": 90000000,
          "type": "number"
        }
      },
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-year-founded",
        "name": "Year Founded",
        "type": "enriched",
        "value": {
          "data": 1952,
          "type": "number"
        }
      }
    ],
    "id": 1,
    "isGlobal": true,
    "name": "Acme"
  },
  "id": 1,
  "listId": 1,
  "type": "company"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get field values on a single List Entry
`GET /v2/lists/{listId}/list-entries/{listEntryId}/fields`

- **Tag:** lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all field values on a single list entry.

All fields will be included by default. The `ids` and `types` parameters can be used to filter the collection.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `array<string>` | No | Field IDs for which to return field data |
| `types` | `array<string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)>` | No | Field Types for which to return field data |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Field results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: company-list-enriched

```json
{
  "data": [
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-description",
      "name": "Description",
      "type": "enriched",
      "value": {
        "data": "Acme is a mega-corporation that manufactures everything from anvils to earthquake pills.",
        "type": "text"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-industry",
      "name": "Industry",
      "type": "enriched",
      "value": {
        "data": [
          "Aerospace",
          "Construction",
          "Consumer Goods"
        ],
        "type": "filterable-text-multi"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-investment-stage",
      "name": "Investment Stage",
      "type": "enriched",
      "value": {
        "data": "Public Markets",
        "type": "filterable-text"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-investors",
      "name": "Investors",
      "type": "enriched",
      "value": {
        "data": [
          "Marvin Acme",
          "Yosemite Sam"
        ],
        "type": "filterable-text-multi"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-amount",
      "name": "Last Funding Amount (USD)",
      "type": "enriched",
      "value": {
        "data": 100000000,
        "type": "number"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-date",
      "name": "Last Funding Date",
      "type": "enriched",
      "value": {
        "data": "2023-01-01T00:00:00Z",
        "type": "datetime"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-linkedin-url",
      "name": "LinkedIn URL",
      "type": "enriched",
      "value": {
        "data": "https://linkedin.com/company/acme",
        "type": "text"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "name": "Location",
      "type": "enriched",
      "value": {
        "data": {
          "city": "Fairfield",
          "continent": null,
          "country": "United States",
          "state": "New Jersey",
          "streetAddress": null
        },
        "type": "location"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-number-of-employees",
      "name": "Number of Employees",
      "type": "enriched",
      "value": {
        "data": 3990,
        "type": "number"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-total-funding-amount",
      "name": "Total Funding Amount (USD)",
      "type": "enriched",
      "value": {
        "data": 90000000,
        "type": "number"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-year-founded",
      "name": "Year Founded",
      "type": "enriched",
      "value": {
        "data": 1952,
        "type": "number"
      }
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/lists/1/list-entries?types=enriched&cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/lists/1/list-entries?types=enriched&cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Perform batch operations on a list entry's fields
`PATCH /v2/lists/{listId}/list-entries/{listEntryId}/fields`

- **Tag:** lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields__PATCH · **Stability:** `beta` · **Auth:** bearerAuth

Perform batch operations on a list entry's fields.

Currently the only operation at the endpoint is `update-fields`, which allows you to update multiple field values with a single request. This is equivalent to calling [the single field update](#operation/v2_lists_listId_list-entries_listEntryId_fields_fieldId__POST) endpoint multiple times.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |

#### Request Body

**Media type:** `application/json`
**Variant:** ListEntryBatchOperationUpdateFields
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` | Yes |  |

**`updates` details**

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier. |
| `value` | `oneOf` | No |  |

Example: update-fields
```json
{
  "operation": "update-fields",
  "updates": [
    {
      "id": "field-1",
      "value": {
        "data": {
          "id": 1
        },
        "type": "company"
      }
    },
    {
      "id": "field-2",
      "value": {
        "data": [
          {
            "id": 1
          },
          {
            "id": 2
          }
        ],
        "type": "company-multi"
      }
    },
    {
      "id": "field-3",
      "value": {
        "data": "2023-01-01T00:00:00Z",
        "type": "datetime"
      }
    },
    {
      "id": "field-4",
      "value": {
        "data": {
          "dropdownOptionId": 1
        },
        "type": "dropdown"
      }
    },
    {
      "id": "field-5",
      "value": {
        "data": [
          {
            "dropdownOptionId": 1
          },
          {
            "dropdownOptionId": 2
          }
        ],
        "type": "dropdown-multi"
      }
    },
    {
      "id": "field-6",
      "value": {
        "data": {
          "city": "San Francisco",
          "continent": "North America",
          "country": "United States",
          "state": "California",
          "streetAddress": "1 Main Street"
        },
        "type": "location"
      }
    },
    {
      "id": "field-7",
      "value": {
        "data": [
          {
            "city": "San Francisco",
            "continent": "North America",
            "country": "United States",
            "state": "California",
            "streetAddress": "1 Main Street"
          },
          {
            "city": "Washington",
            "continent": "North America",
            "country": "United States",
            "state": "DC",
            "streetAddress": "1600 Pennsylvania Avenue NW"
          }
        ],
        "type": "location-multi"
      }
    },
    {
      "id": "field-8",
      "value": {
        "data": 100,
        "type": "number"
      }
    },
    {
      "id": "field-9",
      "value": {
        "data": [
          100,
          200,
          300
        ],
        "type": "number-multi"
      }
    },
    {
      "id": "field-10",
      "value": {
        "data": {
          "id": 1
        },
        "type": "person"
      }
    },
    {
      "id": "field-11",
      "value": {
        "data": [
          {
            "id": 1
          },
          {
            "id": 2
          }
        ],
        "type": "person-multi"
      }
    },
    {
      "id": "field-12",
      "value": {
        "data": {
          "dropdownOptionId": 1
        },
        "type": "ranked-dropdown"
      }
    },
    {
      "id": "field-13",
      "value": {
        "data": "Some new text",
        "type": "text"
      }
    }
  ]
}
```

#### Example Request

```bash
curl --request PATCH 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"operation":"update-fields","updates":[{"id":"field-1","value":{"type":"company","data":{"id":1}}},{"id":"field-2","value":{"type":"company-multi","data":[{"id":1},{"id":2}]}},{"id":"field-3","value":{"type":"datetime","data":"2023-01-01T00:00:00Z"}},{"id":"field-4","value":{"type":"dropdown","data":{"dropdownOptionId":1}}},{"id":"field-5","value":{"type":"dropdown-multi","data":[{"dropdownOptionId":1},{"dropdownOptionId":2}]}},{"id":"field-6","value":{"type":"location","data":{"streetAddress":"1 Main Street","city":"San Francisco","state":"California","country":"United States","continent":"North America"}}},{"id":"field-7","value":{"type":"location-multi","data":[{"streetAddress":"1 Main Street","city":"San Francisco","state":"California","country":"United States","continent":"North America"},{"streetAddress":"1600 Pennsylvania Avenue NW","city":"Washington","state":"DC","country":"United States","continent":"North America"}]}},{"id":"field-8","value":{"type":"number","data":100}},{"id":"field-9","value":{"type":"number-multi","data":[100,200,300]}},{"id":"field-10","value":{"type":"person","data":{"id":1}}},{"id":"field-11","value":{"type":"person-multi","data":[{"id":1},{"id":2}]}},{"id":"field-12","value":{"type":"ranked-dropdown","data":{"dropdownOptionId":1}}},{"id":"field-13","value":{"type":"text","data":"Some new text"}}]}'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListEntryBatchOperationResponse
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` | No |  |

Example: update-fields

```json
{
  "operation": "update-fields"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a single field value
`GET /v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}`

- **Tag:** lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields_fieldId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns a single field value on a list entry.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |
| `fieldId` | `string` | Yes | Field ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: Field
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

Example: company

```json
{
  "enrichmentSource": null,
  "id": "field-1",
  "name": "Field with company value",
  "type": "list",
  "value": {
    "data": {
      "domain": "acme.co",
      "id": 1,
      "name": "Acme"
    },
    "type": "company"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Update a single field value on a List Entry
`POST /v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}`

- **Tag:** lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields_fieldId__POST · **Stability:** `beta` · **Auth:** bearerAuth

Update a single field value.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |
| `fieldId` | `string` | Yes | Field ID |

#### Request Body

**Media type:** `application/json`
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | `oneOf` | No |  |

Example: company
```json
{
  "value": {
    "data": {
      "id": 1
    },
    "type": "company"
  }
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"value":{"type":"company","data":{"id":1}}}'
```

#### Responses

##### 204

No Content

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get metadata on Saved Views
`GET /v2/lists/{listId}/saved-views`

- **Tag:** lists · **OperationId:** v2_lists_listId_saved-views__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Saved Views you have access to view for a specific List.
Returns Saved View configurations including name, column settings, and owner information.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/saved-views' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: SavedViewPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of SavedView results |
| `pagination` | `object` | Yes |  |

**`data` details** — SavedView model See [SavedView](#savedview)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The saved view's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The saved view's name |
| `type` | `string (enum: `sheet`, `board`, `dashboard`)` | Yes | The type for this saved view |
| `createdAt` | `string<date-time>` | Yes | The date that the saved view was created |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "id": 28,
      "name": "my interesting companies",
      "type": "sheet"
    },
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "id": 28,
      "name": "my interesting companies",
      "type": "sheet"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get metadata on a single Saved View
`GET /v2/lists/{listId}/saved-views/{viewId}`

- **Tag:** lists · **OperationId:** v2_lists_listId_saved-views_viewId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve detailed information about a specific Saved View you have access to view.
Returns complete Saved View configuration including name, sorting, and column visibility settings.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `viewId` | `integer<int64>` | Yes | Saved view ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/saved-views/{viewId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: SavedView
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The saved view's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The saved view's name |
| `type` | `string (enum: `sheet`, `board`, `dashboard`)` | Yes | The type for this saved view |
| `createdAt` | `string<date-time>` | Yes | The date that the saved view was created |

Example

```json
{
  "createdAt": "2023-01-01T00:00:00Z",
  "id": 28,
  "name": "my interesting companies",
  "type": "sheet"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get all List Entries on a Saved View
`GET /v2/lists/{listId}/saved-views/{viewId}/list-entries`

- **Tag:** lists · **OperationId:** v2_lists_listId_saved-views_viewId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) on a given Saved View.
Use this endpoint when you need to filter entities or only want **some**
field data to be returned: This endpoint respects the filters set on a Saved View
via web app, and only returns field data corresponding to the columns that have been
pulled into the Saved View via web app.

Though this endpoint respects the Saved View's filters and column/Field selection,
it does not yet preserve sort order. This endpoint also only supports **sheet-type
Saved Views**, and not board- or dashboard-type Saved Views.

See the [Data Model](#section/Data-Model) section for more information about Saved Views.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `viewId` | `integer<int64>` | Yes | Saved view ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/saved-views/{viewId}/list-entries' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListEntryWithEntityPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array/null` | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## meetings

Operations about meetings

### Get metadata on all Meetings
`GET /v2/meetings`

- **Tag:** meetings · **OperationId:** v2_meetings__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Meetings in Affinity. Returns basic information about past and future meeting interactions
and its attendees.

You can filter meetings using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                     |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|----------------------------------|
| `id`                        | Unique identifier for Meetings                                  | `int64`    | `=`                                  | `id=1`                           |
| `startTime`                 | Start time of when Meeting was scheduled                        | `datetime` | `>`, `<`, `>=`, `<=`                 | `startTime>2025-01-01T01:00:00Z` |
| `createdAt`                 | When the Meeting was created in Affinity                        | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt`                 | When the Meeting was updated in Affinity                        | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-01-01T01:00:00Z`|

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/meetings' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: interactions.MeetingPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Meeting results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.Meeting](#interactionsmeeting)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The meeting's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string (enum: `automated`, `manual`)` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). |
| `title` | `string/null` | Yes | The meeting's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the meeting starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the meeting ends |
| `allDay` | `boolean` | Yes | Whether the meeting is all day |
| `creator` | `oneOf` | Yes | The person who created the meeting |
| `organizer` | `oneOf` | Yes | The person who organized the meeting |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the meeting was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the meeting was updated |
| `attendeesPreview` | `object` | Yes | A preview of the attendees in the meeting (Constraints: stability `beta`) |

**`attendeesPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## notes

Operations about notes

### Get all Notes
`GET /v2/notes`

- **Tag:** notes · **OperationId:** v2_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns all notes, with the exception of replies.
You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                    |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|---------------------------------|
| `id`                        | Filter notes by id                                              | `int32`    | `=`                                  | `id=1`                          |
| `creator.id`                | Filter notes by the creator of the note                         | `int32`    | `=`                                  | `creator.id=1`                  |
| `createdAt`                 | Filter notes by when it was created                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt`                 | Filter notes by when it was updated                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-02-03T10:48:24Z`|

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |
| `includes` | `array<string (enum: `companiesPreview`, `personsPreview`, `opportunitiesPreview`, `repliesCount`)>` | No | Additional properties to include in the response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/notes' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: notes.NotesPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note objects |
| `pagination` | `object` | Yes |  |

**`data` details** — Note model See [notes.Note](#notesnote)

**Items**

**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: ai-notetaker

```json
{
  "data": [
    {
      "content": {
        "html": "<p> This is an AI Notetaker note! </p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Doe",
        "primaryEmailAddress": "jane.doe@acme.co",
        "type": "internal"
      },
      "id": 1,
      "mentions": [],
      "type": "ai-notetaker",
      "updatedAt": "2023-01-21T00:00:00Z"
    },
    {
      "content": {
        "html": "<p> This is another AI Notetaker note! </p>"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Doe",
        "primaryEmailAddress": "jane.doe@acme.co",
        "type": "internal"
      },
      "id": 2,
      "mentions": [],
      "type": "ai-notetaker",
      "updatedAt": "2024-01-21T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/notes?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a single Note
`GET /v2/notes/{noteId}`

- **Tag:** notes · **OperationId:** v2_notes_noteId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Get a Note with a given id

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | The id of the Note |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includes` | `array<string (enum: `companiesPreview`, `personsPreview`, `opportunitiesPreview`, `repliesCount`)>` | No | Additional properties to include in the response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/notes/{noteId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: notes.Note
*Type:* oneOf
**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

Example: ai-notetaker

```json
{
  "content": {
    "html": "<p> This is an AI Notetaker note! </p>"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "creator": {
    "firstName": "Jane",
    "id": 1,
    "lastName": "Doe",
    "primaryEmailAddress": "jane.doe@acme.co",
    "type": "internal"
  },
  "id": 1,
  "mentions": [],
  "type": "ai-notetaker",
  "updatedAt": "2023-01-21T00:00:00Z"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Companies attached to a Note
`GET /v2/notes/{noteId}/attached-companies`

- **Tag:** notes · **OperationId:** v2_notes_noteId_attached-companies__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns directly attached companies for a given Note.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | The id of the Note to get attached Companies |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/notes/{noteId}/attached-companies' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyDataPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Company results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "domain": "acme.co",
      "id": 1,
      "name": "Acme"
    },
    {
      "domain": "acme.co",
      "id": 1,
      "name": "Acme"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Opportunities attached to a Note
`GET /v2/notes/{noteId}/attached-opportunities`

- **Tag:** notes · **OperationId:** v2_notes_noteId_attached-opportunities__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns directly attached opportunities for a given Note.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | The id of the Note to get attached Opportunities |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/notes/{noteId}/attached-opportunities' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: OpportunityPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Opportunity results |
| `pagination` | `object` | Yes |  |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: success

```json
{
  "data": [
    {
      "id": 1,
      "listId": 1000,
      "name": "Opp Name"
    },
    {
      "id": 2,
      "listId": 1001,
      "name": "Another Opp Name"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/notes/1/attached-opportunities?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/notes/1/attached-opportunities?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Persons attached to a Note
`GET /v2/notes/{noteId}/attached-persons`

- **Tag:** notes · **OperationId:** v2_notes_noteId_attached-persons__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns directly attached persons for a given Note.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | The id of the Note to get attached Persons |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/notes/{noteId}/attached-persons' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonDataPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Person results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "firstName": "Jane",
      "id": 1,
      "lastName": "Doe",
      "primaryEmailAddress": "jane.doe@acme.co",
      "type": "internal"
    },
    {
      "firstName": "Jane",
      "id": 1,
      "lastName": "Doe",
      "primaryEmailAddress": "jane.doe@acme.co",
      "type": "internal"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get replies for a Note
`GET /v2/notes/{noteId}/replies`

- **Tag:** notes · **OperationId:** v2_notes_noteId_replies__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


This endpoint returns reply notes for a given note id.
You can filter replies using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                    |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|---------------------------------|
| `creator.id`                | Filter notes by the creator of the note                         | `int32`    | `=`                                  | `creator.id=1`                  |
| `createdAt`                 | Filter notes by when it was created                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt`                 | Filter notes by when it was updated                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-02-03T10:48:24Z`|

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | Note ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/notes/{noteId}/replies' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: notes.RepliesPaged
*Type:* object
Replies for a Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note Replies |
| `pagination` | `object` | Yes |  |

**`data` details** — A Reply to a Note, created by a User or AI Notetaker. See [notes.Reply](#notesreply)

**Items**

**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: user-reply

```json
{
  "data": [
    {
      "content": {
        "html": "<p> This is a user reply note. <span data-type=\"note-mention\" data-note-mention-type=\"person\" data-note-mention-person-id=\"1\"> John Doe </span> was mentioned. </p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Doe",
        "primaryEmailAddress": "jane.doe@acme.co",
        "type": "internal"
      },
      "id": 2,
      "mentions": [
        {
          "id": 1,
          "person": {
            "firstName": "John",
            "id": 1,
            "lastName": "Doe",
            "primaryEmailAddress": "john.doe@acme.co",
            "type": "internal"
          },
          "type": "person"
        }
      ],
      "parent": {
        "id": 1
      },
      "type": "user-reply",
      "updatedAt": "2023-02-01T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/notes/1/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/notes/1/replies?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## opportunities

Operations about opportunities

### Get all Opportunities
`GET /v2/opportunities`

- **Tag:** opportunities · **OperationId:** v2_opportunities__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through Opportunities in Affinity.
Returns basic information but **not** field data on each Opportunity.

To access field data on Opportunities, use the `/lists/{list_id}/list-entries`
or the `/v2/lists/{list_id}/saved-views/{view_id}/list-entries` GET endpoint.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `ids` | `array<integer<int64>>` | No | Opportunity IDs |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/opportunities' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: OpportunityPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Opportunity results |
| `pagination` | `object` | Yes |  |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "id": 1,
      "listId": 1,
      "name": "Acme Upsell $10k"
    },
    {
      "id": 1,
      "listId": 1,
      "name": "Acme Upsell $10k"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a single Opportunity
`GET /v2/opportunities/{opportunityId}`

- **Tag:** opportunities · **OperationId:** v2_opportunities_opportunityId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns basic information but **not** field data on the requested Opportunity.

To access field data on Opportunities, use the `/lists/{list_id}/list-entries`
or the `/v2/lists/{list_id}/saved-views/{view_id}/list-entries` GET endpoint.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `opportunityId` | `integer<int64>` | Yes | Opportunity ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/opportunities/{opportunityId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: Opportunity
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

Example

```json
{
  "id": 1,
  "listId": 1,
  "name": "Acme Upsell $10k"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Notes for an Opportunity
`GET /v2/opportunities/{opportunityId}/notes`

- **Tag:** opportunities · **OperationId:** v2_opportunities_opportunityId_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns Notes for a given Opportunity which includes directly attached notes and those attached to persons on this Opportunity.

You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                    |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|---------------------------------|
| `creator.id`                | Filter notes by the creator of the note                         | `int32`    | `=`                                  | `creator.id=1`                  |
| `createdAt`                 | Filter notes by when it was created                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt`                 | Filter notes by when it was updated                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-02-03T10:48:24Z`|

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `opportunityId` | `integer<int64>` | Yes | Opportunity ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/opportunities/{opportunityId}/notes' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: notes.NotesPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note objects |
| `pagination` | `object` | Yes |  |

**`data` details** — Note model See [notes.Note](#notesnote)

**Items**

**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: entities

```json
{
  "data": [
    {
      "content": {
        "html": "<p>test</p><p>%</p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Doe",
        "primaryEmailAddress": "jane.doe@acme.co",
        "type": "internal"
      },
      "id": 1,
      "mentions": [
        {
          "id": 1,
          "person": {
            "firstName": "Jane",
            "id": 1,
            "lastName": "Doe",
            "primaryEmailAddress": "jane.doe@acme.co",
            "type": "internal"
          },
          "type": "person"
        }
      ],
      "permissions": {
        "owner": {
          "firstName": "Jane",
          "id": 1,
          "lastName": "Doe",
          "primaryEmailAddress": "jane.doe@acme.co",
          "type": "internal"
        },
        "sharingType": "private"
      },
      "type": "entities",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/1/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/persons/1/notes?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## personMerges

Operations about person merges

### Get All Person Merges
`GET /v2/person-merges`

- **Tag:** personMerges · **OperationId:** v2_person-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated person merges for the organization.

Returns all person merges initiated by users in your organization, including their current
status, the persons involved, and merge details. You can filter person merges using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| Property | Type | Operators | Values | Examples |
|----------|------|-----------|--------|----------|
| `status` | `enum` | `=` | `in-progress`, `success`, `failed` | `status=failed` |
| `taskId` | `string` | `=` | | `taskId=789e0123-e45b-67c8-d901-234567890123` |

Person merges are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and
organization admin role.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter person merges using Affinity Filtering Language |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/person-merges' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonMergeStatePaged
*Type:* object
Paginated person merge states
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of person merge states |
| `pagination` | `object` | Yes |  |

**`data` details** — Entity representing the state of an individual person merge See [PersonMergeState](#personmergestate)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryPersonId` | `integer<int64>` | Yes | ID of the primary person that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | ID of the duplicate person that was merged into the primary person (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: merges-list

```json
{
  "data": [
    {
      "completedAt": "2025-06-03T10:32:15Z",
      "duplicatePersonId": 67890,
      "errorMessage": null,
      "id": 12,
      "primaryPersonId": 12345,
      "startedAt": "2025-06-03T10:30:00Z",
      "status": "success",
      "taskId": "789e0123-e45b-67c8-d901-234567890123"
    },
    {
      "completedAt": "2025-06-03T09:16:30Z",
      "duplicatePersonId": 98765,
      "errorMessage": "Primary person not found",
      "id": 13,
      "primaryPersonId": 54321,
      "startedAt": "2025-06-03T09:15:00Z",
      "status": "failed",
      "taskId": "456e7890-1234-5678-9012-345678901234"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/merge?cursor=eyJpZCI6NDU2ZTc4OTAtZTEyYi0zNGM1LWQ2NzgtOTAxMjM0NTY3ODkwfQ==",
    "prevUrl": null
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Initiate Person Merge
`POST /v2/person-merges`

- **Tag:** personMerges · **OperationId:** v2_person-merges__POST · **Stability:** `beta` · **Auth:** bearerAuth

Initiate a person merge to combine a duplicate person profile into a primary person profile.

This is an asynchronous process that will merge all data from the duplicate person into the primary person. Once the merge is initiated, you can track its progress using the returned [task URL](#tag/personMerges/operation/v2_tasks_person-merges_taskId__GET).

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and organization admin role.

#### Request Body

**Media type:** `application/json`
Request body for initiating a person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `primaryPersonId` | `integer<int64>` | Yes | The ID of the person profile that will be kept after the merge. All data from the duplicate person will be merged into this person. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | The ID of the person profile that will be merged and then deleted. All data from this person will be transferred to the primary person. (Constraints: ≥ 1; ≤ 9007199254740991) |

Example: merge-persons
```json
{
  "duplicatePersonId": 67890,
  "primaryPersonId": 12345
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/person-merges' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"primaryPersonId":12345,"duplicatePersonId":67890}'
```

#### Responses

##### 202 — application/json

Accepted

**Response schema (`application/json`):**
###### Schema: PersonMergeResponse
*Type:* object
Response body for initiating a person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `taskUrl` | `string<uri>` | Yes | URL to check the status of the merge task |

Example: merge-initiated

```json
{
  "taskUrl": "https://api.affinity.co/v2/tasks/person-merges/123e4567-e89b-12d3-a456-426614174000"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Person Merge
`GET /v2/person-merges/{mergeId}`

- **Tag:** personMerges · **OperationId:** v2_person-merges_mergeId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific person merge.

Returns information about the person merge including its current status, the persons involved, timestamps, and any error information if the merge failed.

The `mergeId` can be obtained from the response of the [Get All Person Merges](#tag/personMerges/operation/v2_person-merges__GET) endpoint, or by filtering person merges by task ID using `/v2/person-merges?filter=taskId={taskId}` after initiating a merge.

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and organization admin role.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `mergeId` | `integer<int64>` | Yes | Person merge ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/person-merges/{mergeId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonMergeState
*Type:* object
Entity representing the state of an individual person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryPersonId` | `integer<int64>` | Yes | ID of the primary person that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | ID of the duplicate person that was merged into the primary person (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |

Example: completed-merge

```json
{
  "completedAt": "2025-06-03T10:32:15Z",
  "duplicatePersonId": 67890,
  "errorMessage": null,
  "id": 12345,
  "primaryPersonId": 12345,
  "startedAt": "2025-06-03T10:30:00Z",
  "status": "success",
  "taskId": "1b9684ad-e954-46d7-9684-ade95436d7dd"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get All Person Merge Tasks
`GET /v2/tasks/person-merges`

- **Tag:** personMerges · **OperationId:** v2_tasks_person-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated person merge tasks for the organization.

Returns all merge tasks initiated by users in your organization, including their current status,
the persons involved, and task details.

You can filter tasks using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| Property | Type | Operators | Values | Examples |
|----------|------|-----------|--------|----------|
| `status` | `enum` | `=` | `in-progress`, `success`, `failed` | `status=failed` |

Tasks are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and
organization admin role.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter tasks using Affinity Filtering Language |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/tasks/person-merges' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonMergeTaskPaged
*Type:* object
Paginated person merge tasks
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of person merge tasks |
| `pagination` | `object` | Yes |  |

**`data` details** — Person merge task details and status for batch operations See [PersonMergeTask](#personmergetask)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: tasks-list

```json
{
  "data": [
    {
      "id": "123e4567-e89b-12d3-a456-426614174000",
      "resultsSummary": {
        "failed": 0,
        "inProgress": 0,
        "success": 1,
        "total": 1
      },
      "status": "success"
    },
    {
      "id": "456e7890-e12b-34c5-d678-901234567890",
      "resultsSummary": {
        "failed": 1,
        "inProgress": 0,
        "success": 0,
        "total": 1
      },
      "status": "failed"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/tasks/person-merges?cursor=eyJpZCI6NDU2ZTc4OTAtZTEyYi0zNGM1LWQ2NzgtOTAxMjM0NTY3ODkwfQ==",
    "prevUrl": null
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Person Merge Task
`GET /v2/tasks/person-merges/{taskId}`

- **Tag:** personMerges · **OperationId:** v2_tasks_person-merges_taskId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific task for person merges.

Returns information about the person merges for a specific task including its overall status,
number of merges in-progress, completed, and failed.

Detailed information about individual merges for this task can be found by querying:
`/v2/person-merges?filter=taskId={taskId}` See [Person
Merges](#tag/personMerges/operation/v2_person-merges__GET) for more details.

Task statuses:

- `in-progress`: The merge task is currently being processed.
- `success`: The merge task completed successfully.
- `failed`: The merge task failed.

Requires the "Manage duplicates" [permission](#section/Getting-Started/Permissions) and
organization admin role.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `taskId` | `string<uuid>` | Yes | Person merge task ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/tasks/person-merges/{taskId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonMergeTask
*Type:* object
Person merge task details and status for batch operations
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |

Example: task-in-progress

```json
{
  "id": "456e7890-e12b-34c5-d678-901234567890",
  "resultsSummary": {
    "failed": 0,
    "inProgress": 1,
    "success": 0,
    "total": 1
  },
  "status": "in-progress"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## persons

Operations about persons

### Get all Persons
`GET /v2/persons`

- **Tag:** persons · **OperationId:** v2_persons__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through Persons in Affinity.
Returns basic information and non-list-specific field data on each Person.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/persons/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Persons will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export All People directory" [permission](#section/Getting-Started/Permissions).

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `ids` | `array<integer<int64>>` | No | People IDs |
| `fieldIds` | `array<string>` | No | Field IDs for which to return field data |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | Field Types for which to return field data |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Person results |
| `pagination` | `object` | Yes |  |

**`data` details** — Person model See [Person](#person)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "emailAddresses": [
        "jane.doe@acme.co",
        "janedoe@gmail.com"
      ],
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        }
      ],
      "firstName": "Jane",
      "id": 1,
      "lastName": "Doe",
      "primaryEmailAddress": "jane.doe@acme.co",
      "type": "internal"
    },
    {
      "emailAddresses": [
        "jane.doe@acme.co",
        "janedoe@gmail.com"
      ],
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        }
      ],
      "firstName": "Jane",
      "id": 1,
      "lastName": "Doe",
      "primaryEmailAddress": "jane.doe@acme.co",
      "type": "internal"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get metadata on Person Fields
`GET /v2/persons/fields`

- **Tag:** persons · **OperationId:** v2_persons_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns metadata on non-list-specific Person Fields.

Use the returned Field IDs to request field data from the GET `/v2/persons` and GET `/v2/persons/{id}` endpoints.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldMetadataPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of FieldMetadata results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [FieldMetadata](#fieldmetadata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `valueType` | `string (enum: `person`, `person-multi`, `company`, `company-multi`, `filterable-text`, …)` | Yes | The type of the data in this Field |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a single Person
`GET /v2/persons/{personId}`

- **Tag:** persons · **OperationId:** v2_persons_personId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns basic information and non-list-specific field data on the requested Person.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/persons/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Persons will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export All People directory" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldIds` | `array<string>` | No | Field IDs for which to return field data |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | Field Types for which to return field data |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: Person
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

Example

```json
{
  "emailAddresses": [
    "jane.doe@acme.co",
    "janedoe@gmail.com"
  ],
  "fields": [
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "name": "Location",
      "type": "enriched",
      "value": {
        "data": {
          "city": "San Francisco",
          "continent": "North America",
          "country": "United States",
          "state": "California",
          "streetAddress": "1 Main Street"
        },
        "type": "location"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "name": "Location",
      "type": "enriched",
      "value": {
        "data": {
          "city": "San Francisco",
          "continent": "North America",
          "country": "United States",
          "state": "California",
          "streetAddress": "1 Main Street"
        },
        "type": "location"
      }
    }
  ],
  "firstName": "Jane",
  "id": 1,
  "lastName": "Doe",
  "primaryEmailAddress": "jane.doe@acme.co",
  "type": "internal"
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a Person's List Entries
`GET /v2/persons/{personId}/list-entries`

- **Tag:** persons · **OperationId:** v2_persons_personId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) for the given Person across all Lists.
Each List Entry includes field data for the Person, including list-specific field data.
Each List Entry also includes metadata about its creation, i.e., when it was added to the List and by whom.

Requires the "Export data from Lists" [permission](#section/Getting-Started/Permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Persons ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/list-entries' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListEntryPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ListEntry results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [ListEntry](#listentry)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | Yes | The fields associated with the list entry |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        }
      ],
      "id": 1,
      "listId": 1
    },
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "fields": [
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        },
        {
          "enrichmentSource": "affinity-data",
          "id": "affinity-data-location",
          "name": "Location",
          "type": "enriched",
          "value": {
            "data": {
              "city": "San Francisco",
              "continent": "North America",
              "country": "United States",
              "state": "California",
              "streetAddress": "1 Main Street"
            },
            "type": "location"
          }
        }
      ],
      "id": 1,
      "listId": 1
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 403 — application/json

Forbidden

**Response schema (`application/json`):**
###### Schema: AuthorizationErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "authorization",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get a Person's Lists
`GET /v2/persons/{personId}/lists`

- **Tag:** persons · **OperationId:** v2_persons_personId_lists__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Lists where the given Person appears as an entry and that you have access to view.
Returns basic List information for each List that contains this Person.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Persons ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/lists' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: ListPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of List results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [List](#list)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example

```json
{
  "data": [
    {
      "creatorId": 1,
      "id": 1,
      "isPublic": false,
      "name": "All companies",
      "ownerId": 1
    },
    {
      "creatorId": 1,
      "id": 1,
      "isPublic": false,
      "name": "All companies",
      "ownerId": 1
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/foo?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

### Get Notes for a Person
`GET /v2/persons/{personId}/notes`

- **Tag:** persons · **OperationId:** v2_persons_personId_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns notes for a given person id which includes directly attached notes, notes on meetings this person attended, and notes where this person is mentioned.

You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name**           | **Description**                                                 | **Type**   | **Allowed Operators**                | **Examples**                    |
|-----------------------------|-----------------------------------------------------------------|------------|--------------------------------------|---------------------------------|
| `creator.id`                | Filter notes by the creator of the note                         | `int32`    | `=`                                  | `creator.id=1`                  |
| `createdAt`                 | Filter notes by when it was created                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt`                 | Filter notes by when it was updated                             | `datetime` | `>`, `<`, `>=`, `<=`                 | `updatedAt>=2025-02-03T10:48:24Z`|

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Persons ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/notes' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: notes.NotesPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note objects |
| `pagination` | `object` | Yes |  |

**`data` details** — Note model See [notes.Note](#notesnote)

**Items**

**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |

Example: entities

```json
{
  "data": [
    {
      "content": {
        "html": "<p>test</p><p>%</p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Doe",
        "primaryEmailAddress": "jane.doe@acme.co",
        "type": "internal"
      },
      "id": 1,
      "mentions": [
        {
          "id": 1,
          "person": {
            "firstName": "Jane",
            "id": 1,
            "lastName": "Doe",
            "primaryEmailAddress": "jane.doe@acme.co",
            "type": "internal"
          },
          "type": "person"
        }
      ],
      "permissions": {
        "owner": {
          "firstName": "Jane",
          "id": 1,
          "lastName": "Doe",
          "primaryEmailAddress": "jane.doe@acme.co",
          "type": "internal"
        },
        "sharingType": "private"
      },
      "type": "entities",
      "updatedAt": "2023-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/1/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/persons/1/notes?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 400 — application/json

Bad Request

**Response schema (`application/json`):**
###### Schema: responses.400
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes |  |

**`errors` details**

**Items**

**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### 404 — application/json

Not Found

**Response schema (`application/json`):**
###### Schema: NotFoundErrors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |

Example

```json
{
  "errors": [
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    },
    {
      "code": "not-found",
      "message": "ð¨ Error! Sound the alarm! ð¨"
    }
  ]
}
```

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

##### DEFAULT — application/json

Errors

**Response schema (`application/json`):**
###### Schema: Errors
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |

**Response Headers**
| Header | Type | Description |
| --- | --- | --- |
| `X-Ratelimit-Limit-User` | `integer` | Number of requests allowed per minute for the user |
| `X-Ratelimit-Limit-User-Remaining` | `integer` | Number of requests remaining for the user |
| `X-Ratelimit-Limit-User-Reset` | `integer` | Time in seconds before the limit resets for the user |
| `X-Ratelimit-Limit-Org` | `integer` | Number of requests allowed per month for the account |
| `X-Ratelimit-Limit-Org-Remaining` | `integer` | Number of requests remaining for the account |
| `X-Ratelimit-Limit-Org-Reset` | `integer` | Time in seconds before the limit resets for the account |

## Schema Reference
### Attendee
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### AttendeesPreview
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### AuthorizationErrors
AuthorizationErrors model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | AuthorizationError errors |

**`errors` details** — See [AuthorizationError](#authorizationerror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### ChatMessage
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The chat message's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `direction` | `string (enum: `received`, `sent`)` | Yes | The direction of the chat message |
| `sentAt` | `string<date-time>` | Yes | The time the chat message was sent |
| `manualCreator` | `object` | Yes |  |
| `participants` | `array<object>` | Yes | The participants of the chat |

**`manualCreator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`participants` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### CompaniesValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many companies |
### CompaniesValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many companies |
### Company
Company model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### CompanyData
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
### CompanyDataPaged
CompanyDataPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Company results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### CompanyListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes | Company model |

**`entity` details** — See [Company](#company)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### CompanyMergeRequest
Request body for initiating a company merge
Request body for initiating a company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `primaryCompanyId` | `integer<int64>` | Yes | The ID of the company profile that will be kept after the merge. All data from the duplicate company will be merged into this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | The ID of the company profile that will be merged and then deleted. All data from this company will be transferred to the primary company. (Constraints: ≥ 1; ≤ 9007199254740991) |
### CompanyMergeResponse
Response body for initiating a company merge
Response body for initiating a company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `taskUrl` | `string<uri>` | Yes | URL to check the status of the merge task |
### CompanyMergeState
Entity representing the state of an individual company merge
Entity representing the state of an individual company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryCompanyId` | `integer<int64>` | Yes | ID of the primary company that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | ID of the duplicate company that was merged into the primary company (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |
### CompanyMergeStatePaged
Paginated list of company merge states
Paginated list of company merge states
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of company merge states |
| `pagination` | `object` | Yes |  |

**`data` details** — Entity representing the state of an individual company merge See [CompanyMergeState](#companymergestate)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryCompanyId` | `integer<int64>` | Yes | ID of the primary company that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | ID of the duplicate company that was merged into the primary company (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### CompanyMergeTask
Company merge task details and status for batch operations
Company merge task details and status for batch operations
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |
### CompanyMergeTaskPaged
Paginated list of company merge tasks
Paginated list of company merge tasks
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of company merge tasks |
| `pagination` | `object` | Yes |  |

**`data` details** — Company merge task details and status for batch operations See [CompanyMergeTask](#companymergetask)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### CompanyPaged
CompanyPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Company results |
| `pagination` | `object` | Yes |  |

**`data` details** — Company model See [Company](#company)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### CompanyReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### CompanyValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### CompanyValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### DateValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `string/null<date-time>` | Yes | The value for a date |
### Dropdown
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown item text |
### DropdownReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### DropdownValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### DropdownValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### DropdownsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many dropdown items |
### DropdownsValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many dropdown items |
### Email
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `subject` | `string/null` | Yes | The subject of the email |
| `sentAt` | `string<date-time>` | Yes | The time the email was sent |
| `from` | `object` | Yes |  |
| `to` | `array<object>` | Yes | The recipients of the email |
| `cc` | `array<object>` | Yes | The cc recipients of the email |

**`from` details** — See [Attendee](#attendee)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`to` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`cc` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### Error
**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |
### Errors
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` | Yes | Errors |

**`errors` details** — See [Error](#error)

**Items**

**Variant:** AuthenticationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** AuthorizationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** BadRequestError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
**Variant:** ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |
### Field
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### FieldMetadata
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `valueType` | `string (enum: `person`, `person-multi`, `company`, `company-multi`, `filterable-text`, …)` | Yes | The type of the data in this Field |
### FieldMetadataPaged
FieldMetadataPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of FieldMetadata results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [FieldMetadata](#fieldmetadata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `valueType` | `string (enum: `person`, `person-multi`, `company`, `company-multi`, `filterable-text`, …)` | Yes | The type of the data in this Field |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### FieldPaged
FieldPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Field results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### FieldUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | `oneOf` | No |  |
### FieldValue
**Variant:** CompaniesValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many companies |
**Variant:** CompanyValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** DateValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `string/null<date-time>` | Yes | The value for a date |
**Variant:** DropdownsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many dropdown items |
**Variant:** DropdownValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** FloatsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many numbers |
**Variant:** FloatValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `number/null` | Yes | The value for a number |
**Variant:** FormulaValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** InteractionValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** LocationsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many locations |
**Variant:** LocationValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** PersonsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many persons |
**Variant:** PersonValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** RankedDropdownValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** TextsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many strings |
**Variant:** TextValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `text`)` | Yes | The type of value |
| `data` | `string/null` | Yes | The value for a string |
### FieldValueUpdate
**Variant:** CompaniesValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many companies |
**Variant:** CompanyValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** DateValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `string/null<date-time>` | Yes | The value for a date |
**Variant:** DropdownValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** DropdownsValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many dropdown items |
**Variant:** FloatValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `number/null` | Yes | The value for a number |
**Variant:** FloatsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many numbers |
**Variant:** LocationValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** LocationsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many locations |
**Variant:** PersonValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** PersonsValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many persons |
**Variant:** RankedDropdownValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
**Variant:** TextValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `text`)` | Yes | The type of value |
| `data` | `string/null` | Yes | The value for a string |
**Variant:** TextsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many strings |
### FloatValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `number/null` | Yes | The value for a number |
### FloatsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many numbers |
### FormulaNumber
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `calculatedValue` | `number/null` | No | Calculated value |
### FormulaValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### Grant
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `api-key`, `access-token`)` | Yes | The type of grant used to authenticate |
| `scopes` | `array<string>` | Yes | The scopes available to the current grant |
| `createdAt` | `string<date-time>` | Yes | When the grant was created |

**`scopes` details** — The scopes available to the current grant

**Items**
### Interaction
**Variant:** ChatMessage
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The chat message's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `direction` | `string (enum: `received`, `sent`)` | Yes | The direction of the chat message |
| `sentAt` | `string<date-time>` | Yes | The time the chat message was sent |
| `manualCreator` | `object` | Yes |  |
| `participants` | `array<object>` | Yes | The participants of the chat |

**`manualCreator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`participants` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** Email
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `subject` | `string/null` | Yes | The subject of the email |
| `sentAt` | `string<date-time>` | Yes | The time the email was sent |
| `from` | `object` | Yes |  |
| `to` | `array<object>` | Yes | The recipients of the email |
| `cc` | `array<object>` | Yes | The cc recipients of the email |

**`from` details** — See [Attendee](#attendee)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`to` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`cc` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
**Variant:** Meeting
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The meeting's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `title` | `string/null` | Yes | The meeting's title |
| `allDay` | `boolean` | Yes | Whether the meeting is an all-day event |
| `startTime` | `string<date-time>` | Yes | The meeting start time |
| `endTime` | `string/null<date-time>` | Yes | The meeting end time |
| `attendees` | `array<object>` | Yes | People attending the meeting |

**`attendees` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
**Variant:** PhoneCall
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The phone call's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `startTime` | `string<date-time>` | Yes | The call start time |
| `attendees` | `array<object>` | Yes | People attending the call |

**`attendees` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### InteractionValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### List
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
### ListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | Yes | The fields associated with the list entry |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### ListEntryBatchOperationRequest
**Variant:** ListEntryBatchOperationUpdateFields
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` | Yes |  |

**`updates` details**

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier. |
| `value` | `oneOf` | No |  |
### ListEntryBatchOperationResponse
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` | No |  |
### ListEntryBatchOperationUpdateFields
Update multiple field values.
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` | Yes |  |

**`updates` details**

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier. |
| `value` | `oneOf` | No |  |
### ListEntryBatchOperations
Allowed values: `update-fields`
### ListEntryPaged
ListEntryPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ListEntry results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [ListEntry](#listentry)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | Yes | The fields associated with the list entry |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### ListEntryWithEntity
**Variant:** CompanyListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes | Company model |

**`entity` details** — See [Company](#company)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` | No | The fields associated with the company |

**`domains` details** — All of the company's domains

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
**Variant:** OpportunityListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes |  |

**`entity` details** — See [OpportunityWithFields](#opportunitywithfields)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | No | The fields associated with the opportunity |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
**Variant:** PersonListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes | Person model |

**`entity` details** — See [Person](#person)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### ListEntryWithEntityPaged
ListEntryWithEntityPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array/null` | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### ListPaged
ListPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of List results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [List](#list)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### ListWithType
ListWithType model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for this list |
### ListWithTypePaged
ListWithTypePaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ListWithType results |
| `pagination` | `object` | Yes |  |

**`data` details** — ListWithType model See [ListWithType](#listwithtype)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for this list |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### Location
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `streetAddress` | `string/null` | Yes | Street address |
| `city` | `string/null` | Yes | City |
| `state` | `string/null` | Yes | State |
| `country` | `string/null` | Yes | Country |
| `continent` | `string/null` | Yes | Continent |
### LocationValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### LocationsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many locations |
### Meeting
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The meeting's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `title` | `string/null` | Yes | The meeting's title |
| `allDay` | `boolean` | Yes | Whether the meeting is an all-day event |
| `startTime` | `string<date-time>` | Yes | The meeting start time |
| `endTime` | `string/null<date-time>` | Yes | The meeting end time |
| `attendees` | `array<object>` | Yes | People attending the meeting |

**`attendees` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### MethodNotAllowedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### NotAcceptableError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### NotFoundError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### NotFoundErrors
NotFoundErrors model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` | Yes | NotFoundError errors |

**`errors` details** — See [NotFoundError](#notfounderror)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### Opportunity
Opportunity model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
### OpportunityListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes |  |

**`entity` details** — See [OpportunityWithFields](#opportunitywithfields)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | No | The fields associated with the opportunity |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### OpportunityPaged
OpportunityPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Opportunity results |
| `pagination` | `object` | Yes |  |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### OpportunityWithFields
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` | No | The fields associated with the opportunity |

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### Pagination
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### PaginationWithTotalCount
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### Person
Person model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### PersonData
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### PersonDataPaged
PersonDataPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Person results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### PersonDataPreview
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of persons |
| `totalCount` | `integer<int64>` | Yes | The total count of persons (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### PersonListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` | Yes | Person model |

**`entity` details** — See [Person](#person)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |
### PersonMergeRequest
Request body for initiating a person merge
Request body for initiating a person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `primaryPersonId` | `integer<int64>` | Yes | The ID of the person profile that will be kept after the merge. All data from the duplicate person will be merged into this person. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | The ID of the person profile that will be merged and then deleted. All data from this person will be transferred to the primary person. (Constraints: ≥ 1; ≤ 9007199254740991) |
### PersonMergeResponse
Response body for initiating a person merge
Response body for initiating a person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `taskUrl` | `string<uri>` | Yes | URL to check the status of the merge task |
### PersonMergeState
Entity representing the state of an individual person merge
Entity representing the state of an individual person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryPersonId` | `integer<int64>` | Yes | ID of the primary person that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | ID of the duplicate person that was merged into the primary person (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |
### PersonMergeStatePaged
Paginated person merge states
Paginated person merge states
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of person merge states |
| `pagination` | `object` | Yes |  |

**`data` details** — Entity representing the state of an individual person merge See [PersonMergeState](#personmergestate)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the merge (Constraints: ≥ 1; ≤ 9007199254740991) |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | Current status of the merge |
| `taskId` | `string<uuid>` | Yes | Identifier for the task this merge belongs to |
| `startedAt` | `string<date-time>` | Yes | Timestamp when the merge started |
| `primaryPersonId` | `integer<int64>` | Yes | ID of the primary person that other profiles were merged into (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | ID of the duplicate person that was merged into the primary person (Constraints: ≥ 1; ≤ 9007199254740991) |
| `completedAt` | `string/null<date-time>` | Yes | Timestamp when the merge completed (success or failure) |
| `errorMessage` | `string/null` | Yes | Error message if the merge failed |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### PersonMergeTask
Person merge task details and status for batch operations
Person merge task details and status for batch operations
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |
### PersonMergeTaskPaged
Paginated person merge tasks
Paginated person merge tasks
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | Array of person merge tasks |
| `pagination` | `object` | Yes |  |

**`data` details** — Person merge task details and status for batch operations See [PersonMergeTask](#personmergetask)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string<uuid>` | Yes | The unique identifier for this merge task |
| `status` | `string (enum: `in-progress`, `success`, `failed`)` | Yes | The current status of the batch operation |
| `resultsSummary` | `object` | Yes | Summary of merges in this batch task |

**`resultsSummary` details** — Summary of merges in this batch task

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `total` | `integer<int32>` | Yes | Total number of merges in the batch (Constraints: ≥ 0; ≤ 2147483647) |
| `inProgress` | `integer<int32>` | Yes | Number of merges currently in progress (Constraints: ≥ 0; ≤ 2147483647) |
| `success` | `integer<int32>` | Yes | Number of successfully completed merges (Constraints: ≥ 0; ≤ 2147483647) |
| `failed` | `integer<int32>` | Yes | Number of failed merges (Constraints: ≥ 0; ≤ 2147483647) |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### PersonPaged
PersonPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Person results |
| `pagination` | `object` | Yes |  |

**`data` details** — Person model See [Person](#person)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type |
| `fields` | `array<object>` | No | The fields associated with the person |

**`emailAddresses` details** — All of the person's email addresses

**Items**

**`fields` details** — See [Field](#field)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | `oneOf` | Yes |  |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### PersonReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### PersonValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### PersonValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### PersonsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many persons |
### PersonsValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The values for many persons |
### PhoneCall
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The phone call's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `startTime` | `string<date-time>` | Yes | The call start time |
| `attendees` | `array<object>` | Yes | People attending the call |

**`attendees` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### RankedDropdown
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown item text |
| `rank` | `integer<int64>` | Yes | Dropdown item rank (Constraints: ≥ 0; ≤ 9007199254740991) |
| `color` | `string/null` | Yes | Dropdown item color |
### RankedDropdownReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dropdownOptionId` | `integer<int64>` | Yes | Ranked Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### RankedDropdownValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### RankedDropdownValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `oneOf` | Yes |  |
### RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### SavedView
SavedView model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The saved view's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The saved view's name |
| `type` | `string (enum: `sheet`, `board`, `dashboard`)` | Yes | The type for this saved view |
| `createdAt` | `string<date-time>` | Yes | The date that the saved view was created |
### SavedViewPaged
SavedViewPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of SavedView results |
| `pagination` | `object` | Yes |  |

**`data` details** — SavedView model See [SavedView](#savedview)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The saved view's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The saved view's name |
| `type` | `string (enum: `sheet`, `board`, `dashboard`)` | Yes | The type for this saved view |
| `createdAt` | `string<date-time>` | Yes | The date that the saved view was created |

**`pagination` details** — See [Pagination](#pagination)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### Tenant
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The tenant's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the tenant |
| `subdomain` | `string<hostname>` | Yes | The tenant's subdomain under affinity.co |
### TextValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `text`)` | Yes | The type of value |
| `data` | `string/null` | Yes | The value for a string |
### TextsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` | Yes | The value for many strings |
### UnprocessableEntityError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### UnsupportedMediaTypeError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### User
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The user's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The user's first name |
| `lastName` | `string/null` | Yes | The user's last name |
| `emailAddress` | `string<email>` | Yes | The user's email address |
### ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |
### WhoAmI
WhoAmI model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `tenant` | `object` | Yes |  |
| `user` | `object` | Yes |  |
| `grant` | `object` | Yes |  |

**`tenant` details** — See [Tenant](#tenant)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The tenant's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the tenant |
| `subdomain` | `string<hostname>` | Yes | The tenant's subdomain under affinity.co |

**`user` details** — See [User](#user)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The user's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The user's first name |
| `lastName` | `string/null` | Yes | The user's last name |
| `emailAddress` | `string<email>` | Yes | The user's email address |

**`grant` details** — See [Grant](#grant)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `api-key`, `access-token`)` | Yes | The type of grant used to authenticate |
| `scopes` | `array<string>` | Yes | The scopes available to the current grant |
| `createdAt` | `string<date-time>` | Yes | When the grant was created |

**`scopes` details** — The scopes available to the current grant

**Items**
### interactions.Call
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The call's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, calls can only be logged as 'manual'. |
| `title` | `string/null` | Yes | The call's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the call starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the call ends |
| `allDay` | `boolean` | Yes | Whether the call is all day |
| `creator` | `oneOf` | Yes | The person who created the call |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the call was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the call was updated |
| `attendeesPreview` | `object` | Yes | A preview of the attendees in the call (Constraints: stability `beta`) |

**`attendeesPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### interactions.CallPaged
CallPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Call results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.Call](#interactionscall)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The call's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, calls can only be logged as 'manual'. |
| `title` | `string/null` | Yes | The call's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the call starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the call ends |
| `allDay` | `boolean` | Yes | Whether the call is all day |
| `creator` | `oneOf` | Yes | The person who created the call |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the call was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the call was updated |
| `attendeesPreview` | `object` | Yes | A preview of the attendees in the call (Constraints: stability `beta`) |

**`attendeesPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### interactions.ChatMessage
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The chat message's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the chat message was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, chat messages can only be logged as 'manual'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the chat message |
| `creator` | `object` | Yes | The creator of the chat message |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the chat message was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the chat message was updated |
| `participantsPreview` | `object` | Yes | A preview of the participants who are in the chat message (Constraints: stability `beta`) |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`participantsPreview` details** — See [interactions.PersonDataPreview](#interactionspersondatapreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of persons |
| `totalCount` | `integer<int64>` | Yes | The total count of persons (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### interactions.ChatMessagePaged
ChatMessagePaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of ChatMessage results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.ChatMessage](#interactionschatmessage)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The chat message's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the chat message was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, chat messages can only be logged as 'manual'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the chat message |
| `creator` | `object` | Yes | The creator of the chat message |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the chat message was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the chat message was updated |
| `participantsPreview` | `object` | Yes | A preview of the participants who are in the chat message (Constraints: stability `beta`) |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`participantsPreview` details** — See [interactions.PersonDataPreview](#interactionspersondatapreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of persons |
| `totalCount` | `integer<int64>` | Yes | The total count of persons (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### interactions.Email
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the email was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, emails can only be logged as 'automated'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the email: 'sent' if the email was sent by an internal user and  'received' if the email was sent to an internal user. |
| `subject` | `string/null` | Yes | The email's subject |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the email was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the email was updated |
| `from` | `object` | Yes | The participant who sent the email |
| `toParticipantsPreview` | `object` | Yes | A preview of the participants in the 'To' field of the email (Constraints: stability `beta`) |
| `ccParticipantsPreview` | `object` | Yes | A preview of the participants who are cc'ed in the email (Constraints: stability `beta`) |

**`from` details** — See [Attendee](#attendee)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`toParticipantsPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`ccParticipantsPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### interactions.EmailPaged
EmailPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Email results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.Email](#interactionsemail)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the email was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, emails can only be logged as 'automated'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the email: 'sent' if the email was sent by an internal user and  'received' if the email was sent to an internal user. |
| `subject` | `string/null` | Yes | The email's subject |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the email was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the email was updated |
| `from` | `object` | Yes | The participant who sent the email |
| `toParticipantsPreview` | `object` | Yes | A preview of the participants in the 'To' field of the email (Constraints: stability `beta`) |
| `ccParticipantsPreview` | `object` | Yes | A preview of the participants who are cc'ed in the email (Constraints: stability `beta`) |

**`from` details** — See [Attendee](#attendee)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`toParticipantsPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`ccParticipantsPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### interactions.Meeting
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The meeting's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string (enum: `automated`, `manual`)` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). |
| `title` | `string/null` | Yes | The meeting's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the meeting starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the meeting ends |
| `allDay` | `boolean` | Yes | Whether the meeting is all day |
| `creator` | `oneOf` | Yes | The person who created the meeting |
| `organizer` | `oneOf` | Yes | The person who organized the meeting |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the meeting was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the meeting was updated |
| `attendeesPreview` | `object` | Yes | A preview of the attendees in the meeting (Constraints: stability `beta`) |

**`attendeesPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |
### interactions.MeetingPaged
MeetingPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A page of Meeting results |
| `pagination` | `object` | Yes |  |

**`data` details** — See [interactions.Meeting](#interactionsmeeting)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The meeting's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string (enum: `automated`, `manual`)` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). |
| `title` | `string/null` | Yes | The meeting's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the meeting starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the meeting ends |
| `allDay` | `boolean` | Yes | Whether the meeting is all day |
| `creator` | `oneOf` | Yes | The person who created the meeting |
| `organizer` | `oneOf` | Yes | The person who organized the meeting |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the meeting was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the meeting was updated |
| `attendeesPreview` | `object` | Yes | A preview of the attendees in the meeting (Constraints: stability `beta`) |

**`attendeesPreview` details** — See [interactions.AttendeesPreview](#interactionsattendeespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [Attendee](#attendee)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | `oneOf` | Yes |  |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.BaseNote
An abstract base class for notes
An abstract base class for notes
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.BaseReply
An abstract base class for note replies, either of a UserNoteReply or AiNotetakerNoteReply
An abstract base class for note replies, either of a UserNoteReply or AiNotetakerNoteReply
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.BaseRootNote
A root note
A root note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.CallInteraction
This is a Call (Event) object attached to a note
This is a Call (Event) object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Call (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.ChatMessageInteraction
A ChatMessage object attached to a note
A ChatMessage object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the ChatMessage (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.CompaniesPreview
A preview for attached Companies on a Note
A preview for attached Companies on a Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
### notes.Content
A note content
A note content
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |
### notes.EmailInteraction
This is an Email object attached to a note
This is an Email object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Email (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.Interaction
An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage.
An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage.
**Variant:** notes.MeetingInteraction
This is a Meeting (Event) object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
**Variant:** notes.CallInteraction
This is a Call (Event) object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Call (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
**Variant:** notes.ChatMessageInteraction
A ChatMessage object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the ChatMessage (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
**Variant:** notes.EmailInteraction
This is an Email object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Email (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.MeetingInteraction
This is a Meeting (Event) object attached to a note
This is a Meeting (Event) object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.Mention
A mention in a note.
A mention in a note.
**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.Note
Note model
**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.NotesPaged
NotesPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note objects |
| `pagination` | `object` | Yes |  |

**`data` details** — Note model See [notes.Note](#notesnote)

**Items**

**Variant:** notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `oneOf` | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `permissions` | `object` | No | The permission settings of a note (Constraints: stability `beta`) |
| `opportunitiesPreview` | `object` | No | A preview for attached Opportunities on a Note (Constraints: stability `beta`) |
| `personsPreview` | `object` | No | A preview for attached Persons on a Note (Constraints: stability `beta`) |
| `companiesPreview` | `object` | No | A preview for attached Companies on a Note (Constraints: stability `beta`) |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`permissions` details** — See [notes.PermissionSettings](#notespermissionsettings)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`opportunitiesPreview` details** — See [notes.OpportunitiesPreview](#notesopportunitiespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |

**`personsPreview` details** — See [notes.PersonsPreview](#notespersonspreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`companiesPreview` details** — See [notes.CompaniesPreview](#notescompaniespreview)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Companies for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [CompanyData](#companydata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### notes.OpportunitiesPreview
A preview for attached Opportunities on a Note
A preview for attached Opportunities on a Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Opportunities for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — Opportunity model See [Opportunity](#opportunity)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
### notes.PermissionSettings
The permission settings of a note
The permission settings of a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharingType` | `string (enum: `private`, `public`, `custom`)` | Yes | The sharing type of the note |
| `owner` | `object` | Yes |  |

**`owner` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.PersonMention
A person mentioned in a note.
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.PersonsPreview
A preview for attached Persons on a Note
A preview for attached Persons on a Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` | No | Preview of attached Persons for a Note |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |

**`data` details** — See [PersonData](#persondata)

**Items**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.RepliesPaged
Replies for a Note
Replies for a Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` | Yes | A page of Note Replies |
| `pagination` | `object` | Yes |  |

**`data` details** — A Reply to a Note, created by a User or AI Notetaker. See [notes.Reply](#notesreply)

**Items**

**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`pagination` details** — See [PaginationWithTotalCount](#paginationwithtotalcount)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int64>` | No | The total count of the collection. Only included if requested via the totalCount query string parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `prevUrl` | `string/null<uri>` | No | URL for the previous page |
| `nextUrl` | `string/null<uri>` | No | URL for the next page |
### notes.Reply
A Reply to a Note, created by a User or AI Notetaker.
A Reply to a Note, created by a User or AI Notetaker.
**Variant:** notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
**Variant:** notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` | No | The meeting this AI Notetaker was invited to. (Constraints: stability `beta`) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`interaction` details** — See [notes.MeetingInteraction](#notesmeetinginteraction)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |
### notes.UserReplyNote
A reply to a note created by a user
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` | Yes | A note content (Constraints: stability `beta`) |
| `creator` | `object` | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

**`content` details** — See [notes.Content](#notescontent)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |

**`creator` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

**`mentions` details** — A mention in a note. See [notes.Mention](#notesmention)

**Items**

**Variant:** notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` | Yes |  |

**`person` details** — See [PersonData](#persondata)

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `external`, `collaborator`)` | Yes | The person's type |

## Error Reference

The API returns structured errors with a `code` discriminator.
| Error Code | Schema |
| --- | --- |
| `authentication` | AuthenticationError |
| `authorization` | AuthorizationError |
| `bad-request` | BadRequestError |
| `conflict` | ConflictError |
| `method-not-allowed` | MethodNotAllowedError |
| `not-acceptable` | NotAcceptableError |
| `not-found` | NotFoundError |
| `not-implemented` | NotImplementedError |
| `rate-limit` | RateLimitError |
| `server` | ServerError |
| `unprocessable-entity` | UnprocessableEntityError |
| `unsupported-media-type` | UnsupportedMediaTypeError |
| `validation` | ValidationError |
