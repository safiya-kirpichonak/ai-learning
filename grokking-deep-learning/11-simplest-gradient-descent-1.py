def neural_network(input, weight):
    return input * weight

INPUT = 0.5
GOAL_PREDICTION = 0.8

weight = 0.5
for iteration in range(20):
    prediction = neural_network(INPUT, weight)
    
    direct_and_amount = (prediction - GOAL_PREDICTION) * INPUT
    
    weight =  weight - direct_and_amount
    
    print(f"Weight: {weight}; Prediction: {prediction}.")
