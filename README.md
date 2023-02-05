# google-cloud-platform
A repository to share and save step, scripts and tips to use and execute bioinformatic analyses on the GCP

## Execute snakemake pipeline on the Google Cloud Platform Life Sciences
1. Download Docker on the local machine
2. Download the image of Ubuntu Linux. Open the power shell terminal and execute the command below:
```
docker pull ubuntu
```

3. Start a docker ubuntu container
4. Open the container terminal
5. Update and upgrade the Linux SO, and install wget tool
```
apt update
apt upgrade
apt install wget
```

6. Download the miniconda management system. Execute the command line below:
```
wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh
```

7. Execute the miniconda installation script
```
bash Miniconda3-py39_4.11.0-Linux-x86_64.sh
```

8. Restart the terminal. Logout and login
9. Installing the mamba management environments. Execute the command line below:
```
conda install mamba -n base -c conda-forge
mamba init
```

10. Installing the tmux and git tools using mamba command line:
```
mamba install -c conda-forge tmux git
```

11. Install the snakemake tool
```
mamba install -c bioconda -c conda-forge snakemake-minimal
```

12. Installing the google cloud platform essentials programs:
```
sudo apt-get install gcc python3-dev python3-setuptools
pip install --upgrade gcloud google-cloud-storage google-api-python-client
mamba install -c conda-forge google-cloud-sdk google-crc32c
```

13. Create an account on the GCP https://cloud.google.com/
14. Access the GCP console https://console.cloud.google.com/home/
15. Create a project
16. Access the Cloud storage at the console left menu and create a bucket (like a google drive)
17. Access the IAM and admin left menu option
- Access the option Service accounts
- Create a service account using the top options
- Add a Key ID and save the json file
18. Enter in the Docker Ubuntu container and export two global variables:
```
export GOOGLE_APPLICATION_CREDENTIALS=<Key ID json file fullpath>
export GOOGLE_CLOUD_PROJECT=<project-id>
```

19. Login on the gcloud tools using command line below:
```
gcloud auth login --no-launch-browser
gcloud init --console-only
```

20. Create an instance for processing
```
gcloud beta compute --project=<project-id> instances create <name-of-instance>--zone=us-west1-a --machine-type=e2-standard-16  --image=ubuntu-2004-focal-v20220419 --image-project=ubuntu-os-cloud
```
https://cloud.google.com/compute/docs/instances/create-start-instance#gcloud_3

21. Create a Cloud Storage bucket
```
gsutil mb gs://<bucket-name>
```

22. Synchronize your file to the bucket
```
gsutil rsync -r <your-directory> gs://<bucket-name>/snakemake-testing-data
```

23. Prepare your snakemake pipeline
24. Execute the snakemake pipeline and indicate the GCP usage
```
snakemake --google-lifesciences --default-remote-prefix <bucket-name>/<your-folder> --use-conda --google-lifesciences-region us-west1-a -j 1
```

25. After finishing all rules of snakemake pipeline, you can stop the instance and save money:
```
gcloud beta compute instances stop <instance-name> --zone=us-west1-a
```

26. Delete all content of the Cloud Storage bucket
```
gsutil rm -r gs://<bucket-name>/*
```

27. Delete the Cloud Storage bucket
```
gsutil rb gs://<bucket-name>
```
