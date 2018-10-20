import numpy as np
import matplotlib.pyplot as plt

def plotPMF(data, bins = 50):
    heights, bins = np.histogram(data,bins=bins)
    heights = heights/sum(heights)
    plt.bar(bins[:-1],heights,width=(max(bins) - min(bins))/len(bins), color="blue", alpha=0.5)
    plt.show()

def cointTossExperiment(heads, tails, ntrials=1000):
    ntosses = heads + tails
    diffs = []
    for i in range(ntrials):
        tosses_outcome = np.random.randint(0,2,ntosses)
        tosses_heads = np.sum(tosses_outcome)
        tosses_tails = ntosses - tosses_heads
        diff = (tosses_heads-tosses_tails)
        diffs.append(diff)

    return diffs

def pValue(diffs, observed_diff):
    count = 0
    for diff in diffs:
        if abs(diff) >= observed_diff:
            count += 1
    p = count/len(diffs)
    return p

def main():
    heads = 140
    tails = 90
    ntrials = 1000
    diffs = cointTossExperiment(heads, tails, ntrials)
    print('P value: ', pValue(diffs, heads-tails))

if __name__ == '__main__':
    main()
