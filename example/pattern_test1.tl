
to drawPolygon :sides :size
    :angle = match :sides with | 3 => 120 | 4 => 90 | 5 => 72 | 6 => 60 | _ => 45
    repeat :sides [
        forward :size
        right :angle
    ]
end

pendown
drawPolygon(3, 60)

penup
goto(120, 0)
pendown
drawPolygon(4, 50)

penup
goto(240, 0)
pendown
drawPolygon(5, 40)
