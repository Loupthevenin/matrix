from matrix import Matrix


def main():
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    print(u.trace())

    u = Matrix([[2.0, -5.0, 0.0], [4.0, 3.0, 7.0], [-2.0, 3.0, 4.0]])
    print(u.trace())

    u = Matrix([[-2.0, -8.0, 4.0], [1.0, -23.0, 4.0], [0.0, 6.0, 4.0]])
    print(u.trace())


if __name__ == "__main__":
    main()
