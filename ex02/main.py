from matrix import Matrix, Vector
from lerp import lerp


def main():
    print(lerp(0.0, 1.0, 0.0))
    print(lerp(0.0, 1.0, 1.0))
    print(lerp(0.0, 1.0, 0.5))
    print(lerp(21.0, 42.0, 0.3))
    lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3).display()
    lerp(
        Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix(
            [[20.0, 10.0], [30.0, 40.0]]), 0.5
    ).display()


if __name__ == "__main__":
    main()
