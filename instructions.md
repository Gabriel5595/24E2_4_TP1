Olá, Gabriel,

Chegamos em uma das etapas de preparação! A cada Teste de Performance (TP) você terá a oportunidade de praticar os conhecimentos adquiridos e receber feedbacks relevantes para o seu aprendizado.

Considere o desenvolvimento de um sistema de notas para uma instituição de ensino. O cadastro deve permitir que sejam alimentadas as notas de três unidades, calcular a média e apresentar o resultado como aprovado, caso a média seja maior ou igual a 7,0. O aluno será identificado pelo número de registro e pelo nome. Utilizando apenas listas, desenvolva os seguintes códigos e funções:

1. Crie uma lista para receber os cadastros de todos os alunos.
2. Crie uma função que solicite os dados do aluno, incluindo nome e sobrenome, e se desejar, as notas. Caso queira, solicite cada uma da notas, caso não, as notas devem ser inicializadas como 0,0. A função deve retornar uma lista contendo os seguintes dados: [“nome sobrenome”, nota1, nota2, nota2, media], sendo dos tipos [string, float, float, float, float].
3. Crie uma função para preencher as notas e calcular a média. Ela deverá receber como parâmetro a lista referente ao aluno que terá suas notas atualizadas, e solicitar a nota que deseja atualizar e calcular a média do aluno. O retorno deve ser a lista que foi recebida como entrada, com os valores de notas e média atualizados.
4. Crie uma função que liste os alunos aprovados ou reprovados. Deverão ser passados como parâmetros a lista com o banco de dados dos alunos e um parâmetro para escolher qual tipo de listagem deve ser feita (aprovado=True ou aprovado=False, para listagem de aprovados e reprovados, respectivamente). O retorno deve ser uma lista com os valores selecionados.
5. Crie uma função que busque um aluno, oferecendo como opções de busca o código do aluno ou o seu nome. Ela deverá retornar uma lista contendo o registro completo do aluno, conforme mostrado na questão 2.
6. Crie uma função para imprimir o boletim de cada aluno. Deverá receber como passagem uma lista com os dados do aluno e se ele foi aprovado ou reprovado, de acordo com o critério de média apresentado no enunciado da questão.
   1. Crie uma função que gerencie o sistema, apresentando as seguintes opções: 
   2. Cadastrar aluno
   3. Editar notas de alunos
   4.  Listar alunos
   5.  Gerar boletim de aluno
   6.  Sair.
