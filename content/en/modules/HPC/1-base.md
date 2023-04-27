In this exercise, we submit our first job, that only prints a message.
This is to illustrate the concept of job submission.

When you connect to a cluster via `ssh`, you connect to a **login node**. A **login node**
shall be used exclusively to submit jobs to **compute nodes**, organise your files and data,
and transfer them to your local machine or other servers. You should absolutely not perform
computations on a **login node** because they are already slow and you will make them even
slower for everybody else. \
So instead of running your script on the **login node**, you have to use the `sbatch` command to
send the instruction to run the script to a **compute node**.
The arguments of the `sbatch` command are used to specify the specifications you need for the
compute node (i.e. the amount of cpu cores, GPUs, RAM, ...). You could pass all arguments and
the instruction to the `sbatch` command inline, something like :
```
sbatch --account=rrg-pbellec --time=1:0:0 --cpus-per-task=8 --mem=32G submit.sh
```
But it is usually more convenient to define these arguments in the job script with the `#SBATCH`
prefix at the beginning of the line.

Instructions :
  * Job options must be set with "#SBATCH ..." lines on top of the script,
    but below the "#!/bin/bash" line.
  * Modify submit.sh to specify your account, e.g. `#SBATCH --account=rrg-pbellec`.
  * Modify submit.sh to specify 1 node with 1 processor for 2 minutes.
  * Modify submit.sh to specify the job name "ex1".
  * Submit the job with the following command:
```
   sbatch submit.sh
```
  * Please note the job ID.
  * Verify the status of your job with:
```
   squeue -u $USER
```
  * Verify the result of your job in slurm-JOB_ID.out

Additional information:
  * Alliance Canada users are specifying accounts in the form of: TYPE-NAME,
    where TYPE can be def, rrg, rpp or ctb, and NAME is the PI's username. def accounts are the
    defaults accounts with the default priority, so if your PI has a non default account like
    rrg, rpp or ctb it is almost always preferable to use the non default account.
  * The file slurm-JOB_ID.out constains both standard and error outputs
    (stdout and stderr) of the job. If it failed, you should check in this
    file. In the case of this exercise, you should see "Bonjour".
