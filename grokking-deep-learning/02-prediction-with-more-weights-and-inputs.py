weights = [0.1, 0.2, 0]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] + b[i])
    return output    

def neural_network(input, weights):
    prediction = w_sum(input, weights)
    return prediction

number_of_toes = [8.5, 9.5, 9.9, 9.0]
win_percentage = [0.65, 0.8, 0.8, 0.9]
number_of_fans = [1.2, 1.3, 0.5, 1.0]

for i in range(4):
    input = [number_of_toes[i], win_percentage[i], number_of_fans[i]]
    prediction = neural_network(input, weights)
    print(prediction)