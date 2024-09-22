import re

def ler_arquivo(file_path):
    with open(file_path, 'r') as file:
        linhas = file.readlines() 
    return [linha.strip() for linha in linhas]

def escrever_em_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding="UTF-8") as arquivo:
        arquivo.write(conteudo) 

def produce_result_string():
    result = ""
    result += "Tokens de Entrada\n" 
    for tokenValido in tokensValidos:
        result += tokenValido + "\n"
    
    result += "\nTabela de Símbolos\n"
    simbolosIndex = 1
    for identificador in identificadores + numerosInteiros + numerosReais:
        result += str(simbolosIndex) + " - " + identificador + "\n"
        simbolosIndex += 1
    
    result += "\nErros nas linhas:\n"
    for tokenInvalido in tokensInvalidos:
        result += tokenInvalido + "\n"
    
    return result

palavrasReservadas = {
    "int" : "INT",
    "double" : "DOUBLE",
    "float" : "FLOAT",
    "real" : "REAL",
    "break" : "BREAK",
    "case" : "CASE",
    "char" : "CHAR",
    "const" : "CONST",
    "continue" : "CONTINUE"
}
comentario = "//"
identificadorRegex = r'^[a-zA-Z][a-zA-Z0-9]*$'
numeroInteiroRegex = r'^[0-9][0-9]$'
numeroRealRegex = r'^[0-9][0-9].[0-9][0-9]$'

tokensValidos = []
tokensInvalidos = []
identificadores = []
numerosInteiros = []
numerosReais = []

def main():
    dados = ler_arquivo('dados.txt')
    lineCounter = 1
    for palavra in dados:
        if palavra in palavrasReservadas:
            tokensValidos.append(f"[{lineCounter}] {palavrasReservadas[palavra]}")
        elif palavra[:len(comentario)] == comentario :
            tokensValidos.append(f"[{lineCounter}] COMENTARIO")
        elif re.match(identificadorRegex, palavra):
            if palavra not in identificadores:
                identificadores.append(palavra)
            index = identificadores.index(palavra)
            tokensValidos.append(f"[{lineCounter}] IDENTIFICADOR {index + 1}")
        elif re.match(numeroInteiroRegex, palavra):
            if palavra not in numerosInteiros:
                numerosInteiros.append(palavra)
            index = numerosInteiros.index(palavra)       
            tokensValidos.append(f"[{lineCounter}] NÚMERO INTEIRO {index + 1}")
        elif re.match(numeroRealRegex, palavra):
            if palavra not in numerosReais:
                numerosReais.append(palavra)
            index = numerosReais.index(palavra)
            tokensValidos.append(f"[{lineCounter}] NÚMERO REAL {index + 1}")
        else:
            tokensInvalidos.append(f"[{lineCounter}] ({palavra})")
        lineCounter += 1

    escrever_em_arquivo("result.txt", produce_result_string())

main()