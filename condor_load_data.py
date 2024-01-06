import time
import sys
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# get start time
t0 = round(time.time(), 3)

# get global variables
dagname = sys.argv[1]
jobname = sys.argv[2]
machine_ip = sys.argv[3]
data_filepath = "/home/ubuntu/data/job/data.txt"
output_path = "/home/ubuntu/data/job/" + dagname

# load file
df_input = pd.read_csv(data_filepath, delimiter=',', index_col=False)
# MinMax scaler
df_input.drop("Date", axis=1, inplace=True)
scaler = MinMaxScaler()
df_input_scaled = scaler.fit_transform(df_input)

scaled_data = np.asarray(df_input_scaled).astype(np.float16)
compressed_path = output_path + "/" + "/scaled_data_" + dagname + ".npz"
np.savez_compressed(compressed_path, scaled_data)

t1 = round(time.time(), 3)
duration = round(t1-t0, 3)

# save live log
# log = 'dagname,jobname,machine_ip,start_time,end_time,duration,other_info\n'
log_file_path = output_path + "/" + 'log_' + dagname + '.txt'
log = ('dagname,jobname,machine_ip,start_time,end_time,duration,other_info\n' +
       dagname + ',' + jobname + ',' + machine_ip + ',' + str(t0) + ',' + str(t1) + ',' + str(duration) + ',\n')
with open(log_file_path, 'a') as file:
    file.write(log)


