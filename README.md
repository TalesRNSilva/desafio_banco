# Desafio sistema bancário.
Desafio criando um sistema bancário em Python do DIO.

## O que fizemos:
1. O extrato é uma lista de strings, em vez de uma string grande.
2. Adicionamos três operações:
    - A primeira "Informações" mostra o limite de saques, o número máximo de saques, o saldo e o número de saques realizados.
    - A segunda, "Virar o dia", reinicia o número de saques realizados.
    - A terceira, "Alterar Exibição", leva o usuário para um prompt onde ele pode alterar o número de transações exibidas no extrato e a largura da exibição do extrato. 
3. Print do extrato é reformulado com base na alteração do extrato em uma lista. Os valores são exibidos de maneira centralizada. Uma vez que o valor da largura da exibição é uma variável, todo print feito também é dinâmico.
4. Alterações menores: a cada saque ou depósito, o valor do saldo é exibido na tela. No extrato, se exibe o saldo total após a transação e o número da transação efetuada. Este último é indexado pelo próprio índice da lista extrato.