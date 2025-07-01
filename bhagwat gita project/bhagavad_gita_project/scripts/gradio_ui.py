import json
import gradio as gr

# Load auto-tagged dataset
with open('/workspaces/Bhagwat-Gita/bhagavad_gita_project/data/processed/bhagavad_gita_auto_tagged_dataset.json', 'r', encoding='utf-8') as f:
    slokas = json.load(f)

# Prepare a simple theme to tag mapping (you can fine-tune later)
problem_to_tag = {
    "stress": "Stress",
    "anger": "Anger Management",
    "fear": "Stress",
    "life purpose": "Life Purpose",
    "mind control": "Mind Control",
    "detachment": "Detachment",
    "duty": "Duty",
    "faith": "Divine Support"
}

# Search function
def find_relevant_slokas(user_input):
    user_input_lower = user_input.lower()
    matched_tag = None

    # Find the closest tag
    for problem, tag in problem_to_tag.items():
        if problem in user_input_lower:
            matched_tag = tag
            break

    if not matched_tag:
        return "Sorry, no matching theme found. Please try using words like stress, anger, duty, etc."

    # Get top 3 matching slokas
    matching_slokas = [sloka for sloka in slokas if matched_tag in sloka['tags']]

    if not matching_slokas:
        return f"No slokas found for the theme '{matched_tag}'. Try a different problem."

    # Prepare response
    response = f"🧘 Relevant Slokas for: {user_input.title()} ({matched_tag})\n\n"
    for sloka in matching_slokas[:3]:
        response += f"📜 Chapter {sloka['chapter']}, Verse {sloka['verse']}\n"
        response += f"Sanskrit: {sloka['sanskrit']}\n"
        response += f"Meaning: {sloka['translation']}\n"
        if sloka.get('additional_commentaries'):
            response += f"Commentary: {sloka['additional_commentaries'][0]['commentary']}\n"
        response += "-" * 50 + "\n"

    return response

# Gradio interface
iface = gr.Interface(
    fn=find_relevant_slokas,
    inputs=gr.Textbox(label="Describe your problem or feeling (e.g., I feel stressed)"),
    outputs="text",
    title="Bhagavad Gita Sloka Recommender",
    description="Enter your problem or feeling and receive relevant slokas from the Bhagavad Gita to guide you."
)

# Launch the app
if __name__ == "__main__":
    iface.launch(share=True)
