import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1/",
    api_key=os.environ["OPENROUTER_API_KEY"],
)
MODEL = os.environ.get("LLM_MODEL", "nvidia/nemotron-3.5-lightning:free")

response = client.chat.completions.create(
    model=MODEL,
    max_tokens=2048,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
)

print(response.choices[0].message.content)
print(f"tokens: {response.usage.prompt_tokens} in / {response.usage.completion_tokens} out")
