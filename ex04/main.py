from matrix import Vector


def main():
    u = Vector([0.0, 0.0, 0.0])
    print(u.norm_1(), u.norm(), u.norm_inf())

    u = Vector([1.0, 2.0, 3.0])
    print(u.norm_1(), u.norm(), u.norm_inf())

    u = Vector([-1.0, -2.0])
    print(u.norm_1(), u.norm(), u.norm_inf())


if __name__ == "__main__":
    main()
