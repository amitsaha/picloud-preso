from pyevolve_rastrigin import *
import cloud

# assuming 10 runs
seed_list=[100*(i+1) for i in range(10)]
runid_list=[i+1 for i in range(10)]

# calls the method defined in pyevolve_rastrigin.py
# which initiates the GA execution.
# Execute the code on PiCloud
jids = cloud.map(run_ga,seed_list,runid_list)

# pull the stat files 
cloud.join(jids)
print cloud.files.list()
for i in range(10):
    cloud.files.get('stats_' + str(i+1) + '.csv','stats_' + str(i+1)+'.csv')

