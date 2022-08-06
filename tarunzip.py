# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:11:18 2022

@author: oxlay
"""

import tarfile
import os
import sys

tar = tarfile.open("pulseTarFile.tar") # Open the Tar File
tar.extractall('./Data') # Extract all data into the prescribed subfolder Data
tar.close() # Close the tar file and end the extraction attempts