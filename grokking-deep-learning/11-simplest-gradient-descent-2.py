def neural_network(input, weight):
    return input * weight

INPUT = 0.5
ALPHA = 0.01
GOAL_PREDICTION = 0.8

weight = 0.5
for iteration in range(4):
    prediction = neural_network(INPUT, weight)

    delta = prediction - GOAL_PREDICTION

    weight_delta = delta * INPUT

    weight = weight - (weight_delta * ALPHA)

    print(f"Weight: {weight}; Prediction: {prediction}.")
