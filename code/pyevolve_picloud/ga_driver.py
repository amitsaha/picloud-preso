#!/usr/bin/python
# Simple demo to show how to run the Pyevolve
# Evolutionary Algorithms framework on PiCloud
# Pyevolve: http://sourceforge.net/projects/pyevolve/ 
# PiCloud: https://www.picloud.com/

# Amit Saha
# http://echorand.me
# For more details, please refer this URL: 

from pyevolve_rastrigin import *
import cloud

# Please change these
cloud.setkey('4027', 'd7277db0e5846403fa15a13a1dc4776ac1245b92')


# List of Random seeds and run-Ids
# assuming 10 runs
seed_list=[100*(i+1) for i in range(10)]
runid_list=[i+1 for i in range(10)]

# calls the method defined in pyevolve_rastrigin.py
# which initiates the GA execution.
# Execute the code on PiCloud
jids = cloud.map(run_ga,seed_list,runid_list)

# check if the jobs are complete, if yes
# pull the stat files 
cloud.join(jids)
print cloud.files.list()
for i in range(10):
    cloud.files.get('stats_' + str(i+1) + '.csv','stats_' + str(i+1)+'.csv')

