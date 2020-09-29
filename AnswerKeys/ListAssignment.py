import random
from matplotlib import pyplot as plt

# Create a list to hold the results this should be 1000 long
#numberOfSamples = 10000
numberOfSamples = 1000


resultsList = []

# Store a variable to be the sample size
sampleSize = 10

# The random numbers will be generated from
# integers starting at 1 up to, but not
# including this number
rangeForSamples = 25

# Loop over each list item
for index in range(numberOfSamples):
    sumForSample = 0
    # loop to generate a list of values
    for sampleindex in range(sampleSize):
        sumForSample = sumForSample + random.randint(1, rangeForSamples)
    # calculate the mean
    meanForSample = sumForSample / sampleSize
    # store the mean
    resultsList.append(meanForSample)
# Create a histogram of the means
plt.hist(resultsList, bins=25)
plt.title("Histogram demonstrating the Central Limit Theorem")
plt.show()
# Try it with different sizes of sample
