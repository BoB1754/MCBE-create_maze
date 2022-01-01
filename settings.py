CEILLING = "air"
WALL = "concrete 4"
FLOOR = "concrete 3"
WIDTH = 7
HEIGHT = 5
RANGE = 25


# wall
TO = ( RANGE // 2 ) * WIDTH - ( RANGE // 2 - 1 ) + 2
END = -( TO + 1 )
STEP = -( WIDTH - 1 )

# lantern
TO_ = ( WIDTH - 1 ) * ( RANGE // 2 )
END_ = -( TO_ + 1 )

assert WIDTH % 2 != 0 and WIDTH > 1, "WIDTH 값은 반드시 1보다 큰 홀수 입력."
assert RANGE % 2 != 0 and RANGE > 0, "RANGE 값은 반드시 0보다 큰 홀수 입력."