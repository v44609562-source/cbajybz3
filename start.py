from langchain_community.llms import FakeListLLM
responses =["Привет! Я твой первый LangChain бот. Установка прошла успешно!"]
llm = FakeListLLM(responses=responses)
question = "проверка связи"
print("отправляю запрос")
answer = llm.invoke(question)
print("-" * 20)
print("ОТВЕТ БОТА:", answer)
print("-" * 20)