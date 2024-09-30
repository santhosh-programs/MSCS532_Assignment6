class MyArray:
    def __init__(self, size):
        self._size = size
        self._arr = [None] * size

    def get(self, index):
        if 0 <= index < self._size:
            return self._arr[index]
        else:
            raise IndexError(
                f'Index {index} out of range for array of size {self._size}.')

    def insert(self, index, value):
        if 0 <= index < self._size:
            self._arr[index] = value
        else:
            raise IndexError(
                f'Index {index} out of range for array of size {self._size}.')

    def delete(self, index):
        if 0 <= index < self._size:
            self._arr[index] = None
        else:
            raise IndexError(
                f'Index {index} out of range for array of size {self._size}.')

    def display(self):
        print(self._arr)


class MyMatrix:
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        # Initialize matrix with None
        self._matrix = [[None for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            return self._matrix[row][col]
        else:
            raise IndexError(
                f'Index ({row}, {col}) out of range for matrix of size {self._rows}x{self._cols}.')

    def insert(self, row, col, value):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            self._matrix[row][col] = value
        else:
            raise IndexError(
                f'Index ({row}, {col}) out of range for matrix of size {self._rows}x{self._cols}.')

    def delete(self, row, col):
        if 0 <= row < self._rows and 0 <= col < self._cols:
            self._matrix[row][col] = None
        else:
            raise IndexError(
                f'Index ({row}, {col}) out of range for matrix of size {self._rows}x{self._cols}.')

    def display(self):
        for row in self._matrix:
            print(row)


if __name__ == "__main__":
    my_array = MyArray(5)
    my_array.insert(0, 10)
    my_array.insert(1, 20)
    my_array.display()
    print(my_array.get(1))
    my_array.delete(1)
    my_array.display()

    my_matrix = MyMatrix(3, 3)
    my_matrix.insert(0, 0, 1)
    my_matrix.insert(1, 1, 2)
    my_matrix.insert(2, 2, 3)
    my_matrix.display()
    print(my_matrix.get(1, 1))  # Output: 2
    my_matrix.delete(1, 1)
    my_matrix.display()
