import re
from pytube import YouTube
from moviepy.editor import *

def mp4(url: str):
    yt = YouTube(url)
    print(yt.streams.get_highest_resolution().filesize)
    if (yt.streams.get_highest_resolution().filesize) > 7900000:
        return None
    stream = yt.streams.filter(progressive=True).order_by('resolution').last()
    stream.download()
    regex = r'[#%{}/<>*?/$\'":+`|=,.]'
    title = re.sub(regex, '', yt.title)
    print(title)
    return f'../caller-8413-backend/{title}.mp4'
def mp3(url: str):
    yt = YouTube(url)
    print(yt.streams.get_highest_resolution().filesize)
    if (yt.streams.get_highest_resolution().filesize) > 50000000:
        return None
    stream = yt.streams.filter(progressive=True).order_by('resolution').last()
    stream.download()
    regex = r'[#%{}/<>*?/$\'":+`|=,.]'
    title = re.sub(regex, '', yt.title)
    print(title)
    mp4 = VideoFileClip(title + '.mp4')
    mp3 = mp4.audio
    mp3.write_audiofile(title + '.mp3')
    mp4.close()
    mp3.close()
    os.remove(title + '.mp4')
    if (os.path.getsize(title + '.mp3') > 7900000):
        os.remove(title + '.mp3')
        return None
    return f'../caller-8413-backend/{title}.mp3'