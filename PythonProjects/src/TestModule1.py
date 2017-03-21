"""
@created:   Feb 20, 2017
@author: scotteverhart
"""

import stringFormatter
import random
import sys

class printStuff():

    outputFileName = 'myTestFile.txt'
    randNum = random.randint(1,10)
    num = range(0,randNum)
    listValues = ["one  ","two  ","three","four ","five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven "]
    
    print
    print "randNum: ",randNum
    print "Values in num: ",num
    print "Values in listValues: ",listValues
    print
    
    def printRange(self):
        self.of =file(self.outputFileName, 'w')
        for i in self.num:
            tmptxt =self.printText(i-1)
            print i,tmptxt
            self.of.write(tmptxt)
            
        print "class processing complete"
            
    def printText(self,listNum):
        
        return stringFormatter.addTwoHyphensBeforeAndAfter(self.listValues[listNum]) + "\t" + \
            stringFormatter.addTwoAsterisksBeforeAndAfter(self.listValues[listNum]) + "\t" + \
            stringFormatter.addTwoCaretsBeforeAndAfter(self.listValues[listNum]) + "\n"
        
if __name__ == '__main__':
    printStuff().printRange()