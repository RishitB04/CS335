
to add :a :b
    return :a + :b
end

:finite = [1..5]
:len = length(:finite)
:fHead = head(:finite)
:fTail = tail(:finite)

:naturals = [1..]
:firstFive = take(5, :naturals)
:infHead = head([1..])
:from20 = take(3, [20..])

pendown

repeat :len [
    forward 20
    right 72
]

penup
goto(150, 0)
pendown

:fLen = length(:firstFive)
repeat :fLen [
    forward head(:firstFive) * 15
    right 72
    :firstFive = tail(:firstFive)
]
