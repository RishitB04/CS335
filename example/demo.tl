type ShapeConfig = Star(:points, :size) | Hexagon(:size)

:baseList = [5, 10, 15]
:offset1, :offset2, :offset3 = :baseList

:multiply = lambda :a :b => :a * :b
:double = :multiply(2)

:lazyMath = lazy ( [1..] |> take(5) |> map(:double) |> fold(lambda :acc :x => :acc + :x, 0) )

:nestedData = [[:offset1, force(:lazyMath)], :offset2]

:extractedVal = match :nestedData with | [[:x, :y], :z] => :x + :y + :z | _ => 0

:finalSize = (:base * :multiplier) + :bonus where :base = :extractedVal, :multiplier = 2, :bonus = 10

:activeShape = Star(36, :finalSize)

:sides = match :activeShape with | Star(:p, :s) => :p | Hexagon(:s) => 6 | _ => 4
:drawLen = match :activeShape with | Star(:p, :s) => :s | Hexagon(:s) => :s | _ => 50

pendown
repeat :sides [
forward :drawLen
right 170
]
penup