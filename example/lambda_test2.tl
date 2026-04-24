
:add = lambda :a :b => :a + :b
:side = :add(30, 50)

:factor = 5
:scaleBy = lambda :x => :x * :factor
:scaled = :scaleBy(10)

pendown

repeat 4 [
    forward :side
    right 90
]

penup
goto(150, 0)
pendown

repeat 5 [
    forward :scaled
    right 72
]
