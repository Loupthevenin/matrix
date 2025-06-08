from matrix import Matrix


def main():
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    print("Original:")
    m1.display()
    print("Transpose:")
    m1.transpose().display()

    m2 = Matrix([[1.0, 0.0, 5.0], [7.0, 2.0, 1.0]])
    print("Original:")
    m2.display()
    print("Transpose:")
    m2.transpose().display()


if __name__ == "__main__":
    main()
