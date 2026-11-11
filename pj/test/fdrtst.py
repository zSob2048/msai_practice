import os
from openai import AzureOpenAI, OpenAI

endpoint = "https://fin-test.openai.azure.com/openai/v1"
deployment_name = "test_model_fin"
api_key = "YOUR_AZURE_API_KEY"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "자본금은 3000인데,.. 카페를 차리면 수익이 날까? 매출은 500정도 나온다더라...",
        }
    ],
    max_completion_tokens=13107,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment_name
)

print(response.choices[0].message.content)