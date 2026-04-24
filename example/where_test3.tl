
:area = :w * :h where :w = 8, :h = 10

pendown
repeat 4 [
    forward :area
    right 90
]

penup
goto(150, 0)
pendown

:computed = :x * :x + :y * :y where :x = 6, :y = 8
repeat 3 [
    forward :computed
    right 120
]
