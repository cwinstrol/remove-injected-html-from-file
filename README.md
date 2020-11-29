remove-injected-html-from-file.py removes injected HTML elements from a file by searching for a malicious string such as a src= attribute. Example use case would be to remove <script> and <img> tags that link to a malicious website, e.g. <script src="maliciouswebsite.com">

Input a single file like wordpress.sql, the script uses .find() to remove tags by searching desired tag type(s) for a string (e.g. "maliciouswebsite.com"), and then outputs new lines to a new file. By default script outputs 2 additional files containing HTML tags both removed (removedFile) and those of same type not removed (notRemovedFile), allowing for both accuracy and removal volume checking.

Modify the following variables to use this script:
    1. file names
    2. string to search
    3. html tag types (unless searching both script and img tags)
