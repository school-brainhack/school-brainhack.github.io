Like in exercise #2, we want to apply the "grayscale" filter to multiple
pictures. In order to use multiple cores on a compute node, we will run
multiple instances of the executable simultaneously.

This time, we will use a tool called GNU-Parallel, which is more
flexible while having a compact syntax.

==== GNU parallel ====

GNU parallel is a powerful tool to execute parallel tasks. It supports two
main input formats:
  * Lists of values on the command line.
  * Lists of values in a file.

Please check the [Alliance Canada wiki](https://docs.alliancecan.ca/wiki/GNU_Parallel) for basic options, and the [official documentation](http://www.gnu.org/software/parallel/man.html) for advanced options.


For this exercise, we will reuse the output of the "ls" command with $( ).
For example, to display the content of "../photos" in
parallel, we would use GNU parallel the following way:
```
   parallel echo {1} ::: $(ls ../photos)
```
In this example, {1} refers to the first variable in the command template.
The operator ":::" separates the template from values for the first variable.
We could define multiple variables ({1}, {2}, etc.) by adding more ":::"
operators at the end of the parallel command.

==== Instructions ====

We will use the parallel command to convert all pictures in
"../photos":

  * Request 2 cores with the --cpus-per-task option in the job submission
    script header.
  * Use the parallel command on filterImage.exe to run it on the list of files in
    "../photos" (you can mimic the example line above, replacing `echo` by the adequate command).
  * Submit the job with the command.
```
   sbatch submit.sh
```
  * Verify that the job generates multiple images in the current folder.

==== Advanced Instructions ====

Modify your job script so that it also creates images applying the "negate" filters (it shouldn't apply both filters at the same time but for each input image, it should create two output files, one with the grayscale filter and one with the negate filter). It should still do that in parallel, so you have to define a second variable to your command template that corresponds to the filter.

  * Verify that the job generates twice as many files in the local folder.

==== No need to specify the number of simultaneous tasks? ====

By default, GNU parallel will use one core per task, and it will launch as many
tasks as there are cores on the system. As soon as a task is completed, the
next one will start automatically.

You may change the default behavious with the "-j" option (see the man page with the `man parallel` command).
