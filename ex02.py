def fibonacci(n):
    sequencia = [0, 1]
    for i in range(2, n):
        sequencia.append(sequencia[i - 1] + sequencia[i - 2])
    return sequencia


n = 100
fibonacci = fibonacci(n)
quantidade_algarismos = len(str(fibonacci[-1]))

print(f"""
Este programa verifica se um numero existe na sequência de Fibonacci
Informar numero ate {quantidade_algarismos - 1} algarismos
""")
numero = int(input("Deseja verificar qual numero :"))

print(fibonacci)

if numero in fibonacci:
    print(f"O numero {numero} está na sequência")
else:
    print(f"O numero {numero} não está sequência")