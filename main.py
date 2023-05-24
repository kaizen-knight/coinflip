# Coin flip checker, one coin low biased at 25%, one at 75%
# 0 represents tails, 1 represents heads

import logging
import random
import pandas as pd
from matplotlib import pyplot
import numpy

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def flipCoin(bias=50):
    flip = random.randint(0, 100)
    logging.debug(f"Probability set to {bias} flip result {flip}")
    if flip <= bias:
        outcome = 1
    else:
        outcome = 0
    logging.debug(f"Outcome of flip at {outcome}")
    return outcome

def switchStrategy(tflips = 10, biaslow = 25, biashigh = 75):
    totalwinnings = 0
    coinchoice = random.randint(0, 1)
    if coinchoice == 1:
        bias = biashigh  # Represents the high bias coin
    else:
        bias = biaslow  # Low bias coin
    logging.debug(f"Initial coin bias {bias}")
    for x in range(tflips):
        result = flipCoin(bias)
        totalwinnings += result
        logging.debug(f"For flip {x} with {bias} coin result was {result}, total winnings now {totalwinnings}")
        if result == 0:
            if bias == biaslow:
                bias = biashigh
            else:
                bias = biaslow
        logging.debug(f"Bias now set to {bias}")
    return totalwinnings

def testStrategy(tflips = 10, biaslow = 25, biashigh = 75, test = 3):
    totalwinnings = 0
    coinchoice = random.randint(0, 1)
    if coinchoice == 1:
        bias = biashigh  # Represents the high bias coin
    else:
        bias = biaslow  # Low bias coin
    logging.debug(f"Initial coin bias {bias}")
    for x in range(tflips):
        result = flipCoin(bias)
        totalwinnings += result
        logging.debug(f"For flip {x} with {bias} coin result was {result}, total winnings now {totalwinnings}")
        if x == test-1:
            estprob = (totalwinnings * 100) / (x+1)
            logging.debug(f"Test conditions now met for coin change on flip {x + 1}, "
                          f"estimated probability as {estprob}")
            if estprob < (0.5): # Biashigh
                logging.debug("Switching coins")
                if bias == biaslow:
                    bias = biashigh
                else:
                    bias = biaslow
            logging.debug(f"Bias now set to {bias}")
    return totalwinnings


def testAll(testsper=100000, maxtests=8):
    logging.debug("Testing swap strategy")
    testresults = {}
    swap = []
    for x in range(testsper):
        result = switchStrategy()
        swap.append(result)
    testresults['Swap'] = swap
    for x in range(maxtests):
        setresults = []
        for y in range(testsper):
            result = testStrategy(test=x)
            setresults.append(result)
        testresults[x] = setresults
    df = pd.DataFrame(testresults)
    return df


testing = testAll()
meanResults = testing.mean()

"""
x = testing['Swap']
y = testing[0]

bins = numpy.linspace(0, 10, 100)

pyplot.hist(x, bins, alpha=0.5, label='Swap', histtype='step', fill=False)
pyplot.hist(y, bins, alpha=0.5, label='0', histtype='step', fill=False)
pyplot.legend(loc='upper right')
pyplot.show()
"""