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

Contact François Paugam if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources
This module was presented by [Greg Kiar](https://github.com/gkiar) during the QLSC 612 course in 2020, with [slides](https://docs.google.com/presentation/d/1n2RlMdmv1p25Xy5thJUhkKGvjtV-dkAIsUXP-AL4ffI/edit#slide=id.g362da58057_0_1) from Joel Grus' talk at JupyterCon 2018.

The video is available below:
<iframe width="560" height="315" src="https://www.youtube.com/embed/zpOQENxs1G4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Exercise

In this exercise we will program a key-based encryption and decryption system. We will implement a version of the [Vignere cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher), but instead of just using the 26 letters of the alphabet, we will use all the unicode characters.

The Vignere cipher consists in shifting the letters of the message to encrypt by the index of the corresponding letter in the key. For example the encryption of the letter B with the key D will result in the letter of new_index = index(B) + index(D) = 2 + 4 = 6, so it will be the 6th letter which is F.

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

In a file `useful_functions.py`, you'll implement the following functions :
* `encrypt_letter(letter, key)` : return the encrypted letter with the key, e.g. `encrypt_letter("l", "h")` should return `'Ô'`.
* `decrypt_letter(letter, key)` : return the decrypted letter with the key, e.g. `decrypt_letter("Ô", "h")` should return `'l'`.
* `process_message(message, key, encrypt)`: return the encrypted message using the letters in `key` if encrypt is `True`, and the decrypted message if encrypt is `False`. For example :
```
process_message('coucou', 'clef', True)
'ÆÛÚÉÒá'

process_message('ÆÛÚÉÒá', 'clef', False)
'coucou'
```

Then in a file `cypher_script.py`:
* use the Argparse library introduced in the video so that a user can call the script with three arguments : `--message`, `--key` and `--mode`. `--message` will contain the path to a text files containing the message. `--key` will be a string directly containing the key. `--mode` will be a string that can take the value `"enc"` or `"dec"` to tell the script if you want to encrypt or decrypt the message.
* The script should import the functions from `useful_functions.py` and use them in its main function to encrypt or decrypt the text in the message file using the text in the key file as the key, and save the results in a file that has the same name as the message file but with a `_encrypted` or `_decrypted` suffix depending on the mode. So calling `python cypher_script.py --message msg_file.txt --key my_key --mode enc` should create a `msg_file_encrypted.txt` file.
* Don't forget to use the `if __name__ == "__main__"`. Even though in this example it won’t make a difference, it is never too early to get used to good practices.

Finally, decrypt the file obtained with :
```
wget https://raw.githubusercontent.com/BrainhackMTL/psy6983_2021/master/content/en/modules/python_scripts/message_encrypted.txt
```
with the following key :
```
my_super_secret_key
```

 * Follow up with François Paugam to validate you completed the exercise correctly.
 * :tada: :tada: :tada: you completed this training module! :tada: :tada: :tada:

<br/>

<details>

<summary> <h2> On the usefulness of "if __name__ == '__main__':" (click to show &#11015) <h2/></summary>

It is not obvious why you shoud put the `if __name__ == "__main__":` line in your script. Indeed in a lot of cases, putting it or not won't change anything to how your code runs. But in specific settings with multiple scripts importing from each pother, not putting it in can quickly lead to a nightmare.
To give you an insight of how and why it is useful, here is an example (if you don't want to read or if you want complementary explanations, here is [a nice youtube video](https://www.youtube.com/watch?v=g_wlZ9IhbTs) about it).

Suppose you have a script to fit a Ridge model on provided data, judiciously named `fit_Ridge.py`, which looks like this :
```
#!/usr/bin/env python
import argparse
import pickle  # pickle is a librairie to save and load python objects.
import numpy as np
from sklearn.linear_model import Ridge

def  fit_Ridge_model(X, Y):
  model = Ridge()
  model.fit(X, Y)
  return model

parser = argparse.ArgumentParser()
parser.add_argument("--X_data_path", type=str)
parser.add_argument("--Y_data_path", type=str)
parser.add_argument("--output_path", type=str)
args = parser.parse_args()

X = np.load(args.X_data_path)
Y = np.load(args.Y_data_path)
model = fit_Ridge_model(X, Y)
pickle.dump(model, open(args.output_path, 'wb'))
```
This script allows the user to provide the paths to two numpy files as data to fit a Ridge model, and to save the model to the provided path with a command like :
```
python fit_Ridge.py --X_data_path data_folder/X.npy --Y_data_path data_folder/Y.npy --output_path models/Ridge.pk
```
There is no `if __name__ == "__main__":` to be seen but, used on its own, the script works fine.

But later, you write an other script `compare_to_Lasso.py` that compare Ridge and Lasso models on the same data, so you need to fit a Ridge model again. Eager to apply the good practices of programming, you judiciously decide not to duplicate the code for fitting a ridge model, but to import the `fit_Ridge_model` function from the `fit_Ridge.py`. Thus your second script looks like that :
```
#!/usr/bin/env python
import numpy as np
import argparse
from sklearn.linear_model import Lasso
from fit_Ridge import fit_Ridge_model

parser = argparse.ArgumentParser()
parser.add_argument("--X_data_path", type=str)
parser.add_argument("--Y_data_path", type=str)
args = parser.parse_args()

X = np.load(args.X_data_path)
Y = np.load(args.Y_data_path)

ridge_model = fit_Ridge_model(X, Y)
lasso_model = Lasso()
lasso_model.fit(X, Y)

ridge_score = ridge_model.score(X, Y)
lasso_score = lasso_model.score(X, Y)

if Ridge_score > lasso_score:
    print("Ridge model is better.")
else:
    print("Lasso model is better.")
```

It seems fine but here when you try to call
```
python compare_to_Lasso.py --X_data_path data_folder/x.npy --Y_data_path data_folder/Y.npy
```
you get an error :
```
Traceback (most recent call last):
  File "compare_lasso_ridge.py", line 5, in <module>
    from fit_Ridge import fit_Ridge_model
  File "/Users/francois/scratch/fit_Ridge.py", line 21, in <module>
    pickle.dump(model, open(args.output_path, 'wb'))
TypeError: expected str, bytes or os.PathLike object, not NoneType
```

The error shows that the script tried to save a model to the path `args.output_path`, which was not defined so it was set to None and raised a TypeError. But our `compare_to_Lasso.py` script never tries to save a model ! Indeed looking at the other lines of the error message, we see that it comes from the import. In fact what happens is that when we try to import the `fit_Ridge_model` fuction from the `fit_Ridge.py` file, python will read the entire file and execute everything that is written in it, so it will try to fit a Ridge model and to save it. But we don't want python to execute everything, we just want it to read the definition of the `fit_Ridge_model` function. That is why here we absolutely need the `if __name__ == "__main__":`, so we modify the `fit_Ridge.py` script like that :
```
#!/usr/bin/env python
import argparse
import pickle  # pickle is a librairie to save and load python objects.
import numpy as np
from sklearn.linear_model import Ridge

def  fit_Ridge_model(X, Y):
    model = Ridge()
    model.fit(X, Y)
    return model

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--X_data_path", type=str)
    parser.add_argument("--Y_data_path", type=str)
    parser.add_argument("--output_path", type=str)
    args = parser.parse_args()

    X = np.load(args.X_data_path)
    Y = np.load(args.Y_data_path)
    model = fit_Ridge_model(X, Y)
    pickle.dump(model, open(args.output_path, 'wb'))
```
Now when importing from this script, python will read the definition of the function, but after that it will not execute the rest, since during the import the variable `__name__` is not set to `"__main__"` but to `"fit_Ridge"`.

In the end using `if __name__ == "__main__":` is the only way to safely import functions from our script, and since you never know for sure that you won't have to import something from a script in the future, putting it in all of your script by default is not a bad idea.

</details>
<br>

## More resources

If you are curious to learn more advanced capabilities for the Argparse library, you can check this [Argparse tutorial](https://docs.python.org/3/howto/argparse.html).

To learn more about python in general, you can check the [tutorials of the official python documentation](https://docs.python.org/3/tutorial/) and choose the topic you want to learn. I also recommend the [porgramiz tutorials](https://www.programiz.com/python-programming) which have nice videos. Finally for even nicer and fancier videos there is the excellent [python programming playlist](https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-) from the youtube channel Socratica.
