inFile = 'pathToInFile'
outFile = 'pathToOutFile' #Name a file path to write output. Python will create this file for you if not already created.
removedFile = 'pathToRemovedFile' #Name a file path to write removed elements. Python will create this file for you if not already created.
notRemovedFile = 'pathToNotRemovedFile' #Name a file path to write elements not removed (those which do not contain stringToFind). Python will create this file for you if not already created.

stringToFind = 'maliciouswebsite.com'

htmlElement1 = '<script'
htmlElement2 = '<img' #To revise this script for one HTML element type remove this line and references to element #2 below. To revise this script for three HTML elements, add references to element #3 below.

with open(inFile, encoding='utf-8', mode='r') as inF, open(outFile, encoding='utf-8', mode='w') as outF, open(removedFile, encoding='utf-8', mode='w') as removedF, open(notRemovedFile, encoding='utf-8', mode='w') as notRemovedF:
 readlines = inF.readlines()
 lineCount = 0
 for line in readlines:
  i = 0
  j = 0
  lineCount += 1
  htmlElement1Start = line.find(htmlElement1)
  imgStart = line.find(htmlElement2)
  while (htmlElement1Start >= 0):
   htmlElement1End = line.find('>', i) + 1
   scriptElem = line[htmlElement1Start:htmlElement1End]
   if scriptElem.find(stringToFind) >= 0:
    line = line[0:htmlElement1Start] + line[htmlElement1End:len(line)]
    removedF.write(scriptElem + '\n')
   else:
    i = htmlElement1End
    notRemovedF.write(scriptElem + '\n')
   htmlElement1Start = line.find('<script', i)
  while (imgStart >= 0):
   imgEnd = line.find('>', j) + 1
   imgElem = line[imgStart:imgEnd]
   if imgElem.find(stringToFind) >= 0:
    line = line[0:imgStart] + line[imgEnd:len(line)]
    removedF.write(imgElem + '\n')
   else:
    j = imgEnd
    notRemovedF.write(imgElem + '\n')
   imgStart = line.find('<img', j)
  outF.write(line)
  print(lineCount)
