import os
import datetime
import webbrowser
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def open_google():
    webbrowser.open("https://www.google.com")
    return "Открываю браузер..."

def get_time():
    now = datetime.datetime.now()
    return f"now {now.strftime('%H:%M')}"

def save_note(text):
    with open("ai_notes.txt", "a", encoding = "utf-8") as f:
        f.write(f"[{datetime.datetime.now()}]{text}\n")
        return "записал"

def read_notes():
    folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(folder, "ai_notes.txt")
    print(f"DEBUG: Ищу файл тут: {file_path}") 
    if not os.path.exists(file_path):
        return "❌ Файл не найден по этому пути."
    with open(file_path, "r", encoding = "utf-8") as f:
        content = f.read()
    return f"📜 Твои записи:\n{content}"

def clear_notes():
    if os.path.exists("ai_notes.txt"):
        os.remove("ai_notes.txt")
        return "🧹 Файл заметок успешно удален!"
    return "❌ Удалять нечего, файл и так пуст."


llm = OllamaLLM(model = "llama3")

template = """Ты — голосовой помощник. У тебя есть команды: ГУГЛ, ВРЕМЯ.
Если просят прочитать заметки или что я записал — пиши 'ЧИТАТЬ'.
если просят удалить или очистить - пиши 'УДАЛИТЬ'.
Если пользователь просит найти что-то, напиши только слово 'ГУГЛ'.
Если пользователь спрашивает который час, напиши только слово 'ВРЕМЯ'.
Если просят записать или запомнить — пиши 'ЗАПИСАТЬ'.
Если это обычный вопрос, просто ответь на него.

Вопрос: {input}
Ответ:"""

prompt = PromptTemplate.from_template(template)
chain = prompt | llm

print("--- Ассистент запущен! (Напиши 'выход', чтобы закончить) ---")

clean_template = "Удали из фразы слова 'запиши', 'запомни', 'сохрани' и выдай только суть на русском. Фраза: {text}"
clean_prompt = PromptTemplate.from_template(clean_template)
clean_chain = clean_prompt | llm

while True:

    user_input = input("Что сделать: ")
    if user_input.lower() in ["выход", "exit", "стоп"]:
        print("good bye")
        break
    
    ai_decision = chain.invoke({"input": user_input}).strip()

    if "ГУГЛ" in ai_decision:
        print(open_google())
    elif "ВРЕМЯ" in ai_decision:
        print(get_time())
    elif "СОХРАНИТЬ" in ai_decision:
        print(save_note(user_input))
    elif "УДАЛИТЬ" in ai_decision:
        print(clear_notes())
    elif "ЧИТАТЬ" in ai_decision:
        print(read_notes())
    elif "ЗАПИСАТЬ" in ai_decision:
        clean_text = clean_chain.invoke({"text": user_input}).strip()
        print(save_note(clean_text))
    else:
        print("ИИ отвечает:", ai_decision)
