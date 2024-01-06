#!/bin/bash

dagid="$1"
jobid="$2"
machine_ip=$(hostname)

source /home/ubuntu/data/miniconda3/bin/activate project
python /home/ubuntu/data/job/condor_clusterN.py "$dagid" "$jobid" "$machine_ip"
conda deactivate
