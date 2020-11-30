remove-injected-html-from-file.py removes injected HTML elements from a file by searching for a malicious string such as a src= attribute. A use case would be to remove script and img tags that link to a malicious website, e.g. <script src="maliciouswebsite.com">

Input a single file like wordpress.sql, the script uses .find() to remove tags by searching desired tag type(s) for a string (e.g. "maliciouswebsite.com"), this program will output new lines to a new file. By default script outputs 2 additional files containing HTML tags both removed (removedFile) and those of same type not removed (notRemovedFile), allowing for both accuracy and removal volume checking.

Modify the following variables to use this script:\
    • inFile, outFile, removedFile, notRemovedFile\
    • stringToFind\
    • htmlElement1, htmlElement2 (unless searching both and only script and img tags)
