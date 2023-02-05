import sys
import os
import getopt

def myfunc(argv):
    arg_json_file = ""
    arg_output = ""
    arg_user = ""
    arg_help = "{0} -j <json-file> -p <project-id> -i <instance-name> -b <bucket-name>".format(argv[0])

    try:
        opts, args = getopt.getopt(argv[1:], "hj:p:i:b:", ["help", "json-file=", "project-id=", "instance-name=", "bucket-name="])
    except:
        print(arg_help)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(arg_help) # print the help message
            sys.exit(2)
        elif opt in ("-j", "--json-file"):
            arg_json_file = arg
        elif opt in ("-p", "--project-id"):
            arg_project_id = arg
        elif opt in ("-i", "--instance-name"):
            arg_instance_name = arg
        elif opt in ("-b", "--bucket-name"):
            arg_bucket_name = arg

    print("export GOOGLE_APPLICATION_CREDENTIALS={json_file}".format(json_file=arg_json_file))
    print("export GOOGLE_CLOUD_PROJECT={project_id}".format(project_id=arg_project_id))

    # gcloud auth login

    print("gcloud beta compute --project={project_id} instances create {instance_name} --zone={zone_name} --machine-type={machine_type} --image=ubuntu-2004-focal-v20220419 --image-project=ubuntu-os-cloud".format(project_id=arg_project_id, instance_name=arg_instance_name, zone_name=arg_zone_name, machine_type=arg_machine_type))
    print("gsutil mb gs://{bucket_name}".format(bucket_name=arg_bucket_name))

    print("gsutil rsync -r data gs://gcp-bucket-andre/snakemake-testing-data")

    print("snakemake --google-lifesciences --default-remote-prefix gs://gcp-bucket-andre/snakemake-testing-data --use-conda --google-lifesciences-region us-east4-c -j 1")
    print("gcloud beta compute instances stop testinstance --zone=us-east4-c")
    print("gcloud beta compute --project=vocal-cyclist-349310 instances delete testinstance --zone=us-east4-c")
    print("gsutil rm gs://bucket-test2-andre/*")
    print("gsutil rb gs://bucket-test2-andre")

if __name__ == "__main__":
    myfunc(sys.argv)
