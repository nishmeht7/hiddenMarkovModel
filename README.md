# hiddenMarkovModel

## About

Shows the most likely sequence of genes given a FASTA sequence of DNA nucleotide. Hidden Markov Model implementation using Viterbi recurrence relations.

## Installation

```shell
# install virtual env if not already installed
pip install virtualenv

# create virtualenv
virtualenv -p <python2.7 path> hmm_ve

# activate virtual environment on macOS or linux
source hmm_ve/bin/activate

#install requirements
pip install -r requirements.txt
```

## Running your own data
```shell
python main.py <path to input file with FASTA DNA sequence>
```






