import os
import json

# Custom JSON encoder function to avoid escaping double quotes
def custom_encoder(obj):
    if isinstance(obj, str):
        return obj.encode('utf-8').decode('unicode_escape')
    return obj

# Specify the folder containing your JSON files
folder_path = 'users'

# Initialize an empty list to store JSON objects
json_objects = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        # Open and read each JSON file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                json_data = json.load(file)
                json_objects.append(json_data)
            except json.JSONDecodeError as e:
                print(f"Error reading {filename}: {e}")

# Create a new JSON file containing the array of JSON objects with custom encoding
output_file_path = 'combined.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(json_objects, output_file, indent=4, ensure_ascii=False, default=custom_encoder)

print(f"Combined JSON file '{output_file_path}' created with {len(json_objects)} JSON objects.")
