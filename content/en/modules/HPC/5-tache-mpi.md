So far, we have used filterImage.exe in serial mode, but this is in fact an
executable that can run in parallel on multiple nodes with MPI.

==== MPI ====

"MPI" means "Message Passing Interface". An MPI application can split the
workload on multiple compute nodes, and each part of the task is computed
in parallel in different processes. Coding an MPI application is relatively
complex. On the other hand, using such an application remains simple.
All one needs to do is to use the "mpiexec" command. For example:
```
  mpiexec ../filterImage.exe ....
```
Note: if some application does not use MPI to split the workload, all created
      processes will do the same workload, and all the workload many times.
      For example: mpiexec hostname.

Note: mpiexec is smart enough to get your SLURM environment and determine how
      many processes must be started on each node.

==== Instructions ====

The filterImage.exe application uses MPI to process multiple images
simultaneously on multiple nodes. For this exercise, we will process all
pictures with 4 processors, i.e. two nodes and two cores per node.

  * Modify submit.sh to request 2 nodes, 2 tasks per node and 1 core per task.
  * Use mpiexec with filterImage.exe.
  * Submit the job with the following command:
    sbatch submit.sh
  * Verify that the task is running properly. You should get new images in
    the current directory.

==== Bonus ====

By default, when filterImage.exe receives a list of filters, it will apply each
filter separately on each image. This allows an easy parallelism. The
executable also accepts an option "--combined true", which allows to combine
listed filters and apply them in order. In other words, the executable applies
the first filter on the original image, then the second filter on the result
of the first filter, and so on. Unfortunately, combining filters reduces the
granularity of the parallelism because each filter depends on the previous
result.

Nevertheless, combining filters may generate interesting results. By using one
pair of cores (to not waste resources), combine both filters "add_noise" and
"monochrome". Compare the resulting image to the monochrome-only one.
What do you see? Can you explain it?
