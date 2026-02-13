from rich.prompt import Prompt
from utils.ui import erro

def validar_mes(mensagem='Mês (1-12)'):
    while True:
        try:
            mes = int(Prompt.ask(mensagem))
        except ValueError:
            erro('Digite um número válido.')
            continue
        
        if 1 <= mes <= 12:
            return mes
        
        erro('Mês Inválido. Use valores entre 1 e 12.')


def validar_ano(mensagem='Ano'):
    while True:
        try:
            ano = int(Prompt.ask(mensagem))
        except ValueError:
            erro('Digite um ano válido')
            continue

        if 2000 <= ano <= 2100:
            return ano
        
        erro('Ano fora do intervalo esperado.')


def validar_valor(mensagem='Valor'):
    while True:
        try:
            valor = float(Prompt.ask(mensagem).replace(",", "."))
        except ValueError:
            erro('Valor inválido.')
            continue
        
        if valor > 0:
            return valor

        erro('O valor deve ser maior que zero.')


def validar_texto(mensagem='Digite um texto'):
    while True:
        texto = Prompt.ask(mensagem).strip()

        if not texto:
            erro('Campo não pode ser vazio.')
        
        if texto.isnumeric():
            erro('Texto não pode ser apenas numérico.')
            continue
        
        return texto