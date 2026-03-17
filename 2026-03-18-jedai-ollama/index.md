---
theme: default
class:
  - lead
  - invert
paginate: true
# backgroundColor: #fff
marp: true
# header: Hello
footer: Alberto Cámara - Python i Ollama - 2026-03-18
---

# **Python** i Ollama:
Fes el teu propi chatbot

**Alberto Cámara**
**Jedai**, 2026-03-18

![bg right:30% w:300](img/ollama.png)

---

# About me

![bg right:30% w:300](https://ber2.github.io/images/pingu.jpg)

- Matemàtic 
- Científic de Dades
- Membre de **PyBcn**

---

# Què farem avui?

- Què és Python? Alguns conceptes bàsics
- Per a què s'usa Python?
- Large Language Models. Ollama
* **Fes el teu propi chatbot**

---

![bg left:35% w:500](img/monty_python.jpg)

# Què és Python?

És un llenguatge de programació creat per **Guido van Rossum** el 1991:

* **Interpretat** (en comptes de compilat)
* **De tipatge dinàmic** (en comptes d'estàtic)
* Fàcil d'aprendre (llegibilitat i sintaxi)

---

![bg right:35% w:300](img/pybcn_logo.png)

Python...
- és de codi obert
- té una comunitat molt activa que:
    - governa la implementació del llenguatge
    - proporciona moltíssimes llibreries

A Barcelona tenim l'associació **PyBcn**: ens trobareu a [pybcn.org](https://pybcn.org)

---

![bg left:40%](img/hacker.jpg)

És molt habitual veure Python usat per a:

* Programació científica i càlcul numèric
* Programació backend
* Automatització
* Anàlisi de Dades, Big Data
* Intel·ligència Artificial

---

# Primer tastet

Hauríeu de tenir **Python** instal·lat a les vostres màquines.

- Obriu un terminal (`Win + R`, escriviu `cmd`, premeu intro).

- Escriviu `python` i premeu intro.

Hauríeu de veure alguna cosa així:

```
Python 3.x.x (default, ...) 
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

---

terminal

---

# LLMs

![bg left:30% width:400](img/chatgpt_logo.png)

Els **Large Language Models** són models d'aprenentatge automàtic que són capaços de generar text amb resultats espectaculars.

Salten a la fama a finals de 2022 amb la publicació de **ChatGPT**, de OpenAI.

Actualment hi ha una gran competició per acaparar la **IA Generativa**: empreses, països, control dels xips, control de les matèries primeres per fabricar xips...

---

# LLMs Open Source

Hi ha jugadors que aposten per publicar els seus models. A destacar:

- Els models `llama`, publicats per **Meta**
- `deepseek`, d'origen xinès, van sacsejar el mercat
- `mistral`, d'origen europeu
- Els models `qwen`, publicats per **Alibaba**
- `gpt-oss` i altres models derivats de la família GPT

---

# Ollama: Integracions

Ollama s'integra amb moltes eines de l'ecosistema IA:

- **Coding Agents**: Claude Code, Codex, Goose, Droid...
- **IDEs & Editors**: VS Code, JetBrains, Xcode, Zed...
- **Assistants**: OpenClaw i similars
- **Chat & RAG**: Onyx
- **Automation**: n8n
- **Notebooks**: marimo

---

# Segon tastet

![bg right:30% width:500](img/ollama.png)

Hauríeu de tenir instal·lat **Ollama**.

Executeu:

```bash
> ollama run qwen3.5:4b
```

Si no teniu prou memòria (<10 RAM):
```bash
> ollama run qwen3.5:0.8b
```

O bé useu el model al núvol (sense descàrrega):
```bash
> ollama run qwen3.5:cloud
```

Podríem preguntar, per exemple:
```
>>> Can you give me a short description of what Python is as a programming language?
```
---

Per tal de permetre que un programa python es comuniqui amb un LLM d'Ollama, cal instal·lar una llibreria:

```
> pip install ollama
```

Finalment, podeu descarregar els fitxers `trivial_pursuit.py` i `chatbot.py` de [TBD].

---

terminal

