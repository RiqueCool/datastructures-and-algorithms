# Selection Sort

## Estratégia

1. Defina o primeiro elemento de cada iteração como o valor minimo;
2. Percorra o restante do array (i + 1) e caso algum numero seja menor, defina-o como o minimo;
3. Insira o minimo no indice atual da iteração.
4. OBS: Selection-Sort é um algoritmo com poucas permutações, útil para sistemas custosos como memória flash.

## Pseudo-código

```
selectionSort(array, size)
    repeat (size - 1) times

    set the first unsorted element as the minimum
    for each of the unsorted elements
        if element < currentMinimum
            set element as new minimum

    swap minimum with first unsorted position
end selectionSort
```
