#Parking Dilemma
def carparkingRoof(cars, k):
    cars.sort()
    min_length = float('inf')
    for i in range(len(cars) - k + 1):
        length = cars[i + k - 1] - cars[i] + 1
        min_length = min(min_length, length)
    return min_length


cars = [6, 2, 12, 7]
k = 3
print(carparkingRoof(cars, k))
