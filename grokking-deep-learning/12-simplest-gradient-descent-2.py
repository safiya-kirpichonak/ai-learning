def neural_network(input, weight):
    return input * weight

def calculate_error(prediction, goal_prediction):
    return (prediction - goal_prediction) ** 2

def calculate_new_weight(weight, weight_delta, use_alpha):
    if use_alpha:
        ALPHA = 0.01
        return weight - (weight_delta * ALPHA)
    else:
        return weight - weight_delta


INPUT = 1.1
GOAL_PREDICTION = 0.8

weight = 0.0
for iteration in range(4):
    prediction = neural_network(INPUT, weight)

    # The error is not in the new weight's calculation, we just find its value.
    error = calculate_error(prediction, GOAL_PREDICTION)

    delta = prediction - GOAL_PREDICTION

    weight_delta = delta * INPUT

    # They don't use ALPHA in the book example here, because it makes learning slower.
    weight = calculate_new_weight(weight, weight_delta, False) 

    print(f"Weight: {weight}; Prediction: {prediction}; Error: {error}.")