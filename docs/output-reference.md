# Output reference

One row per unique job, keyed by country and source ID. [JSON sample](../data/sample-output.json) retains the public field set; descriptions are replaced with a sample notice, HTML removed and questions cleared. Values are a historical snapshot, not current vacancies.

| Field | JSON type |
|---|---|
| `recordType` | string |
| `id` | string |
| `sourceId` | integer, null |
| `countryCode` | string |
| `country` | string, null |
| `source` | string, null |
| `url` | string, null |
| `title` | string, null |
| `companyName` | string, null |
| `companyId` | integer, null |
| `companyLogo` | string, null |
| `companyIndustry` | string, null |
| `companySize` | string, null |
| `companyEmployees` | integer, null |
| `companyRating` | number, null |
| `companyValidated` | boolean, null |
| `companyPro` | boolean, null |
| `confidential` | boolean, null |
| `location` | string, null |
| `city` | string, null |
| `province` | string, null |
| `provinceSemantic` | string, null |
| `address` | string, null |
| `workModality` | string, null |
| `workType` | string, null |
| `contractType` | string, null |
| `seniority` | string, null |
| `area` | string, null |
| `areaSemantic` | string, null |
| `subarea` | string, null |
| `subareaSemantic` | string, null |
| `salaryRaw` | string, null |
| `salaryMin` | number, null |
| `salaryMax` | number, null |
| `salaryCurrency` | string, null |
| `salaryFrequency` | string, null |
| `salaryType` | string, null |
| `salaryRequestedByEmployer` | boolean, null |
| `postedAt` | string, null |
| `postedAtRaw` | string, null |
| `updatedAt` | string, null |
| `expiresAt` | string, null |
| `vacancies` | integer, null |
| `description` | string, null |
| `descriptionHtml` | string, null |
| `educationLevel` | string, null |
| `educationStatus` | string, null |
| `educationRequired` | boolean, null |
| `experience` | string, null |
| `experienceMonths` | integer, null |
| `languages` | array |
| `knowledge` | array |
| `age` | string, null |
| `gender` | string, null |
| `residence` | string, null |
| `benefits` | array |
| `questions` | array |
| `quickApply` | boolean, null |
| `disabilityFriendly` | boolean, null |
| `plan` | string, null |
| `detailStatus` | string |
| `searchQuery` | string, null |
| `scrapedAt` | string |

Salary fields may be null. Dates without a timezone retain portal local time. Check detailStatus for incomplete detail. SUMMARY.status completed/empty indicates completed collection; partial, charge_limit, invalid_input and delivery_unknown require inspection. Platform SUCCEEDED alone does not prove complete collection.
