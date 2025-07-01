import json

# 📂 Paths
base_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_dataset.json'
commentary_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/additional_commentaries.json'
output_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_merged_dataset.json'

# 🧩 Load base dataset
with open(base_path, 'r', encoding='utf-8') as f:
    base_dataset = json.load(f)

# 🧾 Load your additional commentaries
with open(commentary_path, 'r', encoding='utf-8') as f:
    additional_commentaries = json.load(f)

# 🔄 Create lookup by (chapter, verse)
commentary_lookup = {}
for entry in additional_commentaries:
    key = (entry['chapter'], entry['verse'])
    commentary_lookup.setdefault(key, []).append({
        "author": entry.get('author', 'Unknown'),
        "commentary": entry.get('commentary', '')
    })

# 🧠 Merge into base dataset
for sloka in base_dataset:
    key = (sloka['chapter'], sloka['verse'])
    sloka['additional_commentaries'] = commentary_lookup.get(key, [])

# 💾 Save merged dataset
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(base_dataset, f, ensure_ascii=False, indent=4)

print(f"✅ Merged dataset saved at: {output_path}")
