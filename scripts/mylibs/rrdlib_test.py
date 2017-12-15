import unittest
import random
import rrdlib

class RrdToolsLib(unittest.TestCase):
	
	def setUp(self):
		self.rrdlib = rrdlib.Rrdlib()	
		self.rrdlib.id = "id"
		self.rrdlib.desc = "desc"
		self.rrdlib.rrdFilename = "test"
		self.rrdlib.graphFile = "testout"

	def test_shouldReturnEmptyGraphWhenNoDatas(self):
		command = self.rrdlib.getGraph()
		self.assertEquals(command, "rrdtool graph testout ")
		
	def test_shouldAddFilesize(self):
		self.rrdlib.size = [12, 13]
		command = self.rrdlib.getGraph()
		self.assertEquals(command, "rrdtool graph testout -w 12 -h 13 ")

	def test_shouldReturnGraphWithStartDate(self):
		self.rrdlib.start = "123"
		
		command = self.rrdlib.getGraph()

		self.assertEquals(command, "rrdtool graph testout -s 123 ")

	def test_shouldReturnGraphWithData(self):
		self.rrdlib.datas = [{'id' : 'id1', 'desc' : 'desc1', 'col': 'col1'},{'id' : 'id2', 'desc' : 'desc2', 'col' : 'col2'}]

		command = self.rrdlib.getGraph()
                
                self.assertEquals(command, "rrdtool graph testout DEF:id1=test:id1:AVERAGE LINE2:id1#col1:desc1 DEF:id2=test:id2:AVERAGE LINE2:id2#col2:desc2 ")

	def test_shouldAddSlopeMode(self):
		self.rrdlib.slope = True

		command = self.rrdlib.getGraph()
		
		self.assertEquals(command, "rrdtool graph testout --slope-mode ")
		
	def test_shouldAddSince(self):
		self.rrdlib.start = "123"
		command = self.rrdlib.getGraph()
		self.assertEquals(command, "rrdtool graph testout -s 123 ")

if __name__ == "__main__":
	unittest.main()
