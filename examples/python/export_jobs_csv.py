"""Export an existing Dataset in pages. This does not start a new Actor run."""
import argparse
import csv
from common import iter_rows

COLUMNS = ['id','countryCode','title','companyName','location','workModality','postedAt','salaryMin','salaryMax','salaryCurrency','url','detailStatus']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_id')
    parser.add_argument('--output', default='jobs.csv')
    args = parser.parse_args()
    count = 0
    with open(args.output, 'w', newline='', encoding='utf-8-sig') as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, extrasaction='ignore')
        writer.writeheader()
        for row in iter_rows(args.dataset_id):
            writer.writerow(row)
            count += 1
    print(f'Exported {count} rows to {args.output}')

if __name__ == '__main__':
    main()
