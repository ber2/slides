# Aquest programa es pot executar directament per jugar al trivial pursuit fent servir un model LLaMa executat localment.
# El podeu modificar com vulgueu per tal que faci altres coses.
# Algunes idees:
#    - Afegir múltiples jugadors.
#    - Afegir nivells de dificultat.
#    - Demaneu al model que us expliqui la resposta correcta en cas d'error.
#    - Modifiqueu aquest programa per tal que us ajudi a estudiar una assignatura.
#    - Modifiqueu aquest programa per tal que us faci preguntes sobre Python.
#    - Canvieu l'idioma del joc.

import ollama
import random

MODEL = "llama3.2:3b"


# Generem una pregunta nova
def get_trivia_question(category):
    prompt = f"""You are a Trivial Pursuit game master.
    Generate a multiple-choice trivia question about {category}.
    Include four answer options (A, B, C, D).
    Format it like this:

    Question about {category}: <question text>
    A) <option 1>
    B) <option 2>
    C) <option 3>
    D) <option 4>
    """
    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return response['message']['content']


# Validem la resposta
def check_answer(question, user_answer):
    prompt = f"""Here is a trivia question and an answer:

    {question}

    User's answer: {user_answer}

    Is this correct? Reply with 'Yes' or 'No' only."""

    response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": prompt}])
    return "Yes" in response['message']['content']

# Iteració en el joc
score = 0
rounds = 3
categories = ["Geography", "Entertainment", "History", "Arts & Literature", "Science & Nature", "Sports & Leisure"]

for _ in range(rounds):
    category = random.choice(categories)
    question = get_trivia_question(category)
    print("\n" + question)

    user_answer = input("\nYour answer: ").strip().upper()

    if check_answer(question, user_answer):
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Incorrect!")

print(f"\nGame over! Your final score: {score}/{rounds}")
