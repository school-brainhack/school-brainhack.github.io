#### Short answers
**What are some of the main advantages of using the shell?**
Possible responses
- High action-to-keystroke ratio
- Support for automating repetitive tasks
- Capacity to access remote machines

**What are some of disadvantages?**
- Response : Textual nature and how cryptic its commands and operation

**Name a few command lines that enable to read/write/operate on files. What are they used for?**
- Response : Just to name a few : ls, pwd, cd, mv, cp, mkdir

**What is an option, also called flag or switch?**
- Response : Options change the behavior of a command

**What are arguments in a command line?**
- Response : These tell the command what to operate on!


**Can you tell the difference between relative and absolute paths?**
Response : The top of the file system is the root directory, it holds the ENTIRE FILE SYSTEM. Inside are several other directories

**What is Nano?**
- Response : A textfile editor

**You want to move a file to a folder and avoid overwriting another file with the same name. How can you make this move safely?
True/False**
- Response : You can ls the content of the directory to make sure names are not exactly the same. Also, you could refer to the -i flag for "interactive" moving (with warnings!).

#### TRUE/FALSE

**We are always located somewhere in the file system**

           True
**It is possible to be located in more than one place at once**

          False
**You can choose multiple options after a command**

          True
**Changing one directory at a time is the same as providing the full path to the final destination**

          True
**Environmental variables are preceded by $**

          True (in most cases)
          
**Good naming conventions of files include special characters**

          False

#### Exercises 

**Exercice 1**

         No: . refers to the current working directory
         No: / refers to the root directory
         No: Amanda's home directory is /Users/amanda
         No: this goes up two levels, to Users
         Yes: ~ refers to the home directory, which is Users/amanda.
         No: this would navigate to the hom directory inside Users/amanda/data (if it exists)
         Yes: unnecessarily complicated, but correct
         Yes: this is a shortcut to go back to the user's home directory!
         Yes: this goes up one directory, to /Users/amanda
         
**Exercise 2**

2.1.

         No: there is a directory backup in Users
         No: this is the content of /Users/thing/backup, but .. means we are one level up from that
         No: for the same reason as (2)
         Yes: ../backup refers to /Users/backup

2.2.

         No: pwd is not the name of a directory, it is a command.
         Yes: ls without any arguments will list the contents of the current directory.
         Yes: providing the absolute path of the directory will work.

**Exercice : Moving files to a new folder**
          
          mv sucrose.dat maltose.dat ../raw

**Exercise : Renaming files**

          No: this would create a file with the correct name but would not remove the incorrectly named file
          Yes: this would rename the file!
          No, the . indicates where to move the file but does not provide a new name.
          No, the . indicates where to copy the file but does not provide a new name.

**Exercise : Moving and copying**

          No: proteins-saved.dat is located at /Users/jamie
          Yes!
          No: proteins.dat is located at /Users/jamie/data/recombine
          No, proteins-saved.dat is located at /Users/jamie

**Exercise : Copy with multiple filenames**

          When given multiple filenames followed by a directory all the files are copied into the directory.
          When give multiple filenames with no directory, cp throws an error:
          cp: target morse.txt is not a directory

**Exercise : List filenames matching a pattern**

          No: This will give ethane.pdb methane.pdb octane.pdb pentane.pdb
          No: this will give octane.pdb pentane.pdb
          Yes!
          No: This only shows file starting with ethane
