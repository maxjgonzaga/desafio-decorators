#DESAFIO DECORATORS
# Crie um decorador que irá pegar a função que for passado para ele e imprimir o horario atual 
# antes de executar a função e depois imprimir o horario após ter finalizado a execução da função. 
# DICA:  Você tera que usar o modulo datetime para conseguir o horario atual 
# RESOLUÇÃO JONATHAN 
from datetime import datetime 

def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor 

@monitorar_horario
def baixar_musicas(): 
    print('Baixando músicas')

baixar_musicas()