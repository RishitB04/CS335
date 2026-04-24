
:transform = lambda :x => :x + 10
:val1 = :transform(5)

:transform = lambda :x => :x * 10
:val2 = :transform(5)

:compute = lambda :x :y => :x * :x + :y * :y
:val3 = :compute(3, 4)

pendown

repeat 4 [
    forward :val1
    right 90
]

penup
goto(100, 0)
pendown

repeat 4 [
    forward :val2
    right 90
]

penup
goto(0, -100)
pendown

repeat 3 [
    forward :val3
    right 120
]
