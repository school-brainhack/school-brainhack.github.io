In this exercise, we submit a job that only prints a message.
This is to illustrate the concept of job submission.

Instructions :
  * Job options must be set with "#SBATCH ..." lines on top of the script,
    but below the "#!/bin/bash" line
  * Modify submit.sh to specify your account, e.g. `#SBATCH --account=rrg-pbellec`.
  * Modify submit.sh to specify 1 node with 1 processor for 2 minutes.
  * Modify submit.sh to specify the job name "ex1"
  * Submit the job with the following command:
```
   sbatch submit.sh
```
  * Please note the job ID
  * Verify the status of your job with:
```
   squeue -u $USER
```
  * Verify the result of your job in slurm-JOB_ID.out

Additional information:
  * Compute Canada users are specifying accounts in the form of: TYPE-NAME,
    where TYPE can be def, rrg, rpp or ctb, and NAME is the PI's username.
  * The file slurm-JOB_ID.out constains both standard and error outputs
    (stdout and stderr) of the job. If it failed, you should check in this
    file. In the case of this exercise, you should see "Bonjour".
