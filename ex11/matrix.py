from matrix_types import K, Generic, List, Tuple
from copy import deepcopy
import math


class Matrix(Generic[K]):
    def __init__(self, rows: List[List[K]]):
        self.rows = rows

    def add(self, v: "Matrix[K]") -> None:
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                self.rows[i][j] = self.rows[i][j] + v.rows[i][j]

    def sub(self, v: "Matrix[K]") -> None:
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                self.rows[i][j] = self.rows[i][j] - v.rows[i][j]

    def scl(self, a: K) -> None:
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                self.rows[i][j] = self.rows[i][j] * a

    def mul_vec(self, vec: "Vector[K]") -> "Vector[K]":
        result: List[K] = []
        for row in self.rows:
            acc = 0
            for i in range(len(row)):
                acc += row[i] * vec.values[i]
            result.append(acc)
        return Vector(result)

    def mul_mat(self, mat: "Matrix[K]") -> "Matrix[K]":
        transposed = list(zip(*mat.rows))
        result: List[list[K]] = []
        for row in self.rows:
            new_row: List[K] = []
            for col in transposed:
                acc = 0
                for i in range(len(row)):
                    acc += row[i] * col[i]
                new_row.append(acc)
            result.append(new_row)
        return Matrix(result)

    def trace(self) -> K:
        if not self.is_square():
            raise ValueError("Matrix must be square to compute the trace.")
        acc: K = self.rows[0][0]
        for i in range(1, len(self.rows)):
            acc += self.rows[i][i]
        return acc

    def transpose(self) -> "Matrix[K]":
        if not self.rows:
            return Matrix([])
        transposed_rows = [list(col) for col in zip(*self.rows)]
        return Matrix(transposed_rows)

    def row_echelon(self) -> "Matrix[K]":
        mat = deepcopy(self.rows)
        num_rows = len(mat)
        num_cols = len(mat[0]) if mat else 0
        pivot_row = 0
        pivot_col = 0

        for col in range(num_cols):
            # On cherche un pivot dans la colonne courante
            max_row = None
            for r in range(pivot_row, num_rows):
                if abs(mat[r][col]) > 1e-10:
                    max_row = r
                    break

            if max_row is None:
                continue

            mat[pivot_row], mat[max_row] = mat[max_row], mat[pivot_row]

            # Normaliser la ligne du pivot (pivot = 1)
            pivot_val = mat[pivot_row][col]
            mat[pivot_row] = [x / pivot_val for x in mat[pivot_row]]

            for r in range(num_rows):
                if r != pivot_row:
                    factor = mat[r][col]
                    mat[r] = [a - factor * b for a, b in zip(mat[r], mat[pivot_row])]

            pivot_row += 1
            if pivot_row >= num_rows:
                break

        return Matrix(mat)

    def determinant(self) -> float:
        if not self.is_square():
            raise ValueError("Matrix must be square to compute the determinant.")

        n = len(self.rows)

        if n == 1:
            return self.rows[0][0]

        if n == 2:
            a, b = self.rows[0]
            c, d = self.rows[1]
            return a * d - b * c

        if n == 3:
            a, b, c = self.rows[0]
            d, e, f = self.rows[1]
            g, h, i = self.rows[2]
            return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

        if n == 4:

            def minor(
                matrix: "Matrix[K]", row_to_remove: float, col_to_remove: float
            ) -> "Matrix[K]":
                minor_matrix = []
                for i, row in enumerate(matrix):
                    if i == row_to_remove:
                        continue
                    new_row = []
                    for j, value in enumerate(row):
                        if j == col_to_remove:
                            continue
                        new_row.append(value)
                    minor_matrix.append(new_row)
                return minor_matrix

            det = 0.0
            for col in range(4):
                sign = (-1) ** col
                sub_mat = minor(self.rows, 0, col)
                sub_det = Matrix(sub_mat).determinant()
                det += sign * self.rows[0][col] * sub_det
            return det

        raise NotImplementedError("Determinant only implemented for n <= 4")

    def shape(self) -> Tuple[int, int]:
        num_rows: int = len(self.rows)
        num_cols: int = len(self.rows[0]) if self.rows else 0
        return (num_rows, num_cols)

    def is_square(self) -> bool:
        num_rows: int = len(self.rows)
        for row in self.rows:
            if len(row) != num_rows:
                return False
        return True

    def display(self) -> None:
        for row in self.rows:
            print(" ".join(str(value) for value in row))

    def to_vector(self) -> "Vector[K]":
        flat: List[K] = []
        for row in self.rows:
            for value in row:
                flat.append(value)
        return Vector(flat)


class Vector(Generic[K]):
    def __init__(self, values: List[K]):
        self.values = values

    def add(self, v: "Vector[K]") -> None:
        for i in range(len(self.values)):
            self.values[i] = self.values[i] + v.values[i]

    def sub(self, v: "Vector[K]") -> None:
        for i in range(len(self.values)):
            self.values[i] = self.values[i] - v.values[i]

    def scl(self, a: K) -> None:
        for i in range(len(self.values)):
            self.values[i] = self.values[i] * a

    def dot(self, v: "Vector[K]") -> K:
        if len(self.values) != len(v.values):
            raise ValueError("Vector must have the same length")
        result: K = self.values[0] * v.values[0]
        for i in range(1, len(self.values)):
            result += self.values[i] * v.values[i]
        return result

    def norm_1(self) -> float:
        return sum(abs(x) for x in self.values)

    def norm(self) -> float:
        return math.sqrt(sum(x * x for x in self.values))

    def norm_inf(self) -> float:
        return max(abs(x) for x in self.values)

    def shape(self) -> int:
        return len(self.values)

    def display(self) -> None:
        for value in self.values:
            print(value)

    def to_matrix(self, as_row: bool = True) -> "Matrix[K]":
        if as_row:
            return Matrix([self.values[:]])
        else:
            return Matrix([[val] for val in self.values])


def linear_combination(u: List["Vector[K]"], coefs: List[K]) -> "Vector[K]":
    if len(u) != len(coefs):
        raise ValueError("Vectors and coefficients must have the same length.")

    size = u[0].shape()

    result_values: List[K] = [u[0].values[j] * 0 for j in range(size)]

    for i in range(len(u)):
        vec = u[i]
        coef = coefs[i]
        for j in range(size):
            result_values[j] += vec.values[j] * coef

    return Vector(result_values)


def angle_cos(u: Vector[float], v: Vector[float]) -> float:
    dot: float = u.dot(v)
    norm_u: float = u.norm()
    norm_v: float = v.norm()
    if norm_u == 0 or norm_v == 0:
        raise ValueError("Undefined for zero vectors.")
    return dot / (norm_u * norm_v)


def cross_product(u: Vector[float], v: Vector[float]) -> Vector[float]:
    if u.shape() != 3 or v.shape() != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")

    u1, u2, u3 = u.values
    v1, v2, v3 = v.values

    return Vector(
        [
            u2 * v3 - u3 * v2,
            u3 * v1 - u1 * v3,
            u1 * v2 - u2 * v1,
        ]
    )
