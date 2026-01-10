from vectors import vector_matrix_multiplication

#            number_of_toes win_percentage number_of_fans
#            +--------------------------------------------+
# hidden[0]  |     0.1      |     0.2      |    -0.1      |
# hidden[1]  |    -0.1      |     0.1      |     0.9      |
# hidden[2]  |     0.1      |     0.4      |     0.1      |
#            +--------------------------------------------+

#                hidden[0]      hidden[1]     hidden[2]
#            +--------------------------------------------+
# trauma     |     0.3      |     1.1      |    -0.3      |
# wins       |     0.1      |     0.2      |     0.0      |
# sadness    |     0.0      |     1.3      |     0.1      |
#            +--------------------------------------------+
def neural_network(input):
    HIDDEN_LAYER_WEIGHTS = [[0.1, 0.2, -0.1], [-0.1, 0.1, 0.9], [0.1, 0.4, 0.1]]
    PREDICTION_WEIGHTS = [[0.3, 1.1, -0.3], [0.1, 0.2, 0.0], [0.0, 1.3, 0.1]]
    
    hidden_layer_results = vector_matrix_multiplication(input, HIDDEN_LAYER_WEIGHTS)
    
    return vector_matrix_multiplication(hidden_layer_results, PREDICTION_WEIGHTS)


number_of_toes  = [8.5, 9.5, 9.9, 9.0]
win_percentage = [0.65, 0.8, 0.8, 0.9]
number_of_fans = [1.2, 1.3, 0.5, 1.0]

for i in range(len(win_percentage)):
    input = [number_of_toes[i], win_percentage[i], number_of_fans[i]]
    prediction = neural_network(input)
    print(prediction)