import json
import csv
import os

ARQUIVO_JSON = "dados_financeiros.json"

# Dados em memória
receitas = []
despesas = []
metas = {}

# Funções de persistência
def salvar_dados():
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as f:
        json.dump({"receitas": receitas, "despesas": despesas, "metas": metas}, f, indent=4)

def carregar_dados():
    global receitas, despesas, metas
    if os.path.exists(ARQUIVO_JSON):
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as f:
            dados = json.load(f)
            receitas = dados.get("receitas", [])
            despesas = dados.get("despesas", [])
            metas = dados.get("metas", {})

def exportar_csv():
    nome_arquivo = input("Nome do arquivo CSV (ex: relatorio.csv): ")
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tipo", "Valor", "Categoria", "Data"])
        for r in receitas:
            writer.writerow(["Receita", r["valor"], r["categoria"], r["data"]])
        for d in despesas:
            writer.writerow(["Despesa", d["valor"], d["categoria"], d["data"]])
    print("✅ Relatório exportado com sucesso!")


def adicionar_registro(tipo):
    try:
        valor = float(input("Valor: R$ "))
        categoria = input("Categoria: ")
        data = input("Data (dd/mm/aaaa): ")
        registro = {"valor": valor, "categoria": categoria, "data": data}
        if tipo == "receita":
            receitas.append(registro)
        else:
            despesas.append(registro)
        salvar_dados()
        print(f"✅ {tipo.title()} adicionada com sucesso!")
    except ValueError:
        print("❌ Valor inválido.")

def definir_meta():
    mes = input("Mês da meta (mm/aaaa): ")
    try:
        valor = float(input("Valor da meta: R$ "))
        metas[mes] = valor
        salvar_dados()
        print(f"🎯 Meta de R$ {valor:.2f} definida para {mes}.")
    except ValueError:
        print("❌ Valor inválido.")

def gerar_relatorio():
    mes = input("Mês do relatório (mm/aaaa): ")
    receitas_mes = sum(r["valor"] for r in receitas if r["data"].endswith(mes))
    despesas_mes = sum(d["valor"] for d in despesas if d["data"].endswith(mes))
    saldo = receitas_mes - despesas_mes
    meta = metas.get(mes)
    progresso = (saldo / meta * 100) if meta else None

    print("\n📊 RELATÓRIO FINANCEIRO")
    print(f"Mês: {mes}")
    print(f"Receitas: R$ {receitas_mes:.2f}")
    print(f"Despesas: R$ {despesas_mes:.2f}")
    print(f"Saldo: R$ {saldo:.2f}")
    if meta:
        print(f"Meta: R$ {meta:.2f}")
        print(f"Progresso da meta: {progresso:.1f}%")
    else:
        print("Meta: Não definida.")

# Menu principal
def menu():
    carregar_dados()
    while True:
        print("\n=== MENU FINANCEIRO ===")
        print("1. Adicionar Receita")
        print("2. Adicionar Despesa")
        print("3. Definir Meta de Economia")
        print("4. Gerar Relatório Mensal")
        print("5. Exportar Relatório CSV")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_registro("receita")
        elif escolha == "2":
            adicionar_registro("despesa")
        elif escolha == "3":
            definir_meta()
        elif escolha == "4":
            gerar_relatorio()
        elif escolha == "5":
            exportar_csv()
        elif escolha == "6":
            print("👋 Saindo do sistema. Até mais!")
            break
        else:
            print("❌ Opção inválida.")

# Executar
if __name__ == "__main__":
    menu()
