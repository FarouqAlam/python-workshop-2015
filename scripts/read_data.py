# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:29:28 2015

@author: farouq
"""

import os

my_filename = __file__
script_dir = os.path.dirname(my_filename)
root_dir = os.path.dirname(script_dir)
print root_dir

data_dir = os.path.join(root_dir, 'data')
filename = os.path.join(data_dir, 'hamilton.csv')
print "My file exists? {}".format(os.path.exists(filename))

# Looking for Mean Temp

import csv
my_temps = []
parser = csv.reader(open(filename, 'rb'))
header = parser.next()
mean_temp_idx = 9

for line in parser:
    try:
        my_float = float(line[mean_temp_idx])
    except:
        print "Error floating {}".format(line[mean_temp_idx])
    else:
        my_temps.append(my_float)