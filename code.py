import calendar
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def mostrar_tabela_cortes(cortes):
    print('\nEssa é nossa tabela de valores:\n')
    for idx, (nome, valor) in enumerate(cortes.items(), start=1):
        print(f"{idx}. {nome.title()} - {valor}")

def selecionar_corte(cortes):
    mostrar_tabela_cortes(cortes)
    while True:
        escolha = input('\nDigite o número do corte desejado: ')
        if escolha.isdigit() and 1 <= int(escolha) <= len(cortes):
            nome = list(cortes.keys())[int(escolha)-1]
            valor = cortes[nome]
            return f"{nome.title()}: {valor}"
        else:
            print('Erro: Opção inválida. Tente novamente.')

def selecionar_dia():
    dias_validos = {
        'terca': "Terça-Feira",
        'quarta': "Quarta-Feira",
        'quinta': "Quinta-Feira",
        'sexta': "Sexta-Feira",
        'sabado': "Sábado"
    }
    print(calendar.month(2025, 9))
    while True:
        dia = remover_acentos(input('\nQual dia da semana será o corte? (Terça, Quarta, Quinta, Sexta, Sábado)\n')).lower()
        if dia in dias_validos:
            return dias_validos[dia]
        elif dia in ['domingo', 'segunda']:
            print('ERRO: Não abrimos de domingo ou segunda, selecione outra data.')
        else:
            print('Erro: Dia inválido, tente novamente.')

def selecionar_horario():
    horarios = ["10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
    print('\nHorários disponíveis:')
    for idx, h in enumerate(horarios, start=1):
        print(f"{idx}. {h}")
    while True:
        escolha = input('\nDigite o número do horário desejado: ')
        if escolha.isdigit() and 1 <= int(escolha) <= len(horarios):
            return horarios[int(escolha)-1]
        else:
            print('Erro: Horário inválido, tente novamente.')

def selecionar_pagamento():
    pagamentos = ["debito", "credito", "dinheiro", "pix"]
    print('\nFormas de pagamento:')
    for idx, p in enumerate(pagamentos, start=1):
        print(f"{idx}. {p.title()}")
    while True:
        escolha = remover_acentos(input('Qual será a forma de pagamento? ')).lower()
        if escolha in pagamentos:
            return escolha.title()
        else:
            print("Erro: Método de pagamento não aceito. Tente novamente.")

def agendamento(name, cortes):
    print(f'\nOlá, seja bem-vindo(a) ao Sanchess Barber, {name}!')
    corte = selecionar_corte(cortes)
    dia = selecionar_dia()
    horario = selecionar_horario()
    pagamento = selecionar_pagamento()

    print('\n***** CARRINHO *****')
    print(f"Cliente: {name}")
    print(f"Corte: {corte}")
    print(f"Dia: {dia}")
    print(f"Horário: {horario}")
    print(f"Método de pagamento: {pagamento}")
    print('\n***** Prossiga para o pagamento! *****')
    

def main():
    cortes = {
        "degrade": "R$25,00",
        "navalhado": "R$25,00",
        "social": "R$20,00",
        "sombrancelha": "R$20,00",
        "degrade pigmentado": "R$35,00",
        "luzes": "R$100,00",
        "combo": "R$45,00"
    }
    print('Olá, seja bem-vindo ao Sanchess Barber')
    name = input('Qual seu nome? ').strip().title()

    while True:
        primeira_vez = remover_acentos(input(f'{name}, é sua primeira vez cortando conosco? (sim/não) ')).lower()
        if primeira_vez == 'sim':
            print(f'\nSeja muito bem-vindo(a), {name}. Ficamos felizes pela preferência!')
            agendamento(name, cortes)
            break
        elif primeira_vez == 'nao':
            print(f'\nSeja muito bem-vindo(a) novamente, {name}. Ficamos felizes pelo retorno!')
            agendamento(name, cortes)
            break
        else:
            print('Erro: Responda apenas com "sim" ou "não".')

if __name__ == "__main__":
    main()
