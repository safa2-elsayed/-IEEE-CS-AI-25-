def sampleStats(count):

    values=[]
    for i in range (256) :
        values.extend([i] * count[i])

    minimum=min(values)
    maximum=max(values)

    mean = sum(values) / len(values)

    sorted_values = sorted(values)

    if len(sorted_values) % 2 == 0 :
        median = (sorted_values[len(sorted_values) // 2 - 1] + sorted_values[len(sorted_values) // 2]) / 2
    else :
        median = sorted_values[len(sorted_values) // 2]

    mode = max(set(values), key=values.count)
    
    return [
        float(format(minimum, ".5f")),
        float(format(maximum, ".5f")),
        float(format(mean, ".5f")),
        float(format(median, ".5f")),
        float(format(mode, ".5f"))
    ]

if __name__ == '__main__':

    print("Enter the count array (256 integers separated by commas):")
    user_input = input().strip()
    count=list(map(int, user_input.split(',')))

    if len(count) != 256 :
        print("Invalid count array. It should contain 256 integers.")
        exit()

    result = sampleStats(count)

    print("[{:.5f}, {:.5f}, {:.5f}, {:.5f}, {:.5f}]".format(
            result[0], result[1], result[2], result[3], result[4]
        ))
    

     