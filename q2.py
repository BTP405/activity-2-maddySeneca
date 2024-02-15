import matplotlib.pyplot as plt

def graphSnowfall(t):
    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file]

    ranges = [0, 10, 20, 30, 40, 50]
    aggregated_data = []
    for r in ranges:
        count = 0
        for value in snowfall_data:
            if r < value <= r + 10:
                count += 1
        aggregated_data.append(count)

    plt.bar([f'{r+1}-{r+10}cms' for r in ranges], aggregated_data)
    plt.xlabel('Snowfall Range')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation')
    plt.show()
