import math
import copy

godClassMetricsInput = raw_input("Enter all the numbers with comma and trailing space to separate each number: ")
extractedGodClassNumbersList = [int(i) for i in godClassMetricsInput.split(', ') if i.isdigit()]
extractedGodClassNumbersList.sort()

unfilteredList = copy.deepcopy(extractedGodClassNumbersList)
sizeOfEntireDataset = len(extractedGodClassNumbersList)
sumTotal = 0

modeCountsInGodClass = {}

for eachItem in extractedGodClassNumbersList:
  sumTotal += eachItem

  if str(eachItem) in modeCountsInGodClass:
      continue
  else:
      modeCountsInGodClass[str(eachItem)] = extractedGodClassNumbersList.count(eachItem)


smallestNumberInTheEntireDataset = extractedGodClassNumbersList[0]

print("Smallest minimum number of entire data set: " + str(smallestNumberInTheEntireDataset))

largestNumberInTheEntireDataset = extractedGodClassNumbersList[sizeOfEntireDataset - 1]

print("Largest maximum number of entire data set: " + str(largestNumberInTheEntireDataset))

rangeOfTotalDataset = largestNumberInTheEntireDataset - smallestNumberInTheEntireDataset

print("Range of entire data set: " + str(rangeOfTotalDataset))

print("Size of entire data set: " + str(sizeOfEntireDataset))

print("Sum of total numbers: " + str(sumTotal))

meanTotal = float(sumTotal)/float(sizeOfEntireDataset)

print("Mean of entire data set: " + format(meanTotal, '.2f'))

medianTotal = 0

if sizeOfEntireDataset % 2 == 0:
  medianTotal = (extractedGodClassNumbersList[(sizeOfEntireDataset - 1) // 2] +
  extractedGodClassNumbersList[((sizeOfEntireDataset - 1) // 2) + 1]) / float(2)
else:
  medianTotal = extractedGodClassNumbersList[(sizeOfEntireDataset - 1) // 2]

print("Median (2nd Quartile) of entire data set: " + format(medianTotal, '.2f'))

maximumNumberOfOccurrenceFrequency = max(modeCountsInGodClass.values())

modeTotal = [(specificKey, eachKeyValue) for specificKey,eachKeyValue in modeCountsInGodClass.items() if eachKeyValue == maximumNumberOfOccurrenceFrequency]
print("Mode of entire data set (Value, Frequency): " + str(modeTotal))

standardDeviationTotal = 0
squared_difference_of_each_godClassMetric_from_the_mean_total = 0

for eachItem in extractedGodClassNumbersList:
  squared_difference_of_each_godClassMetric_from_the_mean_total += pow(eachItem - meanTotal, 2)

standardDeviationTotal = math.sqrt(squared_difference_of_each_godClassMetric_from_the_mean_total/float(sizeOfEntireDataset - 1))

print("Standard Deviation of entire data set: " + str(standardDeviationTotal))

varianceTotal = pow(standardDeviationTotal, 2)

print("Variance of entire data set: " + str(varianceTotal))

midRangeTotal = (smallestNumberInTheEntireDataset + largestNumberInTheEntireDataset)/float(2)

print("Mid Range of entire data set: " + str(midRangeTotal))

trimmedMeanTotal = (sumTotal - (smallestNumberInTheEntireDataset + largestNumberInTheEntireDataset))/float(sizeOfEntireDataset - 2)

print("Trimmed Mean of entire data set: " + str(trimmedMeanTotal))

for modeItem, modeFrequency in enumerate(modeTotal):
    print("Mode " + modeFrequency[0] + " Frequency: " + str(modeFrequency[1]))
    print("Mode " + modeFrequency[0] + " Frequency %: " + str(modeFrequency[1]/float(sizeOfEntireDataset)))  

centralPositionOfList = 0
    
if sizeOfEntireDataset % 2 == 0:
    extractedGodClassNumbersList.pop((sizeOfEntireDataset - 1) // 2)
    extractedGodClassNumbersList.pop(((sizeOfEntireDataset - 1) // 2) + 1)
    centralPositionOfList = len(extractedGodClassNumbersList)//2
else:
    extractedGodClassNumbersList.pop((sizeOfEntireDataset - 1) // 2)
    centralPositionOfList = len(extractedGodClassNumbersList)//2

lowerPortionOfSortedNumbers = extractedGodClassNumbersList[:centralPositionOfList]
upperPortionOfSortedNumbers = extractedGodClassNumbersList[centralPositionOfList:]

print("Size of List after deleting median: " + str(len(extractedGodClassNumbersList)))


#lowerHalfCalculations
sizeOfLowwerHalfDataset = len(lowerPortionOfSortedNumbers)
sizeOfUpperHalfDataset = len(upperPortionOfSortedNumbers)  

sumTotal = 0

modeCountsInGodClass = {}

print("List of numbers for lower half: " + str(lowerPortionOfSortedNumbers))


for eachItem in lowerPortionOfSortedNumbers:
  sumTotal += eachItem

  if str(eachItem) in modeCountsInGodClass:
      continue
  else:
      modeCountsInGodClass[str(eachItem)] = lowerPortionOfSortedNumbers.count(eachItem)


smallestNumberInTheEntireDataset = lowerPortionOfSortedNumbers[0]

print("Smallest minimum number of lower half: " + str(smallestNumberInTheEntireDataset))

sizeOfLowwerHalfDataset = len(lowerPortionOfSortedNumbers)
sizeOfUpperHalfDataset = len(upperPortionOfSortedNumbers) 
largestNumberInTheEntireDataset = lowerPortionOfSortedNumbers[sizeOfLowwerHalfDataset - 1]

print("Largest maximum number of lower half: " + str(largestNumberInTheEntireDataset))

rangeOfTotalDataset = largestNumberInTheEntireDataset - smallestNumberInTheEntireDataset

print("Range of lower half: " + str(rangeOfTotalDataset))

print("Size of lower half: " + str(sizeOfLowwerHalfDataset))

print("Sum of lower half: " + str(sumTotal))

meanTotal = float(sumTotal)/float(sizeOfLowwerHalfDataset)

print("Mean of lower half: " + format(meanTotal, '.2f'))

medianTotal = 0

if sizeOfLowwerHalfDataset % 2 == 0:
  medianTotal = (lowerPortionOfSortedNumbers[(sizeOfLowwerHalfDataset - 1) // 2] +
  lowerPortionOfSortedNumbers[((sizeOfLowwerHalfDataset - 1) // 2) + 1]) / float(2)
else:
  medianTotal = lowerPortionOfSortedNumbers[(sizeOfLowwerHalfDataset - 1) // 2]

print("Median (1st Quartile) of lower half: " + format(medianTotal, '.2f'))

Q1 = medianTotal

maximumNumberOfOccurrenceFrequency = max(modeCountsInGodClass.values())

modeTotal = [(specificKey, eachKeyValue) for specificKey,eachKeyValue in modeCountsInGodClass.items() if eachKeyValue == maximumNumberOfOccurrenceFrequency]
print("Mode of lower half (Value, Frequency): " + str(modeTotal))

standardDeviationTotal = 0
squared_difference_of_each_godClassMetric_from_the_mean_total = 0

for eachItem in lowerPortionOfSortedNumbers:
  squared_difference_of_each_godClassMetric_from_the_mean_total += pow(eachItem - meanTotal, 2)

standardDeviationTotal = math.sqrt(squared_difference_of_each_godClassMetric_from_the_mean_total/float(sizeOfLowwerHalfDataset - 1))

print("Standard Deviation of lower half: " + str(standardDeviationTotal))

varianceTotal = pow(standardDeviationTotal, 2)

print("Variance of lower half: " + str(varianceTotal))

midRangeTotal = (smallestNumberInTheEntireDataset + largestNumberInTheEntireDataset)/float(2)

print("Mid Range of lower half: " + str(midRangeTotal))

for modeItem, modeFrequency in enumerate(modeTotal):
    print("Mode " + modeFrequency[0] + " Frequency: " + str(modeFrequency[1]))
    print("Mode " + modeFrequency[0] + " Frequency %: " + str(modeFrequency[1]/float(sizeOfLowwerHalfDataset)))  


#upper half

sumTotal = 0

modeCountsInGodClass = {}

print("List of numbers for upper half: " + str(upperPortionOfSortedNumbers))
print("Size of upper half: " + str(sizeOfUpperHalfDataset))

for eachItem in upperPortionOfSortedNumbers:
  sumTotal += eachItem

  if str(eachItem) in modeCountsInGodClass:
      continue
  else:
      modeCountsInGodClass[str(eachItem)] = upperPortionOfSortedNumbers.count(eachItem)


smallestNumberInTheEntireDataset = upperPortionOfSortedNumbers[0]

print("Smallest minimum number of upper half: " + str(smallestNumberInTheEntireDataset))

largestNumberInTheEntireDataset = upperPortionOfSortedNumbers[sizeOfUpperHalfDataset - 1]

print("Largest maximum number of upper half: " + str(largestNumberInTheEntireDataset))

rangeOfTotalDataset = largestNumberInTheEntireDataset - smallestNumberInTheEntireDataset

print("Range of upper half: " + str(rangeOfTotalDataset))


print("Sum of upper half: " + str(sumTotal))

meanTotal = float(sumTotal)/float(sizeOfUpperHalfDataset)

print("Mean of upper half: " + format(meanTotal, '.2f'))

medianTotal = 0

if sizeOfUpperHalfDataset % 2 == 0:
  medianTotal = (upperPortionOfSortedNumbers[(sizeOfUpperHalfDataset - 1) // 2] +
  upperPortionOfSortedNumbers[((sizeOfUpperHalfDataset - 1) // 2) + 1]) / float(2)
else:
  medianTotal = upperPortionOfSortedNumbers[(sizeOfUpperHalfDataset - 1) // 2]

print("Median (3rd Quartile) of upper half: " + format(medianTotal, '.2f'))

Q3 = medianTotal

maximumNumberOfOccurrenceFrequency = max(modeCountsInGodClass.values())

modeTotal = [(specificKey, eachKeyValue) for specificKey,eachKeyValue in modeCountsInGodClass.items() if eachKeyValue == maximumNumberOfOccurrenceFrequency]
print("Mode of upper half (Value, Frequency): " + str(modeTotal))

standardDeviationTotal = 0
squared_difference_of_each_godClassMetric_from_the_mean_total = 0

for eachItem in upperPortionOfSortedNumbers:
  squared_difference_of_each_godClassMetric_from_the_mean_total += pow(eachItem - meanTotal, 2)

standardDeviationTotal = math.sqrt(squared_difference_of_each_godClassMetric_from_the_mean_total/float(sizeOfUpperHalfDataset - 1))

print("Standard Deviation of upper half: " + str(standardDeviationTotal))

varianceTotal = pow(standardDeviationTotal, 2)

print("Variance of upper half: " + str(varianceTotal))

midRangeTotal = (smallestNumberInTheEntireDataset + largestNumberInTheEntireDataset)/float(2)

print("Mid Range of upper half: " + str(midRangeTotal))

for modeItem, modeFrequency in enumerate(modeTotal):
    print("Mode " + modeFrequency[0] + " Frequency: " + str(modeFrequency[1]))
    print("Mode " + modeFrequency[0] + " Frequency %: " + str(modeFrequency[1]/float(sizeOfUpperHalfDataset)))  

print("Q3: " + str(Q3))
print("Q1: " + str(Q1))

IQR = Q3 - Q1

print("IQR: " + str(IQR))


UpperFence = Q3 + 1.5 * IQR

LowerFence = Q1 - 1.5 * IQR

outliersTotal = []

for eachItem in unfilteredList:
    if (eachItem >= UpperFence or eachItem <= LowerFence):
        outliersTotal.append(eachItem)

print("Outliers: " + str(outliersTotal))

sumTotal = 0
beforeDeletionOfOutliers = copy.deepcopy(unfilteredList)
for eachItem in outliersTotal:
    beforeDeletionOfOutliers.remove(eachItem)

print("Length of the original list of numbers after deleting outliers: " + str(len(beforeDeletionOfOutliers)))
print("List of numbers after deleting outliers: " + str(beforeDeletionOfOutliers)) 
for eachItem in beforeDeletionOfOutliers:
    sumTotal += eachItem

standardDeviationTotal = 0
squared_difference_of_each_godClassMetric_from_the_mean_total = 0

meanTotal = float(sumTotal)/float(len(beforeDeletionOfOutliers))
print("Mean after deleting outliers: " + str(meanTotal)) 

for eachItem in beforeDeletionOfOutliers:
    squared_difference_of_each_godClassMetric_from_the_mean_total += pow(eachItem - meanTotal, 2)

standardDeviationTotal = math.sqrt(squared_difference_of_each_godClassMetric_from_the_mean_total/float(len(beforeDeletionOfOutliers) - 1))

print("Standard Deviation after deletion of outliers: " + str(standardDeviationTotal))

varianceTotal = pow(standardDeviationTotal, 2)

print("Variance after deletion of outliers: " + str(varianceTotal))

print("Length of unfiltered list: " + str(len(unfilteredList)))
print("Top 5% Values within the List: " +
       str(unfilteredList[len(unfilteredList) - 5]) +
      ", " + str(unfilteredList[len(unfilteredList) - 4]) +
      ", " + str(unfilteredList[len(unfilteredList) - 3]) +
      ", " + str(unfilteredList[len(unfilteredList) - 2]) +
      ", " + str(unfilteredList[len(unfilteredList) - 1]))

top5Values = [unfilteredList[len(unfilteredList) - 5],
              unfilteredList[len(unfilteredList) - 4],
              unfilteredList[len(unfilteredList) - 3],
              unfilteredList[len(unfilteredList) - 2],
              unfilteredList[len(unfilteredList) - 1]]

sizeOfEntireDataset = len(top5Values)
sumTotal = 0

modeCountsInGodClass = {}

for eachItem in top5Values:
  sumTotal += eachItem

  if str(eachItem) in modeCountsInGodClass:
      continue
  else:
      modeCountsInGodClass[str(eachItem)] = top5Values.count(eachItem)


smallestNumberInTheEntireDataset = top5Values[0]

print("Smallest minimum number of top 5%: " + str(smallestNumberInTheEntireDataset))

largestNumberInTheEntireDataset = top5Values[sizeOfEntireDataset - 1]

print("Largest maximum number of top 5%: " + str(largestNumberInTheEntireDataset))

rangeOfTotalDataset = largestNumberInTheEntireDataset - smallestNumberInTheEntireDataset

print("Range of top 5%: " + str(rangeOfTotalDataset))

print("Size of top 5%: " + str(sizeOfEntireDataset))

print("Sum of top 5%: " + str(sumTotal))

meanTotal = float(sumTotal)/float(sizeOfEntireDataset)

print("Mean of top 5%: " + format(meanTotal, '.2f'))

medianTotal = 0

if sizeOfEntireDataset % 2 == 0:
  medianTotal = (top5Values[(sizeOfEntireDataset - 1) // 2] +
  top5Values[((sizeOfEntireDataset - 1) // 2) + 1]) / float(2)
else:
  medianTotal = top5Values[(sizeOfEntireDataset - 1) // 2]

print("Median of top 5%: " + format(medianTotal, '.2f'))

maximumNumberOfOccurrenceFrequency = max(modeCountsInGodClass.values())

modeTotal = [(specificKey, eachKeyValue) for specificKey,eachKeyValue in modeCountsInGodClass.items() if eachKeyValue == maximumNumberOfOccurrenceFrequency]
print("Mode of top 5% (Value, Frequency): " + str(modeTotal))

standardDeviationTotal = 0
squared_difference_of_each_godClassMetric_from_the_mean_total = 0

for eachItem in top5Values:
  squared_difference_of_each_godClassMetric_from_the_mean_total += pow(eachItem - meanTotal, 2)

standardDeviationTotal = math.sqrt(squared_difference_of_each_godClassMetric_from_the_mean_total/float(sizeOfEntireDataset - 1))

print("Standard Deviation of top 5%: " + str(standardDeviationTotal))

varianceTotal = pow(standardDeviationTotal, 2)

print("Variance of top 5%: " + str(varianceTotal))

midRangeTotal = (smallestNumberInTheEntireDataset + largestNumberInTheEntireDataset)/float(2)

print("Mid Range of top 5%: " + str(midRangeTotal))
