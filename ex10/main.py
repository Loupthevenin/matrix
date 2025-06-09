from matrix import Matrix


def main():
    u = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    u.row_echelon().display()

    u = Matrix([[1.0, 2.0], [3.0, 4.0]])
    u.row_echelon().display()

    u = Matrix([[1.0, 2.0], [2.0, 4.0]])
    u.row_echelon().display()

    u = Matrix(
        [
            [8.0, 5.0, -2.0, 4.0, 28.0],
            [4.0, 2.5, 20.0, 4.0, -4.0],
            [8.0, 5.0, 1.0, 4.0, 17.0],
        ]
    )
    u.row_echelon().display()


if __name__ == "__main__":
    main()
