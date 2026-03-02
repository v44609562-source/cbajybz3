from langchain_ollama import OllamaLLM

# Укажи модель, которая у тебя скачана (например, llama3 или mistral)
# Если не знаешь, какая есть, напиши в терминале: ollama list
llm = OllamaLLM(model="llama3") 

print("Пробую достучаться до Ollama...")
response = llm.invoke("Привет! Ты работаешь через LangChain?")
print("-" * 20)
print(response)
print("-" * 20)

