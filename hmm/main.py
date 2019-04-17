import sys
import re
import numpy as np
import pandas as pd
import math

start_prob = np.array([0.3, 0.2, 0.5])
transition_prob = np.array([[0.5, 0, 0.5], [0.25, 0.5, 0.25], [0.1, 0.4, 0.5]])
emission_prob = np.array([[0.3, 0.1, 0.4, 0.2], [0.1, 0.5, 0.1, 0.3], [0.25, 0.25, 0.25, 0.25]])

gene_dict = {'A': 0, 'C': 1, 'T': 2, 'G': 3}

current_state = np.array([0.0, 0.0, 0.0])
prev_state = np.array([0.0, 0.0, 0.0])

likely_sequence = []
sequence_idx = 0;

def readfile(filename):
    """"This reads the file that is passed as the argument"""
    infile = open(filename,"r")
    seq = infile.read()
    return re.sub('[^acgtACGT]', '', seq).upper()

def getLog(num): 
	if num == 0:
		num = float("-inf")
	else:
		num = math.log(num, 2)
	return num

def initialization(letter):
	idx = 0
	column = gene_dict[letter]
	for state in current_state:
		initialProb = getLog(start_prob[idx])
		emissionProb = getLog(emission_prob[idx][column])
		prob = 0;

		if initialProb == "-inf" or emissionProb == "-inf":
			prob = "-inf"
		else:
			prob = initialProb + emissionProb

		current_state[idx] = prob
		prev_state[idx] = prob
		idx = idx + 1

def getMax(letter, row):
	idx = 0
	column = gene_dict[letter]
	all_probabilities = np.array([0.0, 0.0, 0.0])
	for state in current_state:
		prev_result = prev_state[idx]
		transitionProb = getLog(transition_prob[row][idx])
		if prev_result == "-inf" or transitionProb == "-inf":
			all_probabilities[idx] = "-inf"
		else:
			prob = prev_result + transitionProb
			all_probabilities[idx] = prob
		idx = idx + 1

	return all_probabilities.max()


def iteration(letter):
	idx = 0
	column = gene_dict[letter]
	for state in current_state:
		emissionProb = getLog(emission_prob[idx][column])
		if emissionProb == "-inf":
			current_state[idx] = emissionProb
		else:
			maxVal = getMax(letter, idx)
			prob = emissionProb + maxVal
			current_state[idx] = prob
		idx = idx + 1
	np.copyto(prev_state, current_state)

def getVal(num):
	return 'S' + str(num + 1)

def main():
	sequence = "ATCCGAACCGTACCAGGTCAC"
	try:
		filename = sys.argv[1]
		sequence = readfile(filename)

		print("the sequence is: ", sequence)

		first_letter = sequence[0].upper()
		initialization(first_letter)
		likely_sequence.append(getVal(current_state.argmax()))

		# remove first letter from sequence
		sequence = sequence[1:]
		for letter in sequence:
			letter = letter.upper()
			iteration(letter)
			val = getVal(current_state.argmax())
			likely_sequence.append(val)

		print("the likely_sequence is: ", likely_sequence)
	except IOError:
		print("Sorry file does not exist.")

main();
