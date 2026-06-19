import json
import sys

# Load the JSON file
with open(r'C:\Users\MI PC\psicoeduca\consultas_lotes.json', 'r') as f:
    lotes = json.load(f)

# Generate JSON for lotes 4-69 (indices 3-68) for batch uploading
# We'll create separate JSON files for each lote to make it easy to call the API

for i in range(3, 69):
    lote_num = i + 1
    records = lotes[i]
    
    # Write each lote to a file
    filename = f'C:\\Users\\MI PC\\psicoeduca\\lote_{lote_num}.json'
    with open(filename, 'w') as f:
        json.dump(records, f)
    
    print(f"Created lote_{lote_num}.json with {len(records)} records")

print("\nAll lote files created successfully!")
