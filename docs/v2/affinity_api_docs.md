# Affinity API v2 Documentation (Auto-synced)

> **⚠️ IMPORTANT DISCLAIMER**
>
> **This is an UNOFFICIAL markdown copy of the Affinity API v2 documentation.** The official and authoritative documentation is maintained by Affinity at:
>
> **📚 Official Documentation:** [https://developer.affinity.co/api-reference/openapi.json](https://developer.affinity.co/api-reference/openapi.json)
>
> **Always refer to the official Affinity documentation for the most up-to-date and accurate information.**

> **API version:** This copy documents Affinity API v2 version **2026-09-17**. Each app (API key) has a Default API Version, set in Settings > Manage Apps, and a request can override it with the `X-Affinity-Api-Version` header. If your app defaults to an older version, some fields and endpoints described here will differ. See [Versioning](pages/versioning.md) and [Version Migration](pages/version-migration.md).

> **For AI agents:** Affinity publishes AI-ready v2 docs for every API version: an index at [developer.affinity.co/llms.txt](https://developer.affinity.co/llms.txt) with per-endpoint Markdown pages, and a docs MCP server at `https://developer.affinity.co/mcp` (documentation search only; not the authenticated Affinity MCP server for CRM data). This copy links nested schemas to the Schema Reference instead of repeating them.

---

## About This Document

This markdown version of the Affinity API v2 documentation was generated automatically to provide:

- **Better compatibility with AI coding assistants**
- **Offline access**
- **Text-based search**
- **Version control**
- **Direct raw access**

**Source:** Extracted from the live Affinity API documentation at https://developer.affinity.co/api-reference/openapi.json

> **Note:** The live site renders dynamic multi-language request/response samples in-browser. Because those snippets are generated at runtime and are not embedded in the OpenAPI payload, they cannot be mirrored here. Refer to https://developer.affinity.co/ for the full interactive samples.

**Documentation Version:** This copy is based on the official documentation as it appeared on **October 06, 2026 at 17:12:39 UTC** (Last updated: 10/06/2026 17:12:39 UTC).
**Snapshot:** Captured HTML `openapi.json` (archived with the sync artifacts for QA).

> **⚠️ Use at Your Own Risk**
>
> While every effort is made to ensure accuracy, this is an unofficial copy and may contain errors or outdated information.

## Contact & Support

- **Affinity Support:** [support@affinity.co](mailto:support@affinity.co)
- **Official v2 Documentation:** [https://developer.affinity.co/api-reference/openapi.json](https://developer.affinity.co/api-reference/openapi.json)
- **Official v1 Documentation:** [https://api-docs.affinity.co/](https://api-docs.affinity.co/)
- **Versioning (mirrored):** [pages/versioning.md](pages/versioning.md)
- **Changelog (mirrored):** [pages/previous-changes.md](pages/previous-changes.md)
- **Version Migration (mirrored):** [pages/version-migration.md](pages/version-migration.md)

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
  - [Error Codes](#error-codes)
  - [Versioning](#versioning)
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
- [Changelog](#changelog)
  - [January 30th, 2026](#january-30th-2026)
  - [January 26th, 2026](#january-26th-2026)
  - [January 14th, 2026](#january-14th-2026)
  - [January 1st, 2026](#january-1st-2026)
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
  - [Auth](#auth)
    - [Get current user](#get-current-user)
  - [Calls](#calls)
    - [Get metadata on all Calls](#get-metadata-on-all-calls)
  - [Chat Messages](#chat-messages)
    - [Get metadata on all Chat Messages](#get-metadata-on-all-chat-messages)
  - [Companies](#companies)
    - [Get all Companies](#get-all-companies)
    - [Get metadata on Company Fields](#get-metadata-on-company-fields)
    - [Get dropdown options for a Company Field](#get-dropdown-options-for-a-company-field)
    - [Search Companies](#search-companies)
    - [Field IDs](#field-ids)
    - [`attributeId`](#attributeid)
    - [Search](#search)
    - [Limits](#limits)
    - [Pagination](#pagination-1)
    - [Get a single Company](#get-a-single-company)
    - [Get field values on a single Company](#get-field-values-on-a-single-company)
    - [Perform batch operations on a company's fields](#perform-batch-operations-on-a-companys-fields)
    - [Get a single field value on a Company](#get-a-single-field-value-on-a-company)
    - [Update a single field value on a Company](#update-a-single-field-value-on-a-company)
    - [Get values for a single field on a Company](#get-values-for-a-single-field-on-a-company)
    - [Get a Company's List Entries](#get-a-companys-list-entries)
    - [Get a Company's Lists](#get-a-companys-lists)
    - [Get Notes for a Company](#get-notes-for-a-company)
    - [Get Relationships for a Company](#get-relationships-for-a-company)
  - [Interaction score](#interaction-score)
  - [LinkedIn connections](#linkedin-connections)
  - [Filters](#filters)
  - [Sorting](#sorting)
  - [Company Duplicate Suggestions](#company-duplicate-suggestions)
    - [Get All Company Duplicate Suggestions](#get-all-company-duplicate-suggestions)
  - [Company Merges](#company-merges)
    - [Get All Company Merges](#get-all-company-merges)
    - [Initiate Company Merge](#initiate-company-merge)
    - [Get Company Merge](#get-company-merge)
    - [Get All Company Merge Tasks](#get-all-company-merge-tasks)
    - [Get Company Merge Task](#get-company-merge-task)
  - [Emails](#emails)
    - [Get metadata on all Emails](#get-metadata-on-all-emails)
  - [Feedback](#feedback)
    - [Send Feedback](#send-feedback)
  - [Field Value Changes](#field-value-changes)
    - [Get all field value changes](#get-all-field-value-changes)
  - [Files](#files)
    - [Get all Files](#get-all-files)
    - [Search Files by Keyword](#search-files-by-keyword)
    - [Get a single File](#get-a-single-file)
  - [Inferred Connections](#inferred-connections)
    - [Get Coworker Inferred Connections](#get-coworker-inferred-connections)
  - [Filters](#filters-1)
    - [Get Investor-Executive Inferred Connections](#get-investor-executive-inferred-connections)
  - [Filters](#filters-2)
  - [Lists](#lists)
    - [Get metadata on all Lists](#get-metadata-on-all-lists)
    - [Create a List](#create-a-list)
    - [Get metadata on a single List](#get-metadata-on-a-single-list)
    - [Get metadata on a single List's Fields](#get-metadata-on-a-single-lists-fields)
    - [Get dropdown options for a List Field](#get-dropdown-options-for-a-list-field)
    - [Create a dropdown option for a List Field](#create-a-dropdown-option-for-a-list-field)
    - [Delete a dropdown option for a List Field](#delete-a-dropdown-option-for-a-list-field)
    - [Get a dropdown option for a List Field](#get-a-dropdown-option-for-a-list-field)
    - [Update a dropdown option for a List Field](#update-a-dropdown-option-for-a-list-field)
    - [Get all List Entries on a List](#get-all-list-entries-on-a-list)
    - [Add a List Entry to a List](#add-a-list-entry-to-a-list)
    - [Search List Entries](#search-list-entries)
    - [Field IDs](#field-ids-1)
    - [`attributeId`](#attributeid-1)
    - [Search](#search-1)
    - [Limits](#limits-1)
    - [Pagination](#pagination-2)
    - [Get a single List Entry on a List](#get-a-single-list-entry-on-a-list)
    - [Get Field Value Changes on a List Entry](#get-field-value-changes-on-a-list-entry)
    - [Get field values on a single List Entry](#get-field-values-on-a-single-list-entry)
    - [Perform batch operations on a list entry's fields](#perform-batch-operations-on-a-list-entrys-fields)
    - [Get a single field value](#get-a-single-field-value)
    - [Update a single field value on a List Entry](#update-a-single-field-value-on-a-list-entry)
    - [Get values for a single field on a List Entry](#get-values-for-a-single-field-on-a-list-entry)
    - [Get metadata on Saved Views](#get-metadata-on-saved-views)
    - [Get metadata on a single Saved View](#get-metadata-on-a-single-saved-view)
    - [Get all List Entries on a Saved View](#get-all-list-entries-on-a-saved-view)
  - [Meetings](#meetings)
    - [Get metadata on all Meetings](#get-metadata-on-all-meetings)
    - [Get a single Meeting](#get-a-single-meeting)
  - [Notes](#notes)
    - [Get all Notes](#get-all-notes)
    - [Create a Note](#create-a-note)
    - [Search Notes by Keyword](#search-notes-by-keyword)
    - [Delete a single Note](#delete-a-single-note)
    - [Get a single Note](#get-a-single-note)
    - [Update a single Note](#update-a-single-note)
    - [Get Companies attached to a Note](#get-companies-attached-to-a-note)
    - [Get Opportunities attached to a Note](#get-opportunities-attached-to-a-note)
    - [Get Persons attached to a Note](#get-persons-attached-to-a-note)
    - [Get replies for a Note](#get-replies-for-a-note)
  - [Opportunities](#opportunities)
    - [Get all Opportunities](#get-all-opportunities)
    - [Delete an Opportunity](#delete-an-opportunity)
    - [Get a single Opportunity](#get-a-single-opportunity)
    - [Update an Opportunity](#update-an-opportunity)
    - [Get Notes for an Opportunity](#get-notes-for-an-opportunity)
  - [Person Duplicate Suggestions](#person-duplicate-suggestions)
    - [Get All Person Duplicate Suggestions](#get-all-person-duplicate-suggestions)
  - [Person Merges](#person-merges)
    - [Get All Person Merges](#get-all-person-merges)
    - [Initiate Person Merge](#initiate-person-merge)
    - [Get Person Merge](#get-person-merge)
    - [Get All Person Merge Tasks](#get-all-person-merge-tasks)
    - [Get Person Merge Task](#get-person-merge-task)
  - [Persons](#persons)
    - [Get all Persons](#get-all-persons)
    - [Create a Person](#create-a-person)
    - [Get metadata on Person Fields](#get-metadata-on-person-fields)
    - [Get dropdown options for a Person Field](#get-dropdown-options-for-a-person-field)
    - [Search Persons](#search-persons)
    - [Field IDs](#field-ids-2)
    - [`attributeId`](#attributeid-2)
    - [Search](#search-2)
    - [Limits](#limits-2)
    - [Pagination](#pagination-3)
    - [Delete a Person](#delete-a-person)
    - [Get a single Person](#get-a-single-person)
    - [Get field values on a single Person](#get-field-values-on-a-single-person)
    - [Perform batch operations on a person's fields](#perform-batch-operations-on-a-persons-fields)
    - [Get a single field on a Person](#get-a-single-field-on-a-person)
    - [Update a single field value on a Person](#update-a-single-field-value-on-a-person)
    - [Get values for a single field on a Person](#get-values-for-a-single-field-on-a-person)
    - [Get a Person's List Entries](#get-a-persons-list-entries)
    - [Get a Person's Lists](#get-a-persons-lists)
    - [Get Notes for a Person](#get-notes-for-a-person)
    - [Get Relationships for a Person](#get-relationships-for-a-person)
  - [Interaction score](#interaction-score-1)
  - [LinkedIn connections](#linkedin-connections-1)
  - [Filters](#filters-3)
  - [Sorting](#sorting-1)
  - [Rate Limit](#rate-limit)
    - [Get rate limit usage](#get-rate-limit-usage)
  - [Reminders](#reminders)
    - [Get all Reminders](#get-all-reminders)
    - [Create a Reminder](#create-a-reminder)
    - [Delete a Reminder](#delete-a-reminder)
    - [Get a single Reminder](#get-a-single-reminder)
    - [Update a Reminder](#update-a-reminder)
  - [Semantic Search](#semantic-search)
    - [Semantic Search](#semantic-search-1)
  - [Teams](#teams)
    - [Get metadata on all Teams](#get-metadata-on-all-teams)
    - [Get metadata on a single Team](#get-metadata-on-a-single-team)
  - [Transcripts](#transcripts)
    - [Get all Transcripts](#get-all-transcripts)
    - [Delete a single Transcript](#delete-a-single-transcript)
    - [Get a single Transcript](#get-a-single-transcript)
    - [Get fragments of a transcript](#get-fragments-of-a-transcript)
  - [Users](#users)
    - [Get all Users](#get-all-users)
    - [Get a single User](#get-a-single-user)
  - [Webhooks](#webhooks)
    - [Get all Webhooks](#get-all-webhooks)
    - [Create a Webhook](#create-a-webhook)
    - [Delete a Webhook](#delete-a-webhook)
    - [Get a single Webhook](#get-a-single-webhook)
    - [Update a Webhook](#update-a-webhook)
  - [Schema Reference](#schema-reference)
    - [Attendee](#attendee)
    - [AttendeesPreview](#attendeespreview)
    - [AuthenticationError](#authenticationerror)
    - [AuthorizationError](#authorizationerror)
    - [AuthorizationErrors](#authorizationerrors)
    - [BadRequestError](#badrequesterror)
    - [ChatMessage](#chatmessage)
    - [CompaniesFilter](#companiesfilter)
    - [CompaniesFilterMultiValues](#companiesfiltermultivalues)
    - [CompaniesFilterNoValue](#companiesfilternovalue)
    - [CompaniesValue](#companiesvalue)
    - [CompaniesValuePaged](#companiesvaluepaged)
    - [CompaniesValueUpdate](#companiesvalueupdate)
    - [Company](#company)
    - [CompanyBatchOperationRequest](#companybatchoperationrequest)
    - [CompanyBatchOperationResponse](#companybatchoperationresponse)
    - [CompanyBatchOperationUpdateFields](#companybatchoperationupdatefields)
    - [CompanyBatchOperations](#companybatchoperations)
    - [CompanyData](#companydata)
    - [CompanyDataPaged](#companydatapaged)
    - [CompanyDuplicateSuggestion](#companyduplicatesuggestion)
    - [CompanyDuplicateSuggestionPaged](#companyduplicatesuggestionpaged)
    - [CompanyDuplicateSuggestionProfile](#companyduplicatesuggestionprofile)
    - [CompanyFilter](#companyfilter)
    - [CompanyFilterMultiValues](#companyfiltermultivalues)
    - [CompanyFilterNoValue](#companyfilternovalue)
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
    - [CoworkerConnection](#coworkerconnection)
    - [CoworkerConnectionGroup](#coworkerconnectiongroup)
    - [CoworkerConnectionGroupsPaged](#coworkerconnectiongroupspaged)
    - [CoworkerInference](#coworkerinference)
    - [DateFilter](#datefilter)
    - [DateFilterNoValue](#datefilternovalue)
    - [DateFilterOneValue](#datefilteronevalue)
    - [DateFilterRange](#datefilterrange)
    - [DateFilterRelative](#datefilterrelative)
    - [DateFilterRelativeDate](#datefilterrelativedate)
    - [DateFilterRelativeRange](#datefilterrelativerange)
    - [DateValue](#datevalue)
    - [DealContext](#dealcontext)
    - [DealFundingEvent](#dealfundingevent)
    - [DealMemberRole](#dealmemberrole)
    - [Dropdown](#dropdown)
    - [DropdownFilter](#dropdownfilter)
    - [DropdownFilterMultiValues](#dropdownfiltermultivalues)
    - [DropdownFilterNoValue](#dropdownfilternovalue)
    - [DropdownOption](#dropdownoption)
    - [DropdownOptionBase](#dropdownoptionbase)
    - [DropdownOptionPaged](#dropdownoptionpaged)
    - [DropdownReference](#dropdownreference)
    - [DropdownValue](#dropdownvalue)
    - [DropdownValueUpdate](#dropdownvalueupdate)
    - [DropdownsFilter](#dropdownsfilter)
    - [DropdownsFilterMultiValues](#dropdownsfiltermultivalues)
    - [DropdownsFilterNoValue](#dropdownsfilternovalue)
    - [DropdownsValue](#dropdownsvalue)
    - [DropdownsValuePaged](#dropdownsvaluepaged)
    - [DropdownsValueUpdate](#dropdownsvalueupdate)
    - [Email](#email)
    - [Error](#error)
    - [Errors](#errors)
    - [FeedbackRequest](#feedbackrequest)
    - [Field](#field)
    - [FieldFilterability](#fieldfilterability)
    - [FieldFilterabilityAttributeOnField](#fieldfilterabilityattributeonfield)
    - [FieldFilterabilityFieldOnly](#fieldfilterabilityfieldonly)
    - [FieldMetadata](#fieldmetadata)
    - [FieldMetadataPaged](#fieldmetadatapaged)
    - [FieldPaged](#fieldpaged)
    - [FieldSortability](#fieldsortability)
    - [FieldSortabilityAttribute](#fieldsortabilityattribute)
    - [FieldSortabilityAttributeOnField](#fieldsortabilityattributeonfield)
    - [FieldSortabilityFieldOnly](#fieldsortabilityfieldonly)
    - [FieldUpdate](#fieldupdate)
    - [FieldValue](#fieldvalue)
    - [FieldValueUpdate](#fieldvalueupdate)
    - [FieldValuesPaged](#fieldvaluespaged)
    - [FilterGroup](#filtergroup)
    - [FilterableFieldAttribute](#filterablefieldattribute)
    - [FilterableFieldOperator](#filterablefieldoperator)
    - [FilterableTextFilter](#filterabletextfilter)
    - [FilterableTextFilterMultiValues](#filterabletextfiltermultivalues)
    - [FilterableTextFilterNoValue](#filterabletextfilternovalue)
    - [FilterableTextsFilter](#filterabletextsfilter)
    - [FilterableTextsFilterMultiValues](#filterabletextsfiltermultivalues)
    - [FilterableTextsFilterNoValue](#filterabletextsfilternovalue)
    - [FloatValue](#floatvalue)
    - [FloatsValue](#floatsvalue)
    - [FormulaNumber](#formulanumber)
    - [FormulaValue](#formulavalue)
    - [Grant](#grant)
    - [InferredConnectionCompanyRef](#inferredconnectioncompanyref)
    - [InferredConnectionTarget](#inferredconnectiontarget)
    - [Interaction](#interaction)
    - [InteractionValue](#interactionvalue)
    - [InvestorExecutiveConnection](#investorexecutiveconnection)
    - [InvestorExecutiveConnectionGroup](#investorexecutiveconnectiongroup)
    - [InvestorExecutiveConnectionGroupsPaged](#investorexecutiveconnectiongroupspaged)
    - [InvestorExecutiveInference](#investorexecutiveinference)
    - [List](#list)
    - [ListData](#listdata)
    - [ListEntry](#listentry)
    - [ListEntryBatchOperationRequest](#listentrybatchoperationrequest)
    - [ListEntryBatchOperationResponse](#listentrybatchoperationresponse)
    - [ListEntryBatchOperationUpdateFields](#listentrybatchoperationupdatefields)
    - [ListEntryBatchOperations](#listentrybatchoperations)
    - [ListEntryPaged](#listentrypaged)
    - [ListEntryToBeCreated](#listentrytobecreated)
    - [ListEntryWithEntity](#listentrywithentity)
    - [ListEntryWithEntityPaged](#listentrywithentitypaged)
    - [ListPaged](#listpaged)
    - [ListReference](#listreference)
    - [ListToBeCreated](#listtobecreated)
    - [ListWithType](#listwithtype)
    - [ListWithTypePaged](#listwithtypepaged)
    - [ListsFilter](#listsfilter)
    - [ListsFilterMultiValues](#listsfiltermultivalues)
    - [ListsFilterNoValue](#listsfilternovalue)
    - [ListsValue](#listsvalue)
    - [ListsValuePaged](#listsvaluepaged)
    - [Location](#location)
    - [LocationFilter](#locationfilter)
    - [LocationFilterMultiValues](#locationfiltermultivalues)
    - [LocationFilterNoValue](#locationfilternovalue)
    - [LocationFilterValue](#locationfiltervalue)
    - [LocationValue](#locationvalue)
    - [LocationsFilter](#locationsfilter)
    - [LocationsFilterMultiValues](#locationsfiltermultivalues)
    - [LocationsFilterNoValue](#locationsfilternovalue)
    - [LocationsValue](#locationsvalue)
    - [LocationsValuePaged](#locationsvaluepaged)
    - [Meeting](#meeting)
    - [MethodNotAllowedError](#methodnotallowederror)
    - [NotAcceptableError](#notacceptableerror)
    - [NotFoundError](#notfounderror)
    - [NotFoundErrors](#notfounderrors)
    - [NotImplementedError](#notimplementederror)
    - [NoteValue](#notevalue)
    - [NumberFilter](#numberfilter)
    - [NumberFilterNoValue](#numberfilternovalue)
    - [NumberFilterOneValue](#numberfilteronevalue)
    - [NumberFilterRange](#numberfilterrange)
    - [Opportunity](#opportunity)
    - [OpportunityListEntry](#opportunitylistentry)
    - [OpportunityPaged](#opportunitypaged)
    - [OpportunityReference](#opportunityreference)
    - [OpportunityToBeUpdated](#opportunitytobeupdated)
    - [OpportunityWithFields](#opportunitywithfields)
    - [Pagination](#pagination-4)
    - [PaginationWithTotalCount](#paginationwithtotalcount)
    - [Person](#person)
    - [PersonBatchOperationRequest](#personbatchoperationrequest)
    - [PersonBatchOperationResponse](#personbatchoperationresponse)
    - [PersonBatchOperationUpdateFields](#personbatchoperationupdatefields)
    - [PersonBatchOperations](#personbatchoperations)
    - [PersonData](#persondata)
    - [PersonDataPaged](#persondatapaged)
    - [PersonDataPreview](#persondatapreview)
    - [PersonDuplicateSuggestion](#personduplicatesuggestion)
    - [PersonDuplicateSuggestionPaged](#personduplicatesuggestionpaged)
    - [PersonFilter](#personfilter)
    - [PersonFilterMultiValues](#personfiltermultivalues)
    - [PersonFilterNoValue](#personfilternovalue)
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
    - [PersonsFilter](#personsfilter)
    - [PersonsFilterMultiValues](#personsfiltermultivalues)
    - [PersonsFilterNoValue](#personsfilternovalue)
    - [PersonsValue](#personsvalue)
    - [PersonsValuePaged](#personsvaluepaged)
    - [PersonsValueUpdate](#personsvalueupdate)
    - [PhoneCall](#phonecall)
    - [RankedDropdown](#rankeddropdown)
    - [RankedDropdownFilter](#rankeddropdownfilter)
    - [RankedDropdownFilterMultiValues](#rankeddropdownfiltermultivalues)
    - [RankedDropdownFilterNoValue](#rankeddropdownfilternovalue)
    - [RankedDropdownReference](#rankeddropdownreference)
    - [RankedDropdownValue](#rankeddropdownvalue)
    - [RankedDropdownValuePaged](#rankeddropdownvaluepaged)
    - [RankedDropdownValueUpdate](#rankeddropdownvalueupdate)
    - [RateLimit](#ratelimit)
    - [RateLimitError](#ratelimiterror)
    - [RateLimitWindow](#ratelimitwindow)
    - [Relationship](#relationship)
    - [RelationshipLinkedIn](#relationshiplinkedin)
    - [RelationshipPerson](#relationshipperson)
    - [RelationshipsPaged](#relationshipspaged)
    - [RelativeDate](#relativedate)
    - [RelativeDateRange](#relativedaterange)
    - [RelativeDates](#relativedates)
    - [ReminderData](#reminderdata)
    - [ReminderValue](#remindervalue)
    - [SavedView](#savedview)
    - [SavedViewPaged](#savedviewpaged)
    - [SearchCriteria](#searchcriteria)
    - [SearchSort](#searchsort)
    - [SearchTerm](#searchterm)
    - [SemanticSearchCriteria](#semanticsearchcriteria)
    - [SemanticSearchResult](#semanticsearchresult)
    - [ServerError](#servererror)
    - [Team](#team)
    - [TeamAccessibleListsPreview](#teamaccessiblelistspreview)
    - [TeamBase](#teambase)
    - [TeamMember](#teammember)
    - [TeamMembersPreview](#teammemberspreview)
    - [TeamPaged](#teampaged)
    - [Tenant](#tenant)
    - [TextFilter](#textfilter)
    - [TextFilterNoValue](#textfilternovalue)
    - [TextFilterOneValue](#textfilteronevalue)
    - [TextValue](#textvalue)
    - [TextsValue](#textsvalue)
    - [TextsValuePaged](#textsvaluepaged)
    - [TimeoutError](#timeouterror)
    - [UnprocessableEntityError](#unprocessableentityerror)
    - [UnsupportedMediaTypeError](#unsupportedmediatypeerror)
    - [User](#user)
    - [UserData](#userdata)
    - [UserDataPaged](#userdatapaged)
    - [ValidationError](#validationerror)
    - [ValueFilter](#valuefilter)
    - [WhoAmI](#whoami)
    - [companies.SemanticSearchCompany](#companiessemanticsearchcompany)
    - [dropdownOptions.DropdownOption](#dropdownoptionsdropdownoption)
    - [dropdownOptions.DropdownOptionToBeCreated](#dropdownoptionsdropdownoptiontobecreated)
    - [dropdownOptions.DropdownOptionToBeUpdated](#dropdownoptionsdropdownoptiontobeupdated)
    - [dropdownOptions.RankedDropdownOption](#dropdownoptionsrankeddropdownoption)
    - [dropdownOptions.RankedDropdownOptionToBeCreated](#dropdownoptionsrankeddropdownoptiontobecreated)
    - [dropdownOptions.RankedDropdownOptionToBeUpdated](#dropdownoptionsrankeddropdownoptiontobeupdated)
    - [dropdownOptions.StandardDropdownOptionToBeCreated](#dropdownoptionsstandarddropdownoptiontobecreated)
    - [dropdownOptions.StandardDropdownOptionToBeUpdated](#dropdownoptionsstandarddropdownoptiontobeupdated)
    - [dropdownOptions.StatusDropdownOption](#dropdownoptionsstatusdropdownoption)
    - [dropdownOptions.StatusDropdownOptionToBeCreated](#dropdownoptionsstatusdropdownoptiontobecreated)
    - [dropdownOptions.StatusDropdownOptionToBeUpdated](#dropdownoptionsstatusdropdownoptiontobeupdated)
    - [fieldValueChanges.CompanyEntityData](#fieldvaluechangescompanyentitydata)
    - [fieldValueChanges.CompanyMultiValueChange](#fieldvaluechangescompanymultivaluechange)
    - [fieldValueChanges.CompanyValueChange](#fieldvaluechangescompanyvaluechange)
    - [fieldValueChanges.DatetimeValueChange](#fieldvaluechangesdatetimevaluechange)
    - [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference)
    - [fieldValueChanges.DropdownEntityData](#fieldvaluechangesdropdownentitydata)
    - [fieldValueChanges.DropdownMultiValueChange](#fieldvaluechangesdropdownmultivaluechange)
    - [fieldValueChanges.DropdownValueChange](#fieldvaluechangesdropdownvaluechange)
    - [fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)
    - [fieldValueChanges.Field](#fieldvaluechangesfield)
    - [fieldValueChanges.FieldValueChange](#fieldvaluechangesfieldvaluechange)
    - [fieldValueChanges.FieldValueChangeBase](#fieldvaluechangesfieldvaluechangebase)
    - [fieldValueChanges.FieldValueChangePaged](#fieldvaluechangesfieldvaluechangepaged)
    - [fieldValueChanges.FilterableTextMultiValueChange](#fieldvaluechangesfilterabletextmultivaluechange)
    - [fieldValueChanges.FilterableTextValueChange](#fieldvaluechangesfilterabletextvaluechange)
    - [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry)
    - [fieldValueChanges.LocationMultiValueChange](#fieldvaluechangeslocationmultivaluechange)
    - [fieldValueChanges.LocationValueChange](#fieldvaluechangeslocationvaluechange)
    - [fieldValueChanges.NumberMultiValueChange](#fieldvaluechangesnumbermultivaluechange)
    - [fieldValueChanges.NumberValueChange](#fieldvaluechangesnumbervaluechange)
    - [fieldValueChanges.PersonEntityData](#fieldvaluechangespersonentitydata)
    - [fieldValueChanges.PersonMultiValueChange](#fieldvaluechangespersonmultivaluechange)
    - [fieldValueChanges.PersonValueChange](#fieldvaluechangespersonvaluechange)
    - [fieldValueChanges.RankedDropdownEntityData](#fieldvaluechangesrankeddropdownentitydata)
    - [fieldValueChanges.RankedDropdownValueChange](#fieldvaluechangesrankeddropdownvaluechange)
    - [fieldValueChanges.TextValueChange](#fieldvaluechangestextvaluechange)
    - [fields.FieldUpdate](#fieldsfieldupdate)
    - [files.File](#filesfile)
    - [files.FileBase](#filesfilebase)
    - [files.FileSummary](#filesfilesummary)
    - [files.FileSummaryPaged](#filesfilesummarypaged)
    - [files.KeywordSearchCriteria](#fileskeywordsearchcriteria)
    - [files.KeywordSearchResult](#fileskeywordsearchresult)
    - [files.SearchResult](#filessearchresult)
    - [interactions.Call](#interactionscall)
    - [interactions.CallPaged](#interactionscallpaged)
    - [interactions.ChatMessage](#chatmessage)
    - [interactions.ChatMessagePaged](#interactionschatmessagepaged)
    - [interactions.Email](#email)
    - [interactions.EmailPaged](#interactionsemailpaged)
    - [interactions.Meeting](#meeting)
    - [interactions.MeetingPaged](#interactionsmeetingpaged)
    - [notes.AiNotetakerReplyNote](#notesainotetakerreplynote)
    - [notes.AiNotetakerRootNote](#notesainotetakerrootnote)
    - [notes.BaseNote](#notesbasenote)
    - [notes.BaseReply](#notesbasereply)
    - [notes.BaseRootNote](#notesbaserootnote)
    - [notes.CallInteraction](#notescallinteraction)
    - [notes.CallReference](#notescallreference)
    - [notes.ChatMessageInteraction](#noteschatmessageinteraction)
    - [notes.ChatMessageReference](#noteschatmessagereference)
    - [notes.CompaniesPreview](#notescompaniespreview)
    - [notes.Content](#notescontent)
    - [notes.ContentToBeSaved](#notescontenttobesaved)
    - [notes.EmailInteraction](#notesemailinteraction)
    - [notes.EntitiesNote](#notesentitiesnote)
    - [notes.EntitiesNoteToBeCreated](#notesentitiesnotetobecreated)
    - [notes.Interaction](#notesinteraction)
    - [notes.InteractionNote](#notesinteractionnote)
    - [notes.InteractionNoteToBeCreated](#notesinteractionnotetobecreated)
    - [notes.InteractionReference](#notesinteractionreference)
    - [notes.KeywordSearchCriteria](#noteskeywordsearchcriteria)
    - [notes.KeywordSearchResult](#noteskeywordsearchresult)
    - [notes.MeetingInteraction](#notesmeetinginteraction)
    - [notes.MeetingReference](#notesmeetingreference)
    - [notes.Mention](#notesmention)
    - [notes.Note](#notesnote)
    - [notes.NoteReference](#notesnotereference)
    - [notes.NoteToBeCreated](#notesnotetobecreated)
    - [notes.NoteToBeUpdated](#notesnotetobeupdated)
    - [notes.NotesPaged](#notesnotespaged)
    - [notes.OpportunitiesPreview](#notesopportunitiespreview)
    - [notes.PersonMention](#notespersonmention)
    - [notes.PersonsPreview](#notespersonspreview)
    - [notes.RepliesPaged](#notesrepliespaged)
    - [notes.Reply](#notesreply)
    - [notes.SearchResult](#notessearchresult)
    - [notes.UserReplyNote](#notesuserreplynote)
    - [notes.UserReplyNoteToBeCreated](#notesuserreplynotetobecreated)
    - [persons.PersonToCreate](#personspersontocreate)
    - [reminders.BaseReminder](#remindersbasereminder)
    - [reminders.BaseReminderToBeCreated](#remindersbaseremindertobecreated)
    - [reminders.OneTimeReminder](#remindersonetimereminder)
    - [reminders.OneTimeReminderToBeCreated](#remindersonetimeremindertobecreated)
    - [reminders.RecurringReminder](#remindersrecurringreminder)
    - [reminders.RecurringReminderToBeCreated](#remindersrecurringremindertobecreated)
    - [reminders.Reminder](#remindersreminder)
    - [reminders.ReminderPaged](#remindersreminderpaged)
    - [reminders.ReminderToBeCreated](#remindersremindertobecreated)
    - [reminders.ReminderToBeUpdated](#remindersremindertobeupdated)
    - [reminders.TaggedCompany](#reminderstaggedcompany)
    - [reminders.TaggedOpportunity](#reminderstaggedopportunity)
    - [reminders.TaggedPerson](#reminderstaggedperson)
    - [transcripts.BaseTranscript](#transcriptsbasetranscript)
    - [transcripts.Fragment](#transcriptsfragment)
    - [transcripts.FragmentPaged](#transcriptsfragmentpaged)
    - [transcripts.FragmentsPreview](#transcriptsfragmentspreview)
    - [transcripts.Transcript](#transcriptstranscript)
    - [transcripts.TranscriptPaged](#transcriptstranscriptpaged)
    - [webhooks.SubscriptionType](#webhookssubscriptiontype)
    - [webhooks.Webhook](#webhookswebhook)
    - [webhooks.WebhookPaged](#webhookswebhookpaged)
    - [webhooks.WebhookToBeCreated](#webhookswebhooktobecreated)
    - [webhooks.WebhookToBeUpdated](#webhookswebhooktobeupdated)
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

Affinity API v2 uses API keys and **bearer authentication**.

To generate an API key, navigate to the Manage Apps Page in your Affinity Settings. You will need
the "Generate an API key" role-based permission controlled by your Affinity admin. See
[this Help Center article](https://support.affinity.co/s/article/How-to-Create-and-Manage-API-Keys)
for full instructions on API key generation, and
[this article](https://support.affinity.co/hc/en-us/articles/360015976732-Account-Level-Permissions)
for more information on role-based permissions in Affinity.

Provide your API key as your bearer authentication token to start making calls to Affinity API v2.

You can create multiple API keys and provide a name and description for each. Your API key is able
to read data and perform actions in Affinity on your behalf, so keep it safe as you would a
password. To further secure an API key, you can define an IP Allowlist to limit which IP addresses
or ranges can make API calls using that key.

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
| x-ratelimit-limit-user           | Number of requests allowed per minute for the user      |
| x-ratelimit-limit-user-remaining | Number of requests remaining for the user               |
| x-ratelimit-limit-user-reset     | Time in seconds before the limit resets for the user    |
| x-ratelimit-limit-org            | Number of requests allowed per month for the account    |
| x-ratelimit-limit-org-remaining  | Number of requests remaining for the account            |
| x-ratelimit-limit-org-reset      | Time in seconds before the limit resets for the account |

The `x-ratelimit-limit-org*` headers are absent when no monthly quota applies to the caller, for
example a plan with no monthly cap.

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
| exact match              | all                                                  | =        | content = “hello world” <br> content=hello                                                |
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
| negation                 | all                                                  | !        | content != ”hello world” <br> !(content = ”hello world”) <br> !(content =^ “hello world”) |

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

## Versioning

> **Note (added by this mirror):** The version list below is embedded in the OpenAPI spec and is out of date: it does not list the current version, 2026-09-17. See [Versioning](pages/versioning.md) for the current list.

Versioning in Affinity’s API ensures that your integrations remain stable as updates are introduced.
Within API v2, minor versions identify releases that may include breaking or behavior-changing
modifications, and they allow you to target the exact API behavior your integration depends on.

When you create an API key in the Settings page, you'll select a **Default API Version** for that
key. The current available versions are:

- **2024-01-01** - The current stable version of the v2 API

As new minor versions of Affinity API v2 are introduced, they will appear in this list. You’ll be
able to create new keys using those versions or update an existing key to use a newer version.

## Beta Endpoints

You’ll notice in our documentation that some endpoints will be marked as BETA. These endpoints are
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

# Changelog

> **Note (added by this mirror):** This changelog is embedded in the OpenAPI spec and may lag Affinity's site. See the [full changelog](pages/previous-changes.md).

## January 30th, 2026

- The following endpoints are no longer in BETA:

| Method | URL                                         | Summary                                        |
| ------ | ------------------------------------------- | ---------------------------------------------- |
| GET    | `/v2/notes`                                 | Get all Notes                                  |
| GET    | `/v2/notes/{noteId}`                        | Get a Note with a given id                     |
| GET    | `/v2/notes/{noteId}/attached-companies`     | Get directly attached companies for a Note     |
| GET    | `/v2/notes/{noteId}/attached-opportunities` | Get directly attached opportunities for a Note |
| GET    | `/v2/notes/{noteId}/attached-persons`       | Get directly attached persons for a Note       |
| GET    | `/v2/notes/{noteId}/replies`                | Get reply notes for a given Note               |

## January 26th, 2026

- Added the following endpoints in BETA:

| Method | URL                                        | Summary                              |
| ------ | ------------------------------------------ | ------------------------------------ |
| GET    | `/v2/transcripts`                          | Get All Transcripts                  |
| GET    | `/v2/transcripts/{transcriptId}`           | Get Transcript                       |
| GET    | `/v2/transcripts/{transcriptId}/fragments` | Get Fragments on a single Transcript |

## January 14th, 2026

- Rate limit response headers have been updated to use lowercase formatting. This change affects all
  API endpoints. The new lowercase headers are:

| Header                           | Description                                             |
| -------------------------------- | ------------------------------------------------------- |
| x-ratelimit-limit-user           | Number of requests allowed per minute for the user      |
| x-ratelimit-limit-user-remaining | Number of requests remaining for the user               |
| x-ratelimit-limit-user-reset     | Time in seconds before the limit resets for the user    |
| x-ratelimit-limit-org            | Number of requests allowed per month for the account    |
| x-ratelimit-limit-org-remaining  | Number of requests remaining for the account            |
| x-ratelimit-limit-org-reset      | Time in seconds before the limit resets for the account |

## January 1st, 2026

- API Change: Handling timestamps for date fields. Affinity is standardizing how dates are
  represented across the platform to ensure consistency between the application and the API.
  Starting January 1st, 2026, the API will change how it handles timestamps for date fields. Today,
  timestamps sent to date fields over the API are not visible to users in any CRM interface. After
  this change, the API will ignore any time information included in requests, storing and returning
  values at midnight Pacific Time (PT) on the submitted date.

  **Example:**
  - API request includes: `2024-04-01T15:30:00Z`
  - Affinity will store and return: `2024-04-01T07:00:00.000Z` (equivalent to midnight PT)

  Any existing date field values that currently include timestamps will also be updated to reflect
  midnight PT on their stored date. No action is required unless your integration depends on time
  data within date fields.

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

| Method | URL                                         | Summary                                        |
| ------ | ------------------------------------------- | ---------------------------------------------- |
| GET    | `/v2/person-merges`                         | Get All Person Merge status                    |
| POST   | `/v2/person-merges`                         | Initiate Person Merge                          |
| GET    | `/v2/person-merges/{mergeId}`               | Get Person Merge status                        |
| GET    | `/v2/tasks/person-merges`                   | Get All Person Merge Tasks                     |
| GET    | `/v2/tasks/person-merges/{taskId}`          | Get Person Merge Task                          |
| GET    | `/v2/notes`                                 | Get all Notes                                  |
| GET    | `/v2/notes/{noteId}`                        | Get a Note with a given id                     |
| GET    | `/v2/notes/{noteId}/attached-companies`     | Get directly attached companies for a Note     |
| GET    | `/v2/notes/{noteId}/attached-opportunities` | Get directly attached opportunities for a Note |
| GET    | `/v2/notes/{noteId}/attached-persons`       | Get directly attached persons for a Note       |
| GET    | `/v2/notes/{noteId}/replies`                | Get reply notes for a given Note               |

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
  [Specifying Desired Fields (Field Selection)](https://developer.affinity.co/pages/data-model/working-with-field-data) section
  of these docs for more information. The new `fieldTypes` parameter should make field data
  retrieval easier for users looking to pull data from many similar Fields at a time.

## January 4, 2023

- Most endpoints that return field data now require the user to use the `fieldIds` parameter to
  specify which Fields they want data for. Without `fieldIds` specified, these endpoints will return
  basic entity data but not field data.

## December 12, 2023

- Added the ability to retrieve metadata (e.g. ID, name, type, enrichment source, and data type) on
  Fields. See the [Retrieving Field Metadata](https://developer.affinity.co/pages/data-model/working-with-field-data) section of
  these docs for more information.

## Auth

Operations about Auth

### Get current user
`GET /v2/auth/whoami`

- **Tag:** Auth · **OperationId:** v2_auth_whoami__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `tenant` | `object` ([Tenant](#tenant)) | Yes |  |
| `user` | `object` ([User](#user)) | Yes |  |
| `grant` | `object` ([Grant](#grant)) | Yes |  |

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Calls

Operations about Calls

### Get metadata on all Calls
`GET /v2/calls`

- **Tag:** Calls · **OperationId:** v2_calls__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all calls in Affinity. Returns basic information about the call interaction
and its participants. Will only return calls that the current authenticated user has
permission to see.

You can filter calls using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int64` | `=` | `id=1\|id=2\|id=3` |
| `startTime` | `datetime` | `>`, `<`, `>=`, `<=` | `sentAt>2025-01-01T01:00:00Z` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-01-01T01:00:00Z` |

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
| `data` | `array<object> (≤ 100 items)` ([interactions.Call](#interactionscall)) | Yes | A page of Call results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

## Chat Messages

Operations about chat messages

### Get metadata on all Chat Messages
`GET /v2/chat-messages`

- **Tag:** Chat Messages · **OperationId:** v2_chat-messages__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all chat messages in Affinity. Returns basic information about the chat message
interaction and its participants. Will only return chat messages that the current authenticated
user has permission to see.

You can filter chat messages using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int64` | `=` | `id=1\|id=2\|id=3` |
| `sentAt` | `datetime` | `>`, `<`, `>=`, `<=` | `sentAt>2025-01-01T01:00:00Z` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-01-01T01:00:00Z` |

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
| `data` | `array<object> (≤ 100 items)` ([interactions.ChatMessage](#chatmessage)) | Yes | A page of ChatMessage results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

## Companies

Operations about companies

### Get all Companies
`GET /v2/companies`

- **Tag:** Companies · **OperationId:** v2_companies__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through Companies in Affinity.
Returns basic information and non-list-specific field data on each Company.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/companies/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Companies will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export All Organizations directory" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

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
| `data` | `array<object> (≤ 100 items)` ([Company](#company)) | Yes | A page of Company results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example

```json
{
  "data": [
    {
      "domain": "horizontech.com",
      "domains": [
        "horizontech.com"
      ],
      "fields": [],
      "id": 1,
      "isGlobal": false,
      "name": "Horizon Technologies"
    },
    {
      "domain": "crestwoodcap.com",
      "domains": [
        "crestwoodcap.com"
      ],
      "fields": [],
      "id": 2,
      "isGlobal": false,
      "name": "Crestwood Capital"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/companies?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/companies?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on Company Fields
`GET /v2/companies/fields`

- **Tag:** Companies · **OperationId:** v2_companies_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns metadata on non-list-specific Company Fields.

Use the returned Field IDs to request field data from the GET `/v2/companies` and GET `/v2/companies/{id}` endpoints.

You can filter Fields using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `name` | `text` | `=`, `=~` | `name="Location"`, `name=~loc` |

Use the `includes` query parameter to add optional metadata to each Field in the response. Pass `includes` more than once to request multiple values.

| **Value** | **Adds to each Field** |
|---|---|
| `filterability` | How the field can be used in filter expressions on GET `/v2/companies` and POST `/v2/companies/search` |
| `sortability` | How the field can be used in sort expressions on those endpoints |

Example: `GET /v2/companies/fields?includes=filterability&includes=sortability`

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |
| `includes` | `array<string (enum: `filterability`, `sortability`)>` | No | Additional properties to include in the response |

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
| `data` | `array<object> (≤ 100 items)` ([FieldMetadata](#fieldmetadata)) | Yes | A page of FieldMetadata results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: default

```json
{
  "data": [
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-industry",
      "isRequired": false,
      "name": "Industry",
      "type": "enriched",
      "valueType": "filterable-text-multi"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-amount",
      "isRequired": false,
      "name": "Last Funding Amount (USD)",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-date",
      "isRequired": false,
      "name": "Last Funding Date",
      "type": "enriched",
      "valueType": "datetime"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "isRequired": false,
      "name": "Location",
      "type": "enriched",
      "valueType": "location"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": null,
      "id": "field-1",
      "isRequired": false,
      "name": "Custom global field",
      "type": "global",
      "valueType": "text"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "last-email",
      "isRequired": false,
      "name": "Last Email",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "lists",
      "isRequired": false,
      "name": "Lists",
      "type": "global",
      "valueType": "list-multi"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "notes",
      "isRequired": false,
      "name": "Notes",
      "type": "global",
      "valueType": "note"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "persons",
      "isRequired": false,
      "name": "People",
      "type": "enriched",
      "valueType": "person-multi"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "reminders",
      "isRequired": false,
      "name": "Reminders",
      "type": "global",
      "valueType": "reminder"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/companies/fields?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

### Get dropdown options for a Company Field
`GET /v2/companies/fields/{fieldId}/dropdown-options`

- **Tag:** Companies · **OperationId:** v2_companies_fields_fieldId_dropdown-options__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns the dropdown options for a specific dropdown or ranked-dropdown field on a Company.

Use the returned dropdown option IDs when writing dropdown field values via the field update
endpoints.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldId` | `string` | Yes | Field ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/fields/{fieldId}/dropdown-options' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: DropdownOptionPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([DropdownOption](#dropdownoption)) | Yes | A page of DropdownOption results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: dropdown-options

```json
{
  "data": [
    {
      "id": 1,
      "text": "Seed",
      "type": "dropdown"
    },
    {
      "id": 2,
      "text": "Series A",
      "type": "dropdown"
    },
    {
      "id": 3,
      "text": "Series B",
      "type": "dropdown"
    }
  ],
  "pagination": {
    "nextUrl": null,
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Search Companies
`POST /v2/companies/search`

- **Tag:** Companies · **OperationId:** v2_companies_search__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Search for Companies matching the given criteria.

Accepts an optional combination of filters, sorts, and a search term. Omitting the body is equivalent to `GET /v2/companies` with default pagination.

Requires the "Export All Organizations directory" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

### Field IDs

Field IDs used in `filters`, `sorts`, and `search.fieldIds` follow the formats described in [Working with Field Data](https://developer.affinity.co/pages/data-model/working-with-field-data). Use `GET /v2/companies/fields` to discover the available fields and their `valueType`.

### `attributeId`

Some fields require an `attributeId` to specify which aspect to filter or sort on. The following relationship intelligence fields all use `attributeId: "date-of-activity"`: `last-email`, `first-email`, `last-contact`, `last-event`, `first-event`, `next-event`.

Use `GET /v2/companies/fields` to confirm which fields require an `attributeId`.

### Search

The `search.term` is always matched against the company name and primary domain. Providing `search.fieldIds` extends the search to those additional fields; it does not restrict matching to only those fields. Fields with a `valueType` of `datetime` are not searchable and are silently ignored if included in `search.fieldIds`.

### Limits

- **Items per filter group** (filters or nested groups): 50

- **Values per filter** (e.g. options in `is-any-of`): 100

- **Sort criteria**: 5

- **Search term minimum length**: 3 characters

- **Results per page**: 100

### Pagination

Uses cursor-based pagination.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldIds` | `array<string>` | No | Specific field IDs for which to return field data on each Company. Cannot be used together with `fieldTypes`; use one or the other. Use `GET /v2/companies/fields` to discover available field IDs. |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | A category of fields for which to return field data on each Company. Cannot be used together with `fieldIds`; use one or the other. |
| `cursor` | `string` | No | Cursor for the next or previous page. |
| `limit` | `integer<int32>` | No | Maximum number of Companies to return per page. |
| `totalCount` | `boolean` | No | When `true`, includes the total count of matching Companies in the pagination response. Adds additional query cost; use only when needed. |

#### Request Body

**Media type:** `application/json`
Search criteria for filtering, sorting, and searching. All fields are optional  omitting the body returns all results with default pagination.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | `object` ([FilterGroup](#filtergroup)) | No | A tree of filter conditions to apply. Supports nested AND/OR grouping. Use the relevant fields endpoint for your resource type to discover available fields, their `valueType`, and supported operators. |
| `sorts` | `array<object> (≤ 5 items, ≥ 1 items)` ([SearchSort](#searchsort)) | No | One or more sort criteria, applied in order. Supports up to 5 sort items. Use the relevant fields endpoint for your resource type to discover sortable fields. |
| `search` | `object` ([SearchTerm](#searchterm)) | No | An optional keyword to match against field values. Results must satisfy both the search term AND any provided filters (intersection). Only one search object may be provided. The term is always matched against the entity name and primary identifier; providing `fieldIds` extends the search to additional fields rather than replacing the identity match. |

Example: filter-by-dropdown
```json
{
  "filters": {
    "filters": [
      {
        "fieldId": "field-4574182",
        "operator": "is-any-of",
        "value": [
          {
            "dropdownOptionId": 1
          },
          {
            "dropdownOptionId": 2
          }
        ],
        "valueType": "dropdown"
      }
    ],
    "operator": "and"
  }
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/companies/search' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"filters":{"operator":"and","filters":[{"fieldId":"field-4574182","valueType":"dropdown","operator":"is-any-of","value":[{"dropdownOptionId":1},{"dropdownOptionId":2}]}]}}'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: CompanyPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Company](#company)) | Yes | A page of Company results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example

```json
{
  "data": [
    {
      "domain": "horizontech.com",
      "domains": [
        "horizontech.com"
      ],
      "fields": [],
      "id": 1,
      "isGlobal": false,
      "name": "Horizon Technologies"
    },
    {
      "domain": "crestwoodcap.com",
      "domains": [
        "crestwoodcap.com"
      ],
      "fields": [],
      "id": 2,
      "isGlobal": false,
      "name": "Crestwood Capital"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/companies?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/companies?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Company
`GET /v2/companies/{companyId}`

- **Tag:** Companies · **OperationId:** v2_companies_companyId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns basic information and non-list-specific field data on the requested Company.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/companies/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Companies will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

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
| `fields` | `array<object>` ([Field](#field)) | No | The fields associated with the company |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get field values on a single Company
`GET /v2/companies/{companyId}/fields`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through field values on a single company.

Enriched, global, and relationship-intelligence fields will be included by default. The `ids` and `types` parameters can be used to filter
the collection. These parameters are mutually exclusive.

List fields are not returned by this endpoint. To retrieve or update list field values, use the
[list entry fields](#get-field-values-on-a-single-list-entry) endpoints.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `array<string>` | No | Field IDs for which to return field data |
| `types` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | Field Types for which to return field data |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/fields' \
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
| `data` | `array<object> (≤ 100 items)` ([Field](#field)) | Yes | A page of Field results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: company-enriched

```json
{
  "data": [
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-description",
      "name": "Description",
      "type": "enriched",
      "value": {
        "data": "Horizon Technologies is a leading technology company specializing in enterprise software and cloud infrastructure.",
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
          "Healthcare",
          "Fintech",
          "SaaS"
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
          "Alex Rivera",
          "Taylor Wong"
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
        "data": "https://linkedin.com/company/horizontech",
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
    "nextUrl": "https://api.affinity.co/v2/companies/1/fields?types=enriched&cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/companies/1/fields?types=enriched&cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Perform batch operations on a company's fields
`PATCH /v2/companies/{companyId}/fields`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_fields__PATCH · **Stability:** `beta` · **Auth:** bearerAuth

Perform batch operations on a company's fields.

Currently the only operation at the endpoint is `update-fields`, which allows you to update
multiple field values with a single request. This is equivalent to calling [the single field
update](#update-a-single-field-value-on-a-company) endpoint multiple times. You can
update up to 100 fields per request.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |

#### Request Body

**Media type:** `application/json`
**Variant:** [CompanyBatchOperationUpdateFields](#companybatchoperationupdatefields)
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` ([fields.FieldUpdate](#fieldsfieldupdate)) | Yes |  |

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
curl --request PATCH 'https://api.affinity.co/v2/companies/{companyId}/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"operation":"update-fields","updates":[{"id":"field-1","value":{"type":"company","data":{"id":1}}},{"id":"field-2","value":{"type":"company-multi","data":[{"id":1},{"id":2}]}},{"id":"field-3","value":{"type":"datetime","data":"2023-01-01T00:00:00Z"}},{"id":"field-4","value":{"type":"dropdown","data":{"dropdownOptionId":1}}},{"id":"field-5","value":{"type":"dropdown-multi","data":[{"dropdownOptionId":1},{"dropdownOptionId":2}]}},{"id":"field-6","value":{"type":"location","data":{"streetAddress":"1 Main Street","city":"San Francisco","state":"California","country":"United States","continent":"North America"}}},{"id":"field-7","value":{"type":"location-multi","data":[{"streetAddress":"1 Main Street","city":"San Francisco","state":"California","country":"United States","continent":"North America"},{"streetAddress":"1600 Pennsylvania Avenue NW","city":"Washington","state":"DC","country":"United States","continent":"North America"}]}},{"id":"field-8","value":{"type":"number","data":100}},{"id":"field-9","value":{"type":"number-multi","data":[100,200,300]}},{"id":"field-10","value":{"type":"person","data":{"id":1}}},{"id":"field-11","value":{"type":"person-multi","data":[{"id":1},{"id":2}]}},{"id":"field-12","value":{"type":"ranked-dropdown","data":{"dropdownOptionId":1}}},{"id":"field-13","value":{"type":"text","data":"Some new text"}}]}'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyBatchOperationResponse
*Type:* object
The response body for a single operation within a company batch request.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` ([CompanyBatchOperations](#companybatchoperations)) | No | The type of batch operation that was performed on the company. |

Example: update-fields

```json
{
  "operation": "update-fields"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single field value on a Company
`GET /v2/companies/{companyId}/fields/{fieldId}`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_fields_fieldId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Retrieve a single field on a company. Returns basic information and the field value.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |
| `fieldId` | `string` | Yes | Field ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/fields/{fieldId}' \
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
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`, `hidden`)` | Yes | The field's category. `hidden` is a redaction state rather than a category: it signals a field on a restricted opportunity the caller cannot manage, whose value is masked. |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `eventbrite`, `mailchimp`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | [CompaniesValue](#companiesvalue) \| [CompanyValue](#companyvalue) \| [DateValue](#datevalue) \| [DropdownsValue](#dropdownsvalue) \| [DropdownValue](#dropdownvalue) \| [FloatsValue](#floatsvalue) \| [FloatValue](#floatvalue) \| [FormulaValue](#formulavalue) \| [InteractionValue](#interactionvalue) \| [ListsValue](#listsvalue) \| [LocationsValue](#locationsvalue) \| [LocationValue](#locationvalue) \| [NoteValue](#notevalue) \| [PersonsValue](#personsvalue) \| [PersonValue](#personvalue) \| [RankedDropdownValue](#rankeddropdownvalue) \| [ReminderValue](#remindervalue) \| [TextsValue](#textsvalue) \| [TextValue](#textvalue) | Yes |  |

Example: company

```json
{
  "enrichmentSource": null,
  "id": "field-1",
  "name": "Field with company value",
  "type": "global",
  "value": {
    "data": {
      "domain": "horizontech.com",
      "id": 1,
      "name": "Horizon Technologies"
    },
    "type": "company"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a single field value on a Company
`POST /v2/companies/{companyId}/fields/{fieldId}`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_fields_fieldId__POST · **Stability:** `beta` · **Auth:** bearerAuth

Update a single field value on a company.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |
| `fieldId` | `string` | Yes | Field ID |

#### Request Body

**Media type:** `application/json`
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | No |  |

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
curl --request POST 'https://api.affinity.co/v2/companies/{companyId}/fields/{fieldId}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"value":{"type":"company","data":{"id":1}}}'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get values for a single field on a Company
`GET /v2/companies/{companyId}/fields/{fieldId}/values`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_fields_fieldId_values__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through all values for a field on a company.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |
| `fieldId` | `string` | Yes | Field ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/fields/{fieldId}/values' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldValuesPaged
*Type:* oneOf
**Variant:** [CompaniesValuePaged](#companiesvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `company`, `company-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [DropdownsValuePaged](#dropdownsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `dropdown`, `dropdown-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Dropdown](#dropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [ListsValuePaged](#listsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([ListData](#listdata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [LocationsValuePaged](#locationsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `location`, `location-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Location](#location)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [PersonsValuePaged](#personsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `person`, `person-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [RankedDropdownValuePaged](#rankeddropdownvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([RankedDropdown](#rankeddropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [TextsValuePaged](#textsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `filterable-text-multi`)` | Yes | The type of value |
| `data` | `array<string> (≤ 100 items)` | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: company

```json
{
  "data": [
    {
      "domain": "horizontech.com",
      "id": 1,
      "name": "Horizon Technologies"
    }
  ],
  "pagination": {
    "nextUrl": null,
    "prevUrl": null
  },
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a Company's List Entries
`GET /v2/companies/{companyId}/list-entries`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) for the given Company across all Lists.
Each List Entry includes field data for the Company, including list-specific field data.
Each List Entry also includes metadata about its creation, i.e., when it was added to the List and by whom.

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
| `data` | `array<object> (≤ 100 items)` ([ListEntry](#listentry)) | Yes | A page of ListEntry results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a Company's Lists
`GET /v2/companies/{companyId}/lists`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_lists__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `data` | `array<object> (≤ 100 items)` ([List](#list)) | Yes | A page of List results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Notes for a Company
`GET /v2/companies/{companyId}/notes`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns relevant notes for a given company which includes directly attached notes and notes attached to persons on this company.

You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `creator.id` | `int32` | `=` | `creator.id=1` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-02-03T10:48:24Z` |

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
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Note](#notesnote)) | Yes | A page of Note objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Relationships for a Company
`GET /v2/companies/{companyId}/relationships`

- **Tag:** Companies · **OperationId:** v2_companies_companyId_relationships__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns the relationships for a given company, including the interaction score that measures
the strength of each relationship based on communication patterns such as emails, meetings,
and other interactions.

Each relationship includes two persons (person1 and person2) who have a connection related
to this company.

## Interaction score

The `interactionScore` is a value between `0.0` and `1.0` that reflects how frequently the
two persons interact across email, calendar events, and chat messages. The more interactions,
the higher the score. Recent interactions are weighted slightly higher than older ones. As
rough guidance, scores at or above `0.7` typically indicate two persons that communicate
regularly, scores between `0.4` and `0.7` indicate occasional communication, and scores below
`0.4` indicate only sporadic communication.

## LinkedIn connections

The collection also includes relationships based on a LinkedIn connection between an internal
team member and a person related to this company. Whenever a LinkedIn connection exists between
the two persons in a relationship, `linkedIn` is populated with the date the connection was made.
`linkedIn` is `null` when no LinkedIn connection between the two persons is known by Affinity.
Note that LinkedIn-based relationships which do not have any interaction data will have an
`interactionScore` of `0`.

## Filters

You can filter relationships using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Description** | **Allowed Operators** | **Examples** |
|---|---|---|---|---|
| `interactionScore` | `double` | Strength of the relationship, between `0.0` and `1.0`. Higher means stronger. | `>`, `<`, `>=`, `<=` | `interactionScore>=0.5` |

## Sorting

You can sort relationships using the `orderBy` query parameter. `interactionScore` is the only
sortable property.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `companyId` | `integer<int64>` | Yes | Company ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `orderBy` | `array<string (enum: `interactionScore`, `-interactionScore`)>` | No | Properties to sort by. Defaults to `-interactionScore`. Prefix with `-` for descending order. |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/companies/{companyId}/relationships' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: RelationshipsPaged
*Type:* object
A paginated list of relationships
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Relationship](#relationship)) | Yes | A page of Relationship objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: relationships

```json
{
  "data": [
    {
      "interactionScore": 0.92,
      "linkedIn": null,
      "person1": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com"
      },
      "person2": {
        "firstName": "John",
        "id": 10,
        "lastName": "Doe",
        "primaryEmailAddress": "john.doe@acme.co"
      }
    },
    {
      "interactionScore": 0.68,
      "linkedIn": {
        "connectedOn": "2022-06-15"
      },
      "person1": {
        "firstName": "Priya",
        "id": 2,
        "lastName": "Patel",
        "primaryEmailAddress": "priya.patel@northpointvc.com"
      },
      "person2": {
        "firstName": "Alex",
        "id": 11,
        "lastName": "Kim",
        "primaryEmailAddress": "alex.kim@acme.co"
      }
    },
    {
      "interactionScore": 0.35,
      "linkedIn": null,
      "person1": {
        "firstName": "Sam",
        "id": 3,
        "lastName": null,
        "primaryEmailAddress": "sam@northpointvc.com"
      },
      "person2": {
        "firstName": "Robin",
        "id": 12,
        "lastName": "Hill",
        "primaryEmailAddress": null
      }
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/companies/100/relationships?cursor=ICAgICAgIGFmdGVyOjo6Mw",
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Company Duplicate Suggestions

Operations about company duplicate suggestions

### Get All Company Duplicate Suggestions
`GET /v2/duplicates/company-suggestions`

- **Tag:** Company Duplicate Suggestions · **OperationId:** v2_duplicates_company-suggestions__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Retrieves company duplicate suggestions detected for your organization.

Each suggestion contains a recommended `primaryProfile` and a `duplicateProfiles` array
containing the single company profile Affinity has identified as a likely duplicate, along
with the `matchCriteria` that produced the suggestion. The full company payload is returned
for both sides so that an automated agent can evaluate the suggestion without additional
lookups.

Only actionable suggestions are returned: pairs that have no feedback recorded yet (not
merged, not marked as not-duplicates, and not skipped) and whose underlying company profiles
are still active and eligible to be merged. Suggestions that have already been acted on are
omitted.

You can narrow the results using the `filter` query parameter, which accepts the Affinity
Filtering Language. The filterable properties are:


| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `matchCriteria` | `enum` | `=` | `matchCriteria=name`, `matchCriteria=domain-redirect`, `matchCriteria=domain-match` |

To act on a suggestion, call `POST /v2/company-merges` with the `id` of the `primaryProfile`
and the `id` of the entry in `duplicateProfiles`.

Once the merge is applied, the suggestion stops being returned by this endpoint immediately.
Marking the pair as not duplicates has the same permanent effect. There is currently no way to
retrieve a suggestion after either action.

Skipping a suggestion is not permanent and works differently. It hides a `name` match
suggestion from the user who skipped it for two weeks, after which the suggestion is returned
again. It does not change what other users see, and it does not apply to the other match
criteria.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions), which is
granted to organization admins.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | When `true`, include the total count of the collection in the pagination response |
| `term` | `string` | No | Free-text search term to filter suggestions by company name |
| `filter` | `string` | No | Filter company duplicate suggestions using Affinity Filtering Language |
| `orderBy` | `array<string (enum: `name`, `-name`, `createdAt`, `-createdAt`)>` | No | Properties to order the results by. Prefix with `-` for descending order. Repeat the parameter to order by multiple properties. |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/duplicates/company-suggestions' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CompanyDuplicateSuggestionPaged
*Type:* object
Paginated list of company duplicate suggestions
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([CompanyDuplicateSuggestion](#companyduplicatesuggestion)) | Yes | Array of company duplicate suggestions |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

## Company Merges

Operations about company merges

### Get All Company Merges
`GET /v2/company-merges`

- **Tag:** Company Merges · **OperationId:** v2_company-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated company merges for the organization.

Returns all company merges initiated by users in your organization, including their current
status, the companies involved, and merge details. You can filter company merges using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `status` | `enum` | `=` | `status=in-progress`, `status=success`, `status=failed` |
| `taskId` | `text` | `=` | `taskId=789e0123-e45b-67c8-d901-234567890123` |

Company merges are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and
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
| `data` | `array<object> (≤ 100 items)` ([CompanyMergeState](#companymergestate)) | Yes | Array of company merge states |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Initiate Company Merge
`POST /v2/company-merges`

- **Tag:** Company Merges · **OperationId:** v2_company-merges__POST · **Stability:** `beta` · **Auth:** bearerAuth

Initiate a company merge to combine a duplicate company profile into a primary company profile.

This is an asynchronous process that will merge all data from the duplicate company into the primary company. Once the merge is initiated, you can track its progress using the returned task URL.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and organization admin role.

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get Company Merge
`GET /v2/company-merges/{mergeId}`

- **Tag:** Company Merges · **OperationId:** v2_company-merges_mergeId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific company merge.

Returns information about the company merge including its current status, the companies involved, timestamps, and any error information if the merge failed.

The `mergeId` can be obtained from the response of the [Get All Company Merges](#get-all-company-merges) endpoint, or by filtering company merges by task ID using `/v2/company-merges?filter=taskId={taskId}` after initiating a merge.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and organization admin role.

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get All Company Merge Tasks
`GET /v2/tasks/company-merges`

- **Tag:** Company Merges · **OperationId:** v2_tasks_company-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated company merge tasks for the organization.

Returns all merge tasks initiated by users in your organization, including their current status,
the companies involved, and task details.

You can filter tasks using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `status` | `enum` | `=` | `status=in-progress`, `status=success`, `status=failed` |

Tasks are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and
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
| `data` | `array<object> (≤ 100 items)` ([CompanyMergeTask](#companymergetask)) | Yes | Array of company merge tasks |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get Company Merge Task
`GET /v2/tasks/company-merges/{taskId}`

- **Tag:** Company Merges · **OperationId:** v2_tasks_company-merges_taskId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific task for company merges.

Returns information about the company merges for a specific task including its overall status,
number of merges in-progress, completed, and failed.

Detailed information about individual merges for this task can be found by querying:
`/v2/company-merges?filter=taskId={taskId}` See
[Company Merges](#get-all-company-merges) for more details.

Task statuses:

- `in-progress`: The merge task is currently being processed.
- `success`: The merge task completed successfully.
- `failed`: The merge task failed.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and
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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Emails

Operations about emails

### Get metadata on all Emails
`GET /v2/emails`

- **Tag:** Emails · **OperationId:** v2_emails__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all emails in Affinity. Returns basic information about the email interaction
and its participants. Will only return emails or subject lines that the current authenticated
user has permission to see.

Email bodies (the message content) are not available through the API. Only metadata such as the
subject, participants, and timestamps is returned.

If the authenticated user does not have permission to see an email's subject, the `subject`
field is obfuscated and returned as `********` rather than the actual subject line.

You can filter emails using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int64` | `=` | `id=1\|id=2\|id=3` |
| `sentAt` | `datetime` | `>`, `<`, `>=`, `<=` | `sentAt>2025-01-01T01:00:00Z` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-01-01T01:00:00Z` |

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
| `data` | `array<object> (≤ 100 items)` ([interactions.Email](#email)) | Yes | A page of Email results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

## Feedback

Operations about feedback

### Send Feedback
`POST /v2/feedback`

- **Tag:** Feedback · **OperationId:** v2_feedback__POST · **Stability:** `beta` · **Auth:** bearerAuth

Send feedback to Affinity about a particular product area or feature.

#### Request Body

**Media type:** `application/json`
Request body for sending feedback
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `mcp`, `api`, `other`)` | Yes | The type of feedback being submitted |
| `subject` | `string` | Yes | Subject of the feedback (Constraints: length ≥ 1; length ≤ 255) |
| `body` | `string` | Yes | The details of the feedback, please be thorough and include examples of what you're trying to accomplish and how the product could be improved to support it. (Constraints: length ≥ 1; length ≤ 10000) |

Example: submit-feedback
```json
{
  "body": "When using the MCP tool, the response formatting appears inconsistent",
  "subject": "Issue with MCP tool response formatting",
  "type": "mcp"
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/feedback' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"type":"mcp","subject":"Issue with MCP tool response formatting","body":"When using the MCP tool, the response formatting appears inconsistent"}'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

## Field Value Changes

Operations about field value changes

### Get all field value changes
`GET /v2/field-value-changes`

- **Tag:** Field Value Changes · **OperationId:** v2_field-value-changes__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve field value changes across all entities and fields in your Affinity workspace.

For an overview of field value changes, including which fields support change tracking and how the action types behave, see [Field Value Changes](https://developer.affinity.co/pages/data-model/working-with-field-data#field-value-changes).

This endpoint is built for delta-sync. Within a single sync, follow `pagination.nextUrl` to page through results until it becomes `null`, which means you have reached the most recent change. To run the next incremental sync, record the `changedAt` of the last change you processed and, on your next sync, filter for changes newer than that timestamp (for example, `filter=changedAt>2024-06-01T12:00:00Z`). Do not persist `nextUrl` between syncs, since it is `null` once you are caught up. Changes are returned in ascending order of `changedAt`, then by internal change ID. Only fields with change tracking enabled are included.

You can filter results using the `filter` query parameter.


| **Property Name** | **Type** | **Description** | **Allowed Operators** | **Examples** |
|---|---|---|---|---|
| `field.id` | `text` |  | `=` | `field.id=field-1234` |
| `listEntry.id` | `int64` |  | `=` | `listEntry.id=5678` |
| `changer.id` | `int64` | The person who made the change. | `=` | `changer.id=9012` |
| `changedAt` | `datetime` | When the change was made. | `>`, `<`, `>=`, `<=` | `changedAt>=2025-01-01T00:00:00Z` |
| `actionType` | `text` | The type of change (`add`, `update`, `delete`) | `=` | `actionType=add` |

Filters can be combined:
- `|` (OR) to match any of multiple values: `field.id=field-1 | field.id=field-2`
- `&` (AND) to require all conditions: `changedAt>=2025-01-01T00:00:00Z & changedAt<=2025-12-31T23:59:59Z`

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `orderBy` | `array<string (enum: `changedAt`, `-changedAt`)>` | No | Properties to sort by. Defaults to `changedAt`. Prefix with `-` for descending order. |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/field-value-changes' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: fieldValueChanges.FieldValueChangePaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([fieldValueChanges.FieldValueChange](#fieldvaluechangesfieldvaluechange)) | Yes | The field value changes for this page |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

## Files

Operations about files

### Get all Files
`GET /v2/files`

- **Tag:** Files · **OperationId:** v2_files__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns a page of Files visible to the caller.

You can filter files using the `filter` query parameter. The filter parameter is a string
that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt>=2026-01-01T00:00:00Z` |
| `creator.id` | `int64` | `=` | `creator.id=1` |

Results are ordered by `createdAt` descending (most recently uploaded first).

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/files' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: files.FileSummaryPaged
*Type:* object
A page of FileSummary objects.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([files.FileSummary](#filesfilesummary)) | Yes | A page of FileSummary objects. |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: files

```json
{
  "data": [
    {
      "createdAt": "2026-01-05T09:30:00Z",
      "creator": {
        "id": 1
      },
      "id": 1,
      "name": "pitch-deck.pdf",
      "size": 245760,
      "type": "application/pdf",
      "updatedAt": null
    },
    {
      "createdAt": "2026-01-01T00:00:00Z",
      "creator": null,
      "id": 2,
      "name": "term-sheet.docx",
      "size": 51200,
      "type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
      "updatedAt": "2026-01-02T12:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/files?cursor=ICAgICAgIGFmdGVyOjo6Mg",
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Search Files by Keyword
`POST /v2/files/search`

- **Tag:** Files · **OperationId:** v2_files_search__POST · **Stability:** `beta` · **Auth:** bearerAuth

Search files by keyword. The scope of the search is controlled by the request body:

- Provide `fileIds` to limit the search to specific files.
- Provide `companyId` to limit the search to files associated with a specific company.
- Omit both to search across your entire account.

`fileIds` and `companyId` are mutually exclusive.

Returns up to `limit` files ordered by relevance. Prompts with no strong matches may
still return low-relevance results.

Each result contains a matched file and a single representative excerpt (a matching
passage from that file). Even if a file contains multiple matching passages, it appears
exactly once in the response with one excerpt.

#### Request Body

**Media type:** `application/json`
**Variant:** File Keyword Search Criteria (org-wide or by file IDs)
Search all files in the org, or limit to specific file IDs.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` files ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `fileIds` | `array<integer<int32>> (≤ 100 items)` | No | Limit search to these specific files. Omit for org-wide search. |
| `limit` | `integer<int32>` | No | Maximum number of files to return. (Constraints: ≥ 1; ≤ 100; default `20`) |
**Variant:** File Keyword Search Criteria (by company)
Search files associated with a specific company.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` files ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `companyId` | `integer<int64>` | No | Restrict search to files associated with this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `limit` | `integer<int32>` | No | Maximum number of files to return. (Constraints: ≥ 1; ≤ 100; default `20`) |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/files/search' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: files.KeywordSearchResult
*Type:* object
Results of a keyword search over files.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([files.SearchResult](#filessearchresult)) | Yes | Matching file results, one per file, ordered by relevance. |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single File
`GET /v2/files/{fileId}`

- **Tag:** Files · **OperationId:** v2_files_fileId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns a single file's metadata and a temporary signed download URL.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fileId` | `integer<int32>` | Yes | File ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/files/{fileId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: files.File
*Type:* object
A file uploaded to a company, person, opportunity, or the organization directly.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `downloadUrl` | `string<uri>` | Yes | A temporary signed URL to download the file's contents. Expires 60 seconds after the response is generated. |
| `id` | `integer<int32>` | Yes | The file's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `name` | `string` | Yes | The file's name, including its extension. |
| `size` | `integer<int64>` | Yes | The file's size in bytes. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `type` | `string/null` | Yes | The file's MIME content type. `null` when the content type is not recorded. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who uploaded the file. `null` when the uploader is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the file was uploaded. |
| `updatedAt` | `string/null<date-time>` | Yes | When the file was last updated. `null` if the file has never been updated. |

Example: file

```json
{
  "createdAt": "2026-01-01T00:00:00Z",
  "creator": {
    "id": 1
  },
  "downloadUrl": "https://user-files.affinity.co/deal-files/abc123?signature=xyz",
  "id": 1,
  "name": "pitch-deck.pdf",
  "size": 245760,
  "type": "application/pdf",
  "updatedAt": "2026-01-01T00:00:00Z"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Inferred Connections

Operations about inferred connections

### Get Coworker Inferred Connections
`GET /v2/inferred-connections/coworkers`

- **Tag:** Inferred Connections · **OperationId:** v2_inferred-connections_coworkers__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns inferred connections based on shared work history, grouped by the target person, strongest first.

A connection is the belief that a `source` (a person in your Affinity data, with an `id`, whom you know) might know a `target` (a person not in your Affinity data, described only, whom you want to know), because the two had overlapping employment at a shared company.

The same target can be reachable through several people you know. Connections are grouped by target: each item in `data` is one target together with the `connections` to them. Within a target, connections are ordered strongest first; targets are ordered by their strongest connection, strongest first.

Each `target` carries the company they work at **today** in `target.currentCompany`: the company at which they are a potential contact now, which is not necessarily the shared employer behind the connection.

The `filter` parameter is required and must contain at least one filter. The only currently supported filter is `target.currentCompany.id`, which narrows the targets to a single such company.

## Filters


| **Property Name** | **Type** | **Description** | **Allowed Operators** | **Examples** |
|---|---|---|---|---|
| `target.currentCompany.id` | `integer` | The id of the company the `target` person currently works at. Must reference a single company; filtering on more than one (e.g. `target.currentCompany.id = 1 \| target.currentCompany.id = 2`) returns a `400`. | `=` | `target.currentCompany.id = 123` |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | Yes | Filter options. At least one filter is required; the only currently supported filter is `target.currentCompany.id`, which narrows the targets to the one company the `target` person currently works at. Filtering on more than one company returns a `400`. |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of targets to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/inferred-connections/coworkers' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: CoworkerConnectionGroupsPaged
*Type:* object
A paginated list of shared-work-history connections grouped by target person. Each item is one target and the connections inferred to them.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 50 items)` ([CoworkerConnectionGroup](#coworkerconnectiongroup)) | Yes | A page of targets, each with the shared-work-history connections to them, ordered by each target's strongest connection (strongest first). |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Investor-Executive Inferred Connections
`GET /v2/inferred-connections/investor-executive-connections`

- **Tag:** Inferred Connections · **OperationId:** v2_inferred-connections_investor-executive-connections__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns investor-executive inferred connections, grouped by the target person, strongest first.

A connection is the belief that a `source` (a person in your Affinity data, with an `id`, whom you know) might know a `target` (a person not in your Affinity data, described only, whom you want to know). In this connection type the source is an investor and the target is an executive: the source invested in a company where the target was an executive.

The same target can be reachable through several people you know. Connections are grouped by target: each item in `data` is one target together with the `connections` to them. Within a target, connections are ordered strongest first; targets are ordered by their strongest connection, strongest first.

Each `target` carries the company they work at **today** in `target.currentCompany`: the company at which they are a potential contact now, which is not necessarily the company involved in the investment.

The `filter` parameter is required and must contain at least one filter. The only currently supported filter is `target.currentCompany.id`, which narrows the targets to a single such company.

## Filters


| **Property Name** | **Type** | **Description** | **Allowed Operators** | **Examples** |
|---|---|---|---|---|
| `target.currentCompany.id` | `integer` | The id of the company the `target` person currently works at. Must reference a single company; filtering on more than one (e.g. `target.currentCompany.id = 1 \| target.currentCompany.id = 2`) returns a `400`. | `=` | `target.currentCompany.id = 123` |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | Yes | Filter options. At least one filter is required; the only currently supported filter is `target.currentCompany.id`, which narrows the targets to the one company the `target` person currently works at. Filtering on more than one company returns a `400`. |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of targets to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/inferred-connections/investor-executive-connections' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: InvestorExecutiveConnectionGroupsPaged
*Type:* object
A paginated list of investor-executive connections grouped by target person. Each item is one target and the connections inferred to them.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 50 items)` ([InvestorExecutiveConnectionGroup](#investorexecutiveconnectiongroup)) | Yes | A page of targets, each with the connections to them, ordered by each target's strongest connection (strongest first). |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Lists

Operations about lists

### Get metadata on all Lists
`GET /v2/lists`

- **Tag:** Lists · **OperationId:** v2_lists__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Lists in your organization that you have access to view.
Returns basic information about each List, including name, owner, and privacy settings.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `term` | `string` | No | Case-insensitive substring match on List name. |
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
| `data` | `array<object> (≤ 100 items)` ([ListWithType](#listwithtype)) | Yes | A page of ListWithType results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: success

```json
{
  "data": [
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "creatorId": 1,
      "id": 1,
      "isPublic": false,
      "name": "My Companies",
      "ownerId": 1,
      "type": "company"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "creatorId": 1,
      "id": 2,
      "isPublic": false,
      "name": "My Persons",
      "ownerId": 1,
      "type": "person"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

### Create a List
`POST /v2/lists`

- **Tag:** Lists · **OperationId:** v2_lists__POST · **Stability:** `beta` · **Auth:** bearerAuth

Create a new List.

The List type determines the kind of entities (Companies, Persons, or Opportunities) that can be
added. The requester is recorded as the creator and the owner.

#### Request Body

**Media type:** `application/json`
Request body for creating a new List
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | The name of the List (Constraints: length ≥ 1; length ≤ 255) |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for the List |
| `isPublic` | `boolean` | No | Whether the List is public. Public Lists are visible to all users in the organization. Creating a public List requires the "Share accessible Lists globally" permission. (Constraints: default `False`) |

Example: create-company-list
```json
{
  "isPublic": false,
  "name": "2026 Prospects",
  "type": "company"
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/lists' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"name":"2026 Prospects","type":"company","isPublic":false}'
```

#### Responses

##### 201 — application/json

Created

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
| `createdAt` | `string<date-time>` | Yes | The date and time the list was created |

Example: created-list

```json
{
  "createdAt": "2024-03-07T20:21:42Z",
  "creatorId": 1,
  "id": 42,
  "isPublic": false,
  "name": "2026 Prospects",
  "ownerId": 1,
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on a single List
`GET /v2/lists/{listId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `createdAt` | `string<date-time>` | Yes | The date and time the list was created |

Example: company-list

```json
{
  "createdAt": "2024-03-07T20:21:42Z",
  "creatorId": 1,
  "id": 1,
  "isPublic": false,
  "name": "My Companies",
  "ownerId": 1,
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on a single List's Fields
`GET /v2/lists/{listId}/fields`

- **Tag:** Lists · **OperationId:** v2_lists_listId_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns metadata on the Fields available on a single List.

Use the returned Field IDs to request field data from the GET `/v2/lists/{listId}/list-entries`
endpoint.

You can filter Fields using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `name` | `text` | `=`, `=~` | `name="Status"`, `name=~stat` |

Use the `includes` query parameter to add optional metadata to each Field in the response. Pass `includes` more than once to request multiple values.

| **Value** | **Adds to each Field** |
|---|---|
| `filterability` | How the field can be used in filter expressions on POST `/v2/lists/{listId}/list-entries/search` |
| `sortability` | How the field can be used in sort expressions on that endpoint |

The `time-in-current-status` Field is only filterable and sortable when the List has a Status column configured. On a List without one, its `filterability` and `sortability` are `null`.

Example: `GET /v2/lists/{listId}/fields?includes=filterability&includes=sortability`

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |
| `includes` | `array<string (enum: `filterability`, `sortability`)>` | No | Additional properties to include in the response |

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
| `data` | `array<object> (≤ 100 items)` ([FieldMetadata](#fieldmetadata)) | Yes | A page of FieldMetadata results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: company-list

```json
{
  "data": [
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-description",
      "isRequired": false,
      "name": "Description",
      "type": "enriched",
      "valueType": "text"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-industry",
      "isRequired": false,
      "name": "Industry",
      "type": "enriched",
      "valueType": "filterable-text-multi"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-investment-stage",
      "isRequired": false,
      "name": "Investment Stage",
      "type": "enriched",
      "valueType": "filterable-text"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-investors",
      "isRequired": false,
      "name": "Investors",
      "type": "enriched",
      "valueType": "filterable-text-multi"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-amount",
      "isRequired": false,
      "name": "Last Funding Amount (USD)",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-last-funding-date",
      "isRequired": false,
      "name": "Last Funding Date",
      "type": "enriched",
      "valueType": "datetime"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-linkedin-url",
      "isRequired": false,
      "name": "LinkedIn URL",
      "type": "enriched",
      "valueType": "text"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "isRequired": false,
      "name": "Location",
      "type": "enriched",
      "valueType": "location"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-number-of-employees",
      "isRequired": false,
      "name": "Number of Employees",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-total-funding-amount",
      "isRequired": false,
      "name": "Total Funding Amount (USD)",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-year-founded",
      "isRequired": false,
      "name": "Year Founded",
      "type": "enriched",
      "valueType": "number"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "created-at",
      "isRequired": false,
      "name": "Date Added",
      "type": "enriched",
      "valueType": "datetime"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": null,
      "id": "field-1",
      "isRequired": false,
      "name": "Custom global field",
      "type": "global",
      "valueType": "text"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": null,
      "id": "field-2",
      "isRequired": false,
      "name": "Custom list field",
      "type": "list",
      "valueType": "text"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "first-chat-message",
      "isRequired": false,
      "name": "First Chat Message",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "first-email",
      "isRequired": false,
      "name": "First Email",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "first-event",
      "isRequired": false,
      "name": "First Event",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "last-chat-message",
      "isRequired": false,
      "name": "Last Chat Message",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "last-contact",
      "isRequired": false,
      "name": "Last Contact",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "last-email",
      "isRequired": false,
      "name": "Last Email",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "last-event",
      "isRequired": false,
      "name": "Last Event",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "lists",
      "isRequired": false,
      "name": "Lists",
      "type": "global",
      "valueType": "list-multi"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "next-event",
      "isRequired": false,
      "name": "Next Event",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "notes",
      "isRequired": false,
      "name": "Notes",
      "type": "global",
      "valueType": "note"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "reminders",
      "isRequired": false,
      "name": "Reminders",
      "type": "global",
      "valueType": "reminder"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": null,
      "id": "source-of-introduction",
      "isRequired": false,
      "name": "Source of Introduction",
      "type": "relationship-intelligence",
      "valueType": "person"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "time-in-current-status",
      "isRequired": false,
      "name": "Time in Current Status",
      "type": "enriched",
      "valueType": "datetime"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/lists/1/fields?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/lists/1/fields?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get dropdown options for a List Field
`GET /v2/lists/{listId}/fields/{fieldId}/dropdown-options`

- **Tag:** Lists · **OperationId:** v2_lists_listId_fields_fieldId_dropdown-options__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns the dropdown options for a specific dropdown, ranked-dropdown, or status-dropdown field
on a List.

Use the returned dropdown option IDs when writing dropdown field values via the field update
endpoints.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `fieldId` | `string` | Yes | Field ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/fields/{fieldId}/dropdown-options' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: DropdownOptionPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([DropdownOption](#dropdownoption)) | Yes | A page of DropdownOption results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: dropdown-options

```json
{
  "data": [
    {
      "id": 1,
      "text": "Seed",
      "type": "dropdown"
    },
    {
      "id": 2,
      "text": "Series A",
      "type": "dropdown"
    },
    {
      "id": 3,
      "text": "Series B",
      "type": "dropdown"
    }
  ],
  "pagination": {
    "nextUrl": null,
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Create a dropdown option for a List Field
`POST /v2/lists/{listId}/fields/{fieldId}/dropdown-options`

- **Tag:** Lists · **OperationId:** v2_lists_listId_fields_fieldId_dropdown-options__POST · **Stability:** `beta` · **Auth:** bearerAuth

Create a dropdown option for a List Field.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `fieldId` | `string` | Yes | Field ID |

#### Request Body

**Media type:** `application/json`
**Variant:** [dropdownOptions.StandardDropdownOptionToBeCreated](#dropdownoptionsstandarddropdownoptiontobecreated)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `text` | `string` | Yes | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
**Variant:** [dropdownOptions.RankedDropdownOptionToBeCreated](#dropdownoptionsrankeddropdownoptiontobecreated)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `text` | `string` | Yes | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
**Variant:** [dropdownOptions.StatusDropdownOptionToBeCreated](#dropdownoptionsstatusdropdownoptiontobecreated)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `text` | `string` | Yes | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | Yes | Dropdown option's status category |
| `winRate` | `integer<int32>` | No | The user-designated probability that an entity in this status will progress to a `won` status. Only valid when `statusCategory` is `open`. Must be an integer between 0 and 100 inclusive. (Constraints: ≥ 0; ≤ 100) |

Example: dropdown
```json
{
  "text": "Seed",
  "type": "dropdown"
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/lists/{listId}/fields/{fieldId}/dropdown-options' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"type":"dropdown","text":"Seed"}'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: DropdownOption
*Type:* oneOf
**Variant:** [dropdownOptions.DropdownOption](#dropdownoptionsdropdownoption)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
**Variant:** [dropdownOptions.RankedDropdownOption](#dropdownoptionsrankeddropdownoption)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string/null (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
**Variant:** [dropdownOptions.StatusDropdownOption](#dropdownoptionsstatusdropdownoption)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string/null (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | Yes | Dropdown option's status category |
| `winRate` | `integer/null<int32>` | Yes | The user-designated probability that an entity in this status will progress to a `won` status. Only set on options whose `statusCategory` is `open`; null otherwise. (Constraints: ≥ 0; ≤ 100) |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |

Example: dropdown

```json
{
  "id": 4,
  "text": "Seed",
  "type": "dropdown"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Delete a dropdown option for a List Field
`DELETE /v2/lists/{listId}/fields/{fieldId}/dropdown-options/{dropdownOptionId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_fields_fieldId_dropdown-options_dropdownOptionId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

Delete a dropdown option for a List Field.

**Warning:** This permanently removes the option and clears every field value currently set to
it across all List Entries. The cleared values cannot be recovered.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `fieldId` | `string` | Yes | Field ID |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown option ID |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/lists/{listId}/fields/{fieldId}/dropdown-options/{dropdownOptionId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a dropdown option for a List Field
`GET /v2/lists/{listId}/fields/{fieldId}/dropdown-options/{dropdownOptionId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_fields_fieldId_dropdown-options_dropdownOptionId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Get a single dropdown option for a List Field.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `fieldId` | `string` | Yes | Field ID |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown option ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/fields/{fieldId}/dropdown-options/{dropdownOptionId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: DropdownOption
*Type:* oneOf
**Variant:** [dropdownOptions.DropdownOption](#dropdownoptionsdropdownoption)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
**Variant:** [dropdownOptions.RankedDropdownOption](#dropdownoptionsrankeddropdownoption)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string/null (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
**Variant:** [dropdownOptions.StatusDropdownOption](#dropdownoptionsstatusdropdownoption)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string/null (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | Yes | Dropdown option's status category |
| `winRate` | `integer/null<int32>` | Yes | The user-designated probability that an entity in this status will progress to a `won` status. Only set on options whose `statusCategory` is `open`; null otherwise. (Constraints: ≥ 0; ≤ 100) |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |

Example: dropdown

```json
{
  "id": 4,
  "text": "Seed",
  "type": "dropdown"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a dropdown option for a List Field
`POST /v2/lists/{listId}/fields/{fieldId}/dropdown-options/{dropdownOptionId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_fields_fieldId_dropdown-options_dropdownOptionId__POST · **Stability:** `beta` · **Auth:** bearerAuth

Update a dropdown option for a List Field.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `fieldId` | `string` | Yes | Field ID |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown option ID |

#### Request Body

**Media type:** `application/json`
- `dropdown` type field may update `text`.
- `ranked-dropdown` type field may update `text`, `rank`, and/or `color`.
- `status-dropdown` type field may update `text`, `rank`, `color`, `statusCategory`, and/or `winRate`.
**Variant:** [dropdownOptions.StandardDropdownOptionToBeUpdated](#dropdownoptionsstandarddropdownoptiontobeupdated)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | No | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
**Variant:** [dropdownOptions.RankedDropdownOptionToBeUpdated](#dropdownoptionsrankeddropdownoptiontobeupdated)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | No | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | No | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | No | Dropdown option color |
**Variant:** [dropdownOptions.StatusDropdownOptionToBeUpdated](#dropdownoptionsstatusdropdownoptiontobeupdated)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | No | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | No | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | No | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | No | Dropdown option's status category |
| `winRate` | `integer<int32>` | No | The user-designated probability that an entity in this status will progress to a `won` status. Only valid when `statusCategory` is `open`. Must be an integer between 0 and 100 inclusive. (Constraints: ≥ 0; ≤ 100) |

Example: dropdown
```json
{
  "text": "Series A"
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/lists/{listId}/fields/{fieldId}/dropdown-options/{dropdownOptionId}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"text":"Series A"}'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get all List Entries on a List
`GET /v2/lists/{listId}/list-entries`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

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

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

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
| `data` | `array/null` ([ListEntryWithEntity](#listentrywithentity)) | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: company-list-enriched

```json
{
  "data": [
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "entity": {
        "domain": "horizontech.com",
        "domains": [
          "horizontech.com"
        ],
        "fields": [
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-description",
            "name": "Description",
            "type": "enriched",
            "value": {
              "data": "Horizon Technologies is a leading technology company specializing in enterprise software and cloud infrastructure.",
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
                "Healthcare",
                "Fintech",
                "SaaS"
              ],
              "totalCount": 3,
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
                "Alex Rivera",
                "Taylor Wong"
              ],
              "totalCount": 2,
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
              "data": "https://linkedin.com/company/horizontech",
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
        "name": "Horizon Technologies"
      },
      "id": 1,
      "listId": 1,
      "type": "company"
    },
    {
      "createdAt": "2023-01-01T00:00:00Z",
      "creatorId": 1,
      "entity": {
        "domain": "crestwoodcap.com",
        "domains": [
          "crestwoodcap.com"
        ],
        "fields": [
          {
            "enrichmentSource": "affinity-data",
            "id": "affinity-data-description",
            "name": "Description",
            "type": "enriched",
            "value": {
              "data": "Crestwood Capital is a leading private equity firm focused on technology and growth-stage investments.",
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
                "Pharmaceuticals",
                "Biotechnology",
                "Defense",
                "Security",
                "Chemicals",
                "Research",
                "Technology",
                "Healthcare"
              ],
              "totalCount": 8,
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
                "Jordan Lee",
                "Michael Torres"
              ],
              "totalCount": 2,
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
              "data": "https://linkedin.com/company/crestwoodcap",
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
        "name": "Crestwood Capital"
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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Add a List Entry to a List
`POST /v2/lists/{listId}/list-entries`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Adds a Company or Person to a List as a new List Entry. Opportunities cannot be added with this endpoint.

The type of the entity referenced by `entity.id` is determined by the List's type: a Company ID for a company List, a Person ID for a person List. If no entity of the List's type exists with the given ID, the request is rejected with `400 Bad Request`.

Only the List's own required fields are checked. Required fields on the entity itself were already enforced when the entity was created, so they are not re-checked here.

If the List has a required field, the request is rejected with `400 Bad Request` and the missing field IDs are returned in the response body. This endpoint does not accept field values, so there is no API-level remediation: populate such a List through a UI flow that provides values at add time, or remove the required flag from the List's field configuration.

The new List Entry gets the same initial field values an add in the app gets: the Status field is set to the List's first open Status, and the Owners field is set to the List Entry's creator. The creator defaults to the authenticated user; it can be overridden by providing `creatorId`.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |

#### Request Body

**Media type:** `application/json`
Request body for creating a List Entry on a List. The entity referenced by `entity.id` must
match the List's type: a Company ID for a company List, a Person ID for a person List.
Opportunities cannot be added with this endpoint. An opportunity List's entries are the
opportunities themselves, and each opportunity belongs to exactly one List, so an existing
entity cannot be added to one.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `entity` | `object` | Yes | The Company or Person to add to the List. Provide its `id`; the entity must exist and match the List's type (a Company ID for a company List, a Person ID for a person List). |
| `creatorId` | `integer<int64>` | No | The internal Person ID to record as the List Entry's creator. Defaults to the authenticated user. Must be an internal Person in the same organization as the caller. (Constraints: ≥ 1; ≤ 9007199254740991) |

**`entity` details** — The Company or Person to add to the List. Provide its `id`; the entity must exist and match the List's type (a Company ID for a company List, a Person ID for a person List).

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The ID of the Company or Person. (Constraints: ≥ 1; ≤ 9007199254740991) |

Example: add-company-to-list
```json
{
  "entity": {
    "id": 12345
  }
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/lists/{listId}/list-entries' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"entity":{"id":12345}}'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: ListEntryWithEntity
*Type:* oneOf
**Variant:** [CompanyListEntry](#companylistentry)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([Company](#company)) | Yes | Company model |
**Variant:** [OpportunityListEntry](#opportunitylistentry)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([OpportunityWithFields](#opportunitywithfields)) | Yes | Opportunity model including the opportunity's fields. |
**Variant:** [PersonListEntry](#personlistentry)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([Person](#person)) | Yes | Person model |

Example: created-company-list-entry

```json
{
  "createdAt": "2026-01-01T00:00:00Z",
  "creatorId": 1,
  "entity": {
    "domain": "horizontech.com",
    "domains": [
      "horizontech.com"
    ],
    "fields": [],
    "id": 12345,
    "isGlobal": true,
    "name": "Horizon Technologies"
  },
  "id": 1,
  "listId": 1,
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Search List Entries
`POST /v2/lists/{listId}/list-entries/search`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_search__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Search for List Entries on a List matching the given criteria.

Accepts an optional combination of filters, sorts, and a search term. All fields in the request
body are optional. Omitting the body entirely is equivalent to `GET
/v2/lists/{listId}/list-entries` with default pagination.

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

### Field IDs

Field IDs used in `filters`, `sorts`, and `search.fieldIds` follow the formats described in
[Working with Field Data](https://developer.affinity.co/pages/data-model/working-with-field-data). Use `GET
/v2/lists/{listId}/fields?includes=filterability` to discover which fields are filterable and
what operators each supports. Use `GET /v2/lists/{listId}/fields?includes=sortability` for
sortable fields.

### `attributeId`

Some fields require an `attributeId` to specify which aspect to filter or sort on. The following
relationship intelligence fields all use `attributeId: "date-of-activity"`: `last-email`,
`first-email`, `last-contact`, `last-event`, `first-event`, `next-event`.

Use `GET /v2/lists/{listId}/fields?includes=filterability` to confirm which fields require an
`attributeId`.

### Search

The `search.term` is always matched against the entity's name and primary identifier: company name and primary domain (company lists), person first name, last name, and primary email address (person lists), or opportunity name (opportunity lists). Providing `search.fieldIds` extends the search to those additional fields; it does not restrict matching to only those fields. Fields with a `valueType` of `datetime` are not searchable and are silently ignored if included in `search.fieldIds`.

### Limits

- **Items per filter group** (filters or nested groups): 50

- **Values per filter** (e.g. options in `is-any-of`): 100

- **Sort criteria**: 5

- **Search term minimum length**: 3 characters

- **Results per page**: 100

### Pagination

Uses cursor-based pagination.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | The ID of the List to search |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldIds` | `array<string>` | No | Specific field IDs for which to return field data on each List Entry. Cannot be used together with `fieldTypes` — use one or the other. Use `GET /v2/lists/{listId}/fields` to discover available field IDs. |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)>` | No | A category of fields for which to return field data on each List Entry. Cannot be used together with `fieldIds` — use one or the other. |
| `cursor` | `string` | No | Cursor for the next or previous page. |
| `limit` | `integer<int32>` | No | Maximum number of List Entries to return per page |
| `totalCount` | `boolean` | No | When `true`, includes the total count of matching List Entries in the pagination response. Adds additional query cost; use only when needed. |

#### Request Body

**Media type:** `application/json`
Search criteria for filtering, sorting, and searching. All fields are optional  omitting the body returns all results with default pagination.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | `object` ([FilterGroup](#filtergroup)) | No | A tree of filter conditions to apply. Supports nested AND/OR grouping. Use the relevant fields endpoint for your resource type to discover available fields, their `valueType`, and supported operators. |
| `sorts` | `array<object> (≤ 5 items, ≥ 1 items)` ([SearchSort](#searchsort)) | No | One or more sort criteria, applied in order. Supports up to 5 sort items. Use the relevant fields endpoint for your resource type to discover sortable fields. |
| `search` | `object` ([SearchTerm](#searchterm)) | No | An optional keyword to match against field values. Results must satisfy both the search term AND any provided filters (intersection). Only one search object may be provided. The term is always matched against the entity name and primary identifier; providing `fieldIds` extends the search to additional fields rather than replacing the identity match. |

Example: filter-by-dropdown
```json
{
  "filters": {
    "filters": [
      {
        "fieldId": "field-4574182",
        "operator": "is-any-of",
        "value": [
          {
            "dropdownOptionId": 1
          },
          {
            "dropdownOptionId": 2
          }
        ],
        "valueType": "dropdown"
      }
    ],
    "operator": "and"
  }
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/lists/{listId}/list-entries/search' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"filters":{"operator":"and","filters":[{"fieldId":"field-4574182","valueType":"dropdown","operator":"is-any-of","value":[{"dropdownOptionId":1},{"dropdownOptionId":2}]}]}}'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: ListEntryWithEntityPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array/null` ([ListEntryWithEntity](#listentrywithentity)) | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single List Entry on a List
`GET /v2/lists/{listId}/list-entries/{listEntryId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve a single list entry.
Returns basic information and field data, including list-specific field data.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/lists/{listId}/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, the List Entry will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

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
**Variant:** [CompanyListEntry](#companylistentry)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([Company](#company)) | Yes | Company model |
**Variant:** [OpportunityListEntry](#opportunitylistentry)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([OpportunityWithFields](#opportunitywithfields)) | Yes | Opportunity model including the opportunity's fields. |
**Variant:** [PersonListEntry](#personlistentry)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([Person](#person)) | Yes | Person model |

Example: company-list-enriched

```json
{
  "createdAt": "2023-01-01T00:00:00Z",
  "creatorId": 1,
  "entity": {
    "domain": "horizontech.com",
    "domains": [
      "horizontech.com"
    ],
    "fields": [
      {
        "enrichmentSource": "affinity-data",
        "id": "affinity-data-description",
        "name": "Description",
        "type": "enriched",
        "value": {
          "data": "Horizon Technologies is a leading technology company specializing in enterprise software and cloud infrastructure.",
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
            "Healthcare",
            "Fintech",
            "SaaS"
          ],
          "totalCount": 3,
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
            "Alex Rivera",
            "Taylor Wong"
          ],
          "totalCount": 2,
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
          "data": "https://linkedin.com/company/horizontech",
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
    "name": "Horizon Technologies"
  },
  "id": 1,
  "listId": 1,
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Field Value Changes on a List Entry
`GET /v2/lists/{listId}/list-entries/{listEntryId}/field-value-changes`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_field-value-changes__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the historical value changes on the fields of a List Entry.

For an overview of field value changes, including which fields support change tracking and how the action types behave, see [Field Value Changes](https://developer.affinity.co/pages/data-model/working-with-field-data#field-value-changes).

Each change includes who made the change, when it occurred, the action that was performed, and
the value that was set. Changes are sorted by `changedAt` in ascending order (oldest first).

You can filter field value changes using the `filter` query parameter. The filter parameter is a string that
you can specify conditions based on the following properties.


| **Property Name** | **Type** | **Description** | **Allowed Operators** | **Examples** |
|---|---|---|---|---|
| `field.id` | `text` |  | `=` | `field.id=field-1234` |
| `changedAt` | `datetime` | When the change was made. | `>`, `<`, `>=`, `<=` | `changedAt>2026-01-01T00:00:00Z` |
| `changer.id` | `int64` | The person who made the change. | `=` | `changer.id=1234` |
| `actionType` | `text` | The type of change (`add`, `update`, `delete`) | `=` | `actionType=add` |

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}/field-value-changes' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: fieldValueChanges.FieldValueChangePaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([fieldValueChanges.FieldValueChange](#fieldvaluechangesfieldvaluechange)) | Yes | The field value changes for this page |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get field values on a single List Entry
`GET /v2/lists/{listId}/list-entries/{listEntryId}/fields`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all field values on a single list entry.

All fields will be included by default. The `ids` and `types` parameters can be used to filter the collection.

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
| `data` | `array<object> (≤ 100 items)` ([Field](#field)) | Yes | A page of Field results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

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
        "data": "Horizon Technologies is a leading technology company specializing in enterprise software and cloud infrastructure.",
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
          "Healthcare",
          "Fintech",
          "SaaS"
        ],
        "totalCount": 3,
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
          "Alex Rivera",
          "Taylor Wong"
        ],
        "totalCount": 2,
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
        "data": "https://linkedin.com/company/horizontech",
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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Perform batch operations on a list entry's fields
`PATCH /v2/lists/{listId}/list-entries/{listEntryId}/fields`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields__PATCH · **Stability:** `beta` · **Auth:** bearerAuth

Perform batch operations on a list entry's fields.

Currently the only operation at the endpoint is `update-fields`, which allows you to update multiple field values with a single request. This is equivalent to calling [the single field update](#update-a-single-field-value-on-a-list-entry) endpoint multiple times. You can update up to 100 fields per request.

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |

#### Request Body

**Media type:** `application/json`
**Variant:** [ListEntryBatchOperationUpdateFields](#listentrybatchoperationupdatefields)
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
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | No |  |

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
| `operation` | `string (enum: `update-fields`)` ([ListEntryBatchOperations](#listentrybatchoperations)) | No |  |

Example: update-fields

```json
{
  "operation": "update-fields"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single field value
`GET /v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields_fieldId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns a single field value on a list entry.

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
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`, `hidden`)` | Yes | The field's category. `hidden` is a redaction state rather than a category: it signals a field on a restricted opportunity the caller cannot manage, whose value is masked. |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `eventbrite`, `mailchimp`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | [CompaniesValue](#companiesvalue) \| [CompanyValue](#companyvalue) \| [DateValue](#datevalue) \| [DropdownsValue](#dropdownsvalue) \| [DropdownValue](#dropdownvalue) \| [FloatsValue](#floatsvalue) \| [FloatValue](#floatvalue) \| [FormulaValue](#formulavalue) \| [InteractionValue](#interactionvalue) \| [ListsValue](#listsvalue) \| [LocationsValue](#locationsvalue) \| [LocationValue](#locationvalue) \| [NoteValue](#notevalue) \| [PersonsValue](#personsvalue) \| [PersonValue](#personvalue) \| [RankedDropdownValue](#rankeddropdownvalue) \| [ReminderValue](#remindervalue) \| [TextsValue](#textsvalue) \| [TextValue](#textvalue) | Yes |  |

Example: company

```json
{
  "enrichmentSource": null,
  "id": "field-1",
  "name": "Field with company value",
  "type": "list",
  "value": {
    "data": {
      "domain": "horizontech.com",
      "id": 1,
      "name": "Horizon Technologies"
    },
    "type": "company"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a single field value on a List Entry
`POST /v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields_fieldId__POST · **Stability:** `beta` · **Auth:** bearerAuth

Update a single field value.

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

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
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | No |  |

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get values for a single field on a List Entry
`GET /v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}/values`

- **Tag:** Lists · **OperationId:** v2_lists_listId_list-entries_listEntryId_fields_fieldId_values__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through all values for a field on a list entry.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `listId` | `integer<int64>` | Yes | List ID |
| `listEntryId` | `integer<int64>` | Yes | List Entry ID |
| `fieldId` | `string` | Yes | Field ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/lists/{listId}/list-entries/{listEntryId}/fields/{fieldId}/values' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldValuesPaged
*Type:* oneOf
**Variant:** [CompaniesValuePaged](#companiesvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `company`, `company-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [DropdownsValuePaged](#dropdownsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `dropdown`, `dropdown-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Dropdown](#dropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [ListsValuePaged](#listsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([ListData](#listdata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [LocationsValuePaged](#locationsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `location`, `location-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Location](#location)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [PersonsValuePaged](#personsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `person`, `person-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [RankedDropdownValuePaged](#rankeddropdownvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([RankedDropdown](#rankeddropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [TextsValuePaged](#textsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `filterable-text-multi`)` | Yes | The type of value |
| `data` | `array<string> (≤ 100 items)` | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: company

```json
{
  "data": [
    {
      "domain": "horizontech.com",
      "id": 1,
      "name": "Horizon Technologies"
    }
  ],
  "pagination": {
    "nextUrl": null,
    "prevUrl": null
  },
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on Saved Views
`GET /v2/lists/{listId}/saved-views`

- **Tag:** Lists · **OperationId:** v2_lists_listId_saved-views__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Saved Views you have access to view for a specific List.
Returns basic information about each Saved View, including name, type, and creation date.

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
| `data` | `array<object> (≤ 100 items)` ([SavedView](#savedview)) | Yes | A page of SavedView results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on a single Saved View
`GET /v2/lists/{listId}/saved-views/{viewId}`

- **Tag:** Lists · **OperationId:** v2_lists_listId_saved-views_viewId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve detailed information about a specific Saved View you have access to view.
Returns Saved View configuration including name, type, and creation date.

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get all List Entries on a Saved View
`GET /v2/lists/{listId}/saved-views/{viewId}/list-entries`

- **Tag:** Lists · **OperationId:** v2_lists_listId_saved-views_viewId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) on a given Saved View.
Use this endpoint when you need to filter entities or only want **some**
field data to be returned: This endpoint respects the filters set on a Saved View
via web app, and only returns field data corresponding to the columns that have been
pulled into the Saved View via web app.

Though this endpoint respects the Saved View's filters and column/Field selection,
it does not yet preserve sort order. This endpoint also only supports **sheet-type
Saved Views**, and not board- or dashboard-type Saved Views.

See the [Data Model](https://developer.affinity.co/pages/data-model/the-basics) section for more information about Saved Views.

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

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
| `data` | `array/null` ([ListEntryWithEntity](#listentrywithentity)) | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Meetings

Operations about meetings

### Get metadata on all Meetings
`GET /v2/meetings`

- **Tag:** Meetings · **OperationId:** v2_meetings__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all Meetings in Affinity. Returns basic information about past and future meeting interactions
and its attendees.

You can filter meetings using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int64` | `=` | `id=1\|id=2\|id=3` |
| `startTime` | `datetime` | `>`, `<`, `>=`, `<=` | `startTime>2025-01-01T01:00:00Z` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-01-01T01:00:00Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-01-01T01:00:00Z` |

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
| `data` | `array<object> (≤ 100 items)` ([interactions.Meeting](#meeting)) | Yes | A page of Meeting results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

### Get a single Meeting
`GET /v2/meetings/{meetingId}`

- **Tag:** Meetings · **OperationId:** v2_meetings_meetingId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**

Retrieve detailed information about a specific Meeting you have access to view.
Returns meeting details including title, timing, organizer, creator, and attendee information.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `meetingId` | `integer<int64>` | Yes | Meeting ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/meetings/{meetingId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: interactions.Meeting
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The meeting's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `loggingType` | `string (enum: `automated`, `manual`)` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). |
| `title` | `string/null` | Yes | The meeting's title |
| `startTime` | `string<date-time>` | Yes | The timestamp of when the meeting starts |
| `endTime` | `string/null<date-time>` | Yes | The timestamp of when the meeting ends |
| `allDay` | `boolean` | Yes | Whether the meeting is all day |
| `creator` | [Attendee](#attendee) \| `null` | Yes | The person who created the meeting |
| `organizer` | [Attendee](#attendee) \| `null` | Yes | The person who organized the meeting |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the meeting was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the meeting was updated |
| `attendeesPreview` | `object` ([AttendeesPreview](#attendeespreview)) | Yes | A preview of the attendees in the meeting |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Notes

Operations about notes

### Get all Notes
`GET /v2/notes`

- **Tag:** Notes · **OperationId:** v2_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns all notes, with the exception of replies.
You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int32` | `=` | `id=1\|id=2\|id=3` |
| `creator.id` | `int32` | `=` | `creator.id=1` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-02-03T10:48:24Z` |

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
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Note](#notesnote)) | Yes | A page of Note objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

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
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 1,
      "mentions": [],
      "transcriptId": 1,
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
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 2,
      "mentions": [],
      "transcriptId": 2,
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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Create a Note
`POST /v2/notes`

- **Tag:** Notes · **OperationId:** v2_notes__POST · **Stability:** `beta` · **Auth:** bearerAuth

Create a new note. By default it is authored by the calling user; set `creator` to attribute
it to a different internal person in your organization. Notes can be attached directly to
entities (`Persons`, `Companies`, `Opportunities`), anchored to an interaction (`meeting`,
`call`, or `chat message`), or written as a reply to an existing note.

The `type` field selects the shape of the request body. AI Notetaker note types
(`ai-notetaker`, `ai-notetaker-reply`) are system-generated and cannot be created through
this endpoint.


| **`type`** | **Description** | **Required** | **Optional** |
|------------|-----------------|--------------|--------------|
| `entities` | A note attached directly to one or more entities. | `content`, and at least one of `persons` / `companies` / `opportunities`. | Any combination of `persons` / `companies` / `opportunities`. |
| `interaction` | A note anchored to a meeting, call, or chat message. | `content`, `interaction.{type,id}`. | `persons` / `companies` / `opportunities`, added as direct associations on top of the interaction's own participants. |
| `user-reply` | A reply to an existing root note. Replies have no entity associations or interaction attachment of their own. | `content`, `parent.id` (must reference an existing root note the caller can access). | None |

By default a note is authored by the calling user. To attribute a note to a different member
of your organization, set the optional `creator` field to reference that person by id. The
referenced person must be an active internal person in your organization.

By default a note's creation time is the time of the request. To backfill a historical note,
set the optional `createdAt` field to the time the note should be recorded as created.

**Body content.** `content.html` is rendered HTML that must use only the allowed tags;
submitting restricted tags, attributes, URL schemes, or mention spans will cause the request to
fail. See the request examples below for representative payloads.

#### Request Body

**Media type:** `application/json`
Request body for creating a note. The `type` field selects between three variants:

- `entities`: a note attached directly to one or more Persons, Companies, and/or Opportunities.
- `interaction`: a note attached to a meeting, call, or chat message. May optionally also be associated with additional entities.
- `user-reply`: a reply to an existing root note. Replies have no entity associations or interaction attachment of their own.

Additional notes:

- By default a note is authored by the calling user. To attribute it to another member of your organization, set `creator` to reference that person by id. The referenced person must be an active internal person in your organization.
- By default a note's creation time is the time of the request. To backfill a historical note, set `createdAt` to the time the note should be recorded as created.
- For enterprise customers, the visibility follows the fallback visibility behavior for the organization.
- System-generated note types (`ai-notetaker`, `ai-notetaker-reply`, `email`) cannot be created here.
**Variant:** [notes.EntitiesNoteToBeCreated](#notesentitiesnotetobecreated)
Request body for creating a note attached directly to one or more entities. At least one of `persons`, `companies`, or `opportunities` must include an entry, since a note of this type requires at least one attached entity.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The note type. Must be `entities` to create a note attached to only entities. |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | Yes | The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below. |
| `creator` | `object` ([PersonReference](#personreference)) | No | The person to record as the note's creator. Defaults to the calling user when omitted, and must reference an active internal person in your organization. |
| `createdAt` | `string<date-time>` | No | The time to record as when the note was created. Set this to backfill historical notes with their original date. Defaults to the current time when omitted. |
| `persons` | `array<object> (≤ 100 items)` ([PersonReference](#personreference)) | No | Persons to attach the note to. Each item references a Person by id. |
| `companies` | `array<object> (≤ 100 items)` ([CompanyReference](#companyreference)) | No | Companies to attach the note to. Each item references a Company by id. |
| `opportunities` | `array<object> (≤ 100 items)` ([OpportunityReference](#opportunityreference)) | No | Opportunities to attach the note to. Each item references an Opportunity by id. |
**Variant:** [notes.InteractionNoteToBeCreated](#notesinteractionnotetobecreated)
Request body for creating a note attached to an interaction. Notes can be attached to a meeting, call, or chat message.
`interaction.type` and `interaction.id` are both required and must reference a meeting, call, or chat message the caller can access. Notes of this type are anchored to a single interaction. Entity associations (`persons`, `companies`, `opportunities`) are optional and can supplement the interaction attachment as additional direct associations on top of the interaction's own participants. The interaction participants are implicitly associated with the note by virtue of the interaction attachment, so they do not need to be included in the `persons` array unless the caller wants to create additional direct associations beyond those implied by the interaction itself.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The note type. Must be `interaction` to create an interaction note. |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | Yes | The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below. |
| `creator` | `object` ([PersonReference](#personreference)) | No | The person to record as the note's creator. Defaults to the calling user when omitted, and must reference an active internal person in your organization. |
| `createdAt` | `string<date-time>` | No | The time to record as when the note was created. Set this to backfill historical notes with their original date. Defaults to the current time when omitted. |
| `interaction` | [notes.MeetingReference](#notesmeetingreference) \| [notes.CallReference](#notescallreference) \| [notes.ChatMessageReference](#noteschatmessagereference) | Yes | A reference to the existing interaction that an interaction note will be attached to. Notes can be attached to a meeting, call, or chat message. |
| `persons` | `array<object> (≤ 100 items)` ([PersonReference](#personreference)) | No | Persons to additionally attach the note to, beyond those implied by the interaction itself. Each item references a Person by id. |
| `companies` | `array<object> (≤ 100 items)` ([CompanyReference](#companyreference)) | No | Companies to additionally attach the note to. Each item references a Company by id. |
| `opportunities` | `array<object> (≤ 100 items)` ([OpportunityReference](#opportunityreference)) | No | Opportunities to additionally attach the note to. Each item references an Opportunity by id. |
**Variant:** [notes.UserReplyNoteToBeCreated](#notesuserreplynotetobecreated)
Request body for creating a user reply to an existing note. `parent.id` is required and must reference an existing root note (not itself a reply) that the caller can access.
Reply notes do not support entity associations or interaction attachments. Replies to AI Notetaker notes are also created with `type: user-reply`; the reply itself is a user-authored note, not an AI-generated one.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The note type. Must be `user-reply` to create a reply note. |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | Yes | The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below. |
| `creator` | `object` ([PersonReference](#personreference)) | No | The person to record as the note's creator. Defaults to the calling user when omitted, and must reference an active internal person in your organization. |
| `createdAt` | `string<date-time>` | No | The time to record as when the note was created. Set this to backfill historical notes with their original date. Defaults to the current time when omitted. |
| `parent` | `object` ([notes.NoteReference](#notesnotereference)) | Yes | A reference to an existing note by its id. |

Example: entities
```json
{
  "companies": [
    {
      "id": 10
    }
  ],
  "content": {
    "html": "<p>Followed up after the demo. Strong interest, will recirculate next week.</p>"
  },
  "opportunities": [
    {
      "id": 100
    }
  ],
  "persons": [
    {
      "id": 2
    },
    {
      "id": 3
    }
  ],
  "type": "entities"
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/notes' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"type":"entities","content":{"html":"<p>Followed up after the demo. Strong interest, will recirculate next week.</p>"},"persons":[{"id":2},{"id":3}],"companies":[{"id":10}],"opportunities":[{"id":100}]}'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: notes.Note
*Type:* oneOf
**Variant:** [notes.EntitiesNote](#notesentitiesnote)
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
**Variant:** [notes.InteractionNote](#notesinteractionnote)
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | [notes.MeetingInteraction](#notesmeetinginteraction) \| [notes.CallInteraction](#notescallinteraction) \| [notes.ChatMessageInteraction](#noteschatmessageinteraction) \| [notes.EmailInteraction](#notesemailinteraction) | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
**Variant:** [notes.AiNotetakerRootNote](#notesainotetakerrootnote)
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` ([notes.MeetingInteraction](#notesmeetinginteraction)) | No | The meeting this AI Notetaker was invited to. |
| `transcriptId` | `integer/null<int32>` | Yes | The id of the transcript of the AI notetaker note, or `null` when the org does not retain transcripts or the transcript was deleted. (Constraints: ≥ 1; ≤ 2147483647) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
**Variant:** [notes.UserReplyNote](#notesuserreplynote)
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |
**Variant:** [notes.AiNotetakerReplyNote](#notesainotetakerreplynote)
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` ([notes.MeetingInteraction](#notesmeetinginteraction)) | No | The meeting this AI Notetaker was invited to. |
| `transcriptId` | `integer/null<int32>` | Yes | The id of the transcript of the AI notetaker reply note, or `null` when the org does not retain transcripts or the transcript was deleted. (Constraints: ≥ 1; ≤ 2147483647) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

Example: entities

```json
{
  "content": {
    "html": "<p>Followed up after the demo. Strong interest, will recirculate next week.</p>"
  },
  "createdAt": "2023-01-01T00:00:00Z",
  "creator": {
    "firstName": "Jane",
    "id": 1,
    "lastName": "Smith",
    "primaryEmailAddress": "jane.smith@northpointvc.com",
    "type": "internal"
  },
  "id": 1,
  "mentions": [],
  "type": "entities",
  "updatedAt": null
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Search Notes by Keyword
`POST /v2/notes/search`

- **Tag:** Notes · **OperationId:** v2_notes_search__POST · **Stability:** `beta` · **Auth:** bearerAuth

Search notes by keyword. The scope of the search is controlled by the request body:

- Provide `noteIds` to limit the search to specific notes.
- Provide `companyId` to limit the search to notes associated with a specific company.
- Omit both to search across your entire account.

`noteIds` and `companyId` are mutually exclusive.

Returns up to `limit` notes ordered by relevance. Prompts with no strong matches may
still return low-relevance results.

Each result contains a matched note and a single representative excerpt (a matching
passage from that note). Even if a note contains multiple matching passages, it appears
exactly once in the response with one excerpt.

#### Request Body

**Media type:** `application/json`
**Variant:** Note Keyword Search Criteria (org-wide or by note IDs)
Search all notes in the org, or limit to specific note IDs.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` notes ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `noteIds` | `array<integer<int32>> (≤ 100 items)` | No | Limit search to these specific notes. Omit for org-wide search. |
| `limit` | `integer<int32>` | No | Maximum number of notes to return. (Constraints: ≥ 1; ≤ 100; default `20`) |
**Variant:** Note Keyword Search Criteria (by company)
Search notes associated with a specific company.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` notes ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `companyId` | `integer<int64>` | No | Restrict search to notes associated with this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `limit` | `integer<int32>` | No | Maximum number of notes to return. (Constraints: ≥ 1; ≤ 100; default `20`) |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/notes/search' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: notes.KeywordSearchResult
*Type:* object
Results of a keyword search over notes.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([notes.SearchResult](#notessearchresult)) | Yes | Matching note results, one per note, ordered by relevance. |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Delete a single Note
`DELETE /v2/notes/{noteId}`

- **Tag:** Notes · **OperationId:** v2_notes_noteId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

Delete a note. You can only delete notes you created. Deleting a root note also deletes its
replies (both user replies and AI Notetaker replies); deleting a reply removes only that reply.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | The id of the Note to delete |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/notes/{noteId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Note
`GET /v2/notes/{noteId}`

- **Tag:** Notes · **OperationId:** v2_notes_noteId__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
**Variant:** [notes.EntitiesNote](#notesentitiesnote)
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
**Variant:** [notes.InteractionNote](#notesinteractionnote)
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | [notes.MeetingInteraction](#notesmeetinginteraction) \| [notes.CallInteraction](#notescallinteraction) \| [notes.ChatMessageInteraction](#noteschatmessageinteraction) \| [notes.EmailInteraction](#notesemailinteraction) | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
**Variant:** [notes.AiNotetakerRootNote](#notesainotetakerrootnote)
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` ([notes.MeetingInteraction](#notesmeetinginteraction)) | No | The meeting this AI Notetaker was invited to. |
| `transcriptId` | `integer/null<int32>` | Yes | The id of the transcript of the AI notetaker note, or `null` when the org does not retain transcripts or the transcript was deleted. (Constraints: ≥ 1; ≤ 2147483647) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
**Variant:** [notes.UserReplyNote](#notesuserreplynote)
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |
**Variant:** [notes.AiNotetakerReplyNote](#notesainotetakerreplynote)
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` ([notes.MeetingInteraction](#notesmeetinginteraction)) | No | The meeting this AI Notetaker was invited to. |
| `transcriptId` | `integer/null<int32>` | Yes | The id of the transcript of the AI notetaker reply note, or `null` when the org does not retain transcripts or the transcript was deleted. (Constraints: ≥ 1; ≤ 2147483647) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |

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
    "lastName": "Smith",
    "primaryEmailAddress": "jane.smith@northpointvc.com",
    "type": "internal"
  },
  "id": 1,
  "mentions": [],
  "transcriptId": 1,
  "type": "ai-notetaker",
  "updatedAt": "2023-01-21T00:00:00Z"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a single Note
`POST /v2/notes/{noteId}`

- **Tag:** Notes · **OperationId:** v2_notes_noteId__POST · **Stability:** `beta` · **Auth:** bearerAuth

Make an update to an existing note's body content or its entity associations.

You can only update notes you have write access to. You can update any type of note including
AI Notetaker notes (`ai-notetaker`, `ai-notetaker-reply`), but a note's type itself cannot be
changed.

All body properties are optional: only the properties supplied are updated, and other
properties are left unchanged. For each of `persons`, `companies`, and `opportunities`, you
may:

- omit the field to leave existing associations unchanged
- send an empty array (`[]`) to clear all associations of that kind
- send a non-empty array to replace the existing set with the supplied list.

Reply notes (`user-reply`, `ai-notetaker-reply`) have no entity associations, so only
`content` can be updated for replies.

Updating `content` is subject to the same HTML restrictions as creation; submitting restricted
HTML will cause the request to fail. See the request examples below.

The content of notes that contain @mentions cannot be updated through this endpoint;
attempting to do so returns `400 Bad Request`.

Returns `204 No Content` on success, regardless of whether any properties actually changed.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `noteId` | `integer<int32>` | Yes | The id of the Note to update |

#### Request Body

**Media type:** `application/json`
Request body for updating an existing note. All properties are optional: only those explicitly provided are updated, and other properties are left unchanged.

The properties that may be updated depend on the existing note's type:

- Root notes (`entities`, `interaction`, `ai-notetaker`) may update `content` and the entity association arrays (`persons`, `companies`, `opportunities`).
- Reply notes (`user-reply`, `ai-notetaker-reply`) may update `content` only; attaching `persons`, `companies`, or `opportunities` to a reply note is rejected.

For each of `persons`, `companies`, and `opportunities`, you may:

- omit the field to leave existing associations unchanged
- send an empty array (`[]`) to clear all associations of that kind
- send a non-empty array to replace the existing set with the supplied list.

Any note the caller has write access to can be updated, including AI Notetaker notes. A note's type itself cannot be changed. The content of notes that contain @mentions cannot be updated.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | No | If provided, replaces the note's content. Subject to the same HTML restrictions as creation. |
| `persons` | `array<object> (≤ 100 items)` ([PersonReference](#personreference)) | No | Persons attached to the note. Each item references a Person by id. Only valid for root notes. |
| `companies` | `array<object> (≤ 100 items)` ([CompanyReference](#companyreference)) | No | Companies attached to the note. Each item references a Company by id. Only valid for root notes. |
| `opportunities` | `array<object> (≤ 100 items)` ([OpportunityReference](#opportunityreference)) | No | Opportunities attached to the note. Each item references an Opportunity by id. Only valid for root notes. |

Example: content-only
```json
{
  "content": {
    "html": "<p>Updated recap: pricing approved, contract going out today.</p>"
  }
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/notes/{noteId}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"content":{"html":"<p>Updated recap: pricing approved, contract going out today.</p>"}}'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Companies attached to a Note
`GET /v2/notes/{noteId}/attached-companies`

- **Tag:** Notes · **OperationId:** v2_notes_noteId_attached-companies__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | Yes | A page of Company results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Opportunities attached to a Note
`GET /v2/notes/{noteId}/attached-opportunities`

- **Tag:** Notes · **OperationId:** v2_notes_noteId_attached-opportunities__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `data` | `array<object> (≤ 100 items)` ([Opportunity](#opportunity)) | Yes | A page of Opportunity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: success

```json
{
  "data": [
    {
      "id": 1,
      "isRedacted": false,
      "isRestricted": false,
      "listId": 1000,
      "listName": "Pipeline Q1 2024",
      "name": "Opp Name"
    },
    {
      "id": 2,
      "isRedacted": false,
      "isRestricted": false,
      "listId": 1001,
      "listName": "Enterprise Deals",
      "name": "Another Opp Name"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/notes/1/attached-opportunities?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/notes/1/attached-opportunities?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Persons attached to a Note
`GET /v2/notes/{noteId}/attached-persons`

- **Tag:** Notes · **OperationId:** v2_notes_noteId_attached-persons__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A page of Person results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get replies for a Note
`GET /v2/notes/{noteId}/replies`

- **Tag:** Notes · **OperationId:** v2_notes_noteId_replies__GET · **Stability:** `beta` · **Auth:** bearerAuth

This endpoint returns reply notes for a given note id.
You can filter replies using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `creator.id` | `int32` | `=` | `creator.id=1` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-02-03T10:48:24Z` |

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
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Reply](#notesreply)) | Yes | A page of Note Replies |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: user-reply

```json
{
  "data": [
    {
      "content": {
        "html": "<p> This is a user reply note. <span data-type=\"note-mention\" data-note-mention-type=\"person\" data-note-mention-person-id=\"1\"> Michael Torres </span> was mentioned. </p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 2,
      "mentions": [
        {
          "id": 1,
          "person": {
            "firstName": "Michael",
            "id": 1,
            "lastName": "Torres",
            "primaryEmailAddress": "m.torres@northpointvc.com",
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
    },
    {
      "content": {
        "html": "<p>This is another user reply note.</p>"
      },
      "createdAt": "2023-02-01T00:00:00Z",
      "creator": {
        "firstName": "Michael",
        "id": 2,
        "lastName": "Torres",
        "primaryEmailAddress": "m.torres@northpointvc.com",
        "type": "internal"
      },
      "id": 3,
      "mentions": [],
      "parent": {
        "id": 1
      },
      "type": "user-reply",
      "updatedAt": "2023-03-01T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/notes/1/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/notes/1/replies?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Opportunities

Operations about opportunities

### Get all Opportunities
`GET /v2/opportunities`

- **Tag:** Opportunities · **OperationId:** v2_opportunities__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through Opportunities in Affinity.
Returns basic information but **not** field data on each Opportunity.

To access field data on Opportunities, use the `/lists/{list_id}/list-entries`
or the `/v2/lists/{list_id}/saved-views/{view_id}/list-entries` GET endpoint.

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

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
| `data` | `array<object> (≤ 100 items)` ([Opportunity](#opportunity)) | Yes | A page of Opportunity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Delete an Opportunity
`DELETE /v2/opportunities/{opportunityId}`

- **Tag:** Opportunities · **OperationId:** v2_opportunities_opportunityId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Deletes an Opportunity. Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and manage access to the opportunity.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `opportunityId` | `integer<int64>` | Yes | Opportunity ID |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/opportunities/{opportunityId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Opportunity
`GET /v2/opportunities/{opportunityId}`

- **Tag:** Opportunities · **OperationId:** v2_opportunities_opportunityId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns basic information but **not** field data on the requested Opportunity.

To access field data on Opportunities, use the `/lists/{list_id}/list-entries`
or the `/v2/lists/{list_id}/saved-views/{view_id}/list-entries` GET endpoint.

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
Opportunity model.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity. When `isRedacted` is `true`, the real name is masked and this value is the literal string `[Hidden]`. |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listName` | `string` | Yes | The name of the list that the opportunity belongs to |
| `isRestricted` | `boolean` | Yes | Whether the opportunity is restricted. `false` for customers without the Restricted Opportunities feature enabled. |
| `isRedacted` | `boolean` | Yes | Whether the response is redacted because the requesting user does not have access to this restricted opportunity. The real name is masked as `[Hidden]` when `true`. Always `false` when `isRestricted` is `false`. |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update an Opportunity
`POST /v2/opportunities/{opportunityId}`

- **Tag:** Opportunities · **OperationId:** v2_opportunities_opportunityId__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Updates an Opportunity. Only provided properties are updated; properties omitted from the request keep their current value.

Requires the "Export data from Lists" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and manage access to the opportunity.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `opportunityId` | `integer<int64>` | Yes | Opportunity ID |

#### Request Body

**Media type:** `application/json`
Partial-update request body for an Opportunity. Only provided properties are updated; properties omitted from the request keep their current value.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | The name of the opportunity. (Constraints: length ≥ 1; length ≤ 255) |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/opportunities/{opportunityId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Notes for an Opportunity
`GET /v2/opportunities/{opportunityId}/notes`

- **Tag:** Opportunities · **OperationId:** v2_opportunities_opportunityId_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns Notes for a given Opportunity which includes directly attached notes and those attached to persons on this Opportunity.

You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `creator.id` | `int32` | `=` | `creator.id=1` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-02-03T10:48:24Z` |

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
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Note](#notesnote)) | Yes | A page of Note objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: entities

```json
{
  "data": [
    {
      "content": {
        "html": "<p>Met with the founding team to discuss the Series A term sheet.</p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 1,
      "mentions": [
        {
          "id": 1,
          "person": {
            "firstName": "Jane",
            "id": 1,
            "lastName": "Smith",
            "primaryEmailAddress": "jane.smith@northpointvc.com",
            "type": "internal"
          },
          "type": "person"
        }
      ],
      "type": "entities",
      "updatedAt": "2023-01-01T00:00:00Z"
    },
    {
      "content": {
        "html": "<p>This is another note!</p>"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 2,
      "mentions": [],
      "type": "entities",
      "updatedAt": "2024-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/opportunities/1/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/opportunities/1/notes?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Person Duplicate Suggestions

Operations about person duplicate suggestions

### Get All Person Duplicate Suggestions
`GET /v2/duplicates/person-suggestions`

- **Tag:** Person Duplicate Suggestions · **OperationId:** v2_duplicates_person-suggestions__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Retrieves person duplicate suggestions detected for your organization.

Each suggestion contains a recommended `primaryProfile` and a `duplicateProfiles` array
containing the single person profile Affinity has identified as a likely duplicate, along
with the `matchCriteria` that produced the suggestion. The full person payload is returned
for both sides so that an automated agent can evaluate the suggestion without additional
lookups.

Only actionable suggestions are returned: pairs that have no feedback recorded yet (not
merged, not marked as not-duplicates, and not skipped) and whose underlying person profiles
are still active and eligible to be merged. Suggestions that have already been acted on are
omitted.

You can narrow the results using the `filter` query parameter, which accepts the Affinity
Filtering Language. The filterable properties are:


| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `matchCriteria` | `enum` | `=` | `matchCriteria=name`, `matchCriteria=intelligent` |

To act on a suggestion, call `POST /v2/person-merges` with the `id` of the `primaryProfile`
and the `id` of the entry in `duplicateProfiles`.

Once the merge is applied, the suggestion stops being returned by this endpoint immediately.
Marking the pair as not duplicates has the same permanent effect. There is currently no way to
retrieve a suggestion after either action.

Skipping a suggestion is not permanent and works differently. It hides a `name` match
suggestion from the user who skipped it for two weeks, after which the suggestion is returned
again. It does not change what other users see, and it does not apply to the other match
criteria.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions), which is
granted to organization admins.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | When `true`, include the total count of the collection in the pagination response |
| `term` | `string` | No | Free-text search term to filter suggestions by the person's first name |
| `filter` | `string` | No | Filter person duplicate suggestions using Affinity Filtering Language |
| `orderBy` | `array<string (enum: `name`, `-name`, `createdAt`, `-createdAt`)>` | No | Properties to order the results by. Prefix with `-` for descending order. Repeat the parameter to order by multiple properties. |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/duplicates/person-suggestions' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonDuplicateSuggestionPaged
*Type:* object
Paginated list of person duplicate suggestions
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonDuplicateSuggestion](#personduplicatesuggestion)) | Yes | Array of person duplicate suggestions |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

## Person Merges

Operations about person merges

### Get All Person Merges
`GET /v2/person-merges`

- **Tag:** Person Merges · **OperationId:** v2_person-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated person merges for the organization.

Returns all person merges initiated by users in your organization, including their current
status, the persons involved, and merge details. You can filter person merges using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `status` | `enum` | `=` | `status=in-progress`, `status=success`, `status=failed` |
| `taskId` | `text` | `=` | `taskId=789e0123-e45b-67c8-d901-234567890123` |

Person merges are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and
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
| `data` | `array<object> (≤ 100 items)` ([PersonMergeState](#personmergestate)) | Yes | Array of person merge states |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Initiate Person Merge
`POST /v2/person-merges`

- **Tag:** Person Merges · **OperationId:** v2_person-merges__POST · **Stability:** `beta` · **Auth:** bearerAuth

Initiate a person merge to combine a duplicate person profile into a primary person profile.

This is an asynchronous process that will merge all data from the duplicate person into the primary person. Once the merge is initiated, you can track its progress using the returned task URL.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and organization admin role.

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get Person Merge
`GET /v2/person-merges/{mergeId}`

- **Tag:** Person Merges · **OperationId:** v2_person-merges_mergeId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific person merge.

Returns information about the person merge including its current status, the persons involved, timestamps, and any error information if the merge failed.

The `mergeId` can be obtained from the response of the [Get All Person Merges](#get-all-person-merges) endpoint, or by filtering person merges by task ID using `/v2/person-merges?filter=taskId={taskId}` after initiating a merge.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and organization admin role.

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get All Person Merge Tasks
`GET /v2/tasks/person-merges`

- **Tag:** Person Merges · **OperationId:** v2_tasks_person-merges__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve paginated person merge tasks for the organization.

Returns all merge tasks initiated by users in your organization, including their current status,
the persons involved, and task details.

You can filter tasks using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties:


| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `status` | `enum` | `=` | `status=in-progress`, `status=success`, `status=failed` |

Tasks are returned in reverse chronological order (most recent first).

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and
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
| `data` | `array<object> (≤ 100 items)` ([PersonMergeTask](#personmergetask)) | Yes | Array of person merge tasks |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get Person Merge Task
`GET /v2/tasks/person-merges/{taskId}`

- **Tag:** Person Merges · **OperationId:** v2_tasks_person-merges_taskId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Retrieve the status and details of a specific task for person merges.

Returns information about the person merges for a specific task including its overall status,
number of merges in-progress, completed, and failed.

Detailed information about individual merges for this task can be found by querying:
`/v2/person-merges?filter=taskId={taskId}` See
[Person Merges](#get-all-person-merges) for more details.

Task statuses:

- `in-progress`: The merge task is currently being processed.
- `success`: The merge task completed successfully.
- `failed`: The merge task failed.

Requires the "Manage duplicates" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and
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

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Persons

Operations about persons

### Get all Persons
`GET /v2/persons`

- **Tag:** Persons · **OperationId:** v2_persons__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through Persons in Affinity.
Returns basic information and non-list-specific field data on each Person.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/persons/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Persons will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

Requires the "Export All People directory" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

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
| `data` | `array<object> (≤ 100 items)` ([Person](#person)) | Yes | A page of Person results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example

```json
{
  "data": [
    {
      "emailAddresses": [
        "jane.smith@northpointvc.com"
      ],
      "fields": [],
      "firstName": "Jane",
      "id": 1,
      "lastName": "Smith",
      "primaryEmailAddress": "jane.smith@northpointvc.com",
      "type": "internal"
    },
    {
      "emailAddresses": [
        "m.torres@northpointvc.com"
      ],
      "fields": [],
      "firstName": "Michael",
      "id": 2,
      "lastName": "Torres",
      "primaryEmailAddress": "m.torres@northpointvc.com",
      "type": "external"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/persons?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Create a Person
`POST /v2/persons`

- **Tag:** Persons · **OperationId:** v2_persons__POST · **Stability:** `beta` · **Auth:** bearerAuth

This endpoint is currently in BETA.

Creates a new Person. Setting `fields` values requires the "Edit Global Field Values"
permission and returns a 403 error if the caller lacks it.

#### Request Body

**Media type:** `application/json`
Request body for creating a Person.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `firstName` | `string` | Yes | The person's first name. |
| `lastName` | `string/null` | Yes | The person's last name. |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address. |
| `emailAddresses` | `array<string<email>> (≤ 100 items)` | No | All of the person's email addresses. If not provided, defaults to [{primaryEmailAddress}] |
| `fields` | `array<object> (≤ 100 items)` ([fields.FieldUpdate](#fieldsfieldupdate)) | No | Field-value updates to apply to the newly created Person. |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/persons' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 201 — application/json

Created

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
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type. `internal` - people who are users within your Affinity instance. `external` - people who are not internal. |
| `fields` | `array<object>` ([Field](#field)) | No | The fields associated with the person |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on Person Fields
`GET /v2/persons/fields`

- **Tag:** Persons · **OperationId:** v2_persons_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns metadata on non-list-specific Person Fields.

Use the returned Field IDs to request field data from the GET `/v2/persons` and GET `/v2/persons/{id}` endpoints.

You can filter Fields using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `name` | `text` | `=`, `=~` | `name="Location"`, `name=~loc` |

Use the `includes` query parameter to add optional metadata to each Field in the response. Pass `includes` more than once to request multiple values.

| **Value** | **Adds to each Field** |
|---|---|
| `filterability` | How the field can be used in filter expressions on GET `/v2/persons` and POST `/v2/persons/search` |
| `sortability` | How the field can be used in sort expressions on those endpoints |

Example: `GET /v2/persons/fields?includes=filterability&includes=sortability`

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |
| `includes` | `array<string (enum: `filterability`, `sortability`)>` | No | Additional properties to include in the response |

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
| `data` | `array<object> (≤ 100 items)` ([FieldMetadata](#fieldmetadata)) | Yes | A page of FieldMetadata results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: default

```json
{
  "data": [
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-current-job-title",
      "isRequired": false,
      "name": "Current Job Title",
      "type": "enriched",
      "valueType": "filterable-text"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-industry",
      "isRequired": false,
      "name": "Industry",
      "type": "enriched",
      "valueType": "filterable-text-multi"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-location",
      "isRequired": false,
      "name": "Location",
      "type": "enriched",
      "valueType": "location"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": null,
      "id": "field-1",
      "isRequired": false,
      "name": "Custom global field",
      "type": "global",
      "valueType": "text"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "last-email",
      "isRequired": false,
      "name": "Last Email",
      "type": "relationship-intelligence",
      "valueType": "interaction"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "lists",
      "isRequired": false,
      "name": "Lists",
      "type": "global",
      "valueType": "list-multi"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "notes",
      "isRequired": false,
      "name": "Notes",
      "type": "global",
      "valueType": "note"
    },
    {
      "createdAt": null,
      "description": null,
      "enrichmentSource": null,
      "id": "reminders",
      "isRequired": false,
      "name": "Reminders",
      "type": "global",
      "valueType": "reminder"
    },
    {
      "createdAt": "2024-03-07T20:21:42Z",
      "description": null,
      "enrichmentSource": null,
      "id": "source-of-introduction",
      "isRequired": false,
      "name": "Source of Introduction",
      "type": "relationship-intelligence",
      "valueType": "person"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/fields?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

### Get dropdown options for a Person Field
`GET /v2/persons/fields/{fieldId}/dropdown-options`

- **Tag:** Persons · **OperationId:** v2_persons_fields_fieldId_dropdown-options__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns the dropdown options for a specific dropdown or ranked-dropdown field on a Person.

Use the returned dropdown option IDs when writing dropdown field values via the field update
endpoints.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldId` | `string` | Yes | Field ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/fields/{fieldId}/dropdown-options' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: DropdownOptionPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([DropdownOption](#dropdownoption)) | Yes | A page of DropdownOption results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: dropdown-options

```json
{
  "data": [
    {
      "id": 1,
      "text": "Director",
      "type": "dropdown"
    },
    {
      "id": 2,
      "text": "VP",
      "type": "dropdown"
    },
    {
      "id": 3,
      "text": "C-Level",
      "type": "dropdown"
    }
  ],
  "pagination": {
    "nextUrl": null,
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Search Persons
`POST /v2/persons/search`

- **Tag:** Persons · **OperationId:** v2_persons_search__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Search for Persons matching the given criteria.

Accepts an optional combination of filters, sorts, and a search term. Omitting the body is equivalent to `GET /v2/persons` with default pagination.

Requires the "Export All People directory" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

### Field IDs

Field IDs used in `filters`, `sorts`, and `search.fieldIds` follow the formats described in [Working with Field Data](https://developer.affinity.co/pages/data-model/working-with-field-data). Use `GET /v2/persons/fields` to discover the available fields and their `valueType`.

### `attributeId`

Some fields require an `attributeId` to specify which aspect to filter or sort on. The following relationship intelligence fields all use `attributeId: "date-of-activity"`: `last-email`, `first-email`, `last-contact`, `last-event`, `first-event`, `next-event`.

Use `GET /v2/persons/fields` to confirm which fields require an `attributeId`.

### Search

The `search.term` is always matched against the person's first name, last name, and primary email address. Providing `search.fieldIds` extends the search to those additional fields; it does not restrict matching to only those fields. Fields with a `valueType` of `datetime` are not searchable and are silently ignored if included in `search.fieldIds`.

### Limits

- **Items per filter group** (filters or nested groups): 50

- **Values per filter** (e.g. options in `is-any-of`): 100

- **Sort criteria**: 5

- **Search term minimum length**: 3 characters

- **Results per page**: 100

### Pagination

Uses cursor-based pagination.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldIds` | `array<string>` | No | Specific field IDs for which to return field data on each Person. Cannot be used together with `fieldTypes`; use one or the other. Use `GET /v2/persons/fields` to discover available field IDs. |
| `fieldTypes` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | A category of fields for which to return field data on each Person. Cannot be used together with `fieldIds`; use one or the other. |
| `cursor` | `string` | No | Cursor for the next or previous page. |
| `limit` | `integer<int32>` | No | Maximum number of Persons to return per page. |
| `totalCount` | `boolean` | No | When `true`, includes the total count of matching Persons in the pagination response. Adds additional query cost; use only when needed. |

#### Request Body

**Media type:** `application/json`
Search criteria for filtering, sorting, and searching. All fields are optional  omitting the body returns all results with default pagination.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | `object` ([FilterGroup](#filtergroup)) | No | A tree of filter conditions to apply. Supports nested AND/OR grouping. Use the relevant fields endpoint for your resource type to discover available fields, their `valueType`, and supported operators. |
| `sorts` | `array<object> (≤ 5 items, ≥ 1 items)` ([SearchSort](#searchsort)) | No | One or more sort criteria, applied in order. Supports up to 5 sort items. Use the relevant fields endpoint for your resource type to discover sortable fields. |
| `search` | `object` ([SearchTerm](#searchterm)) | No | An optional keyword to match against field values. Results must satisfy both the search term AND any provided filters (intersection). Only one search object may be provided. The term is always matched against the entity name and primary identifier; providing `fieldIds` extends the search to additional fields rather than replacing the identity match. |

Example: filter-by-dropdown
```json
{
  "filters": {
    "filters": [
      {
        "fieldId": "field-4574182",
        "operator": "is-any-of",
        "value": [
          {
            "dropdownOptionId": 1
          },
          {
            "dropdownOptionId": 2
          }
        ],
        "valueType": "dropdown"
      }
    ],
    "operator": "and"
  }
}
```

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/persons/search' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"filters":{"operator":"and","filters":[{"fieldId":"field-4574182","valueType":"dropdown","operator":"is-any-of","value":[{"dropdownOptionId":1},{"dropdownOptionId":2}]}]}}'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: PersonPaged
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Person](#person)) | Yes | A page of Person results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example

```json
{
  "data": [
    {
      "emailAddresses": [
        "jane.smith@northpointvc.com"
      ],
      "fields": [],
      "firstName": "Jane",
      "id": 1,
      "lastName": "Smith",
      "primaryEmailAddress": "jane.smith@northpointvc.com",
      "type": "internal"
    },
    {
      "emailAddresses": [
        "m.torres@northpointvc.com"
      ],
      "fields": [],
      "firstName": "Michael",
      "id": 2,
      "lastName": "Torres",
      "primaryEmailAddress": "m.torres@northpointvc.com",
      "type": "external"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/persons?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Delete a Person
`DELETE /v2/persons/{personId}`

- **Tag:** Persons · **OperationId:** v2_persons_personId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

This endpoint is currently in BETA.

Deletes a Person. Returns a 403 error if the Person is internal or inferred internal, since
those Persons cannot be deleted.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/persons/{personId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Person
`GET /v2/persons/{personId}`

- **Tag:** Persons · **OperationId:** v2_persons_personId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns basic information and non-list-specific field data on the requested Person.

To retrieve field data, you must use either the `fieldIds` or the `fieldTypes` parameter
to specify the Fields for which you want data returned.
These Field IDs and Types can be found using the GET `/v2/persons/fields` endpoint.
When no `fieldIds` or `fieldTypes` are provided, Persons will be returned without any field data attached.
To supply multiple `fieldIds` or `fieldTypes` parameters, generate a query string that looks like this:
`?fieldIds=field-1234&fieldIds=affinity-data-location` or `?fieldTypes=enriched&fieldTypes=global`.

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
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type. `internal` - people who are users within your Affinity instance. `external` - people who are not internal. |
| `fields` | `array<object>` ([Field](#field)) | No | The fields associated with the person |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get field values on a single Person
`GET /v2/persons/{personId}/fields`

- **Tag:** Persons · **OperationId:** v2_persons_personId_fields__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through field values on a single person.

Enriched, global, and relationship-intelligence fields will be included by default. The `ids` and `types` parameters can be used to filter
the collection. These parameters are mutually exclusive.

List fields are not returned by this endpoint. To retrieve or update list field values, use the
[list entry fields](#get-field-values-on-a-single-list-entry) endpoints.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `ids` | `array<string>` | No | Field IDs for which to return field data |
| `types` | `array<string (enum: `enriched`, `global`, `relationship-intelligence`)>` | No | Field Types for which to return field data |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/fields' \
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
| `data` | `array<object> (≤ 100 items)` ([Field](#field)) | Yes | A page of Field results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: person-enriched

```json
{
  "data": [
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
          "streetAddress": null
        },
        "type": "location"
      }
    },
    {
      "enrichmentSource": "affinity-data",
      "id": "affinity-data-linkedin-url",
      "name": "LinkedIn URL",
      "type": "enriched",
      "value": {
        "data": "https://linkedin.com/in/alex-rivera",
        "type": "text"
      }
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/1/fields?types=enriched&cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/persons/1/fields?types=enriched&cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Perform batch operations on a person's fields
`PATCH /v2/persons/{personId}/fields`

- **Tag:** Persons · **OperationId:** v2_persons_personId_fields__PATCH · **Stability:** `beta` · **Auth:** bearerAuth

Perform batch operations on a person's fields.

Currently the only operation at the endpoint is `update-fields`, which allows you to update
multiple field values with a single request. This is equivalent to calling [the single field
update](#update-a-single-field-value-on-a-person) endpoint multiple times. You can
update up to 100 fields per request.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |

#### Request Body

**Media type:** `application/json`
**Variant:** [PersonBatchOperationUpdateFields](#personbatchoperationupdatefields)
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` ([fields.FieldUpdate](#fieldsfieldupdate)) | Yes |  |

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
curl --request PATCH 'https://api.affinity.co/v2/persons/{personId}/fields' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"operation":"update-fields","updates":[{"id":"field-1","value":{"type":"company","data":{"id":1}}},{"id":"field-2","value":{"type":"company-multi","data":[{"id":1},{"id":2}]}},{"id":"field-3","value":{"type":"datetime","data":"2023-01-01T00:00:00Z"}},{"id":"field-4","value":{"type":"dropdown","data":{"dropdownOptionId":1}}},{"id":"field-5","value":{"type":"dropdown-multi","data":[{"dropdownOptionId":1},{"dropdownOptionId":2}]}},{"id":"field-6","value":{"type":"location","data":{"streetAddress":"1 Main Street","city":"San Francisco","state":"California","country":"United States","continent":"North America"}}},{"id":"field-7","value":{"type":"location-multi","data":[{"streetAddress":"1 Main Street","city":"San Francisco","state":"California","country":"United States","continent":"North America"},{"streetAddress":"1600 Pennsylvania Avenue NW","city":"Washington","state":"DC","country":"United States","continent":"North America"}]}},{"id":"field-8","value":{"type":"number","data":100}},{"id":"field-9","value":{"type":"number-multi","data":[100,200,300]}},{"id":"field-10","value":{"type":"person","data":{"id":1}}},{"id":"field-11","value":{"type":"person-multi","data":[{"id":1},{"id":2}]}},{"id":"field-12","value":{"type":"ranked-dropdown","data":{"dropdownOptionId":1}}},{"id":"field-13","value":{"type":"text","data":"Some new text"}}]}'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: PersonBatchOperationResponse
*Type:* object
The response body for a single operation within a person batch request.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` ([PersonBatchOperations](#personbatchoperations)) | No | The type of batch operation that was performed on the person. |

Example: update-fields

```json
{
  "operation": "update-fields"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single field on a Person
`GET /v2/persons/{personId}/fields/{fieldId}`

- **Tag:** Persons · **OperationId:** v2_persons_personId_fields_fieldId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Retrieve a single field on a person. Returns basic information and the field value.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |
| `fieldId` | `string` | Yes | Field ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/fields/{fieldId}' \
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
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`, `hidden`)` | Yes | The field's category. `hidden` is a redaction state rather than a category: it signals a field on a restricted opportunity the caller cannot manage, whose value is masked. |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `eventbrite`, `mailchimp`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | [CompaniesValue](#companiesvalue) \| [CompanyValue](#companyvalue) \| [DateValue](#datevalue) \| [DropdownsValue](#dropdownsvalue) \| [DropdownValue](#dropdownvalue) \| [FloatsValue](#floatsvalue) \| [FloatValue](#floatvalue) \| [FormulaValue](#formulavalue) \| [InteractionValue](#interactionvalue) \| [ListsValue](#listsvalue) \| [LocationsValue](#locationsvalue) \| [LocationValue](#locationvalue) \| [NoteValue](#notevalue) \| [PersonsValue](#personsvalue) \| [PersonValue](#personvalue) \| [RankedDropdownValue](#rankeddropdownvalue) \| [ReminderValue](#remindervalue) \| [TextsValue](#textsvalue) \| [TextValue](#textvalue) | Yes |  |

Example: company

```json
{
  "enrichmentSource": null,
  "id": "field-1",
  "name": "Field with company value",
  "type": "global",
  "value": {
    "data": {
      "domain": "horizontech.com",
      "id": 1,
      "name": "Horizon Technologies"
    },
    "type": "company"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a single field value on a Person
`POST /v2/persons/{personId}/fields/{fieldId}`

- **Tag:** Persons · **OperationId:** v2_persons_personId_fields_fieldId__POST · **Stability:** `beta` · **Auth:** bearerAuth

Update a single field value on a person.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |
| `fieldId` | `string` | Yes | Field ID |

#### Request Body

**Media type:** `application/json`
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | No |  |

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
curl --request POST 'https://api.affinity.co/v2/persons/{personId}/fields/{fieldId}' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{"value":{"type":"company","data":{"id":1}}}'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get values for a single field on a Person
`GET /v2/persons/{personId}/fields/{fieldId}/values`

- **Tag:** Persons · **OperationId:** v2_persons_personId_fields_fieldId_values__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through all values for a field on a person.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |
| `fieldId` | `string` | Yes | Field ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/fields/{fieldId}/values' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: FieldValuesPaged
*Type:* oneOf
**Variant:** [CompaniesValuePaged](#companiesvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `company`, `company-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [DropdownsValuePaged](#dropdownsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `dropdown`, `dropdown-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Dropdown](#dropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [ListsValuePaged](#listsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([ListData](#listdata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [LocationsValuePaged](#locationsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `location`, `location-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Location](#location)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [PersonsValuePaged](#personsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `person`, `person-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [RankedDropdownValuePaged](#rankeddropdownvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([RankedDropdown](#rankeddropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
**Variant:** [TextsValuePaged](#textsvaluepaged)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `filterable-text-multi`)` | Yes | The type of value |
| `data` | `array<string> (≤ 100 items)` | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

Example: company

```json
{
  "data": [
    {
      "domain": "horizontech.com",
      "id": 1,
      "name": "Horizon Technologies"
    }
  ],
  "pagination": {
    "nextUrl": null,
    "prevUrl": null
  },
  "type": "company"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a Person's List Entries
`GET /v2/persons/{personId}/list-entries`

- **Tag:** Persons · **OperationId:** v2_persons_personId_list-entries__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through the List Entries (AKA rows) for the given Person across all Lists.
Each List Entry includes field data for the Person, including list-specific field data.
Each List Entry also includes metadata about its creation, i.e., when it was added to the List and by whom.

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
| `data` | `array<object> (≤ 100 items)` ([ListEntry](#listentry)) | Yes | A page of ListEntry results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a Person's Lists
`GET /v2/persons/{personId}/lists`

- **Tag:** Persons · **OperationId:** v2_persons_personId_lists__GET · **Stability:** `beta` · **Auth:** bearerAuth

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
| `data` | `array<object> (≤ 100 items)` ([List](#list)) | Yes | A page of List results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Notes for a Person
`GET /v2/persons/{personId}/notes`

- **Tag:** Persons · **OperationId:** v2_persons_personId_notes__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns notes for a given person id which includes directly attached notes, notes on meetings this person attended, and notes where this person is mentioned.

You can filter notes using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `creator.id` | `int32` | `=` | `creator.id=1` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-02-04T10:48:24Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2025-02-03T10:48:24Z` |

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
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Note](#notesnote)) | Yes | A page of Note objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: entities

```json
{
  "data": [
    {
      "content": {
        "html": "<p>Met with the founding team to discuss the Series A term sheet.</p>"
      },
      "createdAt": "2023-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 1,
      "mentions": [
        {
          "id": 1,
          "person": {
            "firstName": "Jane",
            "id": 1,
            "lastName": "Smith",
            "primaryEmailAddress": "jane.smith@northpointvc.com",
            "type": "internal"
          },
          "type": "person"
        }
      ],
      "type": "entities",
      "updatedAt": "2023-01-01T00:00:00Z"
    },
    {
      "content": {
        "html": "<p>This is another note!</p>"
      },
      "createdAt": "2024-01-01T00:00:00Z",
      "creator": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com",
        "type": "internal"
      },
      "id": 2,
      "mentions": [],
      "type": "entities",
      "updatedAt": "2024-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/1/notes?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/persons/1/notes?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get Relationships for a Person
`GET /v2/persons/{personId}/relationships`

- **Tag:** Persons · **OperationId:** v2_persons_personId_relationships__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns the relationships for a given person, including the interaction score that measures the
strength of each relationship based on communication patterns such as emails, meetings, and
other interactions.

Each relationship includes two persons (person1 and person2) who have a connection.

## Interaction score

The `interactionScore` is a value between `0.0` and `1.0` that reflects how frequently the
two persons interact across email, calendar events, and chat messages. The more interactions,
the higher the score. Recent interactions are weighted slightly higher than older ones. As
rough guidance, scores at or above `0.7` typically indicate two persons that communicate
regularly, scores between `0.4` and `0.7` indicate occasional communication, and scores below
`0.4` indicate only sporadic communication.

## LinkedIn connections

The collection also includes relationships based on a LinkedIn connection between the given
person and their internal team member counterpart.

Whenever a LinkedIn connection exists between the two persons in a relationship, `linkedIn` is
populated with the date the connection was made.`linkedIn` is `null` when no
LinkedIn connection exists between the two persons. Note that LinkedIn-based relationships
which do not have any interaction data will have an `interactionScore` of `0`.

## Filters

You can filter relationships using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Description** | **Allowed Operators** | **Examples** |
|---|---|---|---|---|
| `interactionScore` | `double` | Strength of the relationship, between `0.0` and `1.0`. Higher means stronger. | `>`, `<`, `>=`, `<=` | `interactionScore>=0.5` |

## Sorting

You can sort relationships using the `orderBy` query parameter. `interactionScore` is the only
sortable property.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `personId` | `integer<int64>` | Yes | Person ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `filter` | `string` | No | Filter options |
| `orderBy` | `array<string (enum: `interactionScore`, `-interactionScore`)>` | No | Properties to sort by. Defaults to `-interactionScore`. Prefix with `-` for descending order. |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/persons/{personId}/relationships' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: RelationshipsPaged
*Type:* object
A paginated list of relationships
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Relationship](#relationship)) | Yes | A page of Relationship objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: relationships

```json
{
  "data": [
    {
      "interactionScore": 0.85,
      "linkedIn": null,
      "person1": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com"
      },
      "person2": {
        "firstName": "John",
        "id": 100,
        "lastName": "Doe",
        "primaryEmailAddress": "john.doe@acme.co"
      }
    },
    {
      "interactionScore": 0.72,
      "linkedIn": {
        "connectedOn": "2022-06-15"
      },
      "person1": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com"
      },
      "person2": {
        "firstName": "Alex",
        "id": 101,
        "lastName": "Kim",
        "primaryEmailAddress": "alex.kim@acme.co"
      }
    },
    {
      "interactionScore": 0.45,
      "linkedIn": null,
      "person1": {
        "firstName": "Jane",
        "id": 1,
        "lastName": "Smith",
        "primaryEmailAddress": "jane.smith@northpointvc.com"
      },
      "person2": {
        "firstName": "Robin",
        "id": 102,
        "lastName": "Hill",
        "primaryEmailAddress": null
      }
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/persons/1/relationships?cursor=ICAgICAgIGFmdGVyOjo6Mw",
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Rate Limit

Operations about rate limits

### Get rate limit usage
`GET /v2/rate-limit`

- **Tag:** Rate Limit · **OperationId:** v2_rate-limit__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns the current rate limit usage for the authenticated caller.

`orgPerMonth` is included only for callers that have a monthly quota; it is absent for callers that don't have one.

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/rate-limit' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: RateLimit
*Type:* object
Rate limit usage for the authenticated caller. Contains one or two windows depending on the caller's quota configuration: `callerPerMinute` is always present (per-caller minute limit); `orgPerMonth` is present only for callers whose org has a bounded monthly quota (DEVELOPER keys and OAuth apps on capped plans). Absence of `orgPerMonth` indicates no monthly quota applies.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `callerPerMinute` | `object` ([RateLimitWindow](#ratelimitwindow)) | Yes | Rate limit window for per-caller requests within a one-minute period. |
| `orgPerMonth` | `object` ([RateLimitWindow](#ratelimitwindow)) | No | Rate limit window for monthly aggregate requests. Only present for callers with a monthly quota; omitted for API key types without monthly limits. |

Example: with-monthly-quota

```json
{
  "callerPerMinute": {
    "limit": 300,
    "remaining": 299,
    "reset": 42,
    "used": 1
  },
  "orgPerMonth": {
    "limit": 100000,
    "remaining": 99999,
    "reset": 1200000,
    "used": 1
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

## Reminders

Operations about reminders

### Get all Reminders
`GET /v2/reminders`

- **Tag:** Reminders · **OperationId:** v2_reminders__GET · **Stability:** `beta` · **Auth:** bearerAuth

Returns a page of Reminders visible to the caller.

You can filter reminders using the `filter` query parameter. The filter parameter is a string
that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int64` | `=` | `id=1\|id=2\|id=3` |
| `type` | `enum` | `=` | `type=one-time`, `type=recurring` |
| `status` | `enum` | `=` | `status=active`, `status=overdue`, `status=completed` |
| `resetTrigger` | `enum` | `=` | `resetTrigger=interaction`, `resetTrigger=email`, `resetTrigger=event` |
| `dueDate` | `datetime` | `>`, `<`, `>=`, `<=` | `dueDate>=2026-01-01T00:00:00Z` |
| `completedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `completedAt=2026-01-01T00:00:00Z` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt>=2026-01-01T00:00:00Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2026-01-01T00:00:00Z` |
| `owner.id` | `int64` | `=`, `!=` | `owner.id=1\|owner.id=2`, `owner.id!=3` |
| `creator.id` | `int64` | `=` | `creator.id=1` |
| `completer.id` | `int64` | `=` | `completer.id=1` |
| `company.id` | `int64` | `=` | `company.id=42` |
| `person.id` | `int64` | `=` | `person.id=42` |
| `opportunity.id` | `int64` | `=` | `opportunity.id=42` |

Results are ordered by `dueDate` ascending (soonest-due first).

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/reminders' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: reminders.ReminderPaged
*Type:* object
A page of Reminder objects.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([reminders.Reminder](#remindersreminder)) | Yes | A page of Reminder objects. |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Create a Reminder
`POST /v2/reminders`

- **Tag:** Reminders · **OperationId:** v2_reminders__POST · **Stability:** `beta` · **Auth:** bearerAuth

Creates a new Reminder. Exactly one of `company`, `person`, or `opportunity` must be provided.

The `creator` of the new reminder is the user associated with the API key.

#### Request Body

**Media type:** `application/json`
Request body for creating a reminder. Discriminated by `type`  see `reminders.OneTimeReminderToBeCreated` and `reminders.RecurringReminderToBeCreated`. Exactly one of `company`, `person`, or `opportunity` must be provided.
**Variant:** [reminders.OneTimeReminderToBeCreated](#remindersonetimeremindertobecreated)
Request body for creating a one-time reminder. `dueDate` is required.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `one-time` for this variant. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is due. Must be on or after 2000-01-01 and before 9999-01-01. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for the reminder. Must reference an internal user. |
| `content` | `string/null` | No | Free-form text attached to the reminder. |
| `entity` | [reminders.TaggedCompany](#reminderstaggedcompany) \| [reminders.TaggedPerson](#reminderstaggedperson) \| [reminders.TaggedOpportunity](#reminderstaggedopportunity) | Yes | The entity the reminder is attached to. Exactly one of `company`, `person`, or `opportunity` can be tagged on a reminder  the variant is selected by the `type` discriminator. |
**Variant:** [reminders.RecurringReminderToBeCreated](#remindersrecurringremindertobecreated)
Request body for creating a recurring reminder. `recurrence` is required. `dueDate` is optional and computed from `recurrence.periodDays` when omitted.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `recurring` for this variant. |
| `dueDate` | `string<date-time>` | No | When the reminder is due. Optional for recurring reminders; computed from `recurrence.periodDays` when omitted. Must be on or after 2000-01-01 and before 9999-01-01. |
| `recurrence` | `object` | Yes | Recurrence configuration. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for the reminder. Must reference an internal user. |
| `content` | `string/null` | No | Free-form text attached to the reminder. |
| `entity` | [reminders.TaggedCompany](#reminderstaggedcompany) \| [reminders.TaggedPerson](#reminderstaggedperson) \| [reminders.TaggedOpportunity](#reminderstaggedopportunity) | Yes | The entity the reminder is attached to. Exactly one of `company`, `person`, or `opportunity` can be tagged on a reminder  the variant is selected by the `type` discriminator. |

**`recurrence` details** — Recurrence configuration.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | Yes | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | Yes | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 3650) |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/reminders' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: reminders.Reminder
*Type:* oneOf
A reminder to follow up with a person, company, or opportunity. Discriminated by `type`  `one-time` reminders fire once on `dueDate`, and `recurring` reminders reset on a cadence.
**Variant:** [reminders.OneTimeReminder](#remindersonetimereminder)
A reminder that fires once on `dueDate`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `one-time` for this variant. |
| `status` | `string (enum: `active`, `overdue`, `completed`)` | Yes | Derived state. `active` if not completed and due in the future. `overdue` if not completed and due in the past. `completed` if `completedAt` is set. |
| `completedAt` | `string/null<date-time>` | Yes | When the reminder was completed. `null` if the reminder is not yet completed. |
| `recurrence` | `null` | Yes | Always `null` for one-time reminders. |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |
**Variant:** [reminders.RecurringReminder](#remindersrecurringreminder)
A reminder that resets on a recurring cadence. Completion advances `dueDate` by `recurrence.periodDays` instead of setting `completedAt`, so `completedAt` is always `null` for this variant.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `recurring` for this variant. |
| `status` | `string (enum: `active`, `overdue`)` | Yes | Derived state. `active` if due in the future, `overdue` if due in the past. Recurring reminders never reach `completed` because completion rolls `dueDate` forward. |
| `completedAt` | `null` | Yes | Always `null` for recurring reminders. |
| `recurrence` | `object` | Yes | Recurrence configuration. Always non-null for recurring reminders. |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |

**`recurrence` details** — Recurrence configuration. Always non-null for recurring reminders.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | Yes | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | Yes | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 2147483647) |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Delete a Reminder
`DELETE /v2/reminders/{reminderId}`

- **Tag:** Reminders · **OperationId:** v2_reminders_reminderId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Deletes a Reminder. Only the reminder's creator or owner may delete it.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reminderId` | `integer<int64>` | Yes | Reminder ID |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/reminders/{reminderId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Reminder
`GET /v2/reminders/{reminderId}`

- **Tag:** Reminders · **OperationId:** v2_reminders_reminderId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns a single Reminder. Responds with `404` when the reminder does not exist or is not visible to the caller.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reminderId` | `integer<int64>` | Yes | Reminder ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/reminders/{reminderId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: reminders.Reminder
*Type:* oneOf
A reminder to follow up with a person, company, or opportunity. Discriminated by `type`  `one-time` reminders fire once on `dueDate`, and `recurring` reminders reset on a cadence.
**Variant:** [reminders.OneTimeReminder](#remindersonetimereminder)
A reminder that fires once on `dueDate`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `one-time` for this variant. |
| `status` | `string (enum: `active`, `overdue`, `completed`)` | Yes | Derived state. `active` if not completed and due in the future. `overdue` if not completed and due in the past. `completed` if `completedAt` is set. |
| `completedAt` | `string/null<date-time>` | Yes | When the reminder was completed. `null` if the reminder is not yet completed. |
| `recurrence` | `null` | Yes | Always `null` for one-time reminders. |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |
**Variant:** [reminders.RecurringReminder](#remindersrecurringreminder)
A reminder that resets on a recurring cadence. Completion advances `dueDate` by `recurrence.periodDays` instead of setting `completedAt`, so `completedAt` is always `null` for this variant.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `recurring` for this variant. |
| `status` | `string (enum: `active`, `overdue`)` | Yes | Derived state. `active` if due in the future, `overdue` if due in the past. Recurring reminders never reach `completed` because completion rolls `dueDate` forward. |
| `completedAt` | `null` | Yes | Always `null` for recurring reminders. |
| `recurrence` | `object` | Yes | Recurrence configuration. Always non-null for recurring reminders. |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |

**`recurrence` details** — Recurrence configuration. Always non-null for recurring reminders.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | Yes | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | Yes | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 2147483647) |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a Reminder
`POST /v2/reminders/{reminderId}`

- **Tag:** Reminders · **OperationId:** v2_reminders_reminderId__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Updates a Reminder. Only provided fields are changed; omitted fields keep their current value.

Setting `completedAt` marks the reminder complete (for `recurring` reminders, this advances
`dueDate` by `recurrence.periodDays` and `completedAt` remains `null` on the resource).
Setting `completedAt` to `null` marks the reminder incomplete and is rejected for `recurring`
reminders.

Only the reminder's creator or owner may update it (including completing or uncompleting it).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `reminderId` | `integer<int64>` | Yes | Reminder ID |

#### Request Body

**Media type:** `application/json`
Partial-update request body for a reminder. Only provided properties are updated. `recurrence` may only be sent when the reminder's existing `type` is `recurring`. Setting `completedAt` to a non-null value marks the reminder complete (for recurring reminders, this advances `dueDate` by `recurrence.periodDays` and `completedAt` remains `null` on the resource). Setting `completedAt` to `null` marks the reminder incomplete and is rejected for recurring reminders.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | `string/null` | No | Free-form note attached to the reminder. Send `null` to clear. |
| `dueDate` | `string<date-time>` | No | New due date for the reminder. Must be on or after 2000-01-01 and before 9999-01-01. |
| `owner` | `object` | No | The new owner of the reminder. Must reference an internal user. |
| `completedAt` | `string/null<date-time>` | No | Set a value to mark the reminder complete. Send `null` to mark it incomplete (one-time reminders only). `completer` is populated from the API key's owning user. |
| `recurrence` | `object` | No | Update recurrence configuration. Only valid when the reminder's existing `type` is `recurring`. Send only the fields you want to change. |

**`owner` details** — The new owner of the reminder. Must reference an internal user.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | (Constraints: ≥ 1; ≤ 9007199254740991) |

**`recurrence` details** — Update recurrence configuration. Only valid when the reminder's existing `type` is `recurring`. Send only the fields you want to change.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | No | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | No | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 3650) |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/reminders/{reminderId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Semantic Search

Operations about semantic searches

### Semantic Search
`POST /v2/semantic-search`

- **Tag:** Semantic Search · **OperationId:** v2_semantic-search__POST · **Stability:** `beta` · **Auth:** bearerAuth

Perform an AI-powered semantic search. Use the `entityType` field in the request body to specify which entity type to search. Currently only supports companies.

The `prompt` field accepts natural language describing the companies to find. Supported query dimensions include:

- Industry or sector
  - Example: `climate tech companies in our pipeline`
- Descriptive technology or business concepts
  - Example: `biotech companies working on extracellular vesicles`
- Funding information: investment stage, funding date, amount raised, and year founded
  - Example: `Series A companies that raised more than $10M`
- Employee metrics: headcount, hiring rate, and departure rate
  - Example: `companies with more than 100 employees`
- Interaction history
  - Example: `companies our firm emailed recently`
- Relationship strength
  - Example: `companies where we have strong connections`
- Relative time references
  - Example: `AI companies founded in the past 3 years`
- Headquarters location: city, state, country, or region
  - Example: `fintech startups in San Francisco`
- Investor name
  - Example: `companies backed by Sequoia Capital`

These dimensions can be combined in a single prompt, for example `climate tech companies in San Francisco that raised a Series A in the past year`.

Results can be sorted by including the desired sort in the prompt itself, for example `Series B companies with the most funding`. Only one sortable attribute is supported per request.

Use the `listIds` field to scope results to companies on specific lists, and combine it with `prompt` to search semantically within those lists. Retrieve list IDs from `GET /v2/lists`.

The phrases `I`, `we`, and `our firm` always refer to firm-wide data: interaction history and relationship strength cannot be filtered to a specific team member. The phrases `in our pipeline` and `in our network` match companies your firm has interacted with or added to Affinity in general. They do not search for membership in a list literally named "Pipeline" or similar. To search a specific named list, use `listIds`.

The following are not supported:

- Third-party enrichment data such as Crunchbase, PitchBook, or Dealroom.
- Company valuation and revenue metrics.
- Lookup by similarity to a named company, for example `companies like OpenAI`.
- Notes, email body content, or file attachments.
- Custom fields.
- Computed or formula-based sorts, such as a ratio between two fields.

#### Request Body

**Media type:** `application/json`
Semantic search criteria including search prompt and entity type
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search prompt to apply. (Constraints: length ≥ 1; length ≤ 500) |
| `limit` | `integer<int32>` | No | Number of items to include in the response. (Constraints: ≥ 1; ≤ 100; default `100`) |
| `entityType` | `string` | No | The type of entity to search for. |
| `listIds` | `array<integer<int64>> (≤ 100 items)` | No | The IDs of the lists to filter results by. |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/semantic-search' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: SemanticSearchResult
*Type:* object
Includes the list of entities that matched the search prompt and the explanation for the search.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([companies.SemanticSearchCompany](#companiessemanticsearchcompany)) | Yes | The list of entities that matched the search prompt |
| `entityType` | `string` | Yes | The type of entity that was searched. |
| `explanation` | `string` | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Teams

Operations about teams

### Get metadata on all Teams
`GET /v2/teams`

- **Tag:** Teams · **OperationId:** v2_teams__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through all Teams in your organization that you have access to view.

Use the `includes` query parameter to add `membersPreview` and `accessibleListsPreview` to each team. Each preview carries a `totalCount` and a short `data` sample; the full collections are available at `GET /v2/teams/{teamId}/members` and `GET /v2/teams/{teamId}/accessible-lists`. The team's `privacyType` is gated and only returned when the caller has the "Manage Teams" [permission](https://developer.affinity.co/pages/external-api-v2/permissions), the organization has team-based privacy controls enabled, and cross-team visibility is enabled for the organization; it is omitted from every team in the response otherwise.

You can filter Teams using the `filter` query parameter:

| **Property Name**     | **Description**                       | **Type**  | **Allowed Operators**             | **Examples**                |
|-----------------------|---------------------------------------|-----------|-----------------------------------|-----------------------------|
| `id`                  | Filter Teams by id                    | `int64`   | `=`                               | `id=1\|id=2`                |
| `name`                | Filter Teams by name                  | `text`    | `=`, `=^`, `=$`, `=~`             | `name=^Invest`              |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `filter` | `string` | No | Affinity Filter Language expression. See description for filterable properties. |
| `orderBy` | `array<string (enum: `name`, `-name`, `createdAt`, `-createdAt`)>` | No | Sort order. Prefix with `-` for descending. Defaults to `name` ascending. |
| `includes` | `array<string (enum: `membersPreview`, `accessibleListsPreview`)>` | No | Additional properties to include in the response. |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/teams' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: TeamPaged
*Type:* object
A page of Teams
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Team](#team)) | Yes | A page of Team results |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: success

```json
{
  "data": [
    {
      "createdAt": "2024-03-01T15:22:00Z",
      "id": 42,
      "name": "Investments",
      "updatedAt": "2026-04-18T09:11:23Z"
    },
    {
      "createdAt": "2025-06-14T11:00:00Z",
      "id": 57,
      "name": "Platform",
      "updatedAt": null
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/teams?cursor=YWZ0ZXI6OjozNw",
    "prevUrl": null
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

### Get metadata on a single Team
`GET /v2/teams/{teamId}`

- **Tag:** Teams · **OperationId:** v2_teams_teamId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Retrieve detailed information about a specific Team. Optional opt-in properties can be requested
via the `includes` query parameter.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `teamId` | `integer<int64>` | Yes | Team ID |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `includes` | `array<string (enum: `membersPreview`, `accessibleListsPreview`)>` | No | Additional properties to include in the response. |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/teams/{teamId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: Team
*Type:* object
A Team. Opt-in properties are controlled by the `includes` query parameter.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `membersPreview` | `object` ([TeamMembersPreview](#teammemberspreview)) | No | Preview of the team's members. Only included when `membersPreview` is requested via the `includes` query parameter. `totalCount` is the total number of members on the team; full data is available via the paginated endpoint `GET /v2/teams/{teamId}/members`. |
| `accessibleListsPreview` | `object` ([TeamAccessibleListsPreview](#teamaccessiblelistspreview)) | No | Preview of the Lists this team has access to. Only included when `accessibleListsPreview` is requested via the `includes` query parameter. `totalCount` is the total number of Lists this team can access; full data is available via the paginated endpoint `GET /v2/teams/{teamId}/accessible-lists`. |
| `id` | `integer<int64>` | Yes | The unique identifier for the team (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the team |
| `privacyType` | `string (enum: `share-subjects-bodies`, `share-subjects`, `hide-subjects-bodies`, `no-access`)` | No | Visibility policy applied to interactions belonging to this team's members. `share-subjects-bodies` exposes all interactions; `share-subjects` exposes a selective subset; `hide-subjects-bodies` hides interaction content but exposes metadata; `no-access` exposes no interactions. Only returned when the caller has the "Manage Teams" [permission](https://developer.affinity.co/pages/external-api-v2/permissions), the organization has team-based privacy controls enabled, and cross-team visibility is enabled for the organization; omitted from the response otherwise. |
| `createdAt` | `string<date-time>` | Yes | Timestamp when the team was created |
| `updatedAt` | `string/null<date-time>` | Yes | Timestamp when the team was last updated, or null if never updated |

Example: slim

```json
{
  "createdAt": "2024-03-01T15:22:00Z",
  "id": 42,
  "name": "Investments",
  "updatedAt": "2026-04-18T09:11:23Z"
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Transcripts

Operations about transcripts

### Get all Transcripts
`GET /v2/transcripts`

- **Tag:** Transcripts · **OperationId:** v2_transcripts__GET · **Stability:** `beta` · **Auth:** bearerAuth

Paginate through all transcripts and return basic metadata only. Use the single transcript endpoint to fetch the entire transcript data.
Will only return transcripts that the current authenticated user has permission to see.

You can filter transcripts using the `filter` query parameter. The filter parameter is a string that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int32` | `=` | `id=1` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt<2025-02-04T10:48:24Z` |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/transcripts' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: transcripts.TranscriptPaged
*Type:* object
transcripts.TranscriptPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([transcripts.BaseTranscript](#transcriptsbasetranscript)) | Yes | A page of Transcript results |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: success

```json
{
  "data": [
    {
      "createdAt": "2023-01-01T00:00:23Z",
      "id": 1,
      "languageCode": "en",
      "note": {
        "content": {
          "html": "<p> Sarah reviews the company's ARR growth trajectory with Alex. The team discusses expansion revenue drivers and the path to Series B. </p>"
        },
        "createdAt": "2023-01-01T00:00:20Z",
        "creator": {
          "firstName": "Sarah",
          "id": 8,
          "lastName": "Park",
          "primaryEmailAddress": "sarah.park@horizontech.com",
          "type": "internal"
        },
        "id": 742,
        "mentions": [],
        "transcriptId": 1,
        "type": "ai-notetaker",
        "updatedAt": "2023-01-21T00:01:00Z"
      }
    },
    {
      "createdAt": "2023-02-01T00:00:35Z",
      "id": 2,
      "languageCode": "en",
      "note": {
        "content": {
          "html": "<p> Daniel and the founder discuss due diligence findings from the technical review. The team aligns on next steps before the term sheet is finalized. </p>"
        },
        "createdAt": "2023-02-01T00:00:00Z",
        "creator": {
          "firstName": "Daniel",
          "id": 10,
          "lastName": "Kim",
          "primaryEmailAddress": "d.kim@northpointvc.com",
          "type": "internal"
        },
        "id": 844,
        "mentions": [],
        "transcriptId": 2,
        "type": "ai-notetaker",
        "updatedAt": "2023-02-21T00:00:00Z"
      }
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/transcripts?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/transcripts?cursor=ICAgICAgYmVmb3JlOjo6Nw"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `default` | Errors | [Errors](#errors) |

### Delete a single Transcript
`DELETE /v2/transcripts/{transcriptId}`

- **Tag:** Transcripts · **OperationId:** v2_transcripts_transcriptId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Delete a transcript. The AI Notetaker summary note the transcript belongs to is kept. You can
only delete transcripts of notes you created.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `transcriptId` | `integer<int32>` | Yes | The id of the Transcript to delete |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/transcripts/{transcriptId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Transcript
`GET /v2/transcripts/{transcriptId}`

- **Tag:** Transcripts · **OperationId:** v2_transcripts_transcriptId__GET · **Stability:** `beta` · **Auth:** bearerAuth

Get a transcript with a given id with the first 100 fragments of the transcript. Use the /fragments endpoint to fetch all fragments of the transcript.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `transcriptId` | `integer<int32>` | Yes | The id of the Transcript |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/transcripts/{transcriptId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: transcripts.Transcript
*Type:* object
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fragmentsPreview` | `object` ([transcripts.FragmentsPreview](#transcriptsfragmentspreview)) | Yes | A preview for dialogue fragments on a transcript |
| `id` | `integer<int32>` | Yes | The transcript's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `note` | [notes.AiNotetakerRootNote](#notesainotetakerrootnote) \| [notes.AiNotetakerReplyNote](#notesainotetakerreplynote) | Yes | Note associated with the transcript |
| `createdAt` | `string<date-time>` | Yes | The date and time the transcript was created |
| `languageCode` | `string (enum: `de`, `en`, `es`, `fr`, `id`, …)` | Yes | The language code of the transcript |

Example: success

```json
{
  "createdAt": "2023-01-01T00:00:00Z",
  "fragmentsPreview": {
    "data": [
      {
        "content": "Can you walk us through your ARR growth over the past two quarters?",
        "endTimestamp": "00:00:05",
        "speaker": "Sarah Park",
        "startTimestamp": "00:00:01"
      },
      {
        "content": "We went from 1.2 million to 2.5 million ARR — roughly 110% growth.",
        "endTimestamp": "00:00:11",
        "speaker": "Alex Rivera",
        "startTimestamp": "00:00:06"
      },
      {
        "content": "That's impressive. What's primarily driving the expansion?",
        "endTimestamp": "00:00:15",
        "speaker": "Sarah Park",
        "startTimestamp": "00:00:12"
      },
      {
        "content": "Mostly upsells from existing accounts. Our net revenue retention is at 135%.",
        "endTimestamp": "00:00:21",
        "speaker": "Alex Rivera",
        "startTimestamp": "00:00:16"
      }
    ],
    "totalCount": 4
  },
  "id": 1,
  "languageCode": "en",
  "note": {
    "content": {
      "html": "<p> Sarah reviews the company's ARR growth trajectory with Alex. The team discusses expansion revenue drivers and the path to Series B. </p>"
    },
    "createdAt": "2023-01-01T00:00:20Z",
    "creator": {
      "firstName": "Sarah",
      "id": 8,
      "lastName": "Park",
      "primaryEmailAddress": "sarah.park@horizontech.com",
      "type": "internal"
    },
    "id": 742,
    "mentions": [],
    "transcriptId": 1,
    "type": "ai-notetaker",
    "updatedAt": "2023-01-21T00:01:00Z"
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get fragments of a transcript
`GET /v2/transcripts/{transcriptId}/fragments`

- **Tag:** Transcripts · **OperationId:** v2_transcripts_transcriptId_fragments__GET · **Stability:** `beta` · **Auth:** bearerAuth

Get fragments of a transcript given a transcript id.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `transcriptId` | `integer<int32>` | Yes | The id of the Transcript |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/transcripts/{transcriptId}/fragments' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: transcripts.FragmentPaged
*Type:* object
transcripts.FragmentPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([transcripts.Fragment](#transcriptsfragment)) | Yes | A page of Fragments for a transcript |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

Example: success

```json
{
  "data": [
    {
      "content": "Can you walk us through your ARR growth over the past two quarters?",
      "endTimestamp": "00:00:05",
      "speaker": "Sarah Park",
      "startTimestamp": "00:00:01"
    },
    {
      "content": "We went from 1.2 million to 2.5 million ARR — roughly 110% growth.",
      "endTimestamp": "00:00:11",
      "speaker": "Alex Rivera",
      "startTimestamp": "00:00:06"
    },
    {
      "content": "That's impressive. What's primarily driving the expansion?",
      "endTimestamp": "00:00:15",
      "speaker": "Sarah Park",
      "startTimestamp": "00:00:12"
    },
    {
      "content": "Mostly upsells from existing accounts. Our net revenue retention is at 135%.",
      "endTimestamp": "00:00:21",
      "speaker": "Alex Rivera",
      "startTimestamp": "00:00:16"
    }
  ],
  "pagination": {
    "nextUrl": "https://api.affinity.co/v2/transcripts/1/fragments?cursor=ICAgICAgIGFmdGVyOjo6NA",
    "prevUrl": "https://api.affinity.co/v2/transcripts/1/fragments?cursor=ICAgICAgYmVmb3JlOjo6Nw",
    "totalCount": 4
  }
}
```

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Users

Operations about users

### Get all Users
`GET /v2/users`

- **Tag:** Users · **OperationId:** v2_users__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Paginate through internal Users in your organization.

Returns information about each User, including name, primary email address, all email
addresses, photo URL, account status, and account role.

The `emailAddresses` and `role` properties are only returned to callers with the "Manage
Users" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

Use the optional `term` parameter to filter by first name, last name, or primary email address.

You can also filter users using the `filter` query parameter. The filter parameter is a string
that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int32` | `=` | `id=1\|id=2\|id=3` |
| `status` | `enum` | `=` | `status=active` |

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `term` | `string` | No | Case-insensitive search across first name, last name, and primary email address. Returns users matching the term as a substring. |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/users' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: UserDataPaged
*Type:* object
A paginated list of Users
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([UserData](#userdata)) | Yes | A page of UserData results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single User
`GET /v2/users/{userId}`

- **Tag:** Users · **OperationId:** v2_users_userId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns information about a single internal User, including name, primary email
address, all email addresses, photo URL, account status, and account role.

The `userId` path parameter is the same identifier as the User's corresponding Person ID
every internal User has a matching Person record, and they share the same numeric ID. You can
use a Person ID returned from any Persons endpoint here, and vice versa.

The `emailAddresses` and `role` properties are only returned to callers with the "Manage
Users" [permission](https://developer.affinity.co/pages/external-api-v2/permissions).

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `userId` | `integer<int32>` | Yes | User ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/users/{userId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: UserData
*Type:* object
An internal user in your organization, including their name, primary email address, all email addresses, photo URL, account status, and account role.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The user's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `firstName` | `string` | Yes | The user's first name |
| `lastName` | `string/null` | Yes | The user's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The user's primary email address |
| `emailAddresses` | `array<string<email>> (≤ 100 items)` | No | All of the user's email addresses. Only returned when the authenticated user has the "Manage Users" [permission](https://developer.affinity.co/pages/external-api-v2/permissions). |
| `photoUrl` | `string/null<uri>` | Yes | URL of the user's profile photo |
| `status` | `string (enum: `active`, `invited`, `deactivated`)` | Yes | The user's account status. - `active`: the user can sign in and use Affinity. - `invited`: the user has been invited to the product but has not yet accepted   the invitation and thus cannot have taken any actions. - `deactivated`: the user was once active but has been deactivated and can no   longer use the product. |
| `role` | `string` | No | The user's account role. Only returned when the authenticated user has the "Manage Users" [permission](https://developer.affinity.co/pages/external-api-v2/permissions). |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `403` | Forbidden | [AuthorizationErrors](#authorizationerrors) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Webhooks

Operations about webhooks

### Get all Webhooks
`GET /v2/webhooks`

- **Tag:** Webhooks · **OperationId:** v2_webhooks__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns a page of the Webhooks created by the caller. Users allowed to manage all webhooks receive every Webhook in the organization.

You can filter webhooks using the `filter` query parameter. The filter parameter is a string
that you can specify conditions based on the following properties.

| **Property Name** | **Type** | **Allowed Operators** | **Examples** |
|---|---|---|---|
| `id` | `int64` | `=` | `id=1\|id=2` |
| `createdAt` | `datetime` | `>`, `<`, `>=`, `<=` | `createdAt>=2026-01-01T00:00:00Z` |
| `updatedAt` | `datetime` | `>`, `<`, `>=`, `<=` | `updatedAt>=2026-01-01T00:00:00Z` |

Results are ordered by `id` ascending.

#### Query Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `boolean` | No | Include total count of the collection in the pagination response |
| `cursor` | `string` | No | Cursor for the next or previous page |
| `limit` | `integer<int32>` | No | Number of items to include in the page |
| `filter` | `string` | No | Filter options |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/webhooks' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: webhooks.WebhookPaged
*Type:* object
A page of Webhook objects.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([webhooks.Webhook](#webhookswebhook)) | Yes | A page of Webhook objects. |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Create a Webhook
`POST /v2/webhooks`

- **Tag:** Webhooks · **OperationId:** v2_webhooks__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Creates a new Webhook. The `creator` of the new webhook is the user associated with the API key.

The URL is validated with a test delivery before the webhook is created. The request is rejected with a `validation` error on the `url` property when the URL is invalid or unreachable, contains embedded credentials, or already belongs to another webhook in the organization.

The request is rejected with a `bad-request` error, which has no associated property, when the organization has reached its webhook limit.

#### Request Body

**Media type:** `application/json`
Request body for creating a webhook. The URL is validated with a test delivery before the webhook is created.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string<uri>` | Yes | The URL event payloads are delivered to. Must be unique within the organization. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | Yes | The event types the webhook receives. An empty array subscribes the webhook to all event types. |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/webhooks' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 201 — application/json

Created

**Response schema (`application/json`):**
###### Schema: webhooks.Webhook
*Type:* object
A webhook subscription that delivers event notifications to an external URL.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The webhook's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `url` | `string<uri>` | Yes | The URL event payloads are delivered to. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | Yes | The event types this webhook receives. An empty array means the webhook receives all event types. |
| `status` | `string (enum: `active`, `disabled`)` | Yes | Whether the webhook currently delivers events. A `disabled` webhook keeps its configuration but does not deliver events. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who created the webhook. `null` when the creator is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the webhook was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the webhook was last updated. `null` if the webhook has never been updated. |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Delete a Webhook
`DELETE /v2/webhooks/{webhookId}`

- **Tag:** Webhooks · **OperationId:** v2_webhooks_webhookId__DELETE · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Deletes a Webhook. Only the webhook's creator, or a user allowed to manage all webhooks, may delete it.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `webhookId` | `integer<int64>` | Yes | Webhook ID |

#### Example Request

```bash
curl --request DELETE 'https://api.affinity.co/v2/webhooks/{webhookId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Get a single Webhook
`GET /v2/webhooks/{webhookId}`

- **Tag:** Webhooks · **OperationId:** v2_webhooks_webhookId__GET · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Returns a single Webhook created by the caller. Users allowed to manage all webhooks may retrieve any Webhook in the organization. Responds with `404` when the webhook does not exist or is not accessible.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `webhookId` | `integer<int64>` | Yes | Webhook ID |

#### Example Request

```bash
curl --request GET 'https://api.affinity.co/v2/webhooks/{webhookId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 200 — application/json

OK

**Response schema (`application/json`):**
###### Schema: webhooks.Webhook
*Type:* object
A webhook subscription that delivers event notifications to an external URL.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The webhook's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `url` | `string<uri>` | Yes | The URL event payloads are delivered to. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | Yes | The event types this webhook receives. An empty array means the webhook receives all event types. |
| `status` | `string (enum: `active`, `disabled`)` | Yes | Whether the webhook currently delivers events. A `disabled` webhook keeps its configuration but does not deliver events. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who created the webhook. `null` when the creator is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the webhook was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the webhook was last updated. `null` if the webhook has never been updated. |

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

### Update a Webhook
`POST /v2/webhooks/{webhookId}`

- **Tag:** Webhooks · **OperationId:** v2_webhooks_webhookId__POST · **Stability:** `beta` · **Auth:** bearerAuth

> **⚠️ This endpoint is currently in BETA**


Updates a Webhook. Only provided fields are changed; omitted fields keep their current value.

Changing `url` on an active webhook, or setting `status` to `active` on a disabled webhook, triggers a test delivery that validates the URL before the update is applied. URLs containing embedded credentials are rejected.

Only the webhook's creator, or a user allowed to manage all webhooks, may update it.

#### Path Parameters
| Name | Type | Required | Description |
| --- | --- | --- | --- |
| `webhookId` | `integer<int64>` | Yes | Webhook ID |

#### Request Body

**Media type:** `application/json`
Partial-update request body for a webhook. Only provided properties are updated. Changing `url` on an active webhook, or setting `status` to `active` on a disabled webhook, triggers a test delivery that validates the URL before the update is applied.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string<uri>` | No | New delivery URL for the webhook. Must be unique within the organization. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | No | New set of event types the webhook receives. An empty array subscribes the webhook to all event types. |
| `status` | `string (enum: `active`, `disabled`)` | No | Set to `disabled` to pause event delivery, or `active` to resume it. |

#### Example Request

```bash
curl --request POST 'https://api.affinity.co/v2/webhooks/{webhookId}' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

#### Responses

##### 204

No Content

**Response Headers:** the standard rate-limit headers; see [Rate Limit Headers](#rate-limit-headers).

##### Error responses

Each carries the standard rate-limit headers ([Rate Limit Headers](#rate-limit-headers)). See the [Error Reference](#error-reference) for every error code.

| Status | Description | Schema |
| --- | --- | --- |
| `400` | Bad Request | `errors`: [BadRequestError](#badrequesterror) \| [ValidationError](#validationerror) |
| `404` | Not Found | [NotFoundErrors](#notfounderrors) |
| `default` | Errors | [Errors](#errors) |

## Schema Reference
### Attendee
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `emailAddress` | `string/null<email>` | Yes | The email addresses of the attendee |
| `person` | [PersonData](#persondata) \| `null` | Yes |  |
### AttendeesPreview
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Attendee](#attendee)) | Yes | A preview of Attendees |
| `totalCount` | `integer<int64>` | Yes | The total count of Attendees (Constraints: ≥ 0; ≤ 9007199254740991) |
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` ([AuthorizationError](#authorizationerror)) | Yes | AuthorizationError errors |
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
| `manualCreator` | `object` ([PersonData](#persondata)) | Yes |  |
| `participants` | `array<object>` ([PersonData](#persondata)) | Yes | The participants of the chat |
### CompaniesFilter
Filter for multi-company fields
**Variant:** [CompaniesFilterMultiValues](#companiesfiltermultivalues)
**Variant:** [CompaniesFilterNoValue](#companiesfilternovalue)
### CompaniesFilterMultiValues
Filter for multi-company fields matching against one or more companies
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `has-any-of`, `has-none-of`, `has-all-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([CompanyReference](#companyreference)) | Yes | One or more companies to match against |
### CompaniesFilterNoValue
Filter for multi-company fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### CompaniesValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([CompanyData](#companydata)) | Yes | The values for many companies |
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
### CompaniesValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `company`, `company-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### CompaniesValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([CompanyReference](#companyreference)) | Yes | The values for many companies |
### Company
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>>` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `fields` | `array<object>` ([Field](#field)) | No | The fields associated with the company |
### CompanyBatchOperationRequest
**Variant:** [CompanyBatchOperationUpdateFields](#companybatchoperationupdatefields)
### CompanyBatchOperationResponse
The response body for a single operation within a company batch request.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` ([CompanyBatchOperations](#companybatchoperations)) | No | The type of batch operation that was performed on the company. |
### CompanyBatchOperationUpdateFields
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` ([fields.FieldUpdate](#fieldsfieldupdate)) | Yes |  |
### CompanyBatchOperations
The set of supported batch operation types for companies.
Allowed values: `update-fields`
### CompanyData
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
### CompanyDataPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | Yes | A page of Company results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### CompanyDuplicateSuggestion
A suggestion that a company profile is a duplicate of a primary company profile.
Use the `id` of `primaryProfile` and the `id` of the single entry in `duplicateProfiles` with `POST /v2/company-merges` to execute a merge.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | A unique identifier for the duplicate company suggestion |
| `primaryProfile` | `object` ([CompanyDuplicateSuggestionProfile](#companyduplicatesuggestionprofile)) | Yes | The recommended primary company profile that duplicates should be merged into |
| `duplicateProfiles` | `array<object> (≤ 1 items, ≥ 1 items)` ([CompanyDuplicateSuggestionProfile](#companyduplicatesuggestionprofile)) | Yes | The suggested duplicate company profile that should be merged into the primary profile. Always contains exactly one entry today; modeled as an array so that the shape stays compatible if multi-way suggestions are introduced in the future. |
| `matchCriteria` | `string (enum: `name`, `domain-redirect`, `domain-match`)` | Yes | The matching signal that produced this duplicate suggestion.   - `name`: the two companies have very similar names (Low confidence)   - `domain-match`: the two companies have identical domains (High confidence)   - `domain-redirect`: domain associated with the two companies redirect to the same location (Medium confidence) |
### CompanyDuplicateSuggestionPaged
Paginated list of company duplicate suggestions
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([CompanyDuplicateSuggestion](#companyduplicatesuggestion)) | Yes | Array of company duplicate suggestions |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### CompanyDuplicateSuggestionProfile
A company profile returned as part of a company duplicate suggestion
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>> (≤ 100 items)` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is a global profile shared across all organizations, as opposed to being specific to a single organization. |
| `isEnriched` | `boolean` | Yes | Whether the company is enriched with data from our data providers. |
### CompanyFilter
Filter for single-company fields
**Variant:** [CompanyFilterMultiValues](#companyfiltermultivalues)
**Variant:** [CompanyFilterNoValue](#companyfilternovalue)
### CompanyFilterMultiValues
Filter for single-company fields matching against one or more companies
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-any-of`, `is-none-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([CompanyReference](#companyreference)) | Yes | One or more companies to match against |
### CompanyFilterNoValue
Filter for single-company fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### CompanyListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([Company](#company)) | Yes | Company model |
### CompanyMergeRequest
Request body for initiating a company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `primaryCompanyId` | `integer<int64>` | Yes | The ID of the company profile that will be kept after the merge. All data from the duplicate company will be merged into this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicateCompanyId` | `integer<int64>` | Yes | The ID of the company profile that will be merged and then deleted. All data from this company will be transferred to the primary company. (Constraints: ≥ 1; ≤ 9007199254740991) |
### CompanyMergeResponse
Response body for initiating a company merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `taskUrl` | `string<uri>` | Yes | URL to check the status of the merge task |
### CompanyMergeState
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([CompanyMergeState](#companymergestate)) | Yes | Array of company merge states |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### CompanyMergeTask
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([CompanyMergeTask](#companymergetask)) | Yes | Array of company merge tasks |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### CompanyPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Company](#company)) | Yes | A page of Company results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
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
| `data` | [CompanyData](#companydata) \| `null` | Yes |  |
### CompanyValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `null` \| [CompanyReference](#companyreference) | Yes |  |
### ConflictError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### CoworkerConnection
A single inferred connection to a target, based on shared work history. The `source` is the person in your Affinity data who might know the target; `inference` describes the shared employment behind it.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | `object` ([RelationshipPerson](#relationshipperson)) | Yes | The person in your Affinity data, whom you know. |
| `inference` | `object` ([CoworkerInference](#coworkerinference)) | Yes | The shared work history behind the connection. |
### CoworkerConnectionGroup
A target person together with every shared-work-history connection inferred to them. The same target can be reachable through several people you know, so the connections to one target are grouped here under that target.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `target` | `object` ([InferredConnectionTarget](#inferredconnectiontarget)) | Yes | The person not in your Affinity data, whom you want to know. |
| `connections` | `array<object> (≤ 50 items, ≥ 1 items)` ([CoworkerConnection](#coworkerconnection)) | Yes | The shared-work-history connections to this target, ordered strongest first. |
### CoworkerConnectionGroupsPaged
A paginated list of shared-work-history connections grouped by target person. Each item is one target and the connections inferred to them.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 50 items)` ([CoworkerConnectionGroup](#coworkerconnectiongroup)) | Yes | A page of targets, each with the shared-work-history connections to them, ordered by each target's strongest connection (strongest first). |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### CoworkerInference
The belief that the source and target worked together: they were employed at the same company at the same time. The `sharedEmployer` is that company; `overlapStartDate` and `overlapEndDate` bound the period their employment overlapped.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sharedEmployer` | `object` ([InferredConnectionCompanyRef](#inferredconnectioncompanyref)) | Yes | The company at which the source and target were employed at the same time. |
| `overlapStartDate` | `string<date>` | Yes | The first date on which the source and target were both employed at the `sharedEmployer`. |
| `overlapEndDate` | `string<date>` | Yes | The last date on which the source and target were both employed at the `sharedEmployer`. |
### DateFilter
Filter for date fields
**Variant:** [DateFilterOneValue](#datefilteronevalue)
**Variant:** [DateFilterRange](#datefilterrange)
**Variant:** [DateFilterRelative](#datefilterrelative)
**Variant:** [DateFilterRelativeRange](#datefilterrelativerange)
**Variant:** [DateFilterRelativeDate](#datefilterrelativedate)
**Variant:** [DateFilterNoValue](#datefilternovalue)
### DateFilterNoValue
Filter for date fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### DateFilterOneValue
Filter for date fields relative to or matching a single date
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-on`, `is-not-on`, `is-before`, `is-on-or-before`, `is-after`, …)` | Yes | The filter operator |
| `value` | `string<date>` | Yes | The date to filter against |
### DateFilterRange
Filter for date fields within an absolute date range (inclusive)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string` | Yes | The filter operator |
| `value` | `array<string<date>> (≤ 2 items, ≥ 2 items)` | Yes | Two dates defining the inclusive range, start date first, end date second |
### DateFilterRelative
Filter for date fields within a relative date window
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-within-the-last`, `is-not-within-the-last`, `is-within-the-next`, `is-not-within-the-next`)` | Yes | The filter operator |
| `value` | `object` ([RelativeDates](#relativedates)) | Yes | The relative date window definition, specifying an amount and unit |
### DateFilterRelativeDate
Filter for date fields using a single relative duration threshold
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-exactly-relative`, `is-not-exactly-relative`, `is-more-than-relative`, `is-more-than-or-equal-to-relative`, `is-less-than-relative`, …)` | Yes | The filter operator |
| `value` | `object` ([RelativeDate](#relativedate)) | Yes | The relative duration threshold |
### DateFilterRelativeRange
Filter for values between a start and end amount of elapsed time (e.g. between 7 and 30 days)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string` | Yes | The filter operator |
| `value` | `object` ([RelativeDateRange](#relativedaterange)) | Yes | The relative range definition, specifying a start and end amount and a unit |
### DateValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `string/null<date-time>` | Yes | The value for a date |
### DealContext
The deal that ties the source and target together: the funding round, the source's role as the investor, and the target's role as the executive at the company that was funded.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fundingEvent` | `object` ([DealFundingEvent](#dealfundingevent)) | Yes | The funding round behind the connection. |
| `investor` | `object` ([DealMemberRole](#dealmemberrole)) | Yes | The source's role as the investor, at the investing firm. |
| `executive` | `object` ([DealMemberRole](#dealmemberrole)) | Yes | The target's role as the executive, at the company that was funded. |
### DealFundingEvent
The funding round behind the connection: when it happened and its size.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `date` | `string<date>` | Yes | The date the funding round took place. |
| `series` | `string/null` | Yes | The funding round's series, or `null` when not known. |
| `amount` | `number/null<float>` | Yes | The amount raised in the round, in `currencyCode`, or `null` when not known. |
| `currencyCode` | `string/null` | Yes | The ISO 4217 currency code for `amount`, or `null` when not known. |
### DealMemberRole
A party's role in the deal: their title and tenure at the `company` involved. For the investor this is the investing firm; for the executive it is the company they led.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `title` | `string/null` | Yes | The person's title in the role, or `null` when not known. |
| `startDate` | `string<date>` | Yes | The date the person started the role. |
| `endDate` | `string/null<date>` | Yes | The date the person left the role, or `null` when they are still in it. |
| `company` | `object` ([InferredConnectionCompanyRef](#inferredconnectioncompanyref)) | Yes | The company the person held the role at. |
### Dropdown
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown item text |
### DropdownFilter
Filter for dropdown fields
**Variant:** [DropdownFilterMultiValues](#dropdownfiltermultivalues)
**Variant:** [DropdownFilterNoValue](#dropdownfilternovalue)
### DropdownFilterMultiValues
Filter for dropdown fields matching against one or more dropdown options
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-any-of`, `is-none-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([DropdownReference](#dropdownreference)) | Yes | One or more dropdown options to match against |
### DropdownFilterNoValue
Filter for dropdown fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### DropdownOption
**Variant:** [dropdownOptions.DropdownOption](#dropdownoptionsdropdownoption)
**Variant:** [dropdownOptions.RankedDropdownOption](#dropdownoptionsrankeddropdownoption)
**Variant:** [dropdownOptions.StatusDropdownOption](#dropdownoptionsstatusdropdownoption)
### DropdownOptionBase
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
### DropdownOptionPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([DropdownOption](#dropdownoption)) | Yes | A page of DropdownOption results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
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
| `data` | [Dropdown](#dropdown) \| `null` | Yes |  |
### DropdownValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `null` \| [DropdownReference](#dropdownreference) | Yes |  |
### DropdownsFilter
Filter for multi-dropdown fields
**Variant:** [DropdownsFilterMultiValues](#dropdownsfiltermultivalues)
**Variant:** [DropdownsFilterNoValue](#dropdownsfilternovalue)
### DropdownsFilterMultiValues
Filter for multi-dropdown fields matching against one or more dropdown options
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `has-any-of`, `has-none-of`, `has-all-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([DropdownReference](#dropdownreference)) | Yes | One or more dropdown options to match against |
### DropdownsFilterNoValue
Filter for multi-dropdown fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### DropdownsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([Dropdown](#dropdown)) | Yes | The value for many dropdown items |
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
### DropdownsValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `dropdown`, `dropdown-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Dropdown](#dropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### DropdownsValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([DropdownReference](#dropdownreference)) | Yes | The value for many dropdown items |
### Email
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `subject` | `string/null` | Yes | The subject of the email |
| `sentAt` | `string<date-time>` | Yes | The time the email was sent |
| `from` | `object` ([Attendee](#attendee)) | Yes |  |
| `to` | `array<object>` ([Attendee](#attendee)) | Yes | The recipients of the email |
| `cc` | `array<object>` ([Attendee](#attendee)) | Yes | The cc recipients of the email |
### Error
**Variant:** [AuthenticationError](#authenticationerror)
**Variant:** [AuthorizationError](#authorizationerror)
**Variant:** [BadRequestError](#badrequesterror)
**Variant:** [ConflictError](#conflicterror)
**Variant:** [MethodNotAllowedError](#methodnotallowederror)
**Variant:** [NotAcceptableError](#notacceptableerror)
**Variant:** [NotFoundError](#notfounderror)
**Variant:** [NotImplementedError](#notimplementederror)
**Variant:** [RateLimitError](#ratelimiterror)
**Variant:** [ServerError](#servererror)
**Variant:** [TimeoutError](#timeouterror)
**Variant:** [UnprocessableEntityError](#unprocessableentityerror)
**Variant:** [UnsupportedMediaTypeError](#unsupportedmediatypeerror)
**Variant:** [ValidationError](#validationerror)
### Errors
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<oneOf>` ([Error](#error)) | Yes | Errors |
### FeedbackRequest
Request body for sending feedback
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `mcp`, `api`, `other`)` | Yes | The type of feedback being submitted |
| `subject` | `string` | Yes | Subject of the feedback (Constraints: length ≥ 1; length ≤ 255) |
| `body` | `string` | Yes | The details of the feedback, please be thorough and include examples of what you're trying to accomplish and how the product could be improved to support it. (Constraints: length ≥ 1; length ≤ 10000) |
### Field
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`, `hidden`)` | Yes | The field's category. `hidden` is a redaction state rather than a category: it signals a field on a restricted opportunity the caller cannot manage, whose value is masked. |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `eventbrite`, `mailchimp`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `value` | [CompaniesValue](#companiesvalue) \| [CompanyValue](#companyvalue) \| [DateValue](#datevalue) \| [DropdownsValue](#dropdownsvalue) \| [DropdownValue](#dropdownvalue) \| [FloatsValue](#floatsvalue) \| [FloatValue](#floatvalue) \| [FormulaValue](#formulavalue) \| [InteractionValue](#interactionvalue) \| [ListsValue](#listsvalue) \| [LocationsValue](#locationsvalue) \| [LocationValue](#locationvalue) \| [NoteValue](#notevalue) \| [PersonsValue](#personsvalue) \| [PersonValue](#personvalue) \| [RankedDropdownValue](#rankeddropdownvalue) \| [ReminderValue](#remindervalue) \| [TextsValue](#textsvalue) \| [TextValue](#textvalue) | Yes |  |
### FieldFilterability
Describes how a field can be used in filter expressions.
**Variant:** [FieldFilterabilityFieldOnly](#fieldfilterabilityfieldonly)
**Variant:** [FieldFilterabilityAttributeOnField](#fieldfilterabilityattributeonfield)
### FieldFilterabilityAttributeOnField
A field with sub-attributes that are each filtered independently using the field `id`, an attribute `id`, and an operator from that attribute's `operators` list.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filterableFieldType` | `string` | Yes |  |
| `attributes` | `array<object> (≤ 100 items)` ([FilterableFieldAttribute](#filterablefieldattribute)) | Yes | The sub-attributes of this field, each with their own supported operators |
### FieldFilterabilityFieldOnly
A field that is filtered directly using the field `id` and one of the listed `operators`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filterableFieldType` | `string` | Yes |  |
| `operators` | `array<object> (≤ 100 items)` ([FilterableFieldOperator](#filterablefieldoperator)) | Yes | The operators supported for filtering on this field |
### FieldMetadata
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier |
| `name` | `string` | Yes | The field's name |
| `description` | `string/null` | Yes | A description of the field's purpose. `null` if no description was provided. |
| `type` | `string (enum: `enriched`, `global`, `list`, `relationship-intelligence`)` | Yes | The field's type |
| `enrichmentSource` | `string/null (enum: `affinity-data`, `dealroom`, `eventbrite`, `mailchimp`, `None`)` | Yes | The source of the data in this Field (if it is enriched) |
| `valueType` | `string (enum: `person`, `person-multi`, `company`, `company-multi`, `filterable-text`, …)` | Yes | The type of the data in this Field |
| `isRequired` | `boolean` | Yes | Whether a value for this field is required when creating an entity or List Entry. |
| `createdAt` | `string/null<date-time>` | Yes | The date and time this field was created, or `null` for built-in fields that Affinity provides automatically and that therefore have no creation time (for example identity, association, interaction, and some enriched fields). |
| `filterability` | `null` \| [FieldFilterability](#fieldfilterability) | No | How this field can be used in filter expressions. Only present on endpoints that support the `includes` query parameter when `filterability` is requested. `null` if the field is not filterable. |
| `sortability` | `null` \| [FieldSortability](#fieldsortability) | No | How this field can be used in sort expressions. Only present on endpoints that support the `includes` query parameter when `sortability` is requested. `null` if the field is not sortable. |
### FieldMetadataPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([FieldMetadata](#fieldmetadata)) | Yes | A page of FieldMetadata results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### FieldPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Field](#field)) | Yes | A page of Field results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### FieldSortability
Describes how a field can be used in sort expressions.
**Variant:** [FieldSortabilityFieldOnly](#fieldsortabilityfieldonly)
**Variant:** [FieldSortabilityAttributeOnField](#fieldsortabilityattributeonfield)
### FieldSortabilityAttribute
A sub-attribute of a sortable field.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The attribute identifier |
| `name` | `string` | Yes | Human-readable name for the attribute |
| `valueType` | `string (enum: `company-multi`, `date`, `number`, `person`, `person-multi`, …)` | Yes | The value type of this attribute |
### FieldSortabilityAttributeOnField
A field with sub-attributes that can each be sorted on independently using the field `id` and an attribute `id`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sortableFieldType` | `string` | Yes |  |
| `attributes` | `array<object> (≤ 5 items)` ([FieldSortabilityAttribute](#fieldsortabilityattribute)) | Yes | The sub-attributes that can be sorted on |
### FieldSortabilityFieldOnly
A field that is sorted directly by its value. Use the field `id` as `fieldId` in sort expressions.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `sortableFieldType` | `string` | Yes |  |
### FieldUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | No |  |
### FieldValue
**Variant:** [CompaniesValue](#companiesvalue)
**Variant:** [CompanyValue](#companyvalue)
**Variant:** [DateValue](#datevalue)
**Variant:** [DropdownsValue](#dropdownsvalue)
**Variant:** [DropdownValue](#dropdownvalue)
**Variant:** [FloatsValue](#floatsvalue)
**Variant:** [FloatValue](#floatvalue)
**Variant:** [FormulaValue](#formulavalue)
**Variant:** [InteractionValue](#interactionvalue)
**Variant:** [ListsValue](#listsvalue)
**Variant:** [LocationsValue](#locationsvalue)
**Variant:** [LocationValue](#locationvalue)
**Variant:** [NoteValue](#notevalue)
**Variant:** [PersonsValue](#personsvalue)
**Variant:** [PersonValue](#personvalue)
**Variant:** [RankedDropdownValue](#rankeddropdownvalue)
**Variant:** [ReminderValue](#remindervalue)
**Variant:** [TextsValue](#textsvalue)
**Variant:** [TextValue](#textvalue)
### FieldValueUpdate
**Variant:** [CompaniesValueUpdate](#companiesvalueupdate)
**Variant:** [CompanyValueUpdate](#companyvalueupdate)
**Variant:** [DateValue](#datevalue)
**Variant:** [DropdownValueUpdate](#dropdownvalueupdate)
**Variant:** [DropdownsValueUpdate](#dropdownsvalueupdate)
**Variant:** [FloatValue](#floatvalue)
**Variant:** [FloatsValue](#floatsvalue)
**Variant:** [LocationValue](#locationvalue)
**Variant:** [LocationsValue](#locationsvalue)
**Variant:** [PersonValueUpdate](#personvalueupdate)
**Variant:** [PersonsValueUpdate](#personsvalueupdate)
**Variant:** [RankedDropdownValueUpdate](#rankeddropdownvalueupdate)
**Variant:** [TextValue](#textvalue)
**Variant:** [TextsValue](#textsvalue)
### FieldValuesPaged
**Variant:** [CompaniesValuePaged](#companiesvaluepaged)
**Variant:** [DropdownsValuePaged](#dropdownsvaluepaged)
**Variant:** [ListsValuePaged](#listsvaluepaged)
**Variant:** [LocationsValuePaged](#locationsvaluepaged)
**Variant:** [PersonsValuePaged](#personsvaluepaged)
**Variant:** [RankedDropdownValuePaged](#rankeddropdownvaluepaged)
**Variant:** [TextsValuePaged](#textsvaluepaged)
### FilterGroup
A logical group of filters combined with AND or OR. Groups can be nested to build complex filter trees. Each group may contain up to 50 items. Items can be individual filters or nested filter groups.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operator` | `string (enum: `and`, `or`)` | Yes | The logical operator applied to all filters in this group |
| `filters` | `array<oneOf> (≤ 50 items, ≥ 0 items)` | Yes | A list of filters or nested filter groups. |

**`filters` details** — A list of filters or nested filter groups.

**Items**

**Variant:** [ValueFilter](#valuefilter)
**Variant:** [FilterGroup](#filtergroup)
### FilterableFieldAttribute
A sub-attribute of a filterable field, used when a field has multiple independent filterable dimensions (e.g. an interaction field with a `date-of-activity` attribute).
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The attribute identifier |
| `name` | `string` | Yes | Human-readable name for the attribute |
| `valueType` | `string (enum: `date`, `number`, `person-multi`, `text`)` | Yes | The value type of this attribute |
| `operators` | `array<object> (≤ 100 items)` ([FilterableFieldOperator](#filterablefieldoperator)) | Yes | The operators supported for this attribute |
### FilterableFieldOperator
An operator that can be applied to a filterable field or attribute. Use the `id` as the `operator` value in filter requests.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string (enum: `contains`, `does-not-contain`, `ends-with`, `has-all-of`, `has-any-of`, …)` | Yes | The operator identifier |
| `name` | `string` | Yes | Human-readable name for the operator |
| `numberOfValuesRequired` | `string (enum: `none`, `one`, `two`, `multi`)` | Yes | The number of values required for this operator. `none` means no value is needed (e.g. `is-empty`). `one` means a single value. `two` means a range (e.g. `is-between`). `multi` means one or more values (e.g. `has-any-of`). |
| `relativeDateUnits` | `array<string (enum: `minute`, `hour`, `day`, `week`, `month`, …)>` | No | For relative date operators, the list of time units that can be used as the value (e.g. `days`, `weeks`, `months`). Only present on relative date operators. |

**`relativeDateUnits` details** — For relative date operators, the list of time units that can be used as the value (e.g. `days`, `weeks`, `months`). Only present on relative date operators.

**Items**

Allowed values: `minute`, `hour`, `day`, `week`, `month`, `quarter`, `year`
### FilterableTextFilter
Filter for filterable-text fields (single-value structured text with predefined options)
**Variant:** [FilterableTextFilterMultiValues](#filterabletextfiltermultivalues)
**Variant:** [FilterableTextFilterNoValue](#filterabletextfilternovalue)
### FilterableTextFilterMultiValues
Filter for filterable-text fields matching against one or more text values
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-any-of`, `is-none-of`)` | Yes | The filter operator |
| `value` | `array<string> (≤ 100 items, ≥ 1 items)` | Yes | One or more text values to match against |
### FilterableTextFilterNoValue
Filter for filterable-text fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### FilterableTextsFilter
Filter for filterable-text-multi fields (multi-value structured text with predefined options)
**Variant:** [FilterableTextsFilterMultiValues](#filterabletextsfiltermultivalues)
**Variant:** [FilterableTextsFilterNoValue](#filterabletextsfilternovalue)
### FilterableTextsFilterMultiValues
Filter for filterable-text-multi fields matching against one or more text values
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `has-any-of`, `has-none-of`, `has-all-of`)` | Yes | The filter operator |
| `value` | `array<string> (≤ 100 items, ≥ 1 items)` | Yes | One or more text values to match against |
### FilterableTextsFilterNoValue
Filter for filterable-text-multi fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
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
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
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
| `data` | [FormulaNumber](#formulanumber) \| `null` | Yes |  |
### Grant
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `api-key`, `access-token`)` | Yes | The type of grant used to authenticate |
| `scopes` | `array<string>` | Yes | The scopes available to the current grant |
| `createdAt` | `string<date-time>` | Yes | When the grant was created |
### InferredConnectionCompanyRef
A reference to a company that appears in an inferred connection.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string/null` | Yes | The company's name. |
| `domain` | `string/null` | Yes | The company's primary domain, or `null` when not known. |
### InferredConnectionTarget
The `target` of an inferred connection: the person who is not in your Affinity data, described only (no `id`). Includes the company they currently work at, where they are a potential contact now.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fullName` | `string/null` | Yes | The person's full name, or `null` when not known. |
| `title` | `string/null` | Yes | The person's current job title, or `null` when not known. |
| `linkedinUrl` | `string/null` | Yes | A link to the person's LinkedIn profile, or `null` when not known. |
| `currentCompany` | `object` ([InferredConnectionCompanyRef](#inferredconnectioncompanyref)) | Yes | The company the person works at today, at which they are a potential contact now. Filterable by `target.currentCompany.id`. |
### Interaction
**Variant:** [ChatMessage](#chatmessage)
**Variant:** [Email](#email)
**Variant:** [Meeting](#meeting)
**Variant:** [PhoneCall](#phonecall)
### InteractionValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | [Interaction](#interaction) \| `null` | Yes |  |
| `internalPerson` | [PersonData](#persondata) \| `null` | Yes | The team member Affinity attributes the interaction to, matching the person shown for it in the CRM. `null` when no team member can be attributed. |
### InvestorExecutiveConnection
A single inferred connection to a target, where the source invested in a company the target was an executive of. The `source` is the person in your Affinity data who might know the target; `inference` describes the investment behind it.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `source` | `object` ([RelationshipPerson](#relationshipperson)) | Yes | The person in your Affinity data, whom you know. The investor in this connection. |
| `inference` | `object` ([InvestorExecutiveInference](#investorexecutiveinference)) | Yes | Deprecated: use `dealContext`, which carries the investing firm and portfolio company along with the funding round and both parties' roles. This field will be removed while the API is pre-stable; it remains for now to give consumers time to migrate. The investment relationship behind the connection. |
| `dealContext` | `object` ([DealContext](#dealcontext)) | Yes | The deal behind the connection: the funding round and both parties' roles. |
### InvestorExecutiveConnectionGroup
A target person together with every connection inferred to them where the source invested in a company the target was an executive of. The same target can be reachable through several people you know, so the connections to one target are grouped here under that target.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `target` | `object` ([InferredConnectionTarget](#inferredconnectiontarget)) | Yes | The person not in your Affinity data, whom you want to know. The executive in these connections. |
| `connections` | `array<object> (≤ 50 items, ≥ 1 items)` ([InvestorExecutiveConnection](#investorexecutiveconnection)) | Yes | The connections to this target, ordered strongest first. |
### InvestorExecutiveConnectionGroupsPaged
A paginated list of investor-executive connections grouped by target person. Each item is one target and the connections inferred to them.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 50 items)` ([InvestorExecutiveConnectionGroup](#investorexecutiveconnectiongroup)) | Yes | A page of targets, each with the connections to them, ordered by each target's strongest connection (strongest first). |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### InvestorExecutiveInference
The belief that the source invested in a company where the target was an executive. The `investingFirm` is the firm the source invested through, when known; the `portfolioCompany` is the company the target was an executive at.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `investingFirm` | [InferredConnectionCompanyRef](#inferredconnectioncompanyref) \| `null` | Yes | The firm the source invested through, or `null` when not known. |
| `portfolioCompany` | `object` ([InferredConnectionCompanyRef](#inferredconnectioncompanyref)) | Yes | The company the target was an executive at. |
### List
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
| `createdAt` | `string<date-time>` | Yes | The date and time the list was created |
### ListData
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for the list |
| `entityCount` | `integer<int32>` | Yes | The total number of entities in the list (Constraints: ≥ 0; ≤ 2147483647) |
### ListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listName` | `string` | Yes | The name of the list that this list entry belongs to |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` ([Field](#field)) | Yes | The fields associated with the list entry |
### ListEntryBatchOperationRequest
**Variant:** [ListEntryBatchOperationUpdateFields](#listentrybatchoperationupdatefields)
### ListEntryBatchOperationResponse
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` ([ListEntryBatchOperations](#listentrybatchoperations)) | No |  |
### ListEntryBatchOperationUpdateFields
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
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | No |  |
### ListEntryBatchOperations
Allowed values: `update-fields`
### ListEntryPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([ListEntry](#listentry)) | Yes | A page of ListEntry results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### ListEntryToBeCreated
Request body for creating a List Entry on a List. The entity referenced by `entity.id` must
match the List's type: a Company ID for a company List, a Person ID for a person List.
Opportunities cannot be added with this endpoint. An opportunity List's entries are the
opportunities themselves, and each opportunity belongs to exactly one List, so an existing
entity cannot be added to one.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `entity` | `object` | Yes | The Company or Person to add to the List. Provide its `id`; the entity must exist and match the List's type (a Company ID for a company List, a Person ID for a person List). |
| `creatorId` | `integer<int64>` | No | The internal Person ID to record as the List Entry's creator. Defaults to the authenticated user. Must be an internal Person in the same organization as the caller. (Constraints: ≥ 1; ≤ 9007199254740991) |

**`entity` details** — The Company or Person to add to the List. Provide its `id`; the entity must exist and match the List's type (a Company ID for a company List, a Person ID for a person List).

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The ID of the Company or Person. (Constraints: ≥ 1; ≤ 9007199254740991) |
### ListEntryWithEntity
**Variant:** [CompanyListEntry](#companylistentry)
**Variant:** [OpportunityListEntry](#opportunitylistentry)
**Variant:** [PersonListEntry](#personlistentry)
### ListEntryWithEntityPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array/null` ([ListEntryWithEntity](#listentrywithentity)) | Yes | A page of ListEntryWithEntity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### ListPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([List](#list)) | Yes | A page of List results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### ListReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### ListToBeCreated
Request body for creating a new List
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | The name of the List (Constraints: length ≥ 1; length ≤ 255) |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for the List |
| `isPublic` | `boolean` | No | Whether the List is public. Public Lists are visible to all users in the organization. Creating a public List requires the "Share accessible Lists globally" permission. (Constraints: default `False`) |
### ListWithType
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the list |
| `creatorId` | `integer<int64>` | Yes | The ID of the user that created this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `ownerId` | `integer<int64>` | Yes | The ID of the user that owns this list (Constraints: ≥ 1; ≤ 9007199254740991) |
| `isPublic` | `boolean` | Yes | Whether or not the list is public |
| `type` | `string (enum: `company`, `opportunity`, `person`)` | Yes | The entity type for this list |
| `createdAt` | `string<date-time>` | Yes | The date and time the list was created |
### ListWithTypePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([ListWithType](#listwithtype)) | Yes | A page of ListWithType results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### ListsFilter
Filter for multi-list fields
**Variant:** [ListsFilterMultiValues](#listsfiltermultivalues)
**Variant:** [ListsFilterNoValue](#listsfilternovalue)
### ListsFilterMultiValues
Filter for multi-list fields matching against one or more lists
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `has-any-of`, `has-none-of`, `has-all-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([ListReference](#listreference)) | Yes | One or more lists to match against |
### ListsFilterNoValue
Filter for multi-list fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### ListsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([ListData](#listdata)) | Yes | The value for many lists |
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
### ListsValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([ListData](#listdata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### Location
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `streetAddress` | `string/null` | Yes | Street address |
| `city` | `string/null` | Yes | City |
| `state` | `string/null` | Yes | State |
| `country` | `string/null` | Yes | Country |
| `continent` | `string/null` | Yes | Continent |
### LocationFilter
Filter for single-location fields
**Variant:** [LocationFilterMultiValues](#locationfiltermultivalues)
**Variant:** [LocationFilterNoValue](#locationfilternovalue)
### LocationFilterMultiValues
Filter for single-location fields matching against one or more location values
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-any-of`, `is-none-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([LocationFilterValue](#locationfiltervalue)) | Yes | One or more locations to match against |
### LocationFilterNoValue
Filter for single-location fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### LocationFilterValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `streetAddress` | `string` | No | Street address |
| `city` | `string` | No | City |
| `state` | `string` | No | State |
| `country` | `string` | No | Country |
| `continent` | `string` | No | Continent |
### LocationValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | [Location](#location) \| `null` | Yes |  |
### LocationsFilter
Filter for multi-location fields
**Variant:** [LocationsFilterMultiValues](#locationsfiltermultivalues)
**Variant:** [LocationsFilterNoValue](#locationsfilternovalue)
### LocationsFilterMultiValues
Filter for multi-location fields matching against one or more location values
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `has-any-of`, `has-none-of`, `has-all-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([LocationFilterValue](#locationfiltervalue)) | Yes | One or more locations to match against |
### LocationsFilterNoValue
Filter for multi-location fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### LocationsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([Location](#location)) | Yes | The values for many locations |
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
### LocationsValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `location`, `location-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([Location](#location)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
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
| `attendees` | `array<object>` ([Attendee](#attendee)) | Yes | People attending the meeting |
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `errors` | `array<object>` ([NotFoundError](#notfounderror)) | Yes | NotFoundError errors |
### NotImplementedError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### NoteValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | [notes.BaseNote](#notesbasenote) \| `null` | Yes | The value for the note |
### NumberFilter
Filter for number fields
**Variant:** [NumberFilterOneValue](#numberfilteronevalue)
**Variant:** [NumberFilterRange](#numberfilterrange)
**Variant:** [NumberFilterNoValue](#numberfilternovalue)
### NumberFilterNoValue
Filter for number fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### NumberFilterOneValue
Filter for number fields comparing against a single numeric value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-equal-to`, `is-not-equal-to`, `is-greater-than`, `is-greater-than-or-equal-to`, `is-less-than`, …)` | Yes | The filter operator |
| `value` | `number` | Yes | The number to compare against |
### NumberFilterRange
Filter for number fields within a numeric range (inclusive)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string` | Yes | The filter operator |
| `value` | `array<number> (≤ 2 items, ≥ 2 items)` | Yes | Exactly two numbers defining the inclusive range (lower bound first, upper bound second) |
### Opportunity
Opportunity model.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity. When `isRedacted` is `true`, the real name is masked and this value is the literal string `[Hidden]`. |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listName` | `string` | Yes | The name of the list that the opportunity belongs to |
| `isRestricted` | `boolean` | Yes | Whether the opportunity is restricted. `false` for customers without the Restricted Opportunities feature enabled. |
| `isRedacted` | `boolean` | Yes | Whether the response is redacted because the requesting user does not have access to this restricted opportunity. The real name is masked as `[Hidden]` when `true`. Always `false` when `isRestricted` is `false`. |
### OpportunityListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([OpportunityWithFields](#opportunitywithfields)) | Yes | Opportunity model including the opportunity's fields. |
### OpportunityPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Opportunity](#opportunity)) | Yes | A page of Opportunity results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### OpportunityReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The opportunity's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### OpportunityToBeUpdated
Partial-update request body for an Opportunity. Only provided properties are updated; properties omitted from the request keep their current value.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | No | The name of the opportunity. (Constraints: length ≥ 1; length ≤ 255) |
### OpportunityWithFields
Opportunity model including the opportunity's fields.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the opportunity (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the opportunity. |
| `listId` | `integer<int64>` | Yes | The ID of the list that the opportunity belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `fields` | `array<object>` ([Field](#field)) | No | The fields associated with the opportunity. Empty for a redacted opportunity. |
| `isRestricted` | `boolean` | Yes | Whether the opportunity is restricted. `false` for customers without the Restricted Opportunities feature enabled. |
| `isRedacted` | `boolean` | Yes | Whether the response is redacted because the requesting user does not have access to sensitive details of this restricted opportunity. When `true`, `fields` is empty. Always `false` when `isRestricted` is `false`. |
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `emailAddresses` | `array<string<email>>` | Yes | All of the person's email addresses |
| `type` | `string (enum: `internal`, `external`)` | Yes | The person's type. `internal` - people who are users within your Affinity instance. `external` - people who are not internal. |
| `fields` | `array<object>` ([Field](#field)) | No | The fields associated with the person |
### PersonBatchOperationRequest
**Variant:** [PersonBatchOperationUpdateFields](#personbatchoperationupdatefields)
### PersonBatchOperationResponse
The response body for a single operation within a person batch request.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string (enum: `update-fields`)` ([PersonBatchOperations](#personbatchoperations)) | No | The type of batch operation that was performed on the person. |
### PersonBatchOperationUpdateFields
Update multiple field values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `operation` | `string` | Yes |  |
| `updates` | `array<object> (≤ 100 items)` ([fields.FieldUpdate](#fieldsfieldupdate)) | Yes |  |
### PersonBatchOperations
The set of supported batch operation types for persons.
Allowed values: `update-fields`
### PersonData
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The persons's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `collaborator`, `external`)` | Yes | The person's type. `internal` - people who are users within your Affinity instance. `collaborator` - individuals outside of your company who have read-only access to specified Affinity list views and stay updated on your firm's activities. `external` - people who are not internal nor collaborators. |
### PersonDataPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A page of Person results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### PersonDataPreview
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A preview of persons |
| `totalCount` | `integer<int64>` | Yes | The total count of persons (Constraints: ≥ 0; ≤ 9007199254740991) |
### PersonDuplicateSuggestion
A suggestion that a person profile is a duplicate of a primary person profile.
Use the `id` of `primaryProfile` and the `id` of the single entry in `duplicateProfiles` with `POST /v2/person-merges` to execute a merge.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | A unique identifier for the duplicate person suggestion |
| `primaryProfile` | `object` ([Person](#person)) | Yes | The recommended primary person profile that duplicates should be merged into |
| `duplicateProfiles` | `array<object> (≤ 1 items, ≥ 1 items)` ([Person](#person)) | Yes | The suggested duplicate person profile that should be merged into the primary profile. Always contains exactly one entry today; modeled as an array so that the shape stays compatible if multi-way suggestions are introduced in the future. |
| `matchCriteria` | `string (enum: `name`, `intelligent`)` | Yes | The matching signal that produced this duplicate suggestion.   - `name`: the two persons have very similar names (Low confidence)   - `intelligent`: the two persons were identified as duplicates across 40+ sources through email matching (Medium confidence) |
### PersonDuplicateSuggestionPaged
Paginated list of person duplicate suggestions
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonDuplicateSuggestion](#personduplicatesuggestion)) | Yes | Array of person duplicate suggestions |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### PersonFilter
Filter for single-person fields
**Variant:** [PersonFilterMultiValues](#personfiltermultivalues)
**Variant:** [PersonFilterNoValue](#personfilternovalue)
### PersonFilterMultiValues
Filter for single-person fields matching against one or more persons
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-any-of`, `is-none-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([PersonReference](#personreference)) | Yes | One or more persons to match against |
### PersonFilterNoValue
Filter for single-person fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### PersonListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The entity type for this list entry |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `createdAt` | `string<date-time>` | Yes | The date that the list entry was created |
| `creatorId` | `integer/null<int64>` | Yes | The ID of the user that created this list entry (Constraints: ≥ 1; ≤ 9007199254740991) |
| `entity` | `object` ([Person](#person)) | Yes | Person model |
### PersonMergeRequest
Request body for initiating a person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `primaryPersonId` | `integer<int64>` | Yes | The ID of the person profile that will be kept after the merge. All data from the duplicate person will be merged into this person. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `duplicatePersonId` | `integer<int64>` | Yes | The ID of the person profile that will be merged and then deleted. All data from this person will be transferred to the primary person. (Constraints: ≥ 1; ≤ 9007199254740991) |
### PersonMergeResponse
Response body for initiating a person merge
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `taskUrl` | `string<uri>` | Yes | URL to check the status of the merge task |
### PersonMergeState
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonMergeState](#personmergestate)) | Yes | Array of person merge states |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### PersonMergeTask
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
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonMergeTask](#personmergetask)) | Yes | Array of person merge tasks |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### PersonPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Person](#person)) | Yes | A page of Person results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
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
| `data` | [PersonData](#persondata) \| `null` | Yes |  |
### PersonValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `null` \| [PersonReference](#personreference) | Yes |  |
### PersonsFilter
Filter for multi-person fields
**Variant:** [PersonsFilterMultiValues](#personsfiltermultivalues)
**Variant:** [PersonsFilterNoValue](#personsfilternovalue)
### PersonsFilterMultiValues
Filter for multi-person fields matching against one or more persons
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `has-any-of`, `has-none-of`, `has-all-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([PersonReference](#personreference)) | Yes | One or more persons to match against |
### PersonsFilterNoValue
Filter for multi-person fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### PersonsValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([PersonData](#persondata)) | Yes | The values for many persons |
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
### PersonsValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `person`, `person-multi`)` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### PersonsValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array/null` ([PersonReference](#personreference)) | Yes | The values for many persons |
### PhoneCall
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of interaction |
| `id` | `integer<int64>` | Yes | The phone call's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `startTime` | `string<date-time>` | Yes | The call start time |
| `attendees` | `array<object>` ([Attendee](#attendee)) | Yes | People attending the call |
### RankedDropdown
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown item text |
| `rank` | `integer<int64>` | Yes | Dropdown item rank (Constraints: ≥ 0; ≤ 9007199254740991) |
| `color` | `string/null` | Yes | Dropdown item color |
### RankedDropdownFilter
Filter for ranked-dropdown fields
**Variant:** [RankedDropdownFilterMultiValues](#rankeddropdownfiltermultivalues)
**Variant:** [RankedDropdownFilterNoValue](#rankeddropdownfilternovalue)
### RankedDropdownFilterMultiValues
Filter for ranked-dropdown fields matching against one or more ranked dropdown options
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-any-of`, `is-none-of`)` | Yes | The filter operator |
| `value` | `array<object> (≤ 100 items, ≥ 1 items)` ([RankedDropdownReference](#rankeddropdownreference)) | Yes | One or more ranked dropdown options to match against |
### RankedDropdownFilterNoValue
Filter for ranked-dropdown fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
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
| `data` | [RankedDropdown](#rankeddropdown) \| `null` | Yes |  |
### RankedDropdownValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `array<object> (≤ 100 items)` ([RankedDropdown](#rankeddropdown)) | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### RankedDropdownValueUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | `null` \| [RankedDropdownReference](#rankeddropdownreference) | Yes |  |
### RateLimit
Rate limit usage for the authenticated caller. Contains one or two windows depending on the caller's quota configuration: `callerPerMinute` is always present (per-caller minute limit); `orgPerMonth` is present only for callers whose org has a bounded monthly quota (DEVELOPER keys and OAuth apps on capped plans). Absence of `orgPerMonth` indicates no monthly quota applies.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `callerPerMinute` | `object` ([RateLimitWindow](#ratelimitwindow)) | Yes | Rate limit window for per-caller requests within a one-minute period. |
| `orgPerMonth` | `object` ([RateLimitWindow](#ratelimitwindow)) | No | Rate limit window for monthly aggregate requests. Only present for callers with a monthly quota; omitted for API key types without monthly limits. |
### RateLimitError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### RateLimitWindow
A rate limit window with current usage and reset time. Each window tracks requests made within a specific time period (e.g., per minute or per month). The four fields are always present together and represent the same metrics tracked in x-ratelimit-* response headers.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `limit` | `integer<int64>` | Yes | The maximum number of requests allowed in this window. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `remaining` | `integer<int64>` | Yes | The number of requests still available before hitting the limit in this window. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `reset` | `integer<int64>` | Yes | Time in seconds until this window resets. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `used` | `integer<int64>` | Yes | The number of requests already consumed in this window. (Constraints: ≥ 0; ≤ 9007199254740991) |
### Relationship
Represents a relationship between two persons, including the interaction score that measures the strength of their connection based on communication patterns.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `person1` | `object` ([RelationshipPerson](#relationshipperson)) | Yes | The first person in this relationship |
| `person2` | `object` ([RelationshipPerson](#relationshipperson)) | Yes | The second person in this relationship |
| `interactionScore` | `number<double>` | Yes | A score between 0.0 and 1.0 representing the strength of the relationship based on communication patterns such as emails, meetings, and other interactions. Higher scores indicate stronger relationships. (Constraints: ≥ 0; ≤ 1) |
| `linkedIn` | [RelationshipLinkedIn](#relationshiplinkedin) \| `null` | Yes | LinkedIn connection details for these two persons. Present whenever a LinkedIn connection exists between them, regardless of whether this relationship was derived from interaction data or the LinkedIn connection itself. `null` when no LinkedIn connection exists. |
### RelationshipLinkedIn
LinkedIn connection details for the two persons in a relationship.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `connectedOn` | `string<date>` | Yes | The date the LinkedIn connection was established. |
### RelationshipPerson
A person involved in a relationship, including basic identifying information.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The person's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
### RelationshipsPaged
A paginated list of relationships
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Relationship](#relationship)) | Yes | A page of Relationship objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### RelativeDate
A single relative duration, specifying an amount and unit
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `amount` | `integer<int32>` | Yes | The number of units (Constraints: ≥ 0; ≤ 2147483647) |
| `unit` | `string (enum: `minute`, `hour`, `day`, `week`, `month`, …)` | Yes | The time unit for the duration |
### RelativeDateRange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `amount` | `array<integer<int32>> (≤ 2 items, ≥ 2 items)` | Yes | The start and end of the range in units, in that order (e.g. `[7, 30]` with unit `day` means between 7 and 30 days). |
| `unit` | `string (enum: `minute`, `hour`, `day`, `week`, `month`, …)` | Yes | The unit for the relative date filter |
### RelativeDates
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `amount` | `array<integer<int32>> (≤ 2 items, ≥ 1 items)` | Yes | The number of units for the relative date window. Provide one value (e.g. `[30]` means 30 days). For a range, provide two values where the first is the start offset and the second is the end offset from today (e.g. `[7, 30]` means between 7 and 30 days ago). |
| `unit` | `string (enum: `minute`, `hour`, `day`, `week`, `month`, …)` | Yes | The unit for the relative date filter |
### ReminderData
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string (enum: `one-time`, `recurring`)` | Yes | The type of reminder |
| `content` | `string/null` | Yes | Free-form text attached to the reminder |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due |
### ReminderValue
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `data` | [ReminderData](#reminderdata) \| `null` | Yes | The entity's next uncompleted reminder. `null` when the entity has no uncompleted reminder, or when the reminder is not visible to the requesting user. |
### SavedView
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The saved view's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The saved view's name |
| `type` | `string (enum: `sheet`, `board`, `dashboard`)` | Yes | The type for this saved view |
| `createdAt` | `string<date-time>` | Yes | The date that the saved view was created |
### SavedViewPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([SavedView](#savedview)) | Yes | A page of SavedView results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### SearchCriteria
Search criteria for filtering, sorting, and searching. All fields are optional  omitting the body returns all results with default pagination.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `filters` | `object` ([FilterGroup](#filtergroup)) | No | A tree of filter conditions to apply. Supports nested AND/OR grouping. Use the relevant fields endpoint for your resource type to discover available fields, their `valueType`, and supported operators. |
| `sorts` | `array<object> (≤ 5 items, ≥ 1 items)` ([SearchSort](#searchsort)) | No | One or more sort criteria, applied in order. Supports up to 5 sort items. Use the relevant fields endpoint for your resource type to discover sortable fields. |
| `search` | `object` ([SearchTerm](#searchterm)) | No | An optional keyword to match against field values. Results must satisfy both the search term AND any provided filters (intersection). Only one search object may be provided. The term is always matched against the entity name and primary identifier; providing `fieldIds` extends the search to additional fields rather than replacing the identity match. |
### SearchSort
A single sort criterion. Up to 5 sorts may be specified and are applied in order. Use the relevant fields endpoint for your resource type to discover sortable fields and valid `attributeId` values.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fieldId` | `string` | Yes | The ID of the field to sort on (Constraints: length ≥ 1) |
| `attributeId` | `string` | No | The ID of the attribute to sort on. Required for some fields such as relationship intelligence fields. Use the relevant fields endpoint for your resource type to discover which fields require an `attributeId` and what values are valid. (Constraints: length ≥ 1) |
| `direction` | `string (enum: `asc`, `desc`)` | Yes | The sort direction |
### SearchTerm
A single keyword or phrase to match against field values. Multiple terms or comma-separated values are not supported; use a single search string.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `term` | `string` | Yes | The text to search for. Minimum 3 characters. (Constraints: length ≥ 3) |
| `fieldIds` | `array<string> (≤ 100 items, ≥ 1 items)` | No | The IDs of additional fields to match the term against, extending the default identity search. Use the relevant fields endpoint for your resource type to discover available field IDs. Supports up to 100 field IDs.  Fields with a `valueType` of `datetime` are not searchable and are silently ignored if included. |
### SemanticSearchCriteria
Semantic search criteria including search prompt and entity type
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search prompt to apply. (Constraints: length ≥ 1; length ≤ 500) |
| `limit` | `integer<int32>` | No | Number of items to include in the response. (Constraints: ≥ 1; ≤ 100; default `100`) |
| `entityType` | `string` | No | The type of entity to search for. |
| `listIds` | `array<integer<int64>> (≤ 100 items)` | No | The IDs of the lists to filter results by. |
### SemanticSearchResult
Includes the list of entities that matched the search prompt and the explanation for the search.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([companies.SemanticSearchCompany](#companiessemanticsearchcompany)) | Yes | The list of entities that matched the search prompt |
| `entityType` | `string` | Yes | The type of entity that was searched. |
| `explanation` | `string` | Yes |  |
### ServerError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
### Team
A Team. Opt-in properties are controlled by the `includes` query parameter.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `membersPreview` | `object` ([TeamMembersPreview](#teammemberspreview)) | No | Preview of the team's members. Only included when `membersPreview` is requested via the `includes` query parameter. `totalCount` is the total number of members on the team; full data is available via the paginated endpoint `GET /v2/teams/{teamId}/members`. |
| `accessibleListsPreview` | `object` ([TeamAccessibleListsPreview](#teamaccessiblelistspreview)) | No | Preview of the Lists this team has access to. Only included when `accessibleListsPreview` is requested via the `includes` query parameter. `totalCount` is the total number of Lists this team can access; full data is available via the paginated endpoint `GET /v2/teams/{teamId}/accessible-lists`. |
| `id` | `integer<int64>` | Yes | The unique identifier for the team (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the team |
| `privacyType` | `string (enum: `share-subjects-bodies`, `share-subjects`, `hide-subjects-bodies`, `no-access`)` | No | Visibility policy applied to interactions belonging to this team's members. `share-subjects-bodies` exposes all interactions; `share-subjects` exposes a selective subset; `hide-subjects-bodies` hides interaction content but exposes metadata; `no-access` exposes no interactions. Only returned when the caller has the "Manage Teams" [permission](https://developer.affinity.co/pages/external-api-v2/permissions), the organization has team-based privacy controls enabled, and cross-team visibility is enabled for the organization; omitted from the response otherwise. |
| `createdAt` | `string<date-time>` | Yes | Timestamp when the team was created |
| `updatedAt` | `string/null<date-time>` | Yes | Timestamp when the team was last updated, or null if never updated |
### TeamAccessibleListsPreview
Preview of the Lists this team has access to. Only included when `accessibleListsPreview` is requested via the `includes` query parameter. `totalCount` is the total number of Lists this team can access; full data is available via the paginated endpoint `GET /v2/teams/{teamId}/accessible-lists`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int32>` | Yes | Total number of Lists this team can access (Constraints: ≥ 0; ≤ 2147483647) |
| `data` | `array<object> (≤ 10 items)` ([ListWithType](#listwithtype)) | Yes | A preview of the Lists this team can access |
### TeamBase
Base properties shared by all Team representations.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for the team (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the team |
| `privacyType` | `string (enum: `share-subjects-bodies`, `share-subjects`, `hide-subjects-bodies`, `no-access`)` | No | Visibility policy applied to interactions belonging to this team's members. `share-subjects-bodies` exposes all interactions; `share-subjects` exposes a selective subset; `hide-subjects-bodies` hides interaction content but exposes metadata; `no-access` exposes no interactions. Only returned when the caller has the "Manage Teams" [permission](https://developer.affinity.co/pages/external-api-v2/permissions), the organization has team-based privacy controls enabled, and cross-team visibility is enabled for the organization; omitted from the response otherwise. |
| `createdAt` | `string<date-time>` | Yes | Timestamp when the team was created |
| `updatedAt` | `string/null<date-time>` | Yes | Timestamp when the team was last updated, or null if never updated |
### TeamMember
A single member of a team
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier for this team membership (Constraints: ≥ 1; ≤ 9007199254740991) |
| `user` | `object` ([User](#user)) | Yes |  |
| `privacyType` | `string (enum: `share-subjects-bodies`, `share-subjects`, `hide-subjects-bodies`)` | No | Per-member privacy override controlling visibility of this member's interactions. Only returned when the caller has the "Manage Teams" [permission](https://developer.affinity.co/pages/external-api-v2/permissions) and the organization has team-based privacy controls enabled; omitted from the response otherwise. |
| `addedAt` | `string<date-time>` | Yes | Timestamp when the user was added to the team |
### TeamMembersPreview
Preview of the team's members. Only included when `membersPreview` is requested via the `includes` query parameter. `totalCount` is the total number of members on the team; full data is available via the paginated endpoint `GET /v2/teams/{teamId}/members`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `totalCount` | `integer<int32>` | Yes | Total number of members on the team (Constraints: ≥ 0; ≤ 2147483647) |
| `data` | `array<object> (≤ 10 items)` ([TeamMember](#teammember)) | Yes | A preview of the team's members |
### TeamPaged
A page of Teams
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Team](#team)) | Yes | A page of Team results |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### Tenant
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The tenant's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The name of the tenant |
| `subdomain` | `string<hostname>` | Yes | The tenant's subdomain under affinity.co |
### TextFilter
Filter for free-text fields
**Variant:** [TextFilterOneValue](#textfilteronevalue)
**Variant:** [TextFilterNoValue](#textfilternovalue)
### TextFilterNoValue
Filter for free-text fields based on presence or absence of a value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `is-empty`, `is-not-empty`)` | Yes | The filter operator |
### TextFilterOneValue
Filter for free-text fields using a string match against a single value
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `valueType` | `string` | Yes | The type of the field value |
| `fieldId` | `string` | Yes | The ID of the field to filter on |
| `attributeId` | `string` | No | The ID of the attribute to filter on. Required for some fields such as relationship intelligence fields. Use `GET /v2/lists/{listId}/fields?includes=filterability` to discover which fields require an `attributeId` and what values are valid. |
| `operator` | `string (enum: `contains`, `does-not-contain`, `starts-with`, `ends-with`)` | Yes | The filter operator |
| `value` | `string` | Yes | The text string to match against |
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
| `totalCount` | `integer<int32>` | No | The total number of values for this field. When `totalCount` exceeds the length of `data`, additional values can be retrieved using the field values endpoint. (Constraints: ≥ 0; ≤ 2147483647) |
### TextsValuePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string (enum: `filterable-text`, `filterable-text-multi`)` | Yes | The type of value |
| `data` | `array<string> (≤ 100 items)` | Yes | A page of values for this field |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### TimeoutError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
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
### UserData
An internal user in your organization, including their name, primary email address, all email addresses, photo URL, account status, and account role.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The user's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `firstName` | `string` | Yes | The user's first name |
| `lastName` | `string/null` | Yes | The user's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The user's primary email address |
| `emailAddresses` | `array<string<email>> (≤ 100 items)` | No | All of the user's email addresses. Only returned when the authenticated user has the "Manage Users" [permission](https://developer.affinity.co/pages/external-api-v2/permissions). |
| `photoUrl` | `string/null<uri>` | Yes | URL of the user's profile photo |
| `status` | `string (enum: `active`, `invited`, `deactivated`)` | Yes | The user's account status. - `active`: the user can sign in and use Affinity. - `invited`: the user has been invited to the product but has not yet accepted   the invitation and thus cannot have taken any actions. - `deactivated`: the user was once active but has been deactivated and can no   longer use the product. |
| `role` | `string` | No | The user's account role. Only returned when the authenticated user has the "Manage Users" [permission](https://developer.affinity.co/pages/external-api-v2/permissions). |
### UserDataPaged
A paginated list of Users
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([UserData](#userdata)) | Yes | A page of UserData results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### ValidationError
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `code` | `string` | Yes | Error code |
| `message` | `string` | Yes | Error message |
| `param` | `string` | Yes | Param the error refers to |
### ValueFilter
A filter applied to a single field value. The `valueType` determines which filter variant applies and what operators and `value` shapes are valid.
Each filter requires `fieldId`, `valueType`, and `operator`. The `value` field is required for most operators and absent for `is-empty` and `is-not-empty`. Some fields also require an `attributeId`  use the relevant fields endpoint for your resource type to discover available fields, their `valueType`, supported operators, and required `attributeId` values.
**Variant:** [CompanyFilter](#companyfilter)
**Variant:** [CompaniesFilter](#companiesfilter)
**Variant:** [PersonFilter](#personfilter)
**Variant:** [PersonsFilter](#personsfilter)
**Variant:** [DropdownFilter](#dropdownfilter)
**Variant:** [DropdownsFilter](#dropdownsfilter)
**Variant:** [RankedDropdownFilter](#rankeddropdownfilter)
**Variant:** [DateFilter](#datefilter)
**Variant:** [NumberFilter](#numberfilter)
**Variant:** [FilterableTextFilter](#filterabletextfilter)
**Variant:** [FilterableTextsFilter](#filterabletextsfilter)
**Variant:** [TextFilter](#textfilter)
**Variant:** [LocationFilter](#locationfilter)
**Variant:** [LocationsFilter](#locationsfilter)
**Variant:** [ListsFilter](#listsfilter)
### WhoAmI
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `tenant` | `object` ([Tenant](#tenant)) | Yes |  |
| `user` | `object` ([User](#user)) | Yes |  |
| `grant` | `object` ([Grant](#grant)) | Yes |  |
### companies.SemanticSearchCompany
Semantic Search Company result
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
| `domains` | `array<string<hostname>> (≤ 100 items)` | Yes | All of the company's domains |
| `isGlobal` | `boolean` | Yes | Whether or not the company is tenant specific |
| `score` | `string` | Yes | The calculated relevance score for the company against the search prompt. |
### dropdownOptions.DropdownOption
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
### dropdownOptions.DropdownOptionToBeCreated
**Variant:** [dropdownOptions.StandardDropdownOptionToBeCreated](#dropdownoptionsstandarddropdownoptiontobecreated)
**Variant:** [dropdownOptions.RankedDropdownOptionToBeCreated](#dropdownoptionsrankeddropdownoptiontobecreated)
**Variant:** [dropdownOptions.StatusDropdownOptionToBeCreated](#dropdownoptionsstatusdropdownoptiontobecreated)
### dropdownOptions.DropdownOptionToBeUpdated
- `dropdown` type field may update `text`.
- `ranked-dropdown` type field may update `text`, `rank`, and/or `color`.
- `status-dropdown` type field may update `text`, `rank`, `color`, `statusCategory`, and/or `winRate`.
**Variant:** [dropdownOptions.StandardDropdownOptionToBeUpdated](#dropdownoptionsstandarddropdownoptiontobeupdated)
**Variant:** [dropdownOptions.RankedDropdownOptionToBeUpdated](#dropdownoptionsrankeddropdownoptiontobeupdated)
**Variant:** [dropdownOptions.StatusDropdownOptionToBeUpdated](#dropdownoptionsstatusdropdownoptiontobeupdated)
### dropdownOptions.RankedDropdownOption
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string/null (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
### dropdownOptions.RankedDropdownOptionToBeCreated
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `text` | `string` | Yes | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
### dropdownOptions.RankedDropdownOptionToBeUpdated
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | No | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | No | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | No | Dropdown option color |
### dropdownOptions.StandardDropdownOptionToBeCreated
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `text` | `string` | Yes | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
### dropdownOptions.StandardDropdownOptionToBeUpdated
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | No | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
### dropdownOptions.StatusDropdownOption
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string/null (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | Yes | Dropdown option's status category |
| `winRate` | `integer/null<int32>` | Yes | The user-designated probability that an entity in this status will progress to a `won` status. Only set on options whose `statusCategory` is `open`; null otherwise. (Constraints: ≥ 0; ≤ 100) |
| `id` | `integer<int64>` | Yes | Dropdown option's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown option text |
### dropdownOptions.StatusDropdownOptionToBeCreated
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of dropdown option |
| `text` | `string` | Yes | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | Yes | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | Yes | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | Yes | Dropdown option's status category |
| `winRate` | `integer<int32>` | No | The user-designated probability that an entity in this status will progress to a `won` status. Only valid when `statusCategory` is `open`. Must be an integer between 0 and 100 inclusive. (Constraints: ≥ 0; ≤ 100) |
### dropdownOptions.StatusDropdownOptionToBeUpdated
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `text` | `string` | No | Dropdown option text (Constraints: length ≥ 1; length ≤ 255) |
| `rank` | `integer<int32>` | No | Dropdown option rank (sort order) (Constraints: ≥ 0; ≤ 2147483647) |
| `color` | `string (enum: `white`, `gray`, `blue`, `green`, `purple`, …)` | No | Dropdown option color |
| `statusCategory` | `string (enum: `open`, `won`, `lost`, `on-hold`)` | No | Dropdown option's status category |
| `winRate` | `integer<int32>` | No | The user-designated probability that an entity in this status will progress to a `won` status. Only valid when `statusCategory` is `open`. Must be an integer between 0 and 100 inclusive. (Constraints: ≥ 0; ≤ 100) |
### fieldValueChanges.CompanyEntityData
A live company reference in the context of a field value change.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `referenceType` | `string` | Yes | Indicates this is a live entity reference |
| `id` | `integer<int64>` | Yes | The company's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `name` | `string` | Yes | The company's name |
| `domain` | `string/null<hostname>` | Yes | The company's primary domain |
### fieldValueChanges.CompanyMultiValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.CompanyEntityData](#fieldvaluechangescompanyentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The company value. When the company has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.CompanyValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.CompanyEntityData](#fieldvaluechangescompanyentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The company value. When the company has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.DatetimeValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `string<date-time>` | Yes | The datetime value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.DeletedEntityReference
A fallback representation used when the referenced entity (person, company, dropdown option, or ranked-dropdown option) has been deleted from Affinity after the change was recorded. The `displayValue` is a text snapshot captured at the time the change occurred.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `referenceType` | `string` | Yes | Indicates this is a deleted entity reference |
| `displayValue` | `string` | Yes | Text representation of the referenced entity at the time the change was recorded |
### fieldValueChanges.DropdownEntityData
A live dropdown option reference in the context of a field value change.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `referenceType` | `string` | Yes | Indicates this is a live entity reference |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown item text |
### fieldValueChanges.DropdownMultiValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.DropdownEntityData](#fieldvaluechangesdropdownentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The dropdown option value. When the dropdown option has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.DropdownValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.DropdownEntityData](#fieldvaluechangesdropdownentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The dropdown option value. When the dropdown option has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.EntityReference
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The entity's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
### fieldValueChanges.Field
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The unique identifier of the field |
| `entityType` | `string (enum: `person`, `company`, `opportunity`)` | Yes | The type of entity this field belongs to |
| `name` | `string` | Yes | The name of the field |
| `type` | `string (enum: `global`, `list`)` | Yes | Whether this field is global or list-specific |
### fieldValueChanges.FieldValueChange
**Variant:** [fieldValueChanges.CompanyValueChange](#fieldvaluechangescompanyvaluechange)
**Variant:** [fieldValueChanges.CompanyMultiValueChange](#fieldvaluechangescompanymultivaluechange)
**Variant:** [fieldValueChanges.DatetimeValueChange](#fieldvaluechangesdatetimevaluechange)
**Variant:** [fieldValueChanges.DropdownValueChange](#fieldvaluechangesdropdownvaluechange)
**Variant:** [fieldValueChanges.DropdownMultiValueChange](#fieldvaluechangesdropdownmultivaluechange)
**Variant:** [fieldValueChanges.FilterableTextValueChange](#fieldvaluechangesfilterabletextvaluechange)
**Variant:** [fieldValueChanges.FilterableTextMultiValueChange](#fieldvaluechangesfilterabletextmultivaluechange)
**Variant:** [fieldValueChanges.LocationValueChange](#fieldvaluechangeslocationvaluechange)
**Variant:** [fieldValueChanges.LocationMultiValueChange](#fieldvaluechangeslocationmultivaluechange)
**Variant:** [fieldValueChanges.NumberValueChange](#fieldvaluechangesnumbervaluechange)
**Variant:** [fieldValueChanges.NumberMultiValueChange](#fieldvaluechangesnumbermultivaluechange)
**Variant:** [fieldValueChanges.PersonValueChange](#fieldvaluechangespersonvaluechange)
**Variant:** [fieldValueChanges.PersonMultiValueChange](#fieldvaluechangespersonmultivaluechange)
**Variant:** [fieldValueChanges.RankedDropdownValueChange](#fieldvaluechangesrankeddropdownvaluechange)
**Variant:** [fieldValueChanges.TextValueChange](#fieldvaluechangestextvaluechange)
### fieldValueChanges.FieldValueChangeBase
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.FieldValueChangePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([fieldValueChanges.FieldValueChange](#fieldvaluechangesfieldvaluechange)) | Yes | The field value changes for this page |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### fieldValueChanges.FilterableTextMultiValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `string` | Yes | The filterable text value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.FilterableTextValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `string` | Yes | The filterable text value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.ListEntry
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The list entry's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `listId` | `integer<int64>` | Yes | The ID of the list that this list entry belongs to (Constraints: ≥ 1; ≤ 9007199254740991) |
### fieldValueChanges.LocationMultiValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `object` ([Location](#location)) | Yes | The location value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.LocationValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `object` ([Location](#location)) | Yes | The location value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.NumberMultiValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `number<double>` | Yes | The number value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.NumberValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `number<double>` | Yes | The number value. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.PersonEntityData
A live person reference in the context of a field value change.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `referenceType` | `string` | Yes | Indicates this is a live entity reference |
| `id` | `integer<int64>` | Yes | The person's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `firstName` | `string/null` | Yes | The person's first name |
| `lastName` | `string/null` | Yes | The person's last name |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address |
| `type` | `string (enum: `internal`, `collaborator`, `external`)` | Yes | The person's type. `internal` - people who are users within your Affinity instance. `collaborator` - individuals outside of your company who have read-only access to specified Affinity list views and stay updated on your firm's activities. `external` - people who are not internal nor collaborators. |
### fieldValueChanges.PersonMultiValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.PersonEntityData](#fieldvaluechangespersonentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The person value. When the person has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.PersonValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.PersonEntityData](#fieldvaluechangespersonentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The person value. When the person has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.RankedDropdownEntityData
A live ranked dropdown option reference in the context of a field value change.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `referenceType` | `string` | Yes | Indicates this is a live entity reference |
| `dropdownOptionId` | `integer<int64>` | Yes | Dropdown item's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `text` | `string` | Yes | Dropdown item text |
| `rank` | `integer<int64>` | Yes | Dropdown item rank (Constraints: ≥ 0; ≤ 9007199254740991) |
| `color` | `string/null` | Yes | Dropdown item color |
### fieldValueChanges.RankedDropdownValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | [fieldValueChanges.RankedDropdownEntityData](#fieldvaluechangesrankeddropdownentitydata) \| [fieldValueChanges.DeletedEntityReference](#fieldvaluechangesdeletedentityreference) | Yes | The ranked dropdown option value. When the dropdown option has been deleted from Affinity after the change was recorded, a `DeletedEntityReference` with a `displayValue` snapshot is returned instead. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fieldValueChanges.TextValueChange
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of value |
| `value` | `string` | Yes | The text value. Values longer than 2 000 characters may be truncated due to infrastructure limits. |
| `id` | `integer<int64>` | Yes | The unique identifier of this field value change record (Constraints: ≥ 1; ≤ 9007199254740991) |
| `field` | `object` ([fieldValueChanges.Field](#fieldvaluechangesfield)) | Yes | The field whose value changed. |
| `entity` | `object` ([fieldValueChanges.EntityReference](#fieldvaluechangesentityreference)) | Yes | The entity that the field value change occurred in. |
| `listEntry` | [fieldValueChanges.ListEntry](#fieldvaluechangeslistentry) \| `null` | Yes | The list entry that the field value change occurred in. |
| `changer` | [User](#user) \| `null` | Yes | The user who made this change. `null` for system-generated changes (e.g. enrichment updates). |
| `changedAt` | `string<date-time>` | Yes | When the field value change occurred |
| `actionType` | `string (enum: `add`, `update`, `delete`)` | Yes | The type of change. `add`  a value was set for the first time or added to a multi-value field. `update`  an existing single-value field was changed. `delete`  a value was cleared or removed from a multi-value field. Multi-value field types (`person-multi`, `company-multi`, `dropdown-multi`, `number-multi`, `location-multi`, `filterable-text-multi`) only produce `add` or `delete` actions; they never produce `update`. |
### fields.FieldUpdate
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | The field's unique identifier. |
| `value` | [CompaniesValueUpdate](#companiesvalueupdate) \| [CompanyValueUpdate](#companyvalueupdate) \| [DateValue](#datevalue) \| [DropdownValueUpdate](#dropdownvalueupdate) \| [DropdownsValueUpdate](#dropdownsvalueupdate) \| [FloatValue](#floatvalue) \| [FloatsValue](#floatsvalue) \| [LocationValue](#locationvalue) \| [LocationsValue](#locationsvalue) \| [PersonValueUpdate](#personvalueupdate) \| [PersonsValueUpdate](#personsvalueupdate) \| [RankedDropdownValueUpdate](#rankeddropdownvalueupdate) \| [TextValue](#textvalue) \| [TextsValue](#textsvalue) | Yes |  |
### files.File
A file uploaded to a company, person, opportunity, or the organization directly.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `downloadUrl` | `string<uri>` | Yes | A temporary signed URL to download the file's contents. Expires 60 seconds after the response is generated. |
| `id` | `integer<int32>` | Yes | The file's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `name` | `string` | Yes | The file's name, including its extension. |
| `size` | `integer<int64>` | Yes | The file's size in bytes. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `type` | `string/null` | Yes | The file's MIME content type. `null` when the content type is not recorded. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who uploaded the file. `null` when the uploader is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the file was uploaded. |
| `updatedAt` | `string/null<date-time>` | Yes | When the file was last updated. `null` if the file has never been updated. |
### files.FileBase
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The file's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `name` | `string` | Yes | The file's name, including its extension. |
| `size` | `integer<int64>` | Yes | The file's size in bytes. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `type` | `string/null` | Yes | The file's MIME content type. `null` when the content type is not recorded. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who uploaded the file. `null` when the uploader is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the file was uploaded. |
| `updatedAt` | `string/null<date-time>` | Yes | When the file was last updated. `null` if the file has never been updated. |
### files.FileSummary
A file uploaded to a company, person, opportunity, or the organization directly. Use Get a single File to obtain a download URL.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The file's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `name` | `string` | Yes | The file's name, including its extension. |
| `size` | `integer<int64>` | Yes | The file's size in bytes. (Constraints: ≥ 0; ≤ 9007199254740991) |
| `type` | `string/null` | Yes | The file's MIME content type. `null` when the content type is not recorded. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who uploaded the file. `null` when the uploader is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the file was uploaded. |
| `updatedAt` | `string/null<date-time>` | Yes | When the file was last updated. `null` if the file has never been updated. |
### files.FileSummaryPaged
A page of FileSummary objects.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([files.FileSummary](#filesfilesummary)) | Yes | A page of FileSummary objects. |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### files.KeywordSearchCriteria
**Variant:** File Keyword Search Criteria (org-wide or by file IDs)
Search all files in the org, or limit to specific file IDs.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` files ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `fileIds` | `array<integer<int32>> (≤ 100 items)` | No | Limit search to these specific files. Omit for org-wide search. |
| `limit` | `integer<int32>` | No | Maximum number of files to return. (Constraints: ≥ 1; ≤ 100; default `20`) |
**Variant:** File Keyword Search Criteria (by company)
Search files associated with a specific company.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` files ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `companyId` | `integer<int64>` | No | Restrict search to files associated with this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `limit` | `integer<int32>` | No | Maximum number of files to return. (Constraints: ≥ 1; ≤ 100; default `20`) |
### files.KeywordSearchResult
Results of a keyword search over files.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([files.SearchResult](#filessearchresult)) | Yes | Matching file results, one per file, ordered by relevance. |
### files.SearchResult
A matched file and a matching passage. Each file appears at most once per response, regardless of how many passages matched.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `file` | `object` | Yes | The matched file. |
| `pageNumber` | `integer/null<int32>` | Yes | The page where this passage was found. Null for files without page structure. (Constraints: ≥ 1; ≤ 10000) |
| `preview` | `string` | Yes | The matching passage, up to 2,000 characters. (Constraints: length ≤ 2000) |

**`file` details** — The matched file.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The file's unique identifier. (Constraints: ≥ 1; ≤ 2147483647) |
| `name` | `string` | Yes | The file name. |
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
| `creator` | [Attendee](#attendee) \| `null` | Yes | The person who created the call |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the call was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the call was updated |
| `attendeesPreview` | `object` ([AttendeesPreview](#attendeespreview)) | Yes | A preview of the attendees in the call |
### interactions.CallPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([interactions.Call](#interactionscall)) | Yes | A page of Call results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### interactions.ChatMessage
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The chat message's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the chat message was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, chat messages can only be logged as 'manual'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the chat message |
| `creator` | `object` ([PersonData](#persondata)) | Yes | The creator of the chat message |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the chat message was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the chat message was updated |
| `participantsPreview` | `object` ([PersonDataPreview](#persondatapreview)) | Yes | A preview of the participants who are in the chat message |
### interactions.ChatMessagePaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([interactions.ChatMessage](#chatmessage)) | Yes | A page of ChatMessage results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### interactions.Email
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The email's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `sentAt` | `string<date-time>` | Yes | The timestamp of when the email was sent |
| `loggingType` | `string` | Yes | Indicates how the interaction was added to Affinity: either manually by a user ('manual') or automatically through Affinity's capture process ('automated'). Currently, emails can only be logged as 'automated'. |
| `direction` | `string (enum: `sent`, `received`)` | Yes | The direction of the email: 'sent' if the email was sent by an internal user and  'received' if the email was sent to an internal user. |
| `subject` | `string/null` | Yes | The email's subject. If the authenticated user does not have permission to see the subject, it is obfuscated and returned as `********` rather than the actual subject line. |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the email was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the email was updated |
| `from` | `object` ([Attendee](#attendee)) | Yes | The participant who sent the email |
| `toParticipantsPreview` | `object` ([AttendeesPreview](#attendeespreview)) | Yes | A preview of the participants in the 'To' field of the email |
| `ccParticipantsPreview` | `object` ([AttendeesPreview](#attendeespreview)) | Yes | A preview of the participants who are cc'ed in the email |
### interactions.EmailPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([interactions.Email](#email)) | Yes | A page of Email results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
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
| `creator` | [Attendee](#attendee) \| `null` | Yes | The person who created the meeting |
| `organizer` | [Attendee](#attendee) \| `null` | Yes | The person who organized the meeting |
| `createdAt` | `string<date-time>` | Yes | The timestamp of when the meeting was created |
| `updatedAt` | `string/null<date-time>` | Yes | The timestamp of when the meeting was updated |
| `attendeesPreview` | `object` ([AttendeesPreview](#attendeespreview)) | Yes | A preview of the attendees in the meeting |
### interactions.MeetingPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([interactions.Meeting](#meeting)) | Yes | A page of Meeting results |
| `pagination` | `object` ([Pagination](#pagination-4)) | Yes |  |
### notes.AiNotetakerReplyNote
A reply to a Note, created by an AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` ([notes.MeetingInteraction](#notesmeetinginteraction)) | No | The meeting this AI Notetaker was invited to. |
| `transcriptId` | `integer/null<int32>` | Yes | The id of the transcript of the AI notetaker reply note, or `null` when the org does not retain transcripts or the transcript was deleted. (Constraints: ≥ 1; ≤ 2147483647) |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |
### notes.AiNotetakerRootNote
A Root Note object created by the AI Notetaker
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | `object` ([notes.MeetingInteraction](#notesmeetinginteraction)) | No | The meeting this AI Notetaker was invited to. |
| `transcriptId` | `integer/null<int32>` | Yes | The id of the transcript of the AI notetaker note, or `null` when the org does not retain transcripts or the transcript was deleted. (Constraints: ≥ 1; ≤ 2147483647) |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
### notes.BaseNote
A note's content, creator, mentions, and timestamps.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
### notes.BaseReply
An abstract base class for note replies, either of a UserNoteReply or AiNotetakerNoteReply
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |
### notes.BaseRootNote
A root note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
### notes.CallInteraction
This is a Call (Event) object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Call (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.CallReference
A reference to an existing Call that the note will be attached to. This schema describes the request-body shape for attaching a note to a Call. It does not create or modify the Call itself.
The id of the call. This is the same identifier returned as `interaction.id` on the read response and by `GET /v2/calls`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Call to attach the note to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The interaction type. Must be `call` to reference a Call. |
### notes.ChatMessageInteraction
A ChatMessage object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the ChatMessage (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.ChatMessageReference
A reference to an existing Chat Message (e.g. a message from a connected chat integration such as Slack) that the note will be attached to. This schema describes the request-body shape for attaching a note to a Chat Message. It does not create or modify the Chat Message itself.
The id of the chat message. This is the same identifier returned as `interaction.id` on the read response and by `GET /v2/chat-messages`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Chat Message to attach the note to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The interaction type. Must be `chat-message` to reference a Chat Message. |
### notes.CompaniesPreview
A preview for Companies directly attached to the Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([CompanyData](#companydata)) | No | Preview of Companies directly attached to the Note |
| `totalCount` | `integer<int64>` | No | The total count of Companies directly attached to the Note (Constraints: ≥ 0; ≤ 9007199254740991) |
### notes.Content
A note content
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string/null` | Yes | The HTML content of the note |
### notes.ContentToBeSaved
The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `html` | `string` | Yes | The HTML content of the note.  **Allowed tags (with no attributes other than those explicitly noted):** `<p>`, `<br>`, `<strong>`, `<em>`, `<u>`, `<ol>`, `<ul>`, `<li>`, `<span>` (no attributes), `<a>` (only `href` with `http`, `https`, or `mailto` URL schemes).  **Restricted (any of these will cause the request to fail):** inline `style` attributes, `class` attributes, and the `img`, `script`, `iframe`, `style`, `blockquote`, `hr`, `s`, `pre`, `code`, `font` tags.  **Mentions:** mention spans (`<span data-type="note-mention" ...>`) are also restricted. Mentions cannot be created or modified through this endpoint.  **Anchor tag normalization:** For security, the server appends `rel="noopener noreferrer"` and `target="_blank"` to every `<a>` element before the note is saved.  **Valid examples:** `<p>Quick recap of the call.</p>`, `<p>Top action items:</p><ul><li><strong>Send pricing</strong> by Friday</li><li>Follow up with <a href="mailto:jane@acme.co">Jane</a></li></ul>`  **Invalid examples (will cause the request to fail):** `<p style="color:red">Hi</p>` (inline style), `<p><img src="https://example.com/x.png"></p>` (image tag), `<p><span data-type="note-mention" data-note-mention-type="person" data-note-mention-person-id="1">John</span></p>` (mention span) |
### notes.EmailInteraction
This is an Email object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Email (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.EntitiesNote
A Note object attached to an entity (Person, Company, Opportunity)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
### notes.EntitiesNoteToBeCreated
Request body for creating a note attached directly to one or more entities. At least one of `persons`, `companies`, or `opportunities` must include an entry, since a note of this type requires at least one attached entity.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The note type. Must be `entities` to create a note attached to only entities. |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | Yes | The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below. |
| `creator` | `object` ([PersonReference](#personreference)) | No | The person to record as the note's creator. Defaults to the calling user when omitted, and must reference an active internal person in your organization. |
| `createdAt` | `string<date-time>` | No | The time to record as when the note was created. Set this to backfill historical notes with their original date. Defaults to the current time when omitted. |
| `persons` | `array<object> (≤ 100 items)` ([PersonReference](#personreference)) | No | Persons to attach the note to. Each item references a Person by id. |
| `companies` | `array<object> (≤ 100 items)` ([CompanyReference](#companyreference)) | No | Companies to attach the note to. Each item references a Company by id. |
| `opportunities` | `array<object> (≤ 100 items)` ([OpportunityReference](#opportunityreference)) | No | Opportunities to attach the note to. Each item references an Opportunity by id. |
### notes.Interaction
An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage.
**Variant:** [notes.MeetingInteraction](#notesmeetinginteraction)
**Variant:** [notes.CallInteraction](#notescallinteraction)
**Variant:** [notes.ChatMessageInteraction](#noteschatmessageinteraction)
**Variant:** [notes.EmailInteraction](#notesemailinteraction)
### notes.InteractionNote
A Note object attached to an interaction (Email, Meeting, Call, ChatMessage)
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `interaction` | [notes.MeetingInteraction](#notesmeetinginteraction) \| [notes.CallInteraction](#notescallinteraction) \| [notes.ChatMessageInteraction](#noteschatmessageinteraction) \| [notes.EmailInteraction](#notesemailinteraction) | Yes | An interaction attached to a Note. It can be a Meeting, a Call or an ChatMessage. |
| `repliesCount` | `integer<int32>` | No | The number of replies to this note. This is only included if the `repliesCount` parameter is passed in the `includes` in the request and the note is not a reply itself. (Constraints: ≥ 0; ≤ 2147483647) |
| `opportunitiesPreview` | `object` ([notes.OpportunitiesPreview](#notesopportunitiespreview)) | No | A preview for Opportunities directly attached to the Note |
| `personsPreview` | `object` ([notes.PersonsPreview](#notespersonspreview)) | No | A preview for Persons directly attached to the Note |
| `companiesPreview` | `object` ([notes.CompaniesPreview](#notescompaniespreview)) | No | A preview for Companies directly attached to the Note |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |
### notes.InteractionNoteToBeCreated
Request body for creating a note attached to an interaction. Notes can be attached to a meeting, call, or chat message.
`interaction.type` and `interaction.id` are both required and must reference a meeting, call, or chat message the caller can access. Notes of this type are anchored to a single interaction. Entity associations (`persons`, `companies`, `opportunities`) are optional and can supplement the interaction attachment as additional direct associations on top of the interaction's own participants. The interaction participants are implicitly associated with the note by virtue of the interaction attachment, so they do not need to be included in the `persons` array unless the caller wants to create additional direct associations beyond those implied by the interaction itself.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The note type. Must be `interaction` to create an interaction note. |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | Yes | The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below. |
| `creator` | `object` ([PersonReference](#personreference)) | No | The person to record as the note's creator. Defaults to the calling user when omitted, and must reference an active internal person in your organization. |
| `createdAt` | `string<date-time>` | No | The time to record as when the note was created. Set this to backfill historical notes with their original date. Defaults to the current time when omitted. |
| `interaction` | [notes.MeetingReference](#notesmeetingreference) \| [notes.CallReference](#notescallreference) \| [notes.ChatMessageReference](#noteschatmessagereference) | Yes | A reference to the existing interaction that an interaction note will be attached to. Notes can be attached to a meeting, call, or chat message. |
| `persons` | `array<object> (≤ 100 items)` ([PersonReference](#personreference)) | No | Persons to additionally attach the note to, beyond those implied by the interaction itself. Each item references a Person by id. |
| `companies` | `array<object> (≤ 100 items)` ([CompanyReference](#companyreference)) | No | Companies to additionally attach the note to. Each item references a Company by id. |
| `opportunities` | `array<object> (≤ 100 items)` ([OpportunityReference](#opportunityreference)) | No | Opportunities to additionally attach the note to. Each item references an Opportunity by id. |
### notes.InteractionReference
A reference to the existing interaction that an interaction note will be attached to. Notes can be attached to a meeting, call, or chat message.
**Variant:** [notes.MeetingReference](#notesmeetingreference)
**Variant:** [notes.CallReference](#notescallreference)
**Variant:** [notes.ChatMessageReference](#noteschatmessagereference)
### notes.KeywordSearchCriteria
**Variant:** Note Keyword Search Criteria (org-wide or by note IDs)
Search all notes in the org, or limit to specific note IDs.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` notes ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `noteIds` | `array<integer<int32>> (≤ 100 items)` | No | Limit search to these specific notes. Omit for org-wide search. |
| `limit` | `integer<int32>` | No | Maximum number of notes to return. (Constraints: ≥ 1; ≤ 100; default `20`) |
**Variant:** Note Keyword Search Criteria (by company)
Search notes associated with a specific company.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `prompt` | `string` | Yes | The search query. Returns up to `limit` notes ordered by relevance. Prompts with no strong matches may still return low-relevance results. (Constraints: length ≥ 3; length ≤ 500) |
| `companyId` | `integer<int64>` | No | Restrict search to notes associated with this company. (Constraints: ≥ 1; ≤ 9007199254740991) |
| `limit` | `integer<int32>` | No | Maximum number of notes to return. (Constraints: ≥ 1; ≤ 100; default `20`) |
### notes.KeywordSearchResult
Results of a keyword search over notes.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([notes.SearchResult](#notessearchresult)) | Yes | Matching note results, one per note, ordered by relevance. |
### notes.MeetingInteraction
This is a Meeting (Event) object attached to a note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting (Event) (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The type of the Interaction |
### notes.MeetingReference
A reference to an existing Meeting (calendar event) that the note will be attached to. This schema describes the request-body shape for attaching a note to a Meeting. It does not create or modify the Meeting itself.
The id of the meeting. This is the same identifier returned as `interaction.id` on the read response and by `GET /v2/meetings/{meetingId}`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The id of the Meeting to attach the note to (Constraints: ≥ 1; ≤ 9007199254740991) |
| `type` | `string` | Yes | The interaction type. Must be `meeting` to reference a Meeting. |
### notes.Mention
A mention in a note.
**Variant:** [notes.PersonMention](#notespersonmention)
### notes.Note
**Variant:** [notes.EntitiesNote](#notesentitiesnote)
**Variant:** [notes.InteractionNote](#notesinteractionnote)
**Variant:** [notes.AiNotetakerRootNote](#notesainotetakerrootnote)
**Variant:** [notes.UserReplyNote](#notesuserreplynote)
**Variant:** [notes.AiNotetakerReplyNote](#notesainotetakerreplynote)
### notes.NoteReference
A reference to an existing note by its id.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the referenced note (Constraints: ≥ 1; ≤ 2147483647) |
### notes.NoteToBeCreated
Request body for creating a note. The `type` field selects between three variants:

- `entities`: a note attached directly to one or more Persons, Companies, and/or Opportunities.
- `interaction`: a note attached to a meeting, call, or chat message. May optionally also be associated with additional entities.
- `user-reply`: a reply to an existing root note. Replies have no entity associations or interaction attachment of their own.

Additional notes:

- By default a note is authored by the calling user. To attribute it to another member of your organization, set `creator` to reference that person by id. The referenced person must be an active internal person in your organization.
- By default a note's creation time is the time of the request. To backfill a historical note, set `createdAt` to the time the note should be recorded as created.
- For enterprise customers, the visibility follows the fallback visibility behavior for the organization.
- System-generated note types (`ai-notetaker`, `ai-notetaker-reply`, `email`) cannot be created here.
**Variant:** [notes.EntitiesNoteToBeCreated](#notesentitiesnotetobecreated)
**Variant:** [notes.InteractionNoteToBeCreated](#notesinteractionnotetobecreated)
**Variant:** [notes.UserReplyNoteToBeCreated](#notesuserreplynotetobecreated)
### notes.NoteToBeUpdated
Request body for updating an existing note. All properties are optional: only those explicitly provided are updated, and other properties are left unchanged.

The properties that may be updated depend on the existing note's type:

- Root notes (`entities`, `interaction`, `ai-notetaker`) may update `content` and the entity association arrays (`persons`, `companies`, `opportunities`).
- Reply notes (`user-reply`, `ai-notetaker-reply`) may update `content` only; attaching `persons`, `companies`, or `opportunities` to a reply note is rejected.

For each of `persons`, `companies`, and `opportunities`, you may:

- omit the field to leave existing associations unchanged
- send an empty array (`[]`) to clear all associations of that kind
- send a non-empty array to replace the existing set with the supplied list.

Any note the caller has write access to can be updated, including AI Notetaker notes. A note's type itself cannot be changed. The content of notes that contain @mentions cannot be updated.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | No | If provided, replaces the note's content. Subject to the same HTML restrictions as creation. |
| `persons` | `array<object> (≤ 100 items)` ([PersonReference](#personreference)) | No | Persons attached to the note. Each item references a Person by id. Only valid for root notes. |
| `companies` | `array<object> (≤ 100 items)` ([CompanyReference](#companyreference)) | No | Companies attached to the note. Each item references a Company by id. Only valid for root notes. |
| `opportunities` | `array<object> (≤ 100 items)` ([OpportunityReference](#opportunityreference)) | No | Opportunities attached to the note. Each item references an Opportunity by id. Only valid for root notes. |
### notes.NotesPaged
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Note](#notesnote)) | Yes | A page of Note objects |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### notes.OpportunitiesPreview
A preview for Opportunities directly attached to the Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([Opportunity](#opportunity)) | No | Preview of Opportunities directly attached to the Note |
| `totalCount` | `integer<int64>` | No | The total count of Opportunities directly attached to the Note (Constraints: ≥ 0; ≤ 9007199254740991) |
### notes.PersonMention
A person mentioned in a note.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the mention (Constraints: ≥ 1; ≤ 2147483647) |
| `type` | `string` | Yes | The type of mention |
| `person` | `object` ([PersonData](#persondata)) | Yes |  |
### notes.PersonsPreview
A preview for Persons directly attached to the Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([PersonData](#persondata)) | No | Preview of Persons directly attached to the Note |
| `totalCount` | `integer<int64>` | No | The total count of Persons directly attached to the Note (Constraints: ≥ 0; ≤ 9007199254740991) |
### notes.RepliesPaged
Replies for a Note
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([notes.Reply](#notesreply)) | Yes | A page of Note Replies |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### notes.Reply
A Reply to a Note, created by a User or AI Notetaker.
**Variant:** [notes.UserReplyNote](#notesuserreplynote)
**Variant:** [notes.AiNotetakerReplyNote](#notesainotetakerreplynote)
### notes.SearchResult
A matched note and a matching passage. Each note appears at most once per response, regardless of how many passages matched.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `note` | `object` | Yes | The matched note. |
| `preview` | `string` | Yes | The matching passage, up to 2,000 characters. (Constraints: length ≤ 2000) |

**`note` details** — The matched note.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The note's unique identifier. (Constraints: ≥ 1; ≤ 2147483647) |
| `kind` | `string (enum: `note`, `meeting-note`, `email-note`, `ai-summary`, `meeting-ai-summary`, …)` | Yes | The type of note. - `note`: user-written note - `meeting-note`: note attached to a meeting - `email-note`: note from an email thread - `ai-summary`: auto-generated note summary - `meeting-ai-summary`: auto-generated meeting summary - `chat-message-note`: note attached to a chat message |
### notes.UserReplyNote
A reply to a note created by a user
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The type of the note |
| `parent` | `object` | Yes |  |
| `id` | `integer<int32>` | Yes | The id of the note (Constraints: ≥ 1; ≤ 2147483647) |
| `content` | `object` ([notes.Content](#notescontent)) | Yes | A note content |
| `creator` | `object` ([PersonData](#persondata)) | Yes |  |
| `mentions` | `array<oneOf> (≤ 100 items)` ([notes.Mention](#notesmention)) | Yes | The mentions in the note |
| `createdAt` | `string<date-time>` | Yes | The date and time the note was created |
| `updatedAt` | `string/null<date-time>` | Yes | The date and time the note was last updated |

**`parent` details**

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The id of the parent note (Constraints: ≥ 1; ≤ 2147483647) |
### notes.UserReplyNoteToBeCreated
Request body for creating a user reply to an existing note. `parent.id` is required and must reference an existing root note (not itself a reply) that the caller can access.
Reply notes do not support entity associations or interaction attachments. Replies to AI Notetaker notes are also created with `type: user-reply`; the reply itself is a user-authored note, not an AI-generated one.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | The note type. Must be `user-reply` to create a reply note. |
| `content` | `object` ([notes.ContentToBeSaved](#notescontenttobesaved)) | Yes | The note's body content. Only `html` is supported on write; supply rendered HTML limited to the allowed tags listed below. |
| `creator` | `object` ([PersonReference](#personreference)) | No | The person to record as the note's creator. Defaults to the calling user when omitted, and must reference an active internal person in your organization. |
| `createdAt` | `string<date-time>` | No | The time to record as when the note was created. Set this to backfill historical notes with their original date. Defaults to the current time when omitted. |
| `parent` | `object` ([notes.NoteReference](#notesnotereference)) | Yes | A reference to an existing note by its id. |
### persons.PersonToCreate
Request body for creating a Person.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `firstName` | `string` | Yes | The person's first name. |
| `lastName` | `string/null` | Yes | The person's last name. |
| `primaryEmailAddress` | `string/null<email>` | Yes | The person's primary email address. |
| `emailAddresses` | `array<string<email>> (≤ 100 items)` | No | All of the person's email addresses. If not provided, defaults to [{primaryEmailAddress}] |
| `fields` | `array<object> (≤ 100 items)` ([fields.FieldUpdate](#fieldsfieldupdate)) | No | Field-value updates to apply to the newly created Person. |
### reminders.BaseReminder
Shared fields common to both `OneTimeReminder` and `RecurringReminder`. Not used directly  callers receive one of the concrete variants discriminated by `type` on `Reminder`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |
### reminders.BaseReminderToBeCreated
Shared fields common to both `reminders.OneTimeReminderToBeCreated` and `reminders.RecurringReminderToBeCreated`. Not used directly  callers send one of the concrete variants discriminated by `type` on `ReminderToBeCreated`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for the reminder. Must reference an internal user. |
| `content` | `string/null` | No | Free-form text attached to the reminder. |
| `entity` | [reminders.TaggedCompany](#reminderstaggedcompany) \| [reminders.TaggedPerson](#reminderstaggedperson) \| [reminders.TaggedOpportunity](#reminderstaggedopportunity) | Yes | The entity the reminder is attached to. Exactly one of `company`, `person`, or `opportunity` can be tagged on a reminder  the variant is selected by the `type` discriminator. |
### reminders.OneTimeReminder
A reminder that fires once on `dueDate`.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `one-time` for this variant. |
| `status` | `string (enum: `active`, `overdue`, `completed`)` | Yes | Derived state. `active` if not completed and due in the future. `overdue` if not completed and due in the past. `completed` if `completedAt` is set. |
| `completedAt` | `string/null<date-time>` | Yes | When the reminder was completed. `null` if the reminder is not yet completed. |
| `recurrence` | `null` | Yes | Always `null` for one-time reminders. |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |
### reminders.OneTimeReminderToBeCreated
Request body for creating a one-time reminder. `dueDate` is required.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `one-time` for this variant. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is due. Must be on or after 2000-01-01 and before 9999-01-01. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for the reminder. Must reference an internal user. |
| `content` | `string/null` | No | Free-form text attached to the reminder. |
| `entity` | [reminders.TaggedCompany](#reminderstaggedcompany) \| [reminders.TaggedPerson](#reminderstaggedperson) \| [reminders.TaggedOpportunity](#reminderstaggedopportunity) | Yes | The entity the reminder is attached to. Exactly one of `company`, `person`, or `opportunity` can be tagged on a reminder  the variant is selected by the `type` discriminator. |
### reminders.RecurringReminder
A reminder that resets on a recurring cadence. Completion advances `dueDate` by `recurrence.periodDays` instead of setting `completedAt`, so `completedAt` is always `null` for this variant.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `recurring` for this variant. |
| `status` | `string (enum: `active`, `overdue`)` | Yes | Derived state. `active` if due in the future, `overdue` if due in the past. Recurring reminders never reach `completed` because completion rolls `dueDate` forward. |
| `completedAt` | `null` | Yes | Always `null` for recurring reminders. |
| `recurrence` | `object` | Yes | Recurrence configuration. Always non-null for recurring reminders. |
| `id` | `integer<int64>` | Yes | The reminder's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `content` | `string/null` | Yes | Free-form text attached to the reminder. |
| `dueDate` | `string<date-time>` | Yes | When the reminder is next due. |
| `creator` | `object` ([PersonReference](#personreference)) | Yes | The person who created the reminder. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for acting on the reminder. |
| `completer` | [PersonReference](#personreference) \| `null` | Yes | The person who completed the reminder. `null` when the reminder is not completed. May be set on a `recurring` reminder even when `completedAt` is `null`. |
| `company` | [CompanyReference](#companyreference) \| `null` | Yes | The tagged company. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `person` | [PersonReference](#personreference) \| `null` | Yes | The tagged person. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `opportunity` | [OpportunityReference](#opportunityreference) \| `null` | Yes | The tagged opportunity. At most one of `company`, `person`, or `opportunity` is non-null on any given reminder. |
| `createdAt` | `string<date-time>` | Yes | When the reminder was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the reminder was last updated. `null` if the reminder has never been updated. |

**`recurrence` details** — Recurrence configuration. Always non-null for recurring reminders.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | Yes | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | Yes | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 2147483647) |
### reminders.RecurringReminderToBeCreated
Request body for creating a recurring reminder. `recurrence` is required. `dueDate` is optional and computed from `recurrence.periodDays` when omitted.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `recurring` for this variant. |
| `dueDate` | `string<date-time>` | No | When the reminder is due. Optional for recurring reminders; computed from `recurrence.periodDays` when omitted. Must be on or after 2000-01-01 and before 9999-01-01. |
| `recurrence` | `object` | Yes | Recurrence configuration. |
| `owner` | `object` ([PersonReference](#personreference)) | Yes | The person responsible for the reminder. Must reference an internal user. |
| `content` | `string/null` | No | Free-form text attached to the reminder. |
| `entity` | [reminders.TaggedCompany](#reminderstaggedcompany) \| [reminders.TaggedPerson](#reminderstaggedperson) \| [reminders.TaggedOpportunity](#reminderstaggedopportunity) | Yes | The entity the reminder is attached to. Exactly one of `company`, `person`, or `opportunity` can be tagged on a reminder  the variant is selected by the `type` discriminator. |

**`recurrence` details** — Recurrence configuration.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | Yes | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | Yes | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 3650) |
### reminders.Reminder
A reminder to follow up with a person, company, or opportunity. Discriminated by `type`  `one-time` reminders fire once on `dueDate`, and `recurring` reminders reset on a cadence.
**Variant:** [reminders.OneTimeReminder](#remindersonetimereminder)
**Variant:** [reminders.RecurringReminder](#remindersrecurringreminder)
### reminders.ReminderPaged
A page of Reminder objects.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<oneOf> (≤ 100 items)` ([reminders.Reminder](#remindersreminder)) | Yes | A page of Reminder objects. |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### reminders.ReminderToBeCreated
Request body for creating a reminder. Discriminated by `type`  see `reminders.OneTimeReminderToBeCreated` and `reminders.RecurringReminderToBeCreated`. Exactly one of `company`, `person`, or `opportunity` must be provided.
**Variant:** [reminders.OneTimeReminderToBeCreated](#remindersonetimeremindertobecreated)
**Variant:** [reminders.RecurringReminderToBeCreated](#remindersrecurringremindertobecreated)
### reminders.ReminderToBeUpdated
Partial-update request body for a reminder. Only provided properties are updated. `recurrence` may only be sent when the reminder's existing `type` is `recurring`. Setting `completedAt` to a non-null value marks the reminder complete (for recurring reminders, this advances `dueDate` by `recurrence.periodDays` and `completedAt` remains `null` on the resource). Setting `completedAt` to `null` marks the reminder incomplete and is rejected for recurring reminders.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | `string/null` | No | Free-form note attached to the reminder. Send `null` to clear. |
| `dueDate` | `string<date-time>` | No | New due date for the reminder. Must be on or after 2000-01-01 and before 9999-01-01. |
| `owner` | `object` | No | The new owner of the reminder. Must reference an internal user. |
| `completedAt` | `string/null<date-time>` | No | Set a value to mark the reminder complete. Send `null` to mark it incomplete (one-time reminders only). `completer` is populated from the API key's owning user. |
| `recurrence` | `object` | No | Update recurrence configuration. Only valid when the reminder's existing `type` is `recurring`. Send only the fields you want to change. |

**`owner` details** — The new owner of the reminder. Must reference an internal user.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | (Constraints: ≥ 1; ≤ 9007199254740991) |

**`recurrence` details** — Update recurrence configuration. Only valid when the reminder's existing `type` is `recurring`. Send only the fields you want to change.

**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `resetTrigger` | `string (enum: `interaction`, `email`, `event`)` | No | The interaction that resets a recurring reminder's clock. `interaction` covers both emails and calendar events. |
| `periodDays` | `integer<int32>` | No | Number of days between successive due dates. (Constraints: ≥ 1; ≤ 3650) |
### reminders.TaggedCompany
Reference to a Company tagged on a reminder being created.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `company` for this variant. |
| `id` | `integer<int64>` | Yes | The company's unique identifier. (Constraints: ≥ 1; ≤ 9007199254740991) |
### reminders.TaggedOpportunity
Reference to an Opportunity tagged on a reminder being created.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `opportunity` for this variant. |
| `id` | `integer<int64>` | Yes | The opportunity's unique identifier. (Constraints: ≥ 1; ≤ 9007199254740991) |
### reminders.TaggedPerson
Reference to a Person tagged on a reminder being created. Must reference an external person or collaborator.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `type` | `string` | Yes | Discriminator. Always `person` for this variant. |
| `id` | `integer<int64>` | Yes | The person's unique identifier. (Constraints: ≥ 1; ≤ 9007199254740991) |
### transcripts.BaseTranscript
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int32>` | Yes | The transcript's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `note` | [notes.AiNotetakerRootNote](#notesainotetakerrootnote) \| [notes.AiNotetakerReplyNote](#notesainotetakerreplynote) | Yes | Note associated with the transcript |
| `createdAt` | `string<date-time>` | Yes | The date and time the transcript was created |
| `languageCode` | `string (enum: `de`, `en`, `es`, `fr`, `id`, …)` | Yes | The language code of the transcript |
### transcripts.Fragment
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `content` | `string` | Yes | The dialogue fragment of the transcript |
| `speaker` | `string` | Yes | The speaker of the dialogue fragment |
| `startTimestamp` | `string` | Yes | The starting timestamp of the dialogue fragment relative to the beginning of the transcript |
| `endTimestamp` | `string` | Yes | The ending timestamp of the dialogue fragment relative to the beginning of the transcript |
### transcripts.FragmentPaged
transcripts.FragmentPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([transcripts.Fragment](#transcriptsfragment)) | Yes | A page of Fragments for a transcript |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### transcripts.FragmentsPreview
A preview for dialogue fragments on a transcript
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([transcripts.Fragment](#transcriptsfragment)) | No | Preview of dialogue fragments on a transcript |
| `totalCount` | `integer<int64>` | No | The total count of the collection parameter. (Constraints: ≥ 0; ≤ 9007199254740991) |
### transcripts.Transcript
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `fragmentsPreview` | `object` ([transcripts.FragmentsPreview](#transcriptsfragmentspreview)) | Yes | A preview for dialogue fragments on a transcript |
| `id` | `integer<int32>` | Yes | The transcript's unique identifier (Constraints: ≥ 1; ≤ 2147483647) |
| `note` | [notes.AiNotetakerRootNote](#notesainotetakerrootnote) \| [notes.AiNotetakerReplyNote](#notesainotetakerreplynote) | Yes | Note associated with the transcript |
| `createdAt` | `string<date-time>` | Yes | The date and time the transcript was created |
| `languageCode` | `string (enum: `de`, `en`, `es`, `fr`, `id`, …)` | Yes | The language code of the transcript |
### transcripts.TranscriptPaged
transcripts.TranscriptPaged model
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([transcripts.BaseTranscript](#transcriptsbasetranscript)) | Yes | A page of Transcript results |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### webhooks.SubscriptionType
An event type a webhook can subscribe to. Values match the `type` field of delivered webhook payloads and are shared with the v1 webhook API.
Allowed values: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, `note.created`, `note.updated`, `note.deleted`, `field.created`, `field.updated`, `field.deleted`, `field_value.created`, `field_value.updated`, `field_value.deleted`, `person.created`, `person.updated`, `person.deleted`, `organization.created`, `organization.updated`, `organization.deleted`, `organization.merged`, `opportunity.created`, `opportunity.updated`, `opportunity.deleted`, `file.created`, `file.deleted`, `smart_interaction_value.updated`, `reminder.created`, `reminder.updated`, `reminder.deleted`
### webhooks.Webhook
A webhook subscription that delivers event notifications to an external URL.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `integer<int64>` | Yes | The webhook's unique identifier (Constraints: ≥ 1; ≤ 9007199254740991) |
| `url` | `string<uri>` | Yes | The URL event payloads are delivered to. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | Yes | The event types this webhook receives. An empty array means the webhook receives all event types. |
| `status` | `string (enum: `active`, `disabled`)` | Yes | Whether the webhook currently delivers events. A `disabled` webhook keeps its configuration but does not deliver events. |
| `creator` | [PersonReference](#personreference) \| `null` | Yes | The person who created the webhook. `null` when the creator is not recorded. |
| `createdAt` | `string<date-time>` | Yes | When the webhook was created. |
| `updatedAt` | `string/null<date-time>` | Yes | When the webhook was last updated. `null` if the webhook has never been updated. |
### webhooks.WebhookPaged
A page of Webhook objects.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `data` | `array<object> (≤ 100 items)` ([webhooks.Webhook](#webhookswebhook)) | Yes | A page of Webhook objects. |
| `pagination` | `object` ([PaginationWithTotalCount](#paginationwithtotalcount)) | Yes |  |
### webhooks.WebhookToBeCreated
Request body for creating a webhook. The URL is validated with a test delivery before the webhook is created.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string<uri>` | Yes | The URL event payloads are delivered to. Must be unique within the organization. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | Yes | The event types the webhook receives. An empty array subscribes the webhook to all event types. |
### webhooks.WebhookToBeUpdated
Partial-update request body for a webhook. Only provided properties are updated. Changing `url` on an active webhook, or setting `status` to `active` on a disabled webhook, triggers a test delivery that validates the URL before the update is applied.
**Properties**
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `url` | `string<uri>` | No | New delivery URL for the webhook. Must be unique within the organization. |
| `subscriptions` | `array<string (enum: `list.created`, `list.updated`, `list.deleted`, `list_entry.created`, `list_entry.deleted`, …)> (≤ 100 items)` ([webhooks.SubscriptionType](#webhookssubscriptiontype)) | No | New set of event types the webhook receives. An empty array subscribes the webhook to all event types. |
| `status` | `string (enum: `active`, `disabled`)` | No | Set to `disabled` to pause event delivery, or `active` to resume it. |

## Error Reference

The API returns structured errors with a `code` discriminator.
| Error Code | Schema |
| --- | --- |
| `authentication` | [AuthenticationError](#authenticationerror) |
| `authorization` | [AuthorizationError](#authorizationerror) |
| `bad-request` | [BadRequestError](#badrequesterror) |
| `conflict` | [ConflictError](#conflicterror) |
| `method-not-allowed` | [MethodNotAllowedError](#methodnotallowederror) |
| `not-acceptable` | [NotAcceptableError](#notacceptableerror) |
| `not-found` | [NotFoundError](#notfounderror) |
| `not-implemented` | [NotImplementedError](#notimplementederror) |
| `rate-limit` | [RateLimitError](#ratelimiterror) |
| `server` | [ServerError](#servererror) |
| `timeout` | [TimeoutError](#timeouterror) |
| `unprocessable-entity` | [UnprocessableEntityError](#unprocessableentityerror) |
| `unsupported-media-type` | [UnsupportedMediaTypeError](#unsupportedmediatypeerror) |
| `validation` | [ValidationError](#validationerror) |
