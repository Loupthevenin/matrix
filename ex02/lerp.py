from typing import Union
from matrix import Matrix, Vector

K = Union[int, float]


def lerp(
    u: Union[K, Vector[K], Matrix[K]], v: Union[K, Vector[K], Matrix[K]], t: float
) -> Union[K, Vector[K], Matrix[K]]:
    if type(u) != type(v):
        raise TypeError("u and v must be of the same type")

    if isinstance(u, (int, float)):
        return (1 - t) * u + t * v

    elif isinstance(u, Vector):
        if u.shape() != v.shape():
            raise ValueError("Vectors must have the same shape")
        result_values = [
            (1 - t) * u.values[i] + t * v.values[i] for i in range(u.shape())
        ]
        return Vector(result_values)

    elif isinstance(u, Matrix):
        if u.shape() != v.shape():
            raise ValueError("Matrices must have the same shape")
        rows, cols = u.shape()
        result_rows = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = (1 - t) * u.rows[i][j] + t * v.rows[i][j]
                row.append(val)
            result_rows.append(row)
        return Matrix(result_rows)

    else:
        raise TypeError("Unsupported type for lerp")
