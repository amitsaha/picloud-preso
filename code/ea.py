
from pyevolve_rastrigin import *
import cloud

# Please change these
cloud.setkey('4027', 'xxxx')

# List of Random seeds and run-Ids
# assuming 10 runs
seed_list=[100*(i+1) for i in range(10)]
runid_list=[i+1 for i in range(10)]

jids = cloud.map(run_ga,seed_list,runid_list)
cloud.join(jids)

for i in range(10):
    cloud.files.get('stats_' + str(i+1) + '.csv','stats_' + str(i+1)+'.csv')

