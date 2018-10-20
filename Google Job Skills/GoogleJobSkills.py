# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 00:13:38 2018

@author: Stephen
"""

import pandas as pd
import os

#Change working directory
os.chdir('C:/Users/Stephen/Desktop/Documents/A Learning Journey/Kaggle/Google Job Skills')

jobskills = pd.read_csv('job_skills.csv')

print(jobskills[jobskills['Location'] == 'London, United Kingdom'])