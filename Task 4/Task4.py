def get_numbers():
    numbers = list(map(int, input("Enter List Of Numbers: ").split()))
    return numbers

def find_min(numbers) :
    min_value = numbers[0]
    for i in range(len(numbers)):
        if i == 0 or numbers[i] < min_value:
            min_value = numbers[i]
    return min_value

def find_max(numbers) :
    max_value = numbers[0]
    for i in range(len(numbers)):
        if i == 0 or numbers[i] > max_value:
            max_value = numbers[i]
    return max_value

def find_mean(numbers) :
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

def find_median(numbers) :
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    if length % 2 == 0:
        return (sorted_list[length//2 - 1] + sorted_list[length//2]) / 2
    else:
        return sorted_list[length//2]

def find_mode(numbers):
    freq = {}
    max_freq = 0
    mode = None
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_freq:
            max_freq = freq[num]
            mode = num
    return mode

def find_range(numbers) :
    sorted_list = sorted(numbers)
    return sorted_list[-1] - sorted_list[0]

def find_variance(numbers) :
    mean = find_mean(numbers)
    variance = 0
    for i in range(len(numbers)):
        variance += (numbers[i] - mean) ** 2
    return round(variance / (len(numbers)-1) ,2)

def find_STD(numbers) :
    variance = find_variance(numbers)
    return round(variance ** 0.5 ,5)

def find_quartiles(numbers) :
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    q1 = find_median(sorted_list[:length//2])
    q2 = round(find_median(sorted_list))
    q3 = find_median(sorted_list[length//2:])
    return q1,q2,q3

def find_IQR(numbers) :
    sorted_list = sorted(numbers)
    length = len(sorted_list)
    q1 = find_median(sorted_list[:length//2])
    q3 = find_median(sorted_list[length//2:])
    return q3 - q1

numbers = get_numbers()

print("Minimum Value:", find_min(numbers))

print("Maximum Value:", find_max(numbers))

print("Mean:", find_mean(numbers))

print("Median:", find_median(numbers))

print("Mode:", find_mode(numbers))

print("Range:", find_range(numbers))

print("Variance:", find_variance(numbers))

print("Standard Deviation:", find_STD(numbers))

print("Quartiles:", find_quartiles(numbers))

print("Interquartile Range:", find_IQR(numbers))


