import fileinput
import heapq

def overlap(str1, str2):
	"""
	Finds the maximum overlap between strings STR1 and STR2.
	"""
	len1 = len(str1)
	len2 = len(str2)
	maxPossible = min(len(str1), len(str2))
	for maxOver in range(maxPossible, 0, -1):
		if str1[:maxOver] == str2[len2 - maxOver:]:
			return maxOver, str2, str1
		elif str2[:maxOver] == str1[len1 - maxOver:]:
			return maxOver, str1, str2
	return 0, str1, str2

def checkSubstring(str1, str2):
	"""
	Checks if STR1 is a substring of STR2.
	"""
	len1 = len(str1)
	len2 = len(str2)
	for i in range(len2-len1+1):
		if str1 == str2[i:len1 + i]:
			return True
	return False


def getRead(fileName):
	"""
	Given a FILENAME containing short reads, reconstructs the original string.
	"""
	readsFile = fileinput.input(fileName)
	readsList = []
	heap = []
	removed = set()
	for line in readsFile:
		line = line.strip()
		readsList.append(line)
	fileinput.close()
	for i in range(len(readsList)):
		for j in range(i+1, len(readsList)):
			if len(readsList[i]) < len(readsList[j]):
				str1 = readsList[i]
				str2 = readsList[j]
			else:
				str1 = readsList[j]
				str2 = readsList[i]
			if checkSubstring(str1, str2):
				removed.add(str1)
			else:
				result = overlap(str1, str2)
				if result[0]:
					heapq.heappush(heap, [-result[0], result[1], result[2]])
	while heap:
		merge = heapq.heappop(heap)
		currOverlap = -merge[0]
		left = merge[1]
		right = merge[2]
		newRead = left + right[currOverlap:]
		removed.add(left)
		removed.add(right)
		readsList = [read for read in readsList if read not in removed]
		heap = [h for h in heap if h[1] not in removed and h[2] not in removed]
		heapq.heapify(heap)
		for read in readsList:
			result = overlap(read, newRead)
			if result[0]:
 				heapq.heappush(heap, [-result[0], result[1], result[2]])
		readsList.append(newRead)
	return newRead
