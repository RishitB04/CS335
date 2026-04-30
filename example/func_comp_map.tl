:f = lambda :x => :x + 1
:g = lambda :x => :x * 2

:h = compose(:f, :g)
:res = map(:h, {1,2,3})