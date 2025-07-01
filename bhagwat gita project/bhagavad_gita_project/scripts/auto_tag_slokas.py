import json

# Load merged dataset
with open('/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_merged_dataset.json', 'r', encoding='utf-8') as f:
    slokas = json.load(f)

print(f"✅ Total slokas loaded: {len(slokas)}")

# ------------------------------
# Theme-based keyword dictionary
# ------------------------------
keyword_tags = {
    "Duty": ["duty", "action", "perform", "karma", "work", "obligation"],
    "Detachment": ["detachment", "renounce", "renunciation", "abandon", "give up", "desireless"],
    "Anger Management": ["anger", "wrath", "temper"],
    "Mind Control": ["mind", "control", "discipline", "self-control", "yoga"],
    "Stress": ["worry", "stress", "fear", "distress", "confusion"],
    "Life Purpose": ["purpose", "goal", "mission", "surrender", "service"],
    "Divine Support": ["lord", "god", "divine", "krishna", "faith", "trust"]
}

# Lowercase all keywords for safe matching
for tag in keyword_tags:
    keyword_tags[tag] = [word.lower() for word in keyword_tags[tag]]

# ------------------------------
# Tagging function
# ------------------------------
def auto_tag_sloka(sloka_text):
    tags = []
    for theme, keywords in keyword_tags.items():
        for keyword in keywords:
            if keyword in sloka_text.lower():
                tags.append(theme)
                break  # Avoid duplicate tags
    return tags

# ------------------------------
# Apply tagging to each sloka
# ------------------------------
tagged_count = 0

for sloka in slokas:
    combined_text = f"{sloka['translation']} {sloka['word_meaning']}"

    if 'additional_commentaries' in sloka:
        for comment in sloka['additional_commentaries']:
            combined_text += " " + comment['commentary']

    tags = auto_tag_sloka(combined_text)

    sloka['tags'] = tags

    if tags:
        tagged_count += 1

print(f"✅ Total slokas auto-tagged: {tagged_count}")

# ------------------------------
# Save auto-tagged dataset
# ------------------------------
output_path = '/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_auto_tagged_dataset.json'

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(slokas, f, ensure_ascii=False, indent=4)

print(f"✅ Auto-tagged dataset saved at: {output_path}")
