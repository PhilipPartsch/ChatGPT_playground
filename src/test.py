# from https://pypi.org/project/openai/ chapter usage

import os
from openai import OpenAI

try:
    openai_api_key = os.environ.get("OPENAI_API_KEY")
except KeyError:
    openai_api_key = "Token not available!"
    # or raise an error if it's not available so that the workflow fails

client = OpenAI(
    api_key=openai_api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)
