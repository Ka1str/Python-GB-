class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return '\n'.join(['\t'.join(['%d' % i for i in row]) for row in self.matrix_list])

    def __add__(self, other):
        new_matrix = []
        temp_numbers = []

        for i in range(len(self.matrix_list)):

            for j in range(len(self.matrix_list[i])):
                number_sum = self.matrix_list[i][j] + other.matrix_list[i][j]
                temp_numbers.append(number_sum)

                if len(temp_numbers) == len(self.matrix_list[i]):
                    new_matrix.append(temp_numbers)
                    temp_numbers = []

        return Matrix(new_matrix)


my_1 = Matrix(matrix_list=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Матрица №1: \n{my_1}')

my_2 = Matrix(matrix_list=[[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(f'Матрица №2: \n{my_2}')

print(f'Сумма матриц: \n{my_1 + my_2}')
