Like in exercise #3, we want to apply one filter to a set of pictures. But,
this time, we want to apply different filters, one specific filter per job.
In this exercise, we will use a double strategy for parallel computing:
- For each job, we will use GNU parallel to process a set of pictures.
- We will submit a job array in order to run multiple instances of the
  same kind of job.

==== GNU parallel ====

Please check ../3-gnu-parallel/README.en for the description of this tool.

==== Job Arrays ====

Job arrays are a parallel mechanism offered by the scheduler. The global job
array is separated in multiple job instances that are started independently.
Each job instance will be identified by a different value in the
SLURM_ARRAY_TASK_ID environment variable. The possible values are defined by
the job array.

The syntax is the following:
```
  #SBATCH --array=<start>-<end>:<step>
```
For example, for a job array of 5 jobs, where SLURM_ARRAY_TASK_ID would be
1, 3, 5, 7 and 9, we would request:
```
  #SBATCH --array=1-9:2
```

Alternatively, you can define only specific values by listing them separated by commas,
for example if you only want values 2, 5, 8 and 22, you would use :
```
  #SBATCH --array=2,5,8,22
```

==== An Array in Bash ====

Bash supports arrays. A Bash array can be declared the following way:
```
  MY_ARRAY=(value1 value2 value3 value4)
```
To access a specific element in the array:
```
  ${MY_ARRAY[$i]}
```
where $i would be a variable having values from 0 through 3.
That means 'value1' is at position 0, and 'value4' is at position 3.

==== Instructions ====

We will use the parallel command to transform all pictures. We will also
use a job array to apply a different filter for each job.

  * Modify submit.sh to define a job array such that the index will go
    from 0 to 8 inclusive.
  * Use the value of SLURM_ARRAY_TASK_ID to get the proper filter in FILTERS.
  * Submit the job array with the following command:
    sbatch submit.sh
  * Verify that the job array is running fine. Many(!) files should have
    been created.
