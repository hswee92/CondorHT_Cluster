import time
import sys
import os
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
# from tslearn.clustering import KShape
from sklearn.metrics import silhouette_score

# get start time
t0 = round(time.time(), 3)

# get global variables
dagname = sys.argv[1]
jobname = sys.argv[2]
machine_ip = sys.argv[3]
output_path = "/home/ubuntu/data/job/" + dagname

# load k_list
k_list_file = '/home/ubuntu/data/job/k_list.txt'
df_k_list = pd.read_csv(k_list_file, delimiter=',', index_col=False, header=None)
df_k_list['sorted'] = df_k_list[0].sort_values(ascending=False)

# get jobnumber
jobnumber = int(jobname[10:])
k = int(df_k_list['sorted'].iloc[jobnumber-1])

# load data from npz
compressed_path = output_path + "/" + "scaled_data_" + dagname + ".npz"
input_data = np.load(compressed_path, "r")
input_data_array = input_data["arr_0"]

# clustering
t2 = round(time.time(), 3)
kmean_clustering = KMeans(n_clusters=k, random_state=123).fit(input_data_array)
# kmean_clustering = KShape(n_clusters=k, random_state=123).fit(input_data_array)
cluster_labels = kmean_clustering.labels_
sil_score = round(silhouette_score(input_data_array, cluster_labels), 5)
wss_score = round(kmean_clustering.inertia_, 5)
t3 = round(time.time(), 3)
clustering_time = round(t3-t2, 3)

# save result
result_filename = output_path + "/" + 'result_' + dagname + '.txt'
result = str(jobnumber) + ',' + str(k) + ',' + str(sil_score) + ',' + str(wss_score) + ',' + str(clustering_time) + "\n"
with open(result_filename, 'a') as file:
    file.write(result)

t1 = round(time.time(), 3)
duration = round(t1-t0, 3)

# save live log
# log = 'dagname,jobname,machine_ip,start_time,end_time,duration,other_info\n'
log_file_path = output_path + "/" + 'log_' + dagname + '.txt'
log = (dagname + ',' + jobname + ',' + machine_ip + ',' + str(t0) + ',' + str(t1) + ',' + str(duration) + ',' + str(k) + '\n')
with open(log_file_path, 'a') as file:
    file.write(log)

