

import yt_dlp

class MetaDataNotAvailable(Exception):
    pass

class VideoTitleExtractor:

    def __init__(self, yt_dl_args: dict):
        self.videoinfo = ""
        self.yt_opts = yt_dl_args

    def process_video_track(self, video_item: dict) -> tuple:
        '''Process a dictionary of metadata and return None or song_name, artist'''
        try:
            if video_item is None:
                raise MetaDataNotAvailable
            else:
                song_name = video_item["track"]
                artist = video_item["artist"]
                return str(artist), str(song_name)
           
        except (KeyError, MetaDataNotAvailable) as EmptyValue:
            return None, None

    def call_yt_dlp(self, video_id: str) -> dict:
        youtube_url = "https://www.youtube.com/watch?v=" + video_id
        video_info = yt_dlp.YoutubeDL(self.yt_opts).extract_info(
                        youtube_url, download=True)
        return video_info


