"""

"""

import nmpi

COLLAB_ID = 633
expt_dir = "experiment1"

client = nmpi.Client("adavison")
client.collab_source_folder = "spinnaker-neuromorphic-classifier"

client.upload_to_storage(expt_dir, COLLAB_ID,
                         remote_folder=client.collab_source_folder,
                         overwrite=True, include=["*.py", "*.csv", "*.txt"])
job = client.submit_job(source=expt_dir,
                        platform=nmpi.SPINNAKER,
                        collab_id=COLLAB_ID,
                        #config={"pyNN_version": "0.7"},
                        command="BuildAndRunClassifier.py True",
                        wait=True)
if job['status'] == "error":
    print(job['log'])
else:
    filenames = client.download_data(job, local_dir=".")
    print(filenames)
