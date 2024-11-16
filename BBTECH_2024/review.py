data = [1, 2.0, 1.8, 1.5, 2, 30, 20.0 ,10]
b = []
for i in range(1, len(data)):
    print("current run: ")
    print(i)
    print("current data: ")
    print(data[i])
    print("past data: ")
    print(data[i-1])
    if data[i] > data[i-1]:
        b.append(i)
        print("True")
    print("__________")
