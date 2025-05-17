from matrix import Matrix, Vector


def main():
    print("=== Vector ===")
    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.add(v)
    u.display()

    u = Vector([2.0, 3.0])
    v = Vector([5.0, 7.0])
    u.sub(v)
    u.display()

    u = Vector([2.0, 3.0])
    u.scl(2.0)
    u.display()

    print("=== Matrix ===")
    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    u.add(v)
    u.display()

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
    u.sub(v)
    u.display()

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    u.scl(2.0)
    u.display()


if __name__ == "__main__":
    main()

