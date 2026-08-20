import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_text(prompt, max_tokens=60):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.7
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = "Write a short paragraph about the importance of natural language processing in artificial intelligence."
    output = generate_text(prompt)
    print("Prompt:", prompt)
    print("Generated Text:", output)
