""" This module is a set utility functions for computing basic statistical properties """


def mean(values):
    """Calculate mean of a list of numbers (int or float).
        Pass in one parameter - List of numbers"""
    return sum(values) / len(values)


# 2. Calculate sample standard deviation of list of numbers
def standard_deviation(values):
    std_total = 0
    m = mean(values)
    for item in values:
        std_sum = (item - m) ** 2
        std_total += std_sum
    standard_deviation = (std_total / (sample_size - 1)) ** .5
    return standard_deviation


# 3. Standardize the list of numbers
def standardize(list_values):
    m = mean(list_values)
    sd = standard_deviation(list_values)

    for item in list_values:
        item = ((item - m) / sd)

    return list_values


# 4. Moving average of list of values
def moving_average(values, window):
    moving_average_values = []
    for index in range(len(values) - (window - 1)):
        moving_item = sum(values[index:(index + window)]) / window
        moving_average_values.append(moving_item)
    return moving_average_values

if __name__ == '__main__':
    # Test Code
    sample_size = int(input("What is the maximum number in your sample set? "))
    values = list(range(1, sample_size + 1))
    print(values)

    # Print the results
    print(mean(values))
    print(standard_deviation(values))
    print(standardize(values))
    print("The moving averages are ", moving_average(values, 4))
