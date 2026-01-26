from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    temperature=0.6
)

# Prompt for restaurant name
name_prompt = PromptTemplate(
    input_variables=["cuisine"],
    template="I want to open a restaurant for {cuisine} food. Suggest ONE fancy name only."
)

# Prompt for menu
menu_prompt = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest a detailed menu for a restaurant named {restaurant_name}."
)

def generate_restaurant_name_and_items(cuisine):
    name_chain = name_prompt | llm | StrOutputParser()

    menu_chain = (
        RunnableLambda(lambda name: {"restaurant_name": name})
        | menu_prompt
        | llm
        | StrOutputParser()
    )

    restaurant_name = name_chain.invoke({"cuisine": cuisine})
    menu_items = menu_chain.invoke(restaurant_name)

    return {
        "restaurant_name": restaurant_name.strip(),
        "menu_items": menu_items.strip()
    }


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
