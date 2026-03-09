PromissumPy

O PromissumPy é um projeto de estudo que simula um sistema bancário simples desenvolvido em Python. A ideia do projeto é praticar conceitos de programação orientada a objetos, organização de código
e estruturação de um backend de forma mais próxima do que é usado em sistemas reais.

Esse projeto é uma continuação de um sistema que comecei em Java, chamado Promissum Bank, e que agora estou reescrevendo em Python para entender melhor como estruturar aplicações backend e trabalhar
com camadas como domínio, serviços e repositórios.

No sistema é possível criar contas, realizar depósitos, saques e transferências entre contas. No momento os dados ficam armazenados em memória, apenas para fins de aprendizado e testes das funcionalidades.

A estrutura do projeto foi separada em partes para deixar o código mais organizado:

Dominio: onde ficam as classes principais do sistema, como conta e transações.

infraestrutura: responsáveis por simular o armazenamento das contas.

servicos: onde ficam as regras de negócio, como depositar, sacar e transferir dinheiro.

Main: arquivo usado para rodar o sistema e testar as operações.

Esse projeto ainda está em desenvolvimento e pretendo evoluí-lo adicionando novas funcionalidades, como integração com PostgreSQL, registro de transações, melhoria na estrutura do código e testes automatizados.

O objetivo principal desse projeto é aprender melhor como sistemas backend funcionam e praticar a construção de aplicações mais organizadas e próximas de projetos reais.
