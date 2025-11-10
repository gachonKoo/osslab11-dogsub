
from geo import area, volume

def main():
    print("=== Area Test ===")
    print("triangle(3, 4) =", area.triangle(3, 4))
    print("rectangle(2, 5) =", area.rectangle(2, 5))
    print("circle(3) ≈", area.circle(3))

    print("\n=== Volume Test ===")
    print("cube(3) =", volume.cube(3))
    print("rectangular_prism(2, 3, 4) =", volume.rectangular_prism(2, 3, 4))
    print("sphere(2) ≈", volume.sphere(2))

if __name__ == "__main__":
    main()

