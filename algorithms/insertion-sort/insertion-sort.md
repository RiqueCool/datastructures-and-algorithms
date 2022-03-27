# Insertion Sort

## Estratégia

1. Funciona como organizar cartas em um baralho;

2. Considere que o primeiro elemento já está ordenado e vá para o segundo indice;

3. Se a carta do indice - 1 for maior do que a carta do indice atual, troque-as;

4. Repita esse processo até que indice chegue a 0, ou o valor de indice -1, seja menor que o valor do indice atual;


## Pseudo-código

```
insertionSort(array)
    mark first element as sorted

    for each unsorted element X
        'extract' the element X

        for j <- lastSortedIndex down to 0
            if current element j > X
                move sorted element to the right by 1

        break loop and insert X here

end insertionSort
```
