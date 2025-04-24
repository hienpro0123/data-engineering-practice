import os
import json
import csv
import glob


def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f'{name}{a}_')
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, f'{name}{i}_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


def process_json_to_csv(json_path):
    csv_path = os.path.splitext(json_path)[0] + '.csv'

    with open(json_path, 'r', encoding='utf-8') as jf:
        data = json.load(jf)

        # If data is a list of dicts
        if isinstance(data, list):
            flat_data = [flatten_json(item) for item in data]
        else:
            flat_data = [flatten_json(data)]

    # Write to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as cf:
        writer = csv.DictWriter(cf, fieldnames=flat_data[0].keys())
        writer.writeheader()
        writer.writerows(flat_data)


def main():
    json_files = glob.glob("data/**/*.json", recursive=True)
    for json_file in json_files:
        print(f"Processing: {json_file}")
        process_json_to_csv(json_file)


if __name__ == "__main__":
    main()
