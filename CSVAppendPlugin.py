import sys
import numpy
import random
import PyPluMA

class CSVAppendPlugin:
   def input(self, filename):
      #self.myfile = filename
      txtfile = open(filename, 'r')
      self.parameters = dict()
      for line in txtfile:
         contents = line.split('\t')
         self.parameters[contents[0]] = contents[1].strip()
      filestuff = open(self.parameters['csvfile'], 'r')
      if ('row' in self.parameters):
         self.row = True
      else:
         self.row = False
      self.lines = []
      for line in filestuff:
         self.lines.append(line.strip())

   def run(self):
      if (self.row):
         numentries = len(self.lines[0].split('\t'))-1
         newline = self.parameters['row']+","
         for i in range(numentries):
            newline += self.parameters['value']
            if (i != numentries-1):
               newline += ','
         self.lines.append(newline)
      else:
         self.lines[0] += ","+self.parameters['column']
         for i in range(1, len(self.lines)):
            self.lines[i] += ","+self.parameters['value']

   def output(self, filename):
      filestuff2 = open(filename, 'w')
      
      for i in range(len(self.lines)):
         filestuff2.write(self.lines[i])
         if (i != len(self.lines)-1):
            filestuff2.write('\n')



