import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
from IPython.display import YouTubeVideo
from youtube_transcript_api import YouTubeTranscriptApi


def link(utube_link):
    if "=" not in utube_link:
        video_id_list = utube_link.split("/")
        video_id = video_id_list[3]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            result = ""
            for i in transcript:
                result += ' ' + i['text']
            return result
        except:
            return "Sorry there was an issue,Please check if the video have subtitle/captions turned on"
    else:
        video_id_list = utube_link.split("=")
        video_id = video_id_list[1]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            result = ""
            for i in transcript:
                result += ' ' + i['text']
            return result
        except:
            return "Sorry there was an issue,Please check if the video have subtitle/captions turned on"
        else:
            return "Sorry there was an issue,Please check if the video have subtitle/captions turned on"


def summarizer(utube_link):
    if "=" not in utube_link:
        video_id_list = utube_link.split("/")
        video_id = video_id_list[3]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            result = ""
            for i in transcript:
                result += ' ' + i['text']
        except:
            return "Sorry there was an issue,Please check if the video have subtitle/captions turned on"
    else:
        video_id_list = utube_link.split("=")
        video_id = video_id_list[1]
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            result = ""
            for i in transcript:
                result += ' ' + i['text']
            sentence_list = nltk.sent_tokenize(result)
            stopwords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]

            word_frequencies = {}
            for word in nltk.word_tokenize(result):
                if word not in stopwords:
                    if word not in word_frequencies.keys():
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1
            maximum_frequncy = max(word_frequencies.values())
            for word in word_frequencies.keys():
                word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
            sentence_scores = {}
            for sent in sentence_list:
                for word in nltk.word_tokenize(sent.lower()):
                    if word in word_frequencies.keys():
                        if len(sent.split(' ')) < 30:
                            if sent not in sentence_scores.keys():
                                sentence_scores[sent] = word_frequencies[word]
                            else:
                                sentence_scores[sent] += word_frequencies[word]
            summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

            summary = ' '.join(summary_sentences)
            return(summary)
            
        except:
            return "Sorry there was an issue,Please check if the video have subtitle/captions turned on"
        
    
#print(link("https://www.youtube.com/watch?v=A4OmtyaBHFE"))
