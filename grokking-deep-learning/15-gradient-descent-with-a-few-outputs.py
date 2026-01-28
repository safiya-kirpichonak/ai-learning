from vectors import number_multiplication


def neural_network(input, weights):
    return number_multiplication(input, weights)

ALPHA = 0.1

hurt = [0.1, 0.0, 0.0, 0.1]
win = [1, 1, 0, 1]
sad = [0.1, 0.0, 0.1, 0.2]

wlrec = [0.65, 1.0, 1.0, 0.9]

weights = [0.3, 0.2, 0.9]
for i in range(len(win)):
    input = wlrec[i]
    true = [hurt[i], win[i], sad[i]]

    for j in range(10):
        prediction = neural_network(input, weights)

        error = []
        delta = []
        for y in range(len(true)):
            error.append((prediction[y] - true[y]) ** 2)
            delta.append(prediction[y] - true[y])
        
        weight_deltas = number_multiplication(input, weights)

        for x in range(len(weights)):
            weights[x] = weights[x] - (weight_deltas[x] * ALPHA)

        print(f"Weights: {str(weights)}")
        print(f"Weights Deltas: {str(weight_deltas)}")
        print(f"Prediction: {str(prediction)}; True: {true}\n")
    
    break



        