
to double :x
    return :x * 2
end

to add :a :b
    return :a + :b
end

:input = take(4, [10..])
:doubled = map(double, :input)
:dLen = length(:doubled)

:foldInput = take(5, [1..])
:sum5 = fold(add, 0, :foldInput)

pendown

repeat :dLen [
    forward head(:doubled)
    right 90
    :doubled = tail(:doubled)
]

penup
goto(150, 0)
pendown

repeat 4 [
    forward :sum5
    right 90
]
