from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple terms")
model = ChatOpenAI(model="gpt-3.5-turbo")
chain = prompt | model

response = chain.invoke({"topic": "machine learning"})
print(response.content)
