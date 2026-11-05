# Job data workflows

## Compare vacancies across LATAM countries

Use countryCodes to select markets and one keyword. maxItems is shared across the selected countries. Compare countryCode, title, location and workModality; portal taxonomies may differ.

## Run several keyword searches

Run examples/python/batch_job_searches.py for two sequential country/keyword pairs. Each starts a separate run with its own spending cap. Deduplicate combined rows by id. This workflow is implemented by the example, not a batch-keyword Actor feature.

## Export jobs to a spreadsheet

Use examples/python/export_jobs_csv.py with an existing Dataset ID. It reads every page and starts no new collection. This export contains selected scalar columns; JSON preserves nested requirements and benefits.
