
:lazyVal = lazy (50 * 2)
:val1 = force(:lazyVal)
:val2 = force(:lazyVal)

:lazyComplex = lazy (30 + 70)
:val3 = force(:lazyComplex)

pendown

repeat 4 [
    forward :val1
    right 90
]

penup
goto(150, 0)
pendown

repeat 3 [
    forward :val3
    right 120
]
