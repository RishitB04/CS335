:data = [[10, 20], 30]

:result = match :data with
| [] => 0
| [[:a, :b], :c] => :a + :b + :c
| _ => 999

pendown
forward :result
right 90
forward :result
penup