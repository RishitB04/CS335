
:side = :result where :base = 25, :result = :base * 2

pendown
repeat 4 [
    forward :side
    right 90
]

penup
goto(150, 0)
pendown

:triSide = :dist where :speed = 20, :time = 3, :dist = :speed * :time
repeat 3 [
    forward :triSide
    right 120
]
