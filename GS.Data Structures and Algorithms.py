# Mission Control AI — Monitoramento de Missão Espacial
# Global Solution 2026.1 - Data Structures and Algorithms

# Lista que armazena o histórico de todas as leituras da missão
historico_leituras = []


def exibir_menu():
    """
    Função responsável por exibir o menu principal do sistema.
    """
    print("\n========== MISSION CONTROL AI ==========")
    print("1. Inserir dados da missão")
    print("2. Visualizar status atual")
    print("3. Executar análise automática")
    print("4. Exibir histórico das leituras")
    print("5. Encerrar sistema")
    print("========================================")


def inserir_dados():
    """
    Função responsável por receber os dados da missão digitados pelo usuário.
    Os dados são armazenados na lista historico_leituras.
    """
    print("\n--- Inserir dados da missão ---")

    try:
        temperatura = float(input("Digite a temperatura da nave em °C: "))

        # Validação simples da temperatura
        if temperatura < -100 or temperatura > 150:
            print("Erro: temperatura inválida. Digite um valor realista entre -100 °C e 150 °C.")
            return

        energia = float(input("Digite o nível de energia em porcentagem: "))

        # Validação do nível de energia
        if energia < 0 or energia > 100:
            print("Erro: o nível de energia deve estar entre 0% e 100%.")
            return

        comunicacao = int(input("Digite o status da comunicação (1 = ativa, 0 = falha): "))

        # Validação da comunicação
        if comunicacao != 0 and comunicacao != 1:
            print("Erro: a comunicação deve ser 1 para ativa ou 0 para falha.")
            return

        leitura = {
            "temperatura": temperatura,
            "energia": energia,
            "comunicacao": comunicacao,
            "status_operacional": "Aguardando análise"
        }

        historico_leituras.append(leitura)

        print("\nDados inseridos com sucesso!")
        print("Status da leitura: Aguardando análise.")

    except ValueError:
        print("Erro: digite apenas valores numéricos.")


def analisar_dados(leitura):
    """
    Função responsável por analisar uma leitura da missão.
    Ela verifica temperatura, energia e comunicação.
    """
    alertas = []

    if leitura["temperatura"] > 80:
        alertas.append("Alerta de superaquecimento")

    if leitura["energia"] < 20:
        alertas.append("Ativar modo de economia de energia")

    if leitura["comunicacao"] == 0:
        alertas.append("Falha de comunicação")

    # Classificação do status operacional conforme a quantidade de alertas
    if len(alertas) == 0:
        leitura["status_operacional"] = "MISSÃO NORMAL"
    elif len(alertas) == 1:
        leitura["status_operacional"] = "MISSÃO EM ATENÇÃO"
    else:
        leitura["status_operacional"] = "MISSÃO CRÍTICA"

    return alertas


def visualizar_status_atual():
    """
    Função responsável por mostrar a última leitura cadastrada no sistema.
    """
    print("\n--- Status atual da missão ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada ainda.")
    else:
        ultima_leitura = historico_leituras[-1]

        print("Mostrando a leitura mais recente cadastrada:")
        print(f"Temperatura da nave: {ultima_leitura['temperatura']} °C")
        print(f"Nível de energia: {ultima_leitura['energia']}%")

        if ultima_leitura["comunicacao"] == 1:
            print("Comunicação: Ativa")
        else:
            print("Comunicação: Falha")

        print(f"Status operacional: {ultima_leitura['status_operacional']}")


def executar_analise_automatica():
    """
    Função responsável por executar a análise automática da última leitura cadastrada.
    """
    print("\n--- Análise automática da missão ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada para análise.")
    else:
        ultima_leitura = historico_leituras[-1]

        print("Analisando a leitura mais recente cadastrada...")

        alertas = analisar_dados(ultima_leitura)

        if len(alertas) == 0:
            print("Nenhum alerta encontrado na leitura mais recente.")
            print("A missão está operando normalmente.")
        else:
            print("Alertas encontrados na leitura mais recente:")
            for alerta in alertas:
                print(f"- {alerta}")

        print(f"Status operacional atualizado: {ultima_leitura['status_operacional']}")


def exibir_historico():
    """
    Função responsável por exibir todas as leituras armazenadas.
    """
    print("\n--- Histórico das leituras ---")

    if len(historico_leituras) == 0:
        print("Nenhuma leitura foi cadastrada ainda.")
    else:
        contador = 1

        for leitura in historico_leituras:
            print(f"\nLeitura {contador}:")
            print(f"Temperatura: {leitura['temperatura']} °C")
            print(f"Energia: {leitura['energia']}%")

            if leitura["comunicacao"] == 1:
                print("Comunicação: Ativa")
            else:
                print("Comunicação: Falha")

            print(f"Status operacional: {leitura['status_operacional']}")

            contador += 1


def sistema_principal():
    """
    Função principal do programa.
    Controla o funcionamento do menu interativo.
    """
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_dados()

        elif opcao == "2":
            visualizar_status_atual()

        elif opcao == "3":
            executar_analise_automatica()

        elif opcao == "4":
            exibir_historico()

        elif opcao == "5":
            print("\nEncerrando o sistema Mission Control AI...")
            print("Sistema finalizado com sucesso.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


# Início do programa
sistema_principal()