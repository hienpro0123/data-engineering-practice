import os
import json
import csv
import glob

def flatten_json(y):
    """Flatten a nested json file"""
    out = {}

    def flatten(x, name=''):
        if isinstance(x, dict):
            for a in x:
                flatten(x[a], f"{name}{a}_")
        elif isinstance(x, list):
            for i, a in enumerate(x):
                flatten(a, f"{name}{i}_")
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def find_json_files(data_dir):
    return glob.glob(os.path.join(data_dir, '**', '*.json'), recursive=True)

def convert_json_to_csv(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]  # make it a list for uniform processing

    flattened = [flatten_json(entry) for entry in data]

    csv_file = json_file.replace('.json', '.csv')

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=flattened[0].keys())
        writer.writeheader()
        writer.writerows(flattened)

def main():
    data_dir = 'data'
    json_files = find_json_files(data_dir)

    print(f"🔍 Found {len(json_files)} JSON files")

    for file in json_files:
        print(f"📄 Converting {file} to CSV...")
        convert_json_to_csv(file)

    print("✅ All files processed!")


if __name__ == '__main__':
    main()
