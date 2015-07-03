class Test(unittest.TestCase):
	def test1(self):
		answerFile = open('answer1.txt', 'r')
		readsFileName = 'reads1.txt'
		self.assertEquals(getRead(readsFileName), answerFile.read().strip())
		answerFile.close()
	def test2(self):
		answerFile = open('answer2.txt', 'r')
		readsFileName = 'reads2.txt'
		self.assertEquals(getRead(readsFileName), answerFile.read().strip())
		answerFile.close()
	def test3(self):
		answerFile = open('answer3.txt', 'r')
		readsFileName = 'reads3.txt'
		self.assertEquals(getRead(readsFileName), answerFile.read().strip())
		answerFile.close()
	def test4(self):
		answerFile = open('answer4.txt', 'r')
		readsFileName = 'reads4.txt'
		self.assertEquals(getRead(readsFileName), answerFile.read().strip())
		answerFile.close()
	def test5(self):
		answerFile = open('answer5.txt', 'r')
		readsFileName = 'reads5.txt'
		self.assertEquals(getRead(readsFileName), answerFile.read().strip())
		answerFile.close()

unittest.main()
