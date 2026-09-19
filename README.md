# exercicios-cursoemvideo-mundo-python-2

### 1\. Condições Aninhadas (`if`, `elif`, `else`) – Aula 12

* **Conceito:** Enquanto as condições simples e compostas tratam apenas de duas alternativas (verdadeiro ou falso), problemas mais complexos exigem tratar três ou mais opções de caminho[2][3].
* **Estrutura Aninhada:** Quando há múltiplas opções, utilizam-se estruturas condicionais aninhadas, em que uma condição é colocada dentro de outra[4][5].
* **Comando** **elif** **:** Surge da junção das palavras *else* ("senão") e *if* ("se")[4].
* **Regras de Sintaxe:**
  * O bloco sempre se inicia obrigatoriamente com a instrução `if`[6].
  * É possível incluir quantos blocos `elif` forem necessários[5][6].
  * O bloco `else` é opcional no final e pode aparecer no máximo uma vez[5][6].
  * Não é permitido utilizar a instrução `elif` sem um `if` correspondente antes[6].

---

### 2\. Estrutura de Repetição `for` (Laço com Variável de Controle) – Aula 13

* **Conceito:** O `for` é classificado como uma estrutura de repetição com variável de controle, sendo indicado para casos em que se conhece de antemão o limite ou a quantidade exata de repetições a realizar[7].
* **Instrução** **range()** **:** A sintaxe padrão segue o formato `for C in range(inicio, fim, passo):`[10][11].
* **Comportamento do Limite Final:** No Python, a contagem na função `range()` sempre ignora o último número do intervalo informado[12][13]. Dessa forma, `range(1, 10)` executa de 1 até 9; para que a contagem vá até 10, deve-se declarar `range(1, 11)`[12][13].
* **Passo e Contagem Regressiva:** É possível definir o incremento (ex: `range(0, 7, 2)` salta de 2 em 2) ou realizar contagens regressivas atribuindo um valor de passo negativo (ex: `range(6, -1, -1)`)[11].
* **Indentação:** A correta tabulação do código determina quais comandos estão contidos dentro da repetição e quais estão fora[10].

---

### 3\. Estrutura de Repetição `while` (Laço com Teste Lógico) – Aula 14

* **Conceito:** O `while` é uma estrutura de repetição baseada em teste lógico, ideal para cenários em que **não se sabe previamente o limite** de repetições[8].
* **Funcionamento:** A repetição continua sendo executada enquanto a condição lógica verificada no início permanecer verdadeira (`True`)[9][15].
* **Uso de Flags (Pontos de Parada):** É muito aplicado com valores de parada definidos pelo usuário (por exemplo, manter a leitura de dados até que um valor específico, como `0` ou `999`, seja digitado)[15].

---

### 4\. Interrupção de Repetições e F-Strings – Aula 15

* **Loops Infinitos e o Comando** **break** **:**
  * Ao utilizar a sintaxe `while True:`, cria-se um laço de repetição infinito[18].
  * A instrução `break` interrompe a repetição imediatamente, desviando a execução para fora do laço[18].
* **F-Strings (PEP 498):**
  * Recurso de interpolação de strings introduzido a partir do Python 3.6 para simplificar a formatação de saídas de dados[23][24].
  * Permite inserir variáveis diretamente na string utilizando o prefixo `f` e chaves `{}` (ex: `print(f'O {nome} tem {idade} anos')`)[23][25].
  * Suporta especificadores de formatação diretamente nas chaves, como controle de casas decimais (ex: `{salario:.2f}`) e alinhamentos de texto[24].
