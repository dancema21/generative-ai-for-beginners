import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
  base_url = "https://api.perplexity.ai"
  )

deployment="sonar-pro"

persona = input("Which historical figure do you want to speak to ?")
instructions = f"""
You are {persona}.
You are friendly and you answer by using the first person.
Justify your answers by providing a historical event that illustrates what you say.
For instance, I like English people because Churchill helped us win the WW2.
You cannot mention elements that happened after your death.
For instance, 'I won the WW2 war in 1945'.

Limit the answer to 2 sentences.

Don't create content yourself. If you don't know something, tell that you don't remember.
"""

prompt = input(f"You are now speaking to {persona}. Ask anything !")

# interpolate the number of recipes into the prompt an ingredients
messages = [
    {"role": "system", "content": instructions},
    {"role": "user", "content": prompt}
]

completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=600, temperature = 1)

print(completion.choices[0].message.content)
