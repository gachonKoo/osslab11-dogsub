
PI = 3.1415926535

def cube(a):
    """정육면체 부피 = a^3"""
    return a ** 3

def rectangular_prism(width, height, depth):
    """직육면체 부피 = 가로 * 세로 * 높이"""
    return width * height * depth

def sphere(radius):
    """구의 부피 = 4/3 * π * r^3"""
    return (4.0 / 3.0) * PI * (radius ** 3)

