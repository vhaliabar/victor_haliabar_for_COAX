from TikTokApi import TikTokApi
from moviepy.editor import VideoFileClip

def converter_mp4_to_gif(tiktok_video_id='6744084223445044485'):
    api = TikTokApi(custom_verify_fp='verify_l6bnwrg5_FBKwwBLS_SLv6_4GyO_8g8X_mWDHRr9nqzhv')
    video_bytes = api.video(tiktok_video_id).bytes()
    # Saving The Video in .mg4 format 
    with open('saved_video.mp4', 'wb') as output:
        output.write(video_bytes)
        
    # Converting to .gif format
    videoClip = VideoFileClip("saved_video.mp4")
    videoClip.write_gif("saved_video.gif")
    print('Done! Video clip successfully converted into .gif format')
    
if __name__ == '__main__': converter_mp4_to_gif()