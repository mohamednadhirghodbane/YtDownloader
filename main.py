import sys

from pytube import YouTube

link = input("enter the link of the video you wish to download : ")
yt = YouTube(link)
location = 'C:/Users/uif43541/Downloads'
#Title of video
print('Title:' , yt.title)
#Number of views of video
print('Number of views: ' , yt.views , 'views')
#Length of the video
print('Length of video:' ,yt.length, 'seconds')
# #Description of video
# print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)
#Author
print('author is :', yt.author)

# #printing all the available streams
# streams=str(yt.streams).split(",")
# for stream in streams :
#     print(stream)

# AV = input('Would you like an audio or video version a/v : ')
# if AV == 'a' :
#     audio_streams =yt.streams.get_audio_only()
#     for audio_stream in str(audio_streams).split(',') :
#        print(audio_stream)
#     YS = input('procedd to download ? y/n : ')
#     if YS == 'y':
#         audio_streams.download(location)
#     else:
#         sys.exit()
#
# else :
# #progressive streams is a ready to play video with built-in audio
progressive_streams =yt.streams.filter(progressive=True)
for progessive_stream in str(progressive_streams).split(',') :
    print(progessive_stream)
tag = input('\nenter the itag of the stream you wish to download = ')
ys = yt.streams.get_by_itag(tag)
print(ys)
yn = input('would you like to proceed y/n ? : ')
if yn == 'y' :
    ys.download(location)
else :
    sys.exit()
