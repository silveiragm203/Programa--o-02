# ANOTAÇÕES DE FUNDAMENTOS DA PROGRAMAÇÃO

##Tipos de dados em pyhton
1. string
2. number int
3. number float
4. boolean

## Operadores Matématicos - básicos
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão

## Métodos em Python
1. print() -> Exibe informações no terminal.
2. input () -> captura informações do terminal.

## Format em Python

#  Estrutura de Condicional
 ``if (se)`` -> Verifica se uma condição é true (verdadeira). Se for, ele executa o código.
 ``elif (senão se)`` -> é usado para testar várias condições.Ele só executa se todas as condições anteriores forem falsas.
 ``else (senão)`` -> Executa o código se a condição for false (false).

# Laços de repetição
É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop, Laços de repetição ou interação.
`FOR` -> Utilizamos quando sabemos quantas vezes queremos repetir algo.
Sintax:
for (variavel) in range(inicio,fim):
    comandos
[Range()] -> Método que aceita geração de números.
[inicio] -> É inclusivo. é o primeiro número a ser utilizado.
[fim] -> É exclusivo. O número
## Escopo das Variáveis
`Escopo Local` -> A variável ela só é acessada dentro da estrutura que ela foi criada.
`Escopo Global` -> A variável pode ser acessada por todo mundo.

## Variações das variáveis 
Variável em memória -> É declarada quando você não pretende utilizar essa variável em outros cenários.
Váriavel Contadora -> É utilizada para uma lógica onde a repetição irá ser alterada.

`WHILE` -> É utilizado quando não sabemos quantas vezes o programa vai repetir. Ele enquanto uma condição for verdadeira.
Sintaxe:
while condição:
    comandos


## Conversão de tipos em python
 1. int() -> A gente vai incluir qual variável/dado que querremos converter para número inteiro.
 2. float() -> A gente vai incluir qual variável/dado que querremos converter para número decimal.
 3. str() ->  A gente vai incluir qual variável/dado que querremos converter para texto.


  ## Boas Práticas
  1. Qualquer variável em python utiliza o padrão de case , snake_case ou recentemente o cammelCase.
  2. Se você observar alguma estrutura tipo nome (), 90% de chance de ser uma função.
  3. Python não tem constante , porém utilizamos o padrão case , UPPERCASE , para simular que aquela variável não pode ser alterada.
 