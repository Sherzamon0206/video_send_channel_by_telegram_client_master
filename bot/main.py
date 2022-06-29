from pytube import YouTube, Playlist
from telethon.sync import TelegramClient,events
import os
import sys
import re

from io import BytesIO
def send_video(url):
    print("video if ga kirdi")
    try:
        print("video  try  ga kirdi")

        playlist = Playlist(url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        soni = len(playlist.video_urls)
        print("soni: ", soni)

        links = playlist.video_urls
        print(f"try: {links}", )
    except:
        print("video exceptga kirdi")

        links = []
        links.append(url)
        print("except : ", links)

    for link in links:
        buffer = BytesIO()

        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        video.stream_to_buffer(buffer=buffer)
        buffer.seek(0)
        filename = video.title
        print(video.filesize / (2 ** 20))
        try:
            api_id = #######
            api_hash = ###########

            client = TelegramClient('session_name',
                                    api_id,
                                    api_hash,
                                    )

            client.start()
            client.send_message(-1001590382098, "ishladi1")
            client.send_message(-1001590382098, "ishladi2")
            message = client.send_file(-1001590382098, buffer, filename=filename+'.mp4')
        except Exception as e:
            print(e)
            return 0
        return 1