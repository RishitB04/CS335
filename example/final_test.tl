type Shape = Polygon(:sides, :length) | Circle(:radius)

to getBaseLength :offset
return :offset * 2
end

:baseLen = getBaseLength(5)

:factorial = lambda :n => match :n with | 0 => 1 | :x => :x * :factorial(:x - 1)

:infSeq = [1..]
:multiplier = lambda :x => :x * 2
:reducer = lambda :acc :x => :acc + :x

:lazyData = lazy ( :infSeq |> take(4) |> map(:multiplier) |> fold(:reducer, 0) )

:nestedList = [[force(:lazyData), :baseLen], :factorial(3)]

:a, :b = [2, 10]

:unpackRes = match :nestedList with | [[:x, :y], :z] => :x + :y + :z | _ => 0

:calcWhere = (:val * :mult) + :addend where :val = :unpackRes, :mult = :a, :addend = :b

:takeThree = take(3)
:curriedList = :takeThree([10, 20, 30, 40])
:curriedSum = fold(:reducer, 0, :curriedList)

:myShape = Polygon(4, :calcWhere + :curriedSum)

:finalDist = match :myShape with | Polygon(:s, :l) => :l | Circle(:r) => :r * 2 | _ => 0
:finalSides = match :myShape with | Polygon(:s, :l) => :s | _ => 4

pendown
repeat :finalSides [
forward :finalDist
right 360 / :finalSides
]
penup