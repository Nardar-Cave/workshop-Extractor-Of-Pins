# Comece criando uma função chamada pin_extractor com um parâmetro poem. 
# Uma função vazia gera um erro, então adicione pass dentro da função momentaneamente para torná-la válida.

'''def pin_extractor(poem):
    pass'''

# Você precisará de uma variável para armazenar o código secreto enquanto o decodifica, então remova pass e crie uma variável chamada secret_code dentro da função e atribua a ela uma string vazia.

'''def pin_extractor(poem):'''
    secret_code = ""

# Enquanto você trabalha na função, seria útil ter uma chamada de função para fins de depuração, então crie uma variável poem, fora da função, que contenha este poema:

'''Stars and the moon
shine in the sky
white and bright
until the end of the night'''

# Você pode usar uma string de múltiplas linhas para isso.
# E então, chame a função com a variável poem como argumento.

'''def pin_extractor(poem):
    secret_code = ""

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# Há um dígito do pin escondido em cada linha, então dentro da função use o método split para dividir a string em uma lista de linhas. 
# Divida as linhas no caractere de nova linha (\n) e atribua a lista resultante a uma variável chamada lines.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# Você precisa trabalhar em cada linha independentemente: crie um loop sobre lines que use line como variável do loop. Dentro do loop, imprima line.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line in lines:
        print(line)

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# O dígito n-ésimo do pin está oculto como o comprimento da n-ésima palavra na n-ésima linha.
# Para encontrar o comprimento da enésima palavra, o próximo passo é separar a linha do poema em uma lista de palavras: dentro do loop, crie uma variável words e atribua a ela o valor de line dividido em palavras usando o método split.
# Então, adicione uma chamada print com words como seu argumento.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line in lines:
        print(line)
        words = line.split()
        print(words)

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# O dígito n-ésimo do código secreto vem da palavra n-ésima da linha n-ésima, então você precisa saber qual é o número de cada linha.
# Altere o loop para que ele itere em enumerate(lines) e adicione outra variável de loop antes de line chamada line_index.
# Além disso, atualize a chamada print para print(line_index, line).

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(words)

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# Na última linha do loop, atualize a chamada print para que ela imprima a palavra dentro da lista words no índice line_index.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(words[line_index])

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# A função len retorna o comprimento de uma string. Atualize a segunda chamada de print para imprimir o comprimento dessa palavra.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(len(words[line_index]))

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# O comprimento retornado de len é um inteiro, você precisa convertê-lo para uma string usando a função str para poder adicioná-lo à string secret_code.
# Atualize a chamada print para imprimir o comprimento como uma string.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        print(str(len(words[line_index])))

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# Agora você pode concatenar str(len(words[line_index])) a secret_code. 
# Remova a chamada print e use a atribuição aumentada += para concatenação.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
        # print(str(len(words[line_index])))
        secret_code += str(len(words[line_index]))

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# Remova as duas chamadas print e adicione uma instrução return que retorne secret_code na última linha da função.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        words = line.split()
        secret_code += str(len(words[line_index]))
        
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

pin_extractor(poem)'''

# Passe pin_extractor(poem) para a função print para que você possa ver o que a função está retornando.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        words = line.split()
        secret_code += str(len(words[line_index]))
        
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))'''

# Agora a função está fazendo um bom trabalho em extrair o código do poema, mas há um caso limite a considerar: a linha do poema pode ser mais curta do que o esperado e isso faria a função gerar um erro (você pode tentar isso removendo a palavra bright do poema).
# Coloque a linha secret_code += str(len(words[line_index])) em uma declaração if que verifica se há palavras suficientes na lista words.

def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))

# A terceira linha do poema está faltando uma terceira palavra, então o pino é mais curto do que o esperado.
# Adicione uma cláusula else que concatene um '0' a secret_code quando não houver palavras suficientes, para que todas as linhas do poema sejam usadas para buscar dígitos.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
        
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

print(pin_extractor(poem))'''

# Agora o extrator de pinos funciona, mas poderia ser mais eficiente! Ele poderia extrair o pino de muitos poemas ao mesmo tempo!
# Adicione mais dois poemas no escopo global, poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow' e poem3 = 'There\nonce\nwas\na\ndragon', e por enquanto, comente o print com a chamada para pin_extractor.

'''def pin_extractor(poem):
    secret_code = ""
    lines = poem.split("\n")
    for line_index, line in enumerate(lines):
        words = line.split()
        if len(words) > line_index:
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
        
    return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"

poem3 = "There\nonce\nwas\na\ndragon"

# print(pin_extractor(poem))'''

# Atualize o argumento da função para ser poems, depois crie um loop for envolvendo todo o conteúdo atual da função que itere sobre poems e use poem como variável do loop.

'''def pin_extractor(poem):
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        return secret_code

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"

poem3 = "There\nonce\nwas\na\ndragon"

# print(pin_extractor(poem))'''

# Antes do loop, crie uma nova variável secret_codes que tenha um valor inicial de uma lista vazia.
# Então substitua a linha return secret_code por uma linha que adicione secret_code à lista secret_codes.

'''def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"

poem3 = "There\nonce\nwas\na\ndragon"

# print(pin_extractor(poem))'''

# Finalmente, retorne secret_codes, depois descomente a chamada da função e atualize o argumento para ser [poem, poem2, poem3]. 
# Agora sua função funciona com vários poemas ao mesmo tempo e pode extrair vários pinos!
# A função pin_extractor está concluída.

def pin_extractor(poems):
    
    secret_codes = []
    
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

poem2 = "The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow"

poem3 = "There\nonce\nwas\na\ndragon"

print(pin_extractor([poem, poem2, poem3]))