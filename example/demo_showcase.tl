
to double :x
    return :x * 2
end

to half :x
    return :x / 2
end

to add :a :b
    return :a + :b
end

to mul :a :b
    return :a * :b
end

to isLarge :x
    if :x > 30 [
        return 1
    ] else [
        return 0
    ]
end

to drawPolygon :sides :size
    :angle = match :sides with | 3 => 120 | 4 => 90 | 5 => 72 | 6 => 60 | _ => 45
    repeat :sides [
        forward :size
        right :angle
    ]
end

to drawSpiral :steps :size :angleInc
    :i = 0
    repeat :steps [
        forward :size + :i * 2
        right :angleInc
        :i = :i + 1
    ]
end

to drawStar :size
    repeat 5 [
        forward :size
        right 144
    ]
end

to drawBurst :size :count
    repeat :count [
        forward :size
        backward :size
        right 360 / :count
    ]
end

to fractalBranch :len :depth
    if :depth == 0 [
        forward :len
        backward :len
    ] else [
        forward :len
        left 30
        fractalBranch(:len * 2 / 3, :depth - 1)
        right 60
        fractalBranch(:len * 2 / 3, :depth - 1)
        left 30
        backward :len
    ]
end

penup
goto(0, 250)
pendown

drawSpiral(30, 40, 91)

penup
goto(-250, 100)
pendown

:rangeSizes = take(6, [20..])
:bigSizes = filter(isLarge, :rangeSizes)
:scaledSizes = map(double, :bigSizes)

:sLen = length(:scaledSizes)
repeat :sLen [
    forward head(:scaledSizes)
    right 60
    :scaledSizes = tail(:scaledSizes)
]

penup
goto(200, 100)
pendown

:doubleThenHalf = compose(double, half)
:starSize = :doubleThenHalf(80)
drawStar(:starSize)

penup
goto(-300, -100)
pendown

:sides = {3, 4, 5, 6}
:polySize = 40 where :base = 20, :polySize = :base * 2

:sidesLen = length(:sides)
repeat :sidesLen [
    drawPolygon(head(:sides), :polySize)
    penup
    forward 100
    pendown
    :sides = tail(:sides)
]

penup
goto(150, -150)
pendown

:addFive = partial(add, 5)
:burstSize = :addFive(25)
drawBurst(:burstSize, 12)

penup
goto(-100, -250)
pendown

left 90
fractalBranch(60, 4)
right 90

penup
goto(250, -250)
pendown

:lazyAngle = lazy (360 / 8)
:forcedAngle = force(:lazyAngle)

:spiralBase = take(8, [5..])
:spiralSizes = map(double, :spiralBase)
:sLen2 = length(:spiralSizes)
repeat :sLen2 [
    forward head(:spiralSizes)
    right :forcedAngle
    :spiralSizes = tail(:spiralSizes)
]

penup
goto(-300, -350)
pendown

:combined = zipWith(add, {20, 40, 60, 80}, {10, 20, 30, 40})
:cLen = length(:combined)
repeat :cLen [
    forward head(:combined)
    right 90
    :combined = tail(:combined)
]
