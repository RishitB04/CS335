:myList = [10, 20, 30, 40]

:a, :b, :c, :d = :myList

:firstInf, :secondInf = [100..]

pendown
forward :a + :b
right 90
forward :c + :d
right 90
forward :secondInf - 20
right 90
forward :firstInf - 20
penup