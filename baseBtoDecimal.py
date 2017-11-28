# TRANSFORMA NUMERO EM QUALQUER BASE PARA DECIMAL

numero = str(input("Informe o numero: ")) # TRANSFORMA INTEIRO EM STRING (PARA INTERAR ABAIXO)
base = int(input("Informe a base: ")) # LE A BASE
numeroDecimal = []
tamanhoNumero = len(str(numero)) # QUANTIDADE DE DIGITOS DO NUMERO

# FUNCAO RETORNA CADA DIGITO E A POSICAO DELE
for posicao, digito in enumerate(numero):
    digito = int(digito)
    numeroDecimal.append(digito * (base ** (tamanhoNumero - posicao)))

# SOMA OS RESULTADOS
resultado = 0
for digito in numeroDecimal:
    resultado += digito

print("Base 10 > {}".format(numero, base, resultado))
