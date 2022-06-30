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


Additional information:\
The help message of `filterImage.exe` being in French, here is a translation :
```
Apply filters on a series of images
Options:
  -h [ --help ]         Print help messages
  -i [ --srcdir ] arg   Source directory ?
  -o [ --dstdir ] arg   Destination directory ?
  --files arg           File list ?
  --filters arg         Filter(s) to apply : grayscale, edges, emboss,
                        negate, solarize, flip, flop, monochrome, add_noise
  --combined arg (=0)  Should the filters be combined
                       (applied on after the other on each image) ?
```
