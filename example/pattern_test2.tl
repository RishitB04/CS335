
:val = 42
:result = match :val with | 0 => 100 | :n => :n * 2

:sides = 8
:angle = match :sides with | 3 => 120 | 4 => 90 | _ => 45

pendown

forward :result
right 90
forward :result

penup
goto(150, 0)
pendown

repeat :sides [
    forward 30
    right :angle
]
