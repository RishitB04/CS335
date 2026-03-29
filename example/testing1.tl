
to calculateArea :length :width
    return :length * :width
end

to drawTree :length :depth
    if :depth == 0 [
        return
    ] elif :depth == 1 [
        forward :length
        backward :length
    ] else [
        forward :length
        
        left 30
        drawTree(:length , :depth - 1)
        
        right 60
        drawTree(:length, :depth - 1)
        
        left 30
        backward :length
    ]
end

to drawSquare :size
    repeat 4 [
        forward :size
        right 90
    ]
end

to drawTriangle :size
    repeat 3 [
        forward :size
        right 120
    ]
end

to executeShape :shapeFunc :size
    :shapeFunc(:size)
end


:dynamicSize = calculateArea(10, 5)

penup
backward 150
pendown
drawTree(60, 4)

penup
goto(100, 100)
pendown

:myShape = drawSquare
executeShape(:myShape, :dynamicSize)

penup
goto(-100, 100)
pendown

:myShape = drawTriangle
executeShape(:myShape, :dynamicSize)