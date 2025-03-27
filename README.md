# teste-tecnico-salux-revisado


Teste de Python: Questões Teóricas:

1)	Explique a diferença entre programação síncrona e assíncrona em Python. Quando você usaria cada uma?

Na programação síncrona, as operações são executadas de forma sequencial, onde cada tarefa precisa terminar para que a próxima inicie. Já a programação assíncrona, utilizando recursos como o asyncio, permite que operações de I/O sejam executadas de forma concorrente, melhorando a performance em cenários de espera por respostas externas. Uso a abordagem síncrona em tarefas simples ou CPU-bound (limitadas pelo desempenho do processadore) e a assíncrona quando preciso lidar com múltiplas requisições I/O sem bloquear a execução

2)	O que são metaclasses em Python e como elas podem ser úteis?

Metaclasses são classes que definem o comportamento de outras classes. Elas permitem modificar dinamicamente a criação de classes, adicionando ou alterando atributos e metodos. úteis em frameworks e ORMs onde é necessário aplicar padrões ou regras de forma automática durante a definição de classes.

3)	Como funciona o garbage collector do Python e como podemos gerenciar manualmente a memória?

O garbage collector do Python trabalha principalmente com contagem de referências e complementa com um coletor de ciclos para lidar com referências circulares. Para gerenciamento manual, posso usar o módulo gc para forçar a coleta (por exemplo, gc.collect()) ou gerenciar referências com del para liberar objetos não utilizados.


4)	Qual a diferença entre deepcopy e copy em Python?

A função copy realiza uma cópia rasa (shallow copy), replicando apenas o objeto de nível superior, mantendo referências aos objetos aninhados. Já deepcopy cria uma cópia completa, recursivamente duplicando todos os objetos contidos, garantindo independência total entre os objetos copiados.





5)	O que são decorators e como eles funcionam?

Decorators são funções que recebem outra função ou método e retornam uma nova função com comportamento estendido. Permitem, de forma transparente, adicionar funcionalidades como logging, autenticação ou cache sem modificar o código original. Arroba é usado para indicação, no python, assim como em outras linguagens.


6)	Explique o conceito de GIL (Global Interpreter Lock) e como ele afeta o multi-threading em Python?

O GIL é um mecanismo que impede que múltiplas threads executem bytecodes simultaneamente afetando o desempenho em tarefas CPU-bound. Em operações I/O-bound, as threads podem liberar o GIL durante as esperas, mas para processamento intensivo, alternativas como multiprocessing ou linguagens sem GIL são mais adequadas


7)	Como funciona a tipagem dinâmica e forte do Python? Dê um exemplo prático.

Em python, as variáveis não possuem tipo fixo; o tipo está associado ao valor. A linguagem é dinamicamente tipada, o que significa que o tipo é determinado em tempo de execução, e fortemente tipada, evitando conversões implícitas perigosas. Por exemplo, tentar concatenar uma string com um inteiro sem conversão explícita gera um erro 
