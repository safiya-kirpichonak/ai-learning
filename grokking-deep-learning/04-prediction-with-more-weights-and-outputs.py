from vectors import number_multiplication

def neural_network(input):
    WEIGHTS = [0.3, 0.2, 0.9]
    return number_multiplication(input, WEIGHTS)

win_percentage = [0.65, 0.8, 0.8, 0.9]
for i in range(len(win_percentage)):
    prediction = neural_network(win_percentage[i])
    print(prediction)
