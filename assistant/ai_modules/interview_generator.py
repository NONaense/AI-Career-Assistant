from transformers import pipeline

# Load model once when server starts
generator = pipeline("text-generation", model="gpt2")

def generate_questions(role):

    prompt = f"Generate 5 interview questions for a {role}"

    result = generator(
        prompt,
        max_length=120,
        num_return_sequences=1
    )

    return result[0]["generated_text"]