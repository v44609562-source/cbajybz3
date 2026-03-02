from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model = "llama3")
template = """Ты — умный помощник. 
Вопрос: {input}
Ответь максимально подробно и логично."""

prompt = PromptTemplate.from_template(template)

chain = prompt | llm
print("--- Агент Ollama думает ---")
question = "Почему небо голубое, а не зеленое?"
response  =  chain.invoke({"input": question})
print(response)

