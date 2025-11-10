
PI = 3.1415926535

def triangle(base, height):
    """삼각형 넓이 = 1/2 * 밑변 * 높이"""
    return 0.5 * base * height

def rectangle(width, height):
    """직사각형 넓이 = 가로 * 세로"""
    return width * height

def circle(radius):
    """원의 넓이 = π * r^2"""
    return PI * (radius ** 2)

