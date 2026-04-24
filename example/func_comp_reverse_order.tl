:f = lambda :x => :x + 1
:g = lambda :x => :x * 2

:h = compose(:g, :f)
:res = apply(:h, 10)