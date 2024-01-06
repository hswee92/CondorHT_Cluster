#!/bin/bash

dagid="$1"
jobid="$2"
machine_ip=$(hostname)

mkdir -p /home/ubuntu/data/job/$dagid
source /home/ubuntu/data/miniconda3/bin/activate project
python /home/ubuntu/data/job/condor_load_data.py "$dagid" "$jobid" "$machine_ip"
conda deactivate


