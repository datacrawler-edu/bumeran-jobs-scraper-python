"""Two sequential hosted searches; each starts a separate potentially paid run."""
import json
from common import start_once, wait_for_dataset, iter_rows, sample_input

def main():
    jobs = {}
    for country, keyword in [('AR', 'desarrollador'), ('CL', 'vendedor')]:
        payload = {**sample_input(), 'countryCodes': [country], 'query': keyword, 'maxItems': 3}
        dataset_id = wait_for_dataset(start_once(payload, maximum_usd=0.05))
        for row in iter_rows(dataset_id):
            jobs[row['id']] = row
    print(json.dumps(list(jobs.values()), ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
