
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo

def link(utube_link):
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
        


'''def summarized(utube_link):
    video_id_list = utube_link.split("=")
    video_id = video_id_list[1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        result = ""
        for i in transcript:
            result += ' ' + i['text']
        summarizer = pipeline('summarization')
        num_iters = int(len(result)/1000)
        summarized_text = []
        for i in range(0, num_iters + 1):
            start = 0
            start = i * 1000
            end = (i + 1) * 1000
            #print("input text \n" + result[start:end])
            out = summarizer(result[start:end])
            out = out[0]
            out = out['summary_text']
            #print("Summarized text\n"+out)
            summarized_text.append(out)
        return summarized_text
    except:
        return "Sorry there was an issue"'''
    
#print(link("https://www.youtube.com/watch?v=A4OmtyaBHFE"))
