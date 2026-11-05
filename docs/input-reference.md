# Input reference

All 14 public input properties are present in [the sample input](../data/sample-input.json).

| Field | Default | Use |
|---|---|---|
| `countryCodes` | `["AR"]` | Choose one or more countries by name. The matching job board is selected automatically. |
| `query` | `""` | For example: desarrollador, vendedor or data analyst. Leave empty to browse jobs without a keyword. |
| `maxItems` | `50` | Total jobs to save across all selected countries, from 1 to 5,000. Start with a small number to try your search. |
| `workModality` | `""` | Choose remote, hybrid or on-site jobs. Leave Any selected to include all workplaces. |
| `datePosted` | `"any"` | Choose how recently the job was published. Any time includes all available dates. |
| `sort` | `"recent"` | Newest first uses the portal publication date. Relevance follows the portal's default ranking. |
| `seniority` | `""` | Choose the experience level you need, or Any to include all levels. |
| `workType` | `""` | Choose full-time, part-time or another employment type. Any includes all types. |
| `contractType` | `""` | Optional contract type. Leave empty for all contract types. |
| `disabilityFriendly` | `false` | Keep only jobs marked as suitable for candidates with disabilities. |
| `quickApply` | `false` | Keep only jobs that support the portal's quick application flow. |
| `area` | `""` | Optional category name or portal ID, for example comercial-ventas-y-negocios. Leave empty if unsure. |
| `subarea` | `""` | Optional subcategory name or portal ID. Availability depends on the country and job category; leave empty if unsure. |
| `province` | `""` | Optional region name or portal ID, for example argentina\|buenos-aires. Use one country when filtering by a specific region; leave empty to search nationwide. |

Country codes: AR, MX, PE, VE, CL, EC, PA. maxItems is global, 1–5,000. No batch-keyword input, start URLs, incremental mode or ZonaJobs support. The batch example starts separate runs.

Invalid input may be rejected by Apify before startup. Runtime correction warnings name the field and appear in SUMMARY.inputIssues or SUMMARY.errors. Unavailable country filters skip that country; they never trigger a wider unfiltered search.
