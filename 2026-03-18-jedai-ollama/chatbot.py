import ollama

MODEL = "qwen3.5:4b"


def chat():
    messages = []

    print(f"Chatbot (model: {MODEL}). Escriu 'sortir' per acabar.\n")

    while True:
        user_input = input("Tu: ").strip()

        if user_input.lower() == "sortir":
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = ollama.chat(model=MODEL, messages=messages)
        assistant_message = response["message"]["content"]

        messages.append({"role": "assistant", "content": assistant_message})

        print(f"Bot: {assistant_message}\n")


if __name__ == "__main__":
    chat()
