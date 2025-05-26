# ADR 001 - Project Structure Initialization

## Contexto

É necessário criar uma estrutura generalista para APIs REST que seja:

* Versionável
* Flexível o suficiente para servir de base para qualquer API
* Simples e enxuta para agilizar a criação de novas rotas

## Decisão

### Lógica de Negócio

A lógica de negócio será organizada na seguinte estrutura:

* Controller -> Valida as requisições do usuário
* UseCase -> Contém a lógica de negócio
* Contratos -> É feito via Protocol, para facilitar testes unitários
* Repository -> Gerencia a comunicação com o banco de dados

Ordem de consumo:

Controller -> UseCase -> Contrato

O Repositório não é consumido diretamente por ninguém.

## Routers

Existirão 3 tipos de routers:

1. Router Geral, que irá receber:
    * Rotas primordiais (Ex: rotas como health check)
    * Routers de versionamento

2. Router de Versionamento (Ex: V1, V2...)

3. Router de Módulo (Ex: UserRouter, AccountRouter...)

## Middlewares

Eles ficarão na pasta shared e não vão compartilhar informações com os controllers.
Qualquer informação deve ser passada via injeção de dependência, seguindo a estrutura opinada do FastAPI.

## Utils

Essas serão funções para lidar com problemas simples que se repetem em vários módulos. Também ficarão na pasta shared.

## Consequências

* Acoplamento à ORM escolhida, já que não há separação de model e domain, e os relacionamentos também não são
  responsabilidade da aplicação
* Pequena verbosidade adicional devido à criação de protocols, mas ainda assim, menor que a verbosidade de abstract
  classes e com uma garantia de tipagem melhor que callables
* Os middlewares só servirão para mecanismos globais relacionados ao core da aplicação, ficando de fora funções como
  permissão e autenticação
* Overhead inicial na criação dos protocols