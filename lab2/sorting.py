def shellSort(data: list[int]) -> list[int]:
    lastIndex = len(data)
    step = len(data)//2
    while step > 0:
        for i in range(step, lastIndex, 1):
            j = i
            delta = j - step
            while delta >= 0 and data[delta] > data[j]:
                data[delta], data[j] = data[j], data[delta]
                j = delta
                delta = j - step
        step //= 2
    return data