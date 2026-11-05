# Bumeran jobs scraper: Python API and CSV examples

Collect public LATAM vacancies with the hosted Bumeran Jobs Scraper. This guide focuses on calling the API, checking collection status and exporting job data to a spreadsheet.

[Open Bumeran Jobs Scraper on Apify](https://apify.com/datascraperes/bumeran-jobs-scraper?fpr=edudata)

## What this repository helps you do

- Retrieve descriptions, employer information, locations and published salary ranges.
- Search seven countries across Bumeran, Laborum, Multitrabajos and Konzerta.
- Run separate keyword searches and combine rows by job ID.
- Export an existing Dataset to CSV without starting a new collection.

## Example result

Selected fields from a verified job snapshot:

```json
{
  "id": "AR:1118510775",
  "countryCode": "AR",
  "title": "Programador",
  "companyName": "Sanatorio San Jorge",
  "location": "Ushuaia, Tierra del Fuego, Argentina",
  "detailStatus": "complete"
}
```

See [sample-output.json](data/sample-output.json) for three rows. Descriptions are replaced with a sample notice, HTML removed and questions cleared; the public field set is retained. The snapshot does not promise that a vacancy is still open. [CSV sample](data/sample-output.csv) contains selected scalar columns.

## Run without code

Open the [Actor](https://apify.com/datascraperes/bumeran-jobs-scraper?fpr=edudata), select countries, enter a job title or keyword and start with 3 jobs. Leave advanced filters empty initially. Click Start, inspect Dataset and Run summary, then export JSON, CSV or Excel. See the [walkthrough](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify's [Free plan](https://apify.com/pricing?fpr=edudata) includes $5 in monthly prepaid usage and requires no credit card to start. This can fund small tests; it is not unlimited free scraping. Check the current plan terms and Actor price before running. Links to Apify use an affiliate parameter; we may receive a referral commission.

## Quick start for developers

Use Python 3.11+ or Node.js 22+. From the repository root:

```bash
python -m pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN="your-token"
python examples/python/collect_jobs.py
```

PowerShell token setup:

```powershell
$env:APIFY_API_TOKEN = "your-token"
```

The sample requests at most 3 jobs with a $0.05 maximum run charge. Inspect Console if a start response is lost before trying again.

## Input example

```json
{
  "countryCodes": [
    "AR"
  ],
  "query": "desarrollador",
  "maxItems": 3,
  "sort": "recent",
  "area": "",
  "subarea": "",
  "province": "",
  "workType": "",
  "workModality": "",
  "seniority": "",
  "contractType": "",
  "datePosted": "any",
  "disabilityFriendly": false,
  "quickApply": false
}
```

All 14 public fields are explained in the [input reference](docs/input-reference.md). maxItems is a global limit, not a per-country limit.

## Request examples

- [cURL start request](examples/curl-request.md)
- [Python collection](examples/python/collect_jobs.py)
- [Sequential keyword searches](examples/python/batch_job_searches.py)
- [Export an existing Dataset](examples/python/export_jobs_csv.py)
- [JavaScript collection](examples/javascript/request.mjs): run `node examples/javascript/request.mjs`.

Starts are sent once. Python uses pinned apify-client 3.4.0 for reads, typed run polling and paginated Dataset access. Both Python and JavaScript check SUMMARY before accepting collection as complete.

## Output fields

| Field | Meaning |
|---|---|
| id | Country plus source ID; use for deduplicating combined exports. |
| countryCode, source | Market and job board. |
| title, companyName, location | Vacancy, employer and place. |
| description, benefits, questions | Public detail and requirements. |
| salaryMin, salaryMax, salaryCurrency | Employer-published salary; often null. |
| url, postedAt, detailStatus | Source link, publication time and detail quality. |

See the [complete output reference](docs/output-reference.md).

## Common use cases

Recruiting feeds, market comparisons and spreadsheet analysis. The [workflow guide](docs/use-cases.md) explains how to combine searches and preserve job identities.

## Export Bumeran jobs to CSV with Python

```bash
python examples/python/export_jobs_csv.py YOUR_DATASET_ID --output jobs.csv
```

This pages through the existing Dataset and starts no new Actor run. Export JSON when you need nested benefits, languages or requirements.

## Collect job listings across LATAM countries

Use countryCodes with AR, MX, PE, VE, CL, EC or PA. Argentina, Mexico, Peru and Venezuela use Bumeran, Chile uses Laborum, Ecuador uses Multitrabajos and Panama uses Konzerta. For separate keywords, run the sequential workflow; each search has its own spending cap and may return overlapping jobs.

## FAQ

See the [FAQ](docs/faq.md). A keyword without matches is a valid empty result. A nonexistent advanced filter generates a field-specific warning and skips the affected country. SUCCEEDED can still contain partial collection; always inspect SUMMARY.status.

## Limits and pricing

The Actor uses pay-per-event billing: one job-result for each unique saved job. No start event or separate detail event. Empty searches and rejected filters create no job-result events. Saved rows with incomplete details can be billed. maxItems accepts 1–5,000; source restrictions or spending limits can stop a search early.

| Apify tier | Per saved job | Equivalent per 1,000 jobs |
|---|---:|---:|
| FREE | $0.001 | $1.00 |
| BRONZE | $0.0009 | $0.90 |
| SILVER | $0.0008 | $0.80 |
| GOLD | $0.00075 | $0.75 |
| PLATINUM | $0.00075 | $0.75 |
| DIAMOND | $0.00075 | $0.75 |

Verify current rates on the [Actor page](https://apify.com/datascraperes/bumeran-jobs-scraper?fpr=edudata). Salary and employer fields depend on what the source publishes. No ZonaJobs, incremental mode, start URLs or built-in batch keywords.

## Hosted version

[Bumeran Jobs Scraper on Apify](https://apify.com/datascraperes/bumeran-jobs-scraper?fpr=edudata) provides the hosted collection and storage. This repository contains client examples and documentation.

## Responsible use

Use public job data lawfully and respect source terms and applicable privacy obligations. Never commit tokens, cookies or other credentials. This integration does not submit applications or access candidate accounts.

## Support

For example problems, [open a GitHub issue](https://github.com/datacrawler-edu/bumeran-jobs-scraper-python/issues) with sanitized input and the command. For hosted run problems, use the Actor's Issues tab and include the run ID, never your token.

## License

MIT for the documentation and examples; see [LICENSE](LICENSE). The hosted service has its own terms and usage charges.
