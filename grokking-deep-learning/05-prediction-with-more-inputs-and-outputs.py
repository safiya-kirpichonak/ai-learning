from vectors import vector_matrix_multiplication

#         number_of_toes win_percentage number_of_fans
#         +--------------------------------------------+
# trauma  |     0.1      |     0.1      |    -0.3      |
# wins    |     0.1      |     0.2      |     0.0      |
# sadness |     0.0      |     1.3      |     0.1      |
#         +--------------------------------------------+
def neural_network(input):
    WEIGHTS = [[0.1, 0.1, -0.3], [0.1, 0.2, 0.0], [0.0, 1.3, 0.1]]
    return vector_matrix_multiplication(input, WEIGHTS)


number_of_toes  = [8.5, 9.5, 9.9, 9.0]
win_percentage = [0.65, 0.8, 0.8, 0.9]
number_of_fans = [1.2, 1.3, 0.5, 1.0]

for i in range(len(win_percentage)):
    input = [number_of_toes[i], win_percentage[i], number_of_fans[i]]
    prediction = neural_network(input)
    print(prediction)

# First game result:
# [0.555,  - trauma
# 0.9800,  - wins
# 0.9650]  - sadness