from matplotlib import pyplot as plt
file = [_.strip().split(" ") for _ in open("empname.txt", "r").readlines()]

clean = []
for i in file:
    h = []
    for j in i:
        if j != '':
            h.append(j)
    clean.append(h)

finalData = {}
for _ in clean:
    finalData[_[1]] = float(_[2])

accProv = list(finalData.keys())
accCount = list(finalData.values())
plt.rcParams['font.size'] = '8'
fig = plt.figure(figsize= (5,5))
fig.suptitle('Employee Salaries', fontsize=10, weight="bold")
plt.bar(accProv, accCount,color="red")
plt.xticks(rotation=45,ha="right")
plt.yticks()
plt.xlabel("Employee Last Name", fontsize=10,weight="bold")
plt.ylabel("Salary ($USD)", fontsize=10,weight="bold")
plt.show()