﻿# teste-tecnico-salux-revisado



## refatorei o caso prático

## 1. Diferença entre Programação Síncrona e Assíncrona

Na **programação síncrona**, as operações são executadas de forma sequencial — cada tarefa precisa terminar para que a próxima inicie.

Na **programação assíncrona**, (por exemplo, com o módulo `asyncio`) as operações de I/O podem ser realizadas de forma concorrente, permitindo melhor performance quando há muita espera por respostas externas (como requisições de rede ou acesso a disco).

**Quando usar:**
- Síncrona: ideal para tarefas simples ou CPU-bound (limitadas pelo desempenho do processador).
- Assíncrona: excelente em cenários com muitas requisições de I/O, evitando bloqueios desnecessários.

---

## 2. Metaclasses e Como Podem Ser Úteis

**Metaclasses** são classes que definem o comportamento de outras classes. Elas permitem:

- **Modificar dinamicamente** a criação de classes.
- **Adicionar ou alterar** atributos e métodos durante a definição.

São especialmente úteis em frameworks e ORMs, onde se deseja **aplicar padrões ou regras** de forma automática na criação de classes (por exemplo, criando tabelas e mapeamentos de dados sem precisar escrever todo o boilerplate).

---

## 3. Garbage Collector em Python e Gerenciamento de Memória

O **garbage collector** do Python funciona primariamente por **contagem de referências**. Quando um objeto não tem mais referências, ele é coletado. Para lidar com **referências circulares**, o Python tem também um **coletor de ciclos**.

### Gerenciamento Manual
- Usar `gc.collect()` para forçar a coleta de lixo.
- Usar `del` para remover referências de objetos explicitamente, liberando memória antes que o GC atue.

---

## 4. Diferença entre `deepcopy` e `copy`

- **`copy()`** (cópia rasa, *shallow copy*): copia apenas o objeto de nível superior, mantendo referências aos objetos internos.
- **`deepcopy()`** (cópia profunda): cria novas instâncias de todos os objetos internos, garantindo independência total entre o original e a cópia.

Use `deepcopy()` quando for necessário **garantir** que alterações em um objeto copiado não afetem o original.

---

## 5. Decorators e Como Funcionam

Decorators são funções que **recebem** uma função ou método e **retornam** outra função com **comportamento estendido**.

### Exemplos de Uso
- **Logging** automático de parâmetros/retorno de funções.
- **Autenticação**/Autorização em endpoints de API.
- **Cache** de resultados para otimizar chamadas repetitivas.


## 6	Explique o conceito de GIL (Global Interpreter Lock) e como ele afeta o multi-threading em Python?

- O GIL é um mecanismo que impede que múltiplas threads executem bytecodes simultaneamente afetando o desempenho em tarefas CPU-bound. Em operações I/O-bound, as threads podem liberar o GIL durante as esperas, mas para processamento intensivo, alternativas como multiprocessing ou linguagens sem GIL são mais adequadas


## 7.	Como funciona a tipagem dinâmica e forte do Python? Dê um exemplo prático.

- Em python, as variáveis não possuem tipo fixo; o tipo está associado ao valor. A linguagem é dinamicamente tipada, o que significa que o tipo é determinado em tempo de execução, e fortemente tipada, evitando conversões implícitas perigosas. Por exemplo, tentar concatenar uma string com um inteiro sem conversão explícita gera um erro 
