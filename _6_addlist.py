matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

trnsponse_matrix = [[row [i] for row in matrix] for i in  range(len(matrix))]
print(*trnsponse_matrix, sep='\n')
# print(type(trnsponse_matrix)) -> list
