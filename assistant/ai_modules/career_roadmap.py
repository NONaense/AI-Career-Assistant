from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")


def generate_roadmap(role):

    prompt = f"Create a step by step learning roadmap to become a {role}"

    result = generator(prompt, max_length=120, num_return_sequences=1)

    roadmap = result[0]['generated_text']

    return roadmap