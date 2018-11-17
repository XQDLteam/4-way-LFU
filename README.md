# 4-way-LFU
4-way LFU associative cache - Arquitetura e organizção de computadores II

### Mapeamento Conjunto associativo
Compromisso entre mapeamento direto e completamente associativo

Cache  divida em S (4 nesse caso) conjuntos de N blocos/palavras

Se S = 1 -> mapeamento completamente associativo

Se S = número de blocos/palavras da cache -> mapeamento direto

O endereço ```i``` da memoria principal pode mapear para qualquer endereço no conjunto da cache (i mod S):
  
  - Tenho que fazer procura dentro do conjunto;
  
  - Preciso de política de substituição (Quando tenho miss e busco no nível mais abaixo, caso o conjunto já esteja cheio, quem tirar para abrir lugar? - LFU)
  
### Passos para um acesso
  1. Calcular o módulo do endereço que procuro pelo número de conjustos S da cache (ou utilizar os bits menos significativos do endereço);
  
  2. Alimentar a memória associativa deste conjunto com o Tag procurado;
  
  3. Se o Taga não está na memória -> miss (vou para 5);
  
  4. Senão -> hit e acesso a memoria cache com o ndice fornecido pela memória associativa e efetuo a leitura (fim);
  
  5. Se não existir posiço livre no conjunto -> escolho um endereço para substituir (LFU);
  
  6. Busco o endereço procurado no nível mais baixo e coloco em uma posição livre (ou escolhida) da cache cadastrando essa posiço e Tag na memória associativa do conjunto e efetuo a leitura (fim);
  


  

## Material de apoio
PUCRS: Arquitetura e Organização de Computadores II - Unidade 2: Gerência de memória 

https://www.inf.pucrs.br/~flash/orgarq/aulas/memoria

UNIVESP: Organização de Computadores – Aula 12 – Memória Cache

https://www.youtube.com/watch?v=7j7A88izk8E&t=1155s
## Devs

Gustavo "cr0d" Rodrigues

Rodrigo "Bisso" Machado

