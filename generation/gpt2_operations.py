import random
import re
import string
import sys

import nltk
import nltk.tokenize
import numpy
from nltk.sentiment import SentimentIntensityAnalyzer

SAMPLES_SUBSET_DIVISOR = 10


def fill_poem(random_seed, lines, sample_quatrains, required_lines):
    # finds a quatrain from the corpus which is similar in sentiment to the poem's current sentiment to add to the poem.
    if len(lines) < required_lines:
        sia = nltk.sentiment.SentimentIntensityAnalyzer()
        desired_sentiment = numpy.array(list(sia.polarity_scores(text=' '.join(lines)).values()))
        random.seed(random_seed)
        r = list(range(len(sample_quatrains)))
        random.shuffle(r)
        # only consider the first SAMPLES_SUBSET_DIVISOR random samples when finding the most similar sentiment
        r = r[:len(r) // SAMPLES_SUBSET_DIVISOR]
        closest_sentiment_index = 0
        closest_sentiment_dist = sys.maxsize
        for i in r:
            sample_sentiment_i = numpy.array(list(sia.polarity_scores(text=' '.join(sample_quatrains[i])).values()))
            dist = numpy.sqrt(numpy.sum(numpy.square(desired_sentiment - sample_sentiment_i)))
            if dist < closest_sentiment_dist:
                closest_sentiment_index = i
                closest_sentiment_dist = dist
        closest_sentiment_quatrain = sample_quatrains[closest_sentiment_index]
        del sample_quatrains[closest_sentiment_index]
        lines += closest_sentiment_quatrain
    return lines, sample_quatrains


def get_n_prompts(processed_samples, n_prompts, quatrain_length):
    # finds n prompts (single quatrains) which each demonstrate a distinct emotional tone
    emotion_map = {}
    all_emotions = set()
    # original location of this file: https://github.com/attreyabhatt/Sentiment-Analysis/blob/master/emotions.txt
    with open('generation/emotion_cardinality_reducer.txt') as emotion_map_file:
        for emotion_pair in emotion_map_file:
            word, emotion = emotion_pair.replace('\n', '').split(':')
            emotion_map[word] = emotion
            all_emotions.add(emotion)
    all_emotions = list(all_emotions)

    prompts = {}
    while len(prompts) < n_prompts:
        # continually looks for a word matching the input side of the cardinality reducer
        print(len(prompts))
        random_emotion = random.choice(all_emotions)
        random_sample_indices = list(range(len(processed_samples)))
        random.shuffle(random_sample_indices)
        for j in random_sample_indices:
            lines = processed_samples[j].split('\n')
            if len(lines) >= quatrain_length:
                first_quatrain_j = lines[:quatrain_length]
                tokens_j = nltk.tokenize.word_tokenize(' '.join(first_quatrain_j))
                emotions = set()
                for word in set(tokens_j).intersection(emotion_map.keys()):
                    emotions.add(emotion_map[word])
                if random_emotion in emotions and j not in prompts.keys():
                    prompts[random_emotion] = first_quatrain_j
                    break
    return prompts


def load_sample_lines():
    f = open('generation/gpt2_samples.txt', encoding='UTF-8')
    text = f.read()
    samples = re.split(r'={40} SAMPLE \d+ ={40}|<\|endoftext\|>', text)[1:]
    samples = [sample[:((len(sample)) // 4) * 4] for sample in samples if len(sample) >= 4]
    samples = [re.split(r'\n+', sample[1:]) for sample in samples]
    samples = [item for sublist in samples for item in sublist if 4 <= len(item.split(' ')) <= 9]
    for i in range(len(samples)):
        while samples[i][-1] in string.punctuation:
            samples[i] = samples[i][:-1]
    return samples


def load_sample_quatrains(quatrain_length):
    samples = load_sample_lines()
    quatrains = []
    for i in range(0, len(samples), quatrain_length):
        for j in range(quatrain_length):
            quatrains.append([samples[i + j]])
    return quatrains
