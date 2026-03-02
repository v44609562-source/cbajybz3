
from langchain_community.llms import FakeListLLM



responses = [
    "Thought: Мне нужно посчитать 2 + 2. Инструмент: Калькулятор. Ввод: 2+2",
    "Final Answer: Результат вычислений равен 4"
]
llm = FakeListLLM(responses=responses)

def run_simple_agent(querry):
    print(f"Вопрос пользователю: {querry}")
    print("_" * 30)
    for i in range(len(responses)):
        thought = llm.invoke(querry)
        print(f"Шаг {i+1}: {thought}")
        if "final answer" in thought:
            print("_" * 30)
            print(f"ИТОГ:  {thought.split(': ')[1]}")
            break
run_simple_agent("Сколько будет 2 + 2?")