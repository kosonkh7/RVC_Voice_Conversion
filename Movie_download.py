# 유튜브 동영상에서 음성 없는 영상만 다운로드 받기 위한 코드

import pytube

def download_highest_quality_video(url):
    # 유튜브 객체 생성
    youtube = pytube.YouTube(url)

    # 화질 지정
    video_stream = youtube.streams.filter(res="1080p").first()

    # 영상 다운로드
    video_stream.download()

    print('Video downloaded successfully!')

# 다운로드 받을 영상 링크 입력 
video_url = 'https://youtu.be/j5fsk-3-Y7I?list=RDj5fsk-3-Y7I' 

download_highest_quality_video(video_url)

