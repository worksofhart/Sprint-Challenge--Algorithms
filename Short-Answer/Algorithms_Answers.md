#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) **O(n^3)**. The running time of the loop is proportional to the value of n cubed in the expression `while (a < n * n * n>)`

```
O(1)
O(n^3)
    O(1)
```

b) **O(n log(n))**. The other loop is _O(n)_ and the inner loop's running time is halved each time through when `j` is multipled by 2, so it's _O(log(n))_

```
O(1)
O(n)
    O(1)
    O(log(n))
        O(1)
        O(1)
```

c) **O(n)**. The recursive call only results in one more call to `bunnyEars()` for each decreasing value of `bunnies`, so it's equivalent to a `for` loop of

```
ears = 0
    for bunny in range(bunnies):
        ears += 2
```

## Exercise II
