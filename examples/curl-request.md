# Start once with cURL

Set APIFY_API_TOKEN in your environment. Run from the repository root:

```bash
curl --fail-with-body --silent --show-error --retry 0 --max-time 45 \
  -X POST 'https://api.apify.com/v2/acts/datascraperes~bumeran-jobs-scraper/runs?timeout=180&maxTotalChargeUsd=0.05' \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

Copy the returned run ID. Poll GET /v2/actor-runs/{runId}, then inspect the run's SUMMARY record and Dataset. A failed or lost start response does not prove that no run was created: inspect Console before starting again. The examples use bearer headers and do not put tokens in URLs.
