:globalOffset = 10

:makeAdder = lambda :x => lambda :y => :x + :y + :globalOffset
:addFive = :makeAdder(5)
:resLambda = :addFive(20)

to describeNumber :n
    return match :n with | 0 => 100 | 1 => 200 | :x => :x * 10
end

:resMatch = describeNumber(5)

:resWhere = (:val * :multiplier) + :offset where :val = 10, :multiplier = 2, :offset = 5

:infSeq = [1..]

:mapper = lambda :x => :x * 2
:filterer = lambda :x => match :x with | 6 => 1 | 8 => 1 | _ => 0
:reducer = lambda :acc :x => :acc + :x

:lazyComputation = lazy ( :infSeq |> take(4) |> map(:mapper) |> filter(:filterer) |> fold(:reducer, 0) )

:resLazy = force(:lazyComputation)

:factorial = lambda :n => match :n with | 0 => 1 | :x => :x * :factorial(:x - 1)
:applyTwice = lambda :f => lambda :x => :f(:f(:x))
:resHigherOrderRec = :applyTwice(:factorial)(3)

pendown

:sides = match :resLazy with | 14 => 6 | _ => 4
:sideLen = :resMatch

repeat :sides [
    forward :sideLen
    right 360 / :sides
]

penup