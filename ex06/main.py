from matrix import Vector, cross_product


def main():
    u = Vector([0.0, 0.0, 1.0])
    v = Vector([1.0, 0.0, 0.0])
    cross_product(u, v).display()

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    cross_product(u, v).display()

    u = Vector([4.0, 2.0, -3.0])
    v = Vector([-2.0, -5.0, 16.0])
    cross_product(u, v).display()


if __name__ == "__main__":
    main()
