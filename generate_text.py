import json
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text(prompt, temperature):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()


prompt = input("Type your question: ")


temperatures = [0.2, 0.7, 1.0]

results = []

for temp in temperatures:
    print(f"Running gpt-4o-mini with temperature {temp}")
    output = generate_text(prompt, temp)

    results.append({
        "model": "gpt-4o-mini",
        "temperature": temp,
        "output": output
    })


with open("outputs.json", "w") as f:
    json.dump(results, f, indent=2)

print("Done! ")
