:double = lambda :x => :x * 2
:sum = lambda :acc :x => :acc + :x

:pipelineResult = [1..] |> take(5) |> map(:double) |> fold(:sum, 0)

pendown
forward :pipelineResult * 3
penup