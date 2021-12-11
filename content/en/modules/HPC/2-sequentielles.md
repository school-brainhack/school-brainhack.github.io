In this exercise, we want to apply the "grayscale" filter to one picture.

==== Instructions ====

We will use the filterImage.exe application to convert one picture to grayscale.

  * Modify submit.sh in order to load required modules with `module load gcc boost` and call filterImage.exe
    with the "grayscale" filter and one picture file. Use `../filterImage.exe --help` to find the arguments to use.
  * Submit the job with the following command:
```
   sbatch submit.sh
```
  * Verify that the job has generated one image file in the current folder.
    Note: you may download this file to your local computer with any SCP client.
          The visual result can show errors on some lines of pixels.
          The goal of this exercise is only to practice job submission.
