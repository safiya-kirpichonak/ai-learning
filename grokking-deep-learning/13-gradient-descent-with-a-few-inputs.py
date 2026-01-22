from vectors import weight_sum, number_multiplication

# ERROR 
def neural_network(input, weights):
    return weight_sum(input,  weights)


number_of_toes = [8.5, 9.5, 9.9, 9.0]
win_percentage = [0.65, 0.8, 0.8, 0.9]
number_of_fans = [1.2, 1.3, 0.5, 1.0]
win_or_lose_binary = [1, 1, 0, 1]

ALPA = 0.1
weights = [0.1, 0.2, -0.1]
for i in range(len(number_of_toes)):

    input = [number_of_toes[i], win_percentage[i], number_of_fans[i]]
    prediction = neural_network(input, weights)

    true = win_or_lose_binary[i]
    error = (prediction - true) ** 2
    delta = prediction - true

    weights_deltas = number_multiplication(delta, input)

    for j in range(len(weights)):
        weights[i] = weights[i] - (ALPA * weights_deltas[i])
    
    print(f"Weights: {str(weights)}")
    print(f"Weights Deltas: {str(weights_deltas)}")