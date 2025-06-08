from matrix import Vector


def main():
    u1 = Vector([0.0, 0.0])
    v1 = Vector([1.0, 1.0])
    print("u1 . v1 =", u1.dot(v1))

    u2 = Vector([1.0, 1.0])
    v2 = Vector([1.0, 1.0])
    print("u2 . v2 =", u2.dot(v2))

    u3 = Vector([-1.0, 6.0])
    v3 = Vector([3.0, 2.0])
    print("u3 . v3 =", u3.dot(v3))


if __name__ == "__main__":
    main()
