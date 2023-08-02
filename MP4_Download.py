#유튜브 동영상에서 음성만 mp4 형식으로 다운로드 받는 코드

import pytube
import subprocess

def download_video(url):
    # 유튜브 객체 생성
    youtube = pytube.YouTube(url)

    # 화질 지정
    audio_stream = youtube.streams.filter(only_audio=True).first()

    # 다운로드
    audio_stream.download()

    # 파일 경로 지정
    file_path = audio_stream.default_filename

    print('다운로드 완료!')

    return file_path


# 다운로드 받고자 하는 영상 링크 입력
video_url = 'https://youtu.be/j5fsk-3-Y7I?list=RDj5fsk-3-Y7I'  
downloaded_file = download_video(video_url)


