import openai
import os

#openai.api_key = "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"

def generate_rpg_story():
    client = openai.OpenAI(api_key=openai.api_key)

    prompt = (
        "Create a branching storyline for a text-based RPG set at the Grammy Awards. "
        "Follow this format: each event has an event number, a description, "
        "and two choices leading to different numbered events. "
        "Ensure at least 8 decision points, 1 shared child event, and a minimum depth of 5. "
        "Format: event_number | description | left_event | right_event."
    )

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that generates structured RPG stories."},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def save_story_to_file(filename, story_text):
    try:
        with open(filename, "w") as file:
            file.write(story_text)
        print(f"Story saved to {filename}")
    except Exception as e:
        print(f"Error saving story: {e}")


if __name__ == "__main__":
    story_text = generate_rpg_story()
    save_story_to_file("story.txt", story_text)