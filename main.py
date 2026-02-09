from inputs import escolher_aba
from excel_manager import carregar_planilha
from services.finance import registrar_entrada, registrar_gasto


def main():
    wb = carregar_planilha()
    aba = escolher_aba()
    
    if aba is None:
        print("Encerrando o programa.")
        return
    
    elif aba == 'E':
        registrar_entrada(wb)
        print('ENTRADA REGISTRADA COM SUCESSO!')
        
    elif aba == 'G':
        registrar_gasto(wb)
        print('GASTO REGISTRADO COM SUCESSO!')

if __name__ == "__main__":
    main()