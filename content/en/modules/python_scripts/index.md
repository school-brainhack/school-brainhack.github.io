---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Writing scripts in python"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [python, scripts]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "Learning the basics of python scripts' structure. Turning jupyter notebooks into scripts that can be run from anywhere. Introduction to the argument parser."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "python-file-icon.jpg"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 2h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.

If you have any questions regarding the module content please ask them in the relevant module channel on the school Discord server. If you do not have access 
to the server and would like to join, please send us an email at school [dot] brainhack [at] gmail [dot] com.

Contact your local TA if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module is based on [Greg Kiar](https://github.com/gkiar)'s [QLSC 612 course](https://youtu.be/zpOQENxs1G4) in 2020, with [slides](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1) from Joel Grus' talk at JupyterCon 2018.

The video is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/karKf2CCpPA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## Exercise

* Watch the video and follow along the hands on part to do the exercise. If you prefer to do the execercise on your own, the instructions are also written below.

<details>

<summary> <h4> Click to show the exercise instructions &#11015 <h4/></summary>

In this exercise we will program a key-based encryption and decryption system. We will implement a version of the [Vigenere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), but instead of just using the 26 letters of the alphabet, we will use all the unicode characters.

The Vigenere cipher consists in shifting the letters of the message to encrypt by the index of the corresponding letter in the key. For example the encryption of the letter B with the key D will result in the letter of new_index = index(B) + index(D) = 2 + 4 = 6, so it will be the 6th letter which is F.

:warning: Note that here by index I mean the index of the letter in the alphabet and not the index of the letter in the string.


You pair up the letters of the message with the ones of the key one by one, and repeating the key if it is shorter than the message. For example if the message is `message` and the key is `key`, the pairs will be :
```
(m,k),
(e,e),
(s,y),
(s,k),
(a,e),
(g,y),
(e,k)
```

For the indices of the letter, we will not use the the number of the letter in the alphabet, but the unicode index of the letter, which is easily obtained with the native python function `ord`. The reverse operation of getting a letter from its unicode index is obtained with native python function `chr`. There are 1114112 unicode characters handled by python, so we'll have to make sure we have indices in the range 0 to 1114111. To ensure that, we can use values modulo 1114112, i.e. `encrypted_index = (ord(message_letter) + ord(key_letter)) % 1114112`.

### Step 1: Create relevant functions in `useful_functions.py`

  In that file, implement the following functions :
  * `encrypt_letter(letter, key)` : return the encrypted letter with the key, e.g. `encrypt_letter("l", "h")` should return `'Ô'`.
  * `decrypt_letter(letter, key)` : return the decrypted letter with the key, e.g. `decrypt_letter("Ô", "h")` should return `'l'`.
  * `process_message(message, key, encrypt)`: return the encrypted message using the letters in `key` if encrypt is `True`, and the decrypted message if encrypt is `False`. For example :
```
process_message('coucou', 'clef', True)
'ÆÛÚÉÒá'

process_message('ÆÛÚÉÒá', 'clef', False)
'coucou'
```

After creating these function, try to call them in your python terminal or in a JupyterNotebook to try things out.
Are the functions performing as you expected?

To reliably make sure that the `process_message `function works correctly, let's add a test at the end of the `useful_functions.py` file. 
* Define a `message` variable with a word (e.g. `message = "word"`), then a `key` variable with an other word (e.g. `key = "key"`). 
* Use `process_message` to generate the encryption of the `message` variable with the `key` in an `encrypted_msg` variable.
* Use the `process_message` function again to decrypt the `encrypted_msg` variable (still using the same `key`) in a `decrypted_msg` variable.
* Verify that `message == decrypted_msg` by printing "Test passed" if it is true and "Test failed" if it is false. 

Now we have a proper test of our `process_message` function, and we can run it by executing the `useful_functions.py` script. However we don't want to run the test when we just import the functions from the file, so we will need to use the `if __name__ == "__main__":` statement.
* Put the test in an `if __name__ == "__main__":` block.

Now we have our functions and a test to validate them, we can conclude the first part of the exercise.

### Step 2: Create a file `cypher_script.py`:

* use the Argparse library introduced in the video so that a user can call the script with four arguments : `-i`, `-o`, `-k` and `-m`. `-i` will contain the path to the input text files containing the message. `-o` will contain the path for the output file where the processed message will be written. `-k` will be a string directly containing the key. `-m` will be the mode: a string that can take the value `"encryption"` or `"decryption"` to tell the script if you want to encrypt or decrypt the input message.
* The script should import the functions from `useful_functions.py` and use them in its main function to encrypt or decrypt the text in the input file using the text in the key file as the key, and save the results in the output file. So calling `python cypher_script.py -i msg_file.txt -o msg_encrypted.txt -k my_key -m encryption` should create a `msg_encrypted.txt` file.
* Don't forget to write the code under `if __name__ == "__main__"`. Even though in this file it won’t make a difference, it is never too early to get used to good practices.

<br/>

</details>

<br/>

### Last step: verify your implementation

Finally, decrypt the file obtained with :
```
wget https://raw.githubusercontent.com/school-brainhack/school-brainhack.github.io/main/content/en/modules/python_scripts/message_encrypted.txt
```
with the following key :
```
my_super_secret_key
```
Can you see something cool in the decrypted file ?

 * Follow up with your local TA(s) to validate you completed the exercises correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:


## More resources

If you are curious to learn more advanced capabilities for the Argparse library, you can check this [Argparse tutorial](https://docs.python.org/3/howto/argparse.html).

To learn more about python in general, you can check the [tutorials of the official python documentation](https://docs.python.org/3/tutorial/) and choose the topic you want to learn. I also recommend the [porgramiz tutorials](https://www.programiz.com/python-programming) which have nice videos. Finally for even nicer and fancier videos there is the excellent [python programming playlist](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-) from the youtube channel Socratica.
