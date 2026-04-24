
to applyFunc :fn :val
    return :fn(:val)
end

:double = lambda :x => :x * 2
:size = :double(50)

pendown

repeat 4 [
    forward :size
    right 90
]

penup
goto(150, 0)
pendown

:result = applyFunc(:double, 40)
repeat 3 [
    forward :result
    right 120
]
