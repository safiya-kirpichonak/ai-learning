def neural_network(input):
    WEIGHT = 0.5
    return input * WEIGHT


prediction = neural_network(0.5)


GOAL_PREDICTION = 0.8
error = (prediction - GOAL_PREDICTION) ** 2
print(error)
