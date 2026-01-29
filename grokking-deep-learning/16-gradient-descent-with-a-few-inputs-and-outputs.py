from vectors import vector_matrix_multiplication, outer_product


def neutral_network(input, weights):
    return vector_matrix_multiplication(input, weights)


ALPHA = 0.01

NUMBER_OF_TOES = [8.5, 9.5, 9.9, 9.0]
WIN_PERCENTAGE = [0.65, 0.8, 0.8, 0.9]
NUMBER_OF_FANS = [1.2, 1.3, 0.5, 1.0]

DAMAGE = [0.1, 0.0, 0.0, 0.1]
WIN_OR_LOSE = [1, 1, 0, 1]
FANS_SADNESS = [0.1, 0.0, 0.1, 0.2]

WIN_PROBABILITY = [0.65, 1.0, 1.0, 0.9]

weights = [[0.1, 0.1, -0.3], [0.1, 0.2, 0.0], [0.0, 1.3, 0.1]]
for i in range(len(NUMBER_OF_TOES)):

    input = [NUMBER_OF_TOES[i], WIN_PERCENTAGE[i], NUMBER_OF_FANS[i]]
    true = [DAMAGE[i], WIN_OR_LOSE[i], FANS_SADNESS[i]]

    for j in range(1):
        prediction = neutral_network(input, weights)

        error = []
        delta = []
        for y in range(len(true)):
            error.append(prediction[y] - true[y] ** 2)
            delta.append(prediction[y] - true[y])

        weight_deltas = outer_product(input, delta)
        print(f"weight_deltas: {weight_deltas}")

    break