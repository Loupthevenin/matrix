from matrix import Matrix, Vector


def main():
    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Vector([4.0, 2.0])
    u.mul_vec(v).display()

    u = Matrix([[2.0, 0.0], [0.0, 2.0]])
    v = Vector([4.0, 2.0])
    u.mul_vec(v).display()

    u = Matrix([[2.0, -2.0], [-2.0, 2.0]])
    v = Vector([4.0, 2.0])
    u.mul_vec(v).display()

    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Matrix([[1.0, 0.0], [0.0, 1.0]])
    u.mul_mat(v).display()

    u = Matrix([[1.0, 0.0], [0.0, 1.0]])
    v = Matrix([[2.0, 1.0], [4.0, 2.0]])
    u.mul_mat(v).display()

    u = Matrix([[3.0, -5.0], [6.0, 8.0]])
    v = Matrix([[2.0, 1.0], [4.0, 2.0]])
    u.mul_mat(v).display()


if __name__ == "__main__":
    main()
