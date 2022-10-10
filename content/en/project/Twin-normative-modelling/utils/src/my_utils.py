import pandas as pd

def read_input(file):
    infile = pd.read_csv(file, sep='\t')
    return(infile)


def return_columnames(file):
    for col in file.columns:
        print(col)

def convert_sex(infile):
    if infile.endswith('.txt'):
        file = pd.read_csv(infile, sep='', header="none")
    else: 
        file = infile
    return file



