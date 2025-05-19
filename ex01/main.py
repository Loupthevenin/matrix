from matrix import Matrix, Vector, linear_combination


def main():
    e1 = Vector([1.0, 0.0, 0.0])
    e2 = Vector([0.0, 1.0, 0.0])
    e3 = Vector([0.0, 0.0, 1.0])
    v1 = Vector([1.0, 2.0, 3.0])
    v2 = Vector([0.0, 10.0, -100.0])

    result1 = linear_combination([e1, e2, e3], [10.0, -2.0, 0.5])
    result1.display()
    print("---")

    result2 = linear_combination([v1, v2], [10.0, -2.0])
    result2.display()


if __name__ == "__main__":
    main()
