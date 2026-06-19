import json
import os

# Load the main JSON
with open(r'C:\Users\MI PC\psicoeduca\consultas_lotes.json', 'r', encoding='utf-8') as f:
    lotes = json.load(f)

# We've uploaded lotes 1-2 (50+50=100) and lote 3 (50) and lote 4 (50)
# Now we need lotes 5-69 (indices 4-68)

baseId = "appfPbIIS3UgNvOKC"
tableId = "tblfohS1ZEkvFkGFw"

# Create individual batch files for each lote
output_dir = r'C:\Users\MI PC\psicoeduca\batch_jsons'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(4, 69):  # lotes 5-69 (indices 4-68)
    lote_num = i + 1
    records = lotes[i]
    
    # Create the payload
    payload = {
        "baseId": baseId,
        "tableId": tableId,
        "records": records
    }
    
    # Save to file
    filename = os.path.join(output_dir, f'lote_{lote_num}_payload.json')
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(payload, f)
    
    print(f"Lote {lote_num}: {len(records)} records - {filename}")

print(f"\nCreated payloads for lotes 5-69")
