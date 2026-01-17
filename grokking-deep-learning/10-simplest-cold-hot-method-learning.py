def neural_network(input, weight):
    return input * weight

def calculate_error(prediction):
    GOAL_PREDICTION = 0.8
    return (GOAL_PREDICTION - prediction) ** 2

INPUT = 0.5
STEP_AMOUNT = 0.001

weight = 0.5
for iteration in range(1102):
    prediction = neural_network(INPUT, weight)
    error = calculate_error(prediction)

    print(f"{str(iteration)}. Error: {str(error)}; Prediction: {str(prediction)}; Weight: {str(weight)}.")

    up_prediction = neural_network(INPUT, (weight + STEP_AMOUNT))
    up_error = calculate_error(up_prediction)

    down_prediction = neural_network(INPUT, (weight - STEP_AMOUNT))
    down_error = calculate_error(down_prediction)

    if(down_error < up_error):
        weight = weight - STEP_AMOUNT
    elif(down_error > up_error):
        weight = weight + STEP_AMOUNT

# 1101. Error: 2.4999999996708233e-07; Prediction: 0.8004999999999671; Weight: 1.6009999999999343.