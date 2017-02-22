arrayLength = input()
arrayInput = input()
arrayInput = [int(i) for i in arrayInput.split()]
arrayInput.sort()
arrayCount = 1
arrayLow = []
arrayHigh = []
for i in arrayInput:
    if arrayCount <= int(arrayLength) / 2:
        arrayLow.append(i)
        arrayCount += 1
    else:
        arrayHigh.append(i)
arrayLow.reverse()
arrayZip = [item for pair in zip(arrayLow, arrayHigh) for item in pair]
print(' '.join(map(str, arrayZip)))
