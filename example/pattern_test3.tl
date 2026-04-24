
to getSpeed :level
    return match :level with | 1 => 10 | 2 => 20 | 3 => 40 | _ => 5
end

:speed1 = getSpeed(1)
:speed2 = getSpeed(2)
:speed3 = getSpeed(3)
:speedDefault = getSpeed(99)

pendown

forward :speed1
right 90
forward :speed2
right 90
forward :speed3
right 90
forward :speedDefault
