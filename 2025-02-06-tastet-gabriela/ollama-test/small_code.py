import random

secret = random.randint(1, 10)

guess = int(input("Endevina un nombre entre 1 i 10:\n"))

# Python fa servir indentació per marcar blocs de codi
# No cal posar ; per separar statements
if guess == secret:
    print("Ho has encertat!")
else:
    print(f"T'has equivocat, el nombre era {secret}")
