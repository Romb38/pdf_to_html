# -*- coding: utf-8 -*-

import os
import principalFunctions.pdfToHtmlMain as pdfMain

def pdfToHtmlFile(filePath,FINALPATH = os.getcwd(),name = ""):
    """Transform a pdf file into a html file"""
    argv = ["-f",filePath,"-p",FINALPATH,"-n",name]
    pdfMain.pdfToHtml(argv)

def pdfToHtmlOnline(URL,FINALPATH = os.getcwd(), name = ""):
    argv = ["-o",URL,"-p",FINALPATH,"-n",name]
    pdfMain.pdfToHtml(argv)