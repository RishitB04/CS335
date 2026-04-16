
to double :x
    return :x * 2
end

pendown

:side = :result where :base = 25, :result = :base * 2

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

penup
goto(-150, 0)
pendown

:pentSide = :total where :a = 15, :b = 25, :total = :a + :b

repeat 5 [
    forward :pentSide
    right 72
]

penup
goto(0, -200)
pendown

:hexSide = :val where :val = 35

repeat 6 [
    forward :hexSide
    right 60
]

penup
goto(200, -200)
pendown

:area = :w * :h where :w = 8, :h = 10

repeat 4 [
    forward :area
    right 90
]

penup
goto(-200, -200)
pendown

:computed = :x * :x + :y * :y where :x = 6, :y = 8

repeat 3 [
    forward :computed
    right 120
]
