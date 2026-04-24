:add = lambda :x :y => :x + :y
:addTwenty = :add(20)

:takeThree = take(3)

:list = :takeThree([10, 20, 30, 40, 50])
:sum = fold(:add, 0, :list)
:finalResult = :addTwenty(:sum)

pendown
forward :finalResult
penup