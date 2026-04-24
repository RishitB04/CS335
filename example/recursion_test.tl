:factorial = lambda :n => match :n with
| 0 => 1
| :x => :x * :factorial(:x - 1)

:factResult = :factorial(4)

pendown
right 90
forward :factResult * 2