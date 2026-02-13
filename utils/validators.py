from rich.prompt import Prompt
from utils.ui import erro

def validar_mes(mensagem='Mês (1-12)'):
        try:
            mes = int(Prompt.ask(mensagem))
        except ValueError:
            erro('Digite um número válido.')
            return None
        
        if mes < 1 or mes > 12:
            erro('Mês Inválido. Use valores entre 1 e 12.')
            return None
        
        return mes


def validar_ano(mensagem='Ano'):
    try:
        ano = int(Prompt.ask(mensagem))
    except ValueError:
        erro('Digite um ano válido')

    if ano < 2000 or ano > 2100:
        erro('Ano fora do intervalo esperado.')
        return None
    
    return ano


def validar_valor(mensagem='Valor'):
    try:
        valor = float(Prompt.ask(mensagem).replace(",", "."))
    except ValueError:
        erro('Valor inválido.')
        return None
    
    if valor <= 0:
        erro('O valor deve ser maior que zero.')
        return None
    
    return valor