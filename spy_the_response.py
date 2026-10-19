import os
from openai import OpenAI

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.environ["GEMINI_API_KEY"],
)
r = client.chat.completions.create(
    model="gemini-flash-latest",
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
)
print(r)
print("---")
print("finish_reason:", r.choices[0].finish_reason)
print("usage:", r.usage)
