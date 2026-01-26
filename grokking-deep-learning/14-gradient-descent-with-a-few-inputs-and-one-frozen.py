from vectors import weight_sum, number_multiplication


def neural_network(input, weights):
    return weight_sum(input,  weights)


ALPA = 0.01
WIN_OR_LOSE_BINARY = [1]
NUMBER_OF_TOES = [8.5]
NUMBER_OF_FANS = [1.2]
WIN_PERCENTAGE = [0.65]

weights = [0.1, 0.2, -0.1]
for i in range(len(NUMBER_OF_TOES)):
    input = [NUMBER_OF_TOES[i], WIN_PERCENTAGE[i], NUMBER_OF_FANS[i]]
    true = WIN_OR_LOSE_BINARY[i]

    for j in range(100):
        prediction = neural_network(input, weights)

        error = (prediction - true) ** 2
        delta = prediction - true

        weights_deltas = number_multiplication(delta, input)
        weights_deltas[0] = 0

        for y in range(len(weights)):
            weights[y] = weights[y] - (ALPA * weights_deltas[y])
    
        print(f"Prediction: {prediction}; True: {true}; Error: {error}")
        print(f"Weights: {str(weights)}")
        print(f"Weights Deltas: {str(weights_deltas)}\n")
    
    break