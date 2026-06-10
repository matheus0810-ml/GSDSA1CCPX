# GSDSA1CCPX

# Documentação do Projeto — Mission Control AI

## 1. Identificação

**Aluno:** Matheus Carpinheiro Moreno
**RM:** 571770
**Turma:** 1CCPX
**Curso:** Ciência da Computação — 1º semestre
**Instituição:** FIAP
**Disciplina:** Data Structures and Algorithms
**Projeto:** Global Solution 2026.1
**Nome do sistema:** Mission Control AI — Monitoramento de Missão Espacial

---

## 2. Contextualização do Projeto

O projeto **Mission Control AI — Monitoramento de Missão Espacial** foi desenvolvido com o objetivo de simular um sistema simples de controle e acompanhamento de uma missão espacial experimental.

De acordo com o enunciado da Global Solution, o sistema deve monitorar informações básicas da missão, como **temperatura da nave**, **nível de energia**, **comunicação** e **status operacional**, utilizando conceitos de programação como condicionais, laços de repetição, listas/vetores e funções. 

Em uma missão espacial real, sistemas computacionais são responsáveis por acompanhar dados importantes para garantir a segurança e o funcionamento correto da operação. Neste projeto, essa ideia foi representada por meio de um programa em Python que permite cadastrar leituras simuladas, analisar automaticamente os dados e apresentar alertas quando algum valor estiver fora do esperado.

---

## 3. Objetivo do Sistema

O objetivo principal do sistema é permitir que o usuário insira dados simulados de uma missão espacial e receba uma análise automática sobre a situação da operação.

O programa verifica três informações principais:

**Temperatura da nave:** usada para identificar risco de superaquecimento.
**Nível de energia:** usado para identificar necessidade de economia de energia.
**Comunicação:** usada para verificar se a missão está com comunicação ativa ou com falha.

Com base nesses dados, o sistema atualiza o **status operacional da missão**, classificando a situação como normal, em atenção ou crítica.

---

## 4. Linguagem Utilizada

A linguagem escolhida para o desenvolvimento foi **Python**, por ser uma linguagem simples, clara e adequada para projetos introdutórios de lógica de programação e estruturas de dados.

O enunciado permite o uso de linguagens como C, Python ou JavaScript, e o projeto foi desenvolvido em Python para facilitar a organização do menu, das funções, das validações e do histórico de leituras. 

---

## 5. Funcionalidades do Sistema

O sistema possui um menu interativo com cinco opções principais:

1. Inserir dados da missão
2. Visualizar status atual
3. Executar análise automática
4. Exibir histórico das leituras
5. Encerrar sistema

Essas opções seguem o que foi solicitado no enunciado da atividade, que pede um menu com inserção de dados, visualização de status, análise automática, histórico de leituras e encerramento do sistema. 

---

# Explicação Lógica do Código

## 6. Estrutura Geral do Programa

O código começa criando uma lista chamada:

```python
historico_leituras = []
```

Essa lista é responsável por armazenar todas as leituras cadastradas pelo usuário durante a execução do programa. Cada leitura é salva como um dicionário contendo temperatura, energia, comunicação e status operacional. 

Essa escolha atende ao requisito de uso de estruturas de dados, pois o programa utiliza uma lista para guardar várias leituras e dicionários para organizar as informações de cada leitura.

---

## 7. Função `exibir_menu()`

A função `exibir_menu()` mostra o menu principal do sistema no terminal.

Ela apresenta as opções disponíveis para o usuário escolher o que deseja fazer. Essa função ajuda a deixar o código mais organizado, pois evita que o menu fique repetido em várias partes do programa. 

---

## 8. Função `inserir_dados()`

A função `inserir_dados()` é responsável por receber os dados digitados pelo usuário.

Primeiro, o sistema solicita a temperatura da nave. Depois, verifica se o valor está dentro de uma faixa realista, entre **-100 °C e 150 °C**. Caso o valor esteja fora desse intervalo, o programa exibe uma mensagem de erro e não salva a leitura.

Depois, o sistema solicita o nível de energia. A energia precisa estar entre **0% e 100%**. Se o usuário digitar um valor menor que 0 ou maior que 100, o sistema também exibe uma mensagem de erro.

Em seguida, o programa solicita o status da comunicação, aceitando apenas:

```python
1 = comunicação ativa
0 = falha de comunicação
```

Se o usuário digitar qualquer outro valor, a leitura não será cadastrada.

Quando todos os dados são válidos, o programa cria uma leitura com o seguinte formato:

```python
leitura = {
    "temperatura": temperatura,
    "energia": energia,
    "comunicacao": comunicacao,
    "status_operacional": "Aguardando análise"
}
```

Essa leitura é adicionada à lista `historico_leituras`. 

---

## 9. Função `analisar_dados(leitura)`

A função `analisar_dados()` é responsável pela análise automática da missão.

Ela recebe uma leitura e verifica três condições principais:

```python
if leitura["temperatura"] > 80:
    alertas.append("Alerta de superaquecimento")
```

Se a temperatura for maior que 80 °C, o sistema identifica risco de superaquecimento.

```python
if leitura["energia"] < 20:
    alertas.append("Ativar modo de economia de energia")
```

Se a energia for menor que 20%, o sistema indica a necessidade de economia de energia.

```python
if leitura["comunicacao"] == 0:
    alertas.append("Falha de comunicação")
```

Se a comunicação for igual a 0, o sistema identifica falha de comunicação.

Essas verificações seguem exatamente as condições obrigatórias do enunciado: temperatura maior que 80 gera alerta de superaquecimento, energia menor que 20 indica economia de energia e comunicação igual a 0 indica falha de comunicação. 

---

## 10. Classificação do Status Operacional

Após verificar os alertas, o sistema classifica a situação da missão de acordo com a quantidade de problemas encontrados.

Se não houver nenhum alerta:

```python
status_operacional = "MISSÃO NORMAL"
```

Se houver apenas um alerta:

```python
status_operacional = "MISSÃO EM ATENÇÃO"
```

Se houver dois ou mais alertas:

```python
status_operacional = "MISSÃO CRÍTICA"
```

Essa lógica torna o sistema mais completo, pois além de mostrar os alertas específicos, também apresenta uma classificação geral da missão. 

---

## 11. Função `visualizar_status_atual()`

A função `visualizar_status_atual()` mostra a última leitura cadastrada no sistema.

Se ainda não houver nenhuma leitura salva, o programa informa que nenhuma leitura foi cadastrada. Caso exista pelo menos uma leitura, o sistema mostra:

**Temperatura da nave**
**Nível de energia**
**Status da comunicação**
**Status operacional da missão**

Para acessar a leitura mais recente, o programa usa:

```python
ultima_leitura = historico_leituras[-1]
```

Isso significa que ele pega o último item da lista de histórico. 

---

## 12. Função `executar_analise_automatica()`

A função `executar_analise_automatica()` analisa a leitura mais recente cadastrada.

Se não houver nenhuma leitura, o sistema informa que não existem dados para análise. Caso exista uma leitura, o programa chama a função `analisar_dados()` e exibe os alertas encontrados.

Se nenhum alerta for encontrado, o sistema informa que a missão está operando normalmente.

Se houver alertas, eles são exibidos um por um usando um laço de repetição:

```python
for alerta in alertas:
    print(f"- {alerta}")
```

Depois disso, o programa mostra o status operacional atualizado. 

---

## 13. Função `exibir_historico()`

A função `exibir_historico()` mostra todas as leituras armazenadas na lista `historico_leituras`.

Se a lista estiver vazia, o sistema informa que nenhuma leitura foi cadastrada. Caso contrário, o programa percorre todas as leituras usando um laço `for` e exibe os dados de cada uma.

Essa função atende ao requisito de histórico das leituras, permitindo que o usuário acompanhe os registros feitos durante a execução do programa. 

---

## 14. Função `sistema_principal()`

A função `sistema_principal()` controla o funcionamento geral do programa.

Ela usa um laço de repetição `while True` para manter o sistema funcionando até que o usuário escolha a opção 5, que encerra o programa.

A cada repetição, o menu é exibido novamente e o usuário pode escolher uma das opções disponíveis.

A lógica principal é feita com estruturas condicionais:

```python
if opcao == "1":
    inserir_dados()
elif opcao == "2":
    visualizar_status_atual()
elif opcao == "3":
    executar_analise_automatica()
elif opcao == "4":
    exibir_historico()
elif opcao == "5":
    break
else:
    print("Opção inválida.")
```

Essa estrutura permite controlar o fluxo do sistema de forma simples e organizada. 

---

# Explicação do Fluxograma

O fluxograma representa visualmente o caminho lógico do sistema.

Ele começa no bloco **Início** e em seguida apresenta a etapa de escolha da opção no menu. O usuário pode escolher entre inserir dados, visualizar o status atual, executar análise automática, exibir o histórico ou encerrar o sistema.

Na opção de inserir dados, o fluxograma mostra a entrada da temperatura, do nível de energia e da comunicação. Depois de cada entrada, ocorre uma validação. Se algum valor for inválido, o sistema exibe uma mensagem de erro e retorna ao fluxo principal. Se todos os valores forem válidos, os dados são salvos no histórico com o status inicial de “Aguardando análise”.

Na parte de análise automática, o fluxograma mostra as verificações de temperatura maior que 80, energia menor que 20 e comunicação igual a 0. Cada condição pode gerar um alerta específico.

Depois disso, o sistema verifica a quantidade de alertas para definir o status operacional:

**0 alertas:** Missão normal
**1 alerta:** Missão em atenção
**2 ou 3 alertas:** Missão crítica

Por fim, o sistema pode continuar no menu ou ser encerrado quando o usuário escolher a opção 5.

---

# Estruturas de Programação Utilizadas

## Condicionais

As estruturas condicionais são usadas para verificar opções do menu, validar dados digitados e analisar as condições da missão.

Exemplos:

```python
if temperatura < -100 or temperatura > 150:
```

```python
if energia < 0 or energia > 100:
```

```python
if leitura["temperatura"] > 80:
```

## Laços de repetição

O laço `while True` mantém o menu funcionando até o usuário escolher encerrar o sistema.

O laço `for` é usado para percorrer os alertas e também para exibir todas as leituras do histórico.

## Lista

A lista `historico_leituras` armazena todas as leituras cadastradas durante a execução do programa.

## Dicionário

Cada leitura é armazenada em formato de dicionário, separando os dados por chave e valor.

## Funções

O código foi dividido em funções para deixar o programa mais organizado, facilitar a leitura e separar responsabilidades.

---

# Relação com os Critérios de Avaliação

O projeto atende aos critérios de avaliação indicados no enunciado.

No critério **Funcionamento do Sistema**, o programa possui menu, cadastro de dados, análise automática, histórico e encerramento.

No critério **Uso correto das estruturas de dados**, o sistema utiliza lista, dicionários, laços de repetição, condicionais e funções.

No critério **Organização do código**, as responsabilidades foram separadas em funções específicas, deixando o sistema mais limpo e compreensível.

No critério **Lógica implementada**, o programa analisa corretamente temperatura, energia e comunicação, emitindo alertas e classificando o status operacional da missão. 

---

# Conclusão

O sistema **Mission Control AI — Monitoramento de Missão Espacial** simula de forma simples e organizada o acompanhamento de uma missão espacial experimental.

O programa permite cadastrar dados simulados, validar as informações inseridas, analisar automaticamente a situação da missão, emitir alertas e armazenar o histórico das leituras.

A lógica implementada atende aos requisitos da Global Solution 2026.1 da disciplina Data Structures and Algorithms, utilizando conceitos fundamentais de programação, como funções, listas, dicionários, condicionais e laços de repetição.

Dessa forma, o projeto demonstra como a programação pode ser aplicada em um cenário de monitoramento operacional, aproximando conceitos acadêmicos de uma situação prática relacionada à indústria espacial.
