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

Binary search would be the most efficient way to zero in on `f`.

def find_safe_floor(floors):
low_floor = 1
high_floor = floors

    # Loop until we find the safe floor by ruling out unsafe ones
    while low_floor <= high_floor:
        # Go to the middle floor of the building
        middle_floor = (high_floor + low_floor) // 2

        # Drop an egg
        is_broken = drop_egg_from_floor(middle_floor) # True if egg breaks

        # If it breaks, we know our safe floor will be lower, so go to the mid point between the bottom and the current floor - 1
        if is_broken is True:
            high_floor = middle_floor - 1
        # Else look higher, going to the mid point between the current and top floor to see if there we can push our unbroken egg drop record further and get into the Guinness Book
        else:
            low_floor = middle_floor + 1

    return high_floor

Working repl.it: https://repl.it/@mhartdev/Egg-Drop
