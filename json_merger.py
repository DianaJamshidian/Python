import json
import glob

def merge_json_files(path):
    result = []
    for file in glob.glob(f"{path}/*.json"):
        with open(file, 'r') as f:
            data = json.load(f)
            result.extend(data if isinstance(data, list) else [data])
    with open('merged.json', 'w') as f:
        json.dump(result, f, indent=4)
    print("Merged file created successfully.")

if __name__ == "__main__":
    merge_json_files('./data')
