from vectors import weight_sum, number_multiplication


def neural_network(input, weights):
    return weight_sum(input,  weights)

ALPA = 0.1
WIN_OR_LOSE_BINARY = [1, 1, 0, 1]
NUMBER_OF_TOES = [8.5, 9.5, 9.9, 9.0]
NUMBER_OF_FANS = [1.2, 1.3, 0.5, 1.0]
WIN_PERCENTAGE = [0.65, 0.8, 0.8, 0.9]


weights = [0.1, 0.2, -0.1]
for i in range(len(NUMBER_OF_TOES)):

    input = [NUMBER_OF_TOES[i], WIN_PERCENTAGE[i], NUMBER_OF_FANS[i]]
    prediction = neural_network(input, weights)

    true = WIN_OR_LOSE_BINARY[i]
    error = (prediction - true) ** 2
    delta = prediction - true

    weights_deltas = number_multiplication(delta, input)

    for j in range(len(weights)):
        weights[j] = weights[j] - (ALPA * weights_deltas[j])
    
    print(f"Weights: {str(weights)}")
    print(f"Weights Deltas: {str(weights_deltas)}\n")