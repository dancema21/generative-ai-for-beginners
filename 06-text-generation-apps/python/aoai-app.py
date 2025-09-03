import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
  base_url = "https://api.perplexity.ai"
  )

deployment="sonar-pro"

number_recipes = input("Number of recipies :")
ingredients = input("List of ingredients (for example : chicken, carrots, eggs) :")
filter = input("Any ingredients you don't wont (for example : olives) :")

# add your completion code
prompt = f"""Show me {number_recipes} recipes for a dish with the following ingredients: {ingredients}. The recipies should not include the following ingredients : {filter}. Per recipe, gie the name of the dish and all the ingredients used"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
old_prompt_result = completion.choices[0].message.content

prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."
new_prompt = f"{old_prompt_result} {prompt}"
messages = [{"role": "user", "content": new_prompt}]

new_completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=1200)

print("Shopping list:")
print(new_completion.choices[0].message.content)

