import json

# Load the merged dataset
with open('/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_merged_dataset.json', 'r', encoding='utf-8') as f:
    slokas = json.load(f)

print(f"✅ Total slokas loaded: {len(slokas)}")

# ------------------------------
# Create manual tagging dictionary
# Format: (chapter, verse): [tags]
# ------------------------------

tagging_dict = {
    (2, 47): ["Duty", "Detachment"],
    (4, 7): ["Divine Support", "Life Purpose"],
    (6, 5): ["Mind Control", "Self-Elevation"],
    (3, 30): ["Detachment", "Karma Yoga"],
    (2, 56): ["Anger Management", "Emotional Stability"],
    (18, 66): ["Surrender", "Faith", "Divine Support"]
    # 👉 Add more manually as you study the meanings
}

# ------------------------------
# Apply tags to the slokas
# ------------------------------
tagged_count = 0

for sloka in slokas:
    key = (sloka['chapter'], sloka['verse'])
    sloka['tags'] = tagging_dict.get(key, [])
    if sloka['tags']:
        tagged_count += 1

print(f"✅ Total slokas tagged: {tagged_count}")

# ------------------------------
# Save the tagged dataset
# ------------------------------
output_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_tagged_dataset.json'

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(slokas, f, ensure_ascii=False, indent=4)

print(f"✅ Tagged dataset saved at: {output_path}")
