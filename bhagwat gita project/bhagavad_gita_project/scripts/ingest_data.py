# Install pandas

# Import necessary libraries
import pandas as pd
import json

# Load CSV file
csv_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/raw/Bhagwad_Gita.csv'  # Update this path if needed
df = pd.read_csv(csv_path)

# View the first few rows
print(df.head())

# View the column names
print(df.columns)

# Create a unified data structure
all_slokas = []

for index, row in df.iterrows():
    sloka = {
        "chapter": int(row['Chapter']),
        "verse": int(row['Verse']),
        "sanskrit": row['Shloka'],  # ✅ Correct column
        "transliteration": row['Transliteration'],
        "word_meaning": row['WordMeaning'],
        "translation": row['EngMeaning'],
        "hindi_meaning": row['HinMeaning'],
        "tags": []  # For future tagging
    }
    all_slokas.append(sloka)

print(f"Total Slokas Loaded: {len(all_slokas)}")
print("Sample Sloka:", all_slokas[0])

# Save as JSON
output_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_dataset.json'

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(all_slokas, f, ensure_ascii=False, indent=4)

print("✅ Dataset successfully saved as JSON!")