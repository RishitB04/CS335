:f = lambda :x => :x + 1
:g = lambda :x => :x * 2

:h = compose(:f, :g)

:res = apply(:h, lazy(10))