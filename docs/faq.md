# FAQ

## Is this the scraper source?
This repository contains integration examples for the [hosted Actor](https://apify.com/datascraperes/bumeran-jobs-scraper?fpr=edudata).

## Which countries and brands are covered?
AR, MX, PE, VE, CL, EC and PA: Bumeran, Laborum, Multitrabajos and Konzerta. ZonaJobs is not included.

## Why did my filter return no results?
Read SUMMARY and the log. An unavailable category, subcategory or region skips the affected country with an actionable warning. A valid keyword can simply have no matches.

## How are jobs billed?
One job-result per unique job saved. Details have no extra event. Empty or rejected searches create no job-result events. Saved jobs with incomplete details can still be billed; inspect detailStatus. Check current rates on the Actor page.

## Can I resume after a network error in the example?
If a start response is lost, inspect recent runs in Console before starting again. Read an existing run or export its Dataset; the examples never automatically replay a potentially paid start. The hosted Actor can recover the same run's saved results, but separate runs are separate searches.

## Are all successful runs complete?
No. Inspect SUMMARY.status. The examples reject incomplete statuses even when the platform status is SUCCEEDED.
