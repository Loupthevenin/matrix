from matrix_types import K, Generic, List, Tuple


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
