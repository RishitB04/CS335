
:hexSide = :val where :val = 35

pendown
repeat 6 [
    forward :hexSide
    right 60
]

penup
goto(150, 0)
pendown

:pentSide = :total where :a = 15, :b = 25, :total = :a + :b
repeat 5 [
    forward :pentSide
    right 72
]
