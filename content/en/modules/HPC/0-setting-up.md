
The goal of these exercises is to familiarize yourself with job submissions on
a cluster. To do that, we will use a home-made image processing tool called
"filterImage.exe" and a set of images.

The set of images you will use are the images in the `photos` folder.

===== Compiling filterImage.exe =====

The image processing tool must be built (i.e. compiled). To do that, you first
need to load appropriate modules. The compilation requires GNU compilers and
the BOOST library. To load these modules:
```
   module purge
   module load gcc boost
   module list
```
Here `module purge` is first called to unload all potentially loaded module, so that we only have
the module mentioned in the `module load` command, to avoid any eventual conflict between modules.
Some module might not be unloaded unless you use the `--force` flag, but that's ok in our case, we don't need
to remove everything.
`module list` lists all our modules.


Once all required modules are loaded, you can compile filterImage.exe with the command:
```
   make
```
This will create a file named filterImage.exe in your directory. This
executable will be used for each exercise.

===== Outline of Exercises =====

Each exercise is located in its own directory. Each exercise has a
README.en file, a submit.sh file that you will edit, and a solution.sh file.
Try exercises according to your needs:

  * 1-base
   
    Getting started with job submission: useful for any use case.

  * 2-sequentielles

    This exercise is useful if you run multiple serial jobs running for hours

  * 3-gnu-parallel

    This exercise is useful if you run multiple short serial jobs (<1 hour)

  * 4-lot-de-taches

    This exercise is useful if you run hundreds of jobs; you need job arrays

  * 5-tache-mpi

    This exercise is useful if you run parallel jobs with MPI on multiple nodes
