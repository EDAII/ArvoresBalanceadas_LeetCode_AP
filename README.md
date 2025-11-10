## Alunos  
| Matrícula | Nome |  
|-----------------------|---------------------|  
| 20/2015868 | Alexandre Lema Xavier Júnior |  
| 22/1031354| Pedro Henrique Fernandino da Silva |  

## Sobre 
Resolução de questões do LeetCode (2 difíceis e 2 médias) pelos integrantes do grupo com o objetivo de demonstrar o conhecimento adquirido nesse módulo (Árvores Balanceadas) da disciplina.

## Questões

|Questão | Dificuldade |
| -- | -- |
| [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)| Média |
| [315. Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/)| Difícil |
| [732. My Calendar III](https://leetcode.com/problems/my-calendar-iii/)| Difícil |
| [3713. Longest Balanced Substring I](https://leetcode.com/problems/longest-balanced-substring-i/description/)| Média |


### [109 - Média](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/) 
O exercício “Convert Sorted List to Binary Search Tree” (LeetCode 109) pede para converter uma lista ligada ordenada em ordem crescente em uma árvore binária de busca (BST) balanceada, onde a diferença de altura entre as subárvores esquerda e direita de qualquer nó não ultrapasse 1.
A solução implementada em C++ utiliza a abordagem de conversão da lista ligada para um vetor, o que facilita o acesso direto aos elementos pelo índice. Em seguida, é aplicada uma construção recursiva da árvore, escolhendo sempre o elemento central do vetor como raiz da subárvore atual, garantindo assim o balanceamento natural da BST.

![Print da Resolução 109](imagens/109.png)

### [315 - Difícil](https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/) 
O exercício "315. Count of Smaller Numbers After Self" do LeetCode pede para, dado um array de inteiros nums, retornar um novo array onde cada posição i contém a quantidade de números menores que nums[i] que aparecem à direita dele no vetor original.
A solução foi implementada com um Merge Sort modificado, utilizando a técnica de Dividir e Conquistar. Durante o processo de mesclagem (merge), é contabilizado quantos elementos do lado direito são menores que o elemento atual do lado esquerdo, essas contagens são acumuladas em um vetor auxiliar, permitindo determinar, para cada elemento, quantos números menores aparecem após ele, esse método tem complexidade O(n log n).

![Print da Resolução 315](imagens/315.png)

### [732. My Calendar I - Média](https://leetcode.com/problems/my-calendar-iii/description/) 
O exercício “My Calendar I” (LeetCode 729) pede para implementar uma agenda que receba intervalos [start, end) e permita aceitar apenas eventos que não se sobrepõem aos já registrados.
A solução usa uma estrutura ordenada para armazenar os intervalos e, a cada novo evento, verifica se ele conflita com o intervalo imediatamente anterior ou posterior. Se não houver sobreposição, o evento é inserido; caso contrário, é rejeitado. Essa abordagem garante o controle eficiente dos intervalos sem interseções.

![Print da Resolução 732](imagens/732.png)

### [3713. Longest Balanced Substring I- Díficil](https://leetcode.com/problems/longest-balanced-substring-i/description/) 
O exercício “Balanced Subsequence Sum” (LeetCode 3713) pede para encontrar a maior soma possível de uma subsequência que obedeça à condição nums[j] - nums[i] ≥ j - i entre elementos consecutivos.
A solução observa que essa condição equivale a exigir que a subsequência seja não decrescente no valor nums[i] - i. Assim, agrupa-se os elementos pelo valor nums[i] - i, soma-se todos os nums[i] de cada grupo e escolhe-se o grupo com maior soma, obtendo a subsequência balanceada de soma máxima.

![Print da Resolução 3713](imagens/3713.png)



## Vídeo de explicação das Questões:
