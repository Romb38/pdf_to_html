# -*- coding: utf-8 -*-

import sys
import pdfToHtmlMain as pdfMain


if __name__ == "__main__":
    print("Use -h for help\n")
    pdfMain.pdfToHtml(sys.argv[1:])