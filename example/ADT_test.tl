type Option = Some(:val) | None
type Shape = Circle(:radius) | Rect(:w, :h)

:myVal = Some(50)
:myShape = Rect(100, 50)

:multiplier = match :myVal with
| None => 0
| Some(:v) => :v

:moveDist = match :myShape with
| Circle(:r) => :r * 2
| Rect(:w, :h) => :w + :h
| _ => 0

pendown
forward :multiplier
right 90
forward :moveDist
penup