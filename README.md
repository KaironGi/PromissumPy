PromissumPy – Descrição e Guia de Evolução

O PromissumPy é um projeto de estudo que simula um sistema bancário em Python, como continuação do sistema original em Java chamado Promissum Bank. O objetivo é praticar programação orientada a objetos, organização de código e construção de um backend estruturado de forma próxima a sistemas reais.

Funcionalidades Atuais

Atualmente, o PromissumPy permite:

Gerenciamento de contas

Criação de contas vinculadas a clientes.

Controle de status: Ativa, Bloqueada, Encerrada.

Validação de operações apenas para contas ativas.

Operações financeiras

Depósito de valores em contas.

Saque com verificação de saldo.

Transferência entre contas com checagem de saldo e status de contas.

Controle de concorrência via versão da conta.

Idempotência de operações para evitar transações duplicadas.

Sessões e autenticação básica

Criação de sessões por user_id e token.

Validação de login antes de realizar operações financeiras.

Controle de acesso garantindo que apenas o dono da conta possa operar sobre ela.

Persistência em memória

Repositórios de contas, transações e sessões armazenam dados em memória para teste e aprendizado.

Cálculo de saldo

Saldo calculado dinamicamente a partir das transações na própria entidade Conta.

Isso evita inconsistências e garante que o saldo reflita corretamente todas as operações.

Estrutura do Projeto

O projeto está organizado em camadas:

Dominio: Classes principais (Conta, Transacao, Cliente) e regras de negócio fundamentais.

Infraestrutura: Repositórios de armazenamento em memória (RepositorioContaMemoria, RepositorioTransacaoMemoria, RepositorioSessaoMemoria).

Servicos: Regras de negócio aplicadas às operações bancárias (ServicoConta), incluindo validações e integração com o verificador de login.

Segurança: Gestão de sessões e verificação de login (Sessao, VerificadorLogin).

Main: Arquivo para rodar o sistema e testar operações.

Problemas Corrigidos e Cuidados Atuais

Durante o desenvolvimento, foram identificados pontos complicados:

Saldo incorreto

Inicialmente, ServicoConta.calcular_saldo() usava apenas o repositório de transações externo, ignorando a lógica interna da Conta.

Agora, o saldo é acessado diretamente via conta.saldo, refletindo corretamente depósitos, saques e transferências.

Validação de usuário e sessão

Antes, não havia verificação se o usuário tinha permissão para operar a conta.

Agora, ServicoConta exige user_id e token válidos, e verifica se o usuário é dono da conta.

Duplicidade e concorrência

Operações duplicadas e conflito de versão agora são tratados na entidade Conta (_operacoes_processadas e _versao).

Como Garantir que o Sistema Funcione

Para executar o PromissumPy corretamente:

Criar clientes antes de criar contas.

Criar sessões usando VerificadorLogin e usar o token para operações.

Utilizar o ServicoConta para todas as operações, não acessando diretamente _transacoes da conta.

Consultar o saldo via conta.saldo para garantir consistência.

Sempre salvar a conta no repositório após depósitos, saques ou transferências.
