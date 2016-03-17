import sys
import json

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1], 'r')
    tweet_file = open(sys.argv[2], 'r')
    
    # construct a dict
    dict = construct_dict(sent_file)
    # for each of the line, extract the tweet and then calculate the score
    i = 0
    for line in tweet_file:
    	data = json.loads(line)
    	if "text" in data:
    		# if this is a tweet, print its score
    		tweet = data['text']
    		print get_score(dict, tweet)
    	i +=1

def construct_dict(sent_file):
	scores = {} # initialize an empty dictionary
	for line in sent_file:
	  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
	  scores[term] = int(score)  # Convert the score to an integer.
	return scores

## given the dict and a single tweet, return the score of this tweet
def get_score(dict, tweet):
	score = 0
	for word in tweet.split(" "):
		if word in dict:
			current_score = dict[word]
		else:
			current_score = 0
		score += current_score
	return score

if __name__ == '__main__':
    main()