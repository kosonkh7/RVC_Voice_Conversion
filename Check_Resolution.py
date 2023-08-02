from moviepy.editor import VideoFileClip

def get_video_resolution(file_path):
    # 영상 파일 로드
    video = VideoFileClip(file_path)

    resolution = f"{video.w} x {video.h}"

    return resolution


# 해상도 구하고자 하는 영상 파일 경로 및 이름 입력
file_path = '이런엔딩.mp4'  

video_resolution = get_video_resolution(file_path)

if video_resolution == '1920 x 1080' :
    video_resolution = '1080p Full HD'

elif video_resolution == '1280 x 720' :
    video_resolution = '720p HD'

print('Video resolution:', video_resolution)
