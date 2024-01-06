import time
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

# get start time
t0 = round(time.time(), 3)

# get global variables
dagname = sys.argv[1]
jobname = sys.argv[2]
machine_ip = sys.argv[3]
output_path = "/home/ubuntu/data/job/" + dagname

# load dataset
filename = output_path + "/" + 'result_' + dagname + '.txt'
df_input = pd.read_csv(filename, delimiter=',', index_col=False, header=None)
print(df_input)
df_input.columns = ['job','k', 'silhouette_score', 'wss_score', 'duration']
df_input.sort_values(by=['k'], inplace=True)

# silhouette score
plt.plot(df_input['k'], df_input['silhouette_score'], marker='x', color='royalblue')
plt.xlabel('K Number')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis For Optimal k')
plt.grid()
plt.savefig(output_path + "/" + 'result_sil_' + dagname + '.jpg')
plt.close()

# silhouette score
plt.plot(df_input['k'], df_input['wss_score'], marker='x', color='forestgreen')
plt.xlabel('K Number')
plt.ylabel('WSS Score')
plt.title('WSS Analysis For Optimal k')
plt.grid()
plt.savefig(output_path + "/" + 'result_wss_' + dagname + '.jpg')
plt.close()

# clustering duration
plt.plot(df_input['k'], df_input['duration'], marker='x', color='orange')
plt.xlabel('K Number')
plt.ylabel('Duration (s)')
plt.title('Duration Analysis For Optimal k')
plt.grid()
plt.savefig(output_path + "/" + 'result_time_' + dagname + '.jpg')
plt.close()

t1 = round(time.time(), 3)
duration = round(t1-t0, 3)

# save live log
# log = 'dagname,jobname,machine_ip,start_time,end_time,duration,other_info\n'
log_file_path = output_path + "/" + 'log_' + dagname + '.txt'
log = (dagname + ',' + jobname + ',' + machine_ip + ',' + str(t0) + ',' + str(t1) + ',' + str(duration) + ',\n')
with open(log_file_path, 'a') as file:
    file.write(log)
