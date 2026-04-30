:f = lambda :x => :x + 1
:g = lambda :x => :x * 2
:k = lambda :x => :x - 3

:h = compose(:f, :g)
:final = compose(:h, :k)

:res = apply(:final, 10)