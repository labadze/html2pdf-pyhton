#! /usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import pdfkit

# THIS IS HTML TO PDF CONVERTER Developed By Archil Labadze
# 2019 Supports Python 2.7 & Python 3 >
# Files will be placed in same directory
# you must define input file name with .html extension and output file name with .pdf extension
# You have install pdfkit via pip and import sys and argprse
# If you are using this script on server you have install  wkhtmltopdf and x11 Webfonts (maybe).


#  This class converts html to pdf using command line
class ConvertHTML2PDF(object):
    def __init__(self, args):
        # using pdfkit library for this operation
        pdfkit.from_file(args.i, args.o)
        # getting exit code
        sys.exit()


# Using parser to  get arguments of command line by default it's input and output file
parser = argparse.ArgumentParser()
parser.add_argument(
    # '--in',
    'i',
    type=str,
    # default='input-2-convert.html',
    help='HTML File to convert with .html ext')
parser.add_argument(
    # '--out',
    'o',
    type=str,
    # default='output-converted.pdf',
    help='Converted File name with .pdf ext')
args = parser.parse_args()
ConvertHTML2PDF(args)
