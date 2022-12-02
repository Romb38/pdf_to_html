**General functioning:**

This tool converts a PDF file to an HTML file

**Internal functioning:**

Creates temp file, generates HTML from it and makes it usable
In case of KeyboardInterrupt, temp file will stay in the respository

**Libraries included:**

    `In the computer:`
        -sys (force usage under windows)
        - os (same)
    
    `Open Source:`
        -shutil (paste the file from a location to another)


**Shell command :**

    `Request line options:`
        -f + <filePath>     if the file is in the computer
        -o + <URL>          if the file is online

    `Facultative Options:`   
        -p + <PATH>         add path to stock output HTML file, default: current file

        -n + <fileName>     add name to output HTML file, default: PDF file name

        -h                  show this page

    Ex : pdfToHtml.py -f <PATH> -p C:/ -n <FileName>

**Function Library:**

import pdfToHtmlLib

    `Function for the file on computer:`

    pdfToHtmlFile(filePath, FINALPATH = *<current file>*, name = *<file-name.PDF>*)

    `Fuction for online file:`

    pdfToHtmlOnline(URL,FINALPATH = *<current file>*,name = *<file-name.PDF>*)