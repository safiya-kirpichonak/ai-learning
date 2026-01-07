def neural_network(input):
    WEIGHT = 0.1
    prediction = input * WEIGHT
    return prediction

number_of_toes = [8.5, 9.5, 10, 9]
for t in number_of_toes:
    prediction = neural_network(t)
    print(prediction)