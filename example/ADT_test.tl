type Option = Some(:v) | None

:getTopTwo = take(2)
:resList = :getTopTwo([1..10])

:resOptions = :resList |> map(Some)

:add = lambda :a :b => :a + :b
:sumFold = fold(:add)
:sumFromZero = :sumFold(0)
:resSum = :sumFromZero([1, 2, 3, 4])

:finalVal = match nth(:resOptions, 1) with 
    | Some(:x) => :x * :resSum 
    | None => 0

pendown
forward :finalVal