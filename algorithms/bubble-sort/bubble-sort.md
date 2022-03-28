# Insertion Sort

## Estratégia

1. Funciona como bolhas na aguá que sobem a superficie;
2. Compare o primeiro indice com o segundo, o segundo com o terceiro, ... até o final;
3. Repita isso N vezes, onde N é a quantidade de itens no array;
4. Uma variável extra pode ser utilizado para verificar se não ouve nenhuma iteração e parar o loop economizando tempo.

## Pseudo-código

```
bubbleSort(array)
  swapped <- false
  for i <- 1 to indexOfLastUnsortedElement - 1

    if leftElement > rightElement
      swap leftElement and rightElement
      swapped <- true

end bubbleSort
```
