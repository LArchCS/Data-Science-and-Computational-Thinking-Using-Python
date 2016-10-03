import pylab

# You may have to change this path
WORDLIST_FILENAME = "E:\Edx\MIT_Python_2\Week2\L4P5\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5


def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    ratio = []
    for i in wordList:
        vow = 0
        for a in i:
            if a in 'aeiou':
                vow += 1
            ratio.append(float(vow)/float(len(i)))
    mean = sum(ratio)/len(ratio)
    sd = stdDev(ratio)
    pylab.figure('Ratio of Vowels')
    pylab.hist(ratio, numBins)
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.title('Ratio of Vowels in wordList',  fontsize=20)
    pylab.xlabel('Ratio of Vowels', fontsize=20)
    pylab.ylabel('Number of Words', fontsize=20)
    pylab.text((xmax-xmin)*0.5, (ymax-ymin)*0.75,
               'Mean Ratio of Vowels in Words' + '\n' + '= ' + str(round(mean, 4))+ '\n\n'  + 'SD Ratio of Vowels in Words' + '\n' +'= '  + str(round(sd, 4)))
    
    
                     
                                            

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
    pylab.show()

    
