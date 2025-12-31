weight = 0.1

def neural_network(input, weight):
    prediction = input * weight
    return prediction

number_of_toes = [8.5, 9.5, 10, 9]
for t in number_of_toes:
    prediction = neural_network(t, weight)
    print(prediction)