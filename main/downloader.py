import os

# Create a directory to save the videos in, if it doesn't already exist
if not os.path.exists('youtube_videos'):
    os.makedirs('youtube_videos')

# Open the text file containing the YouTube links
with open('youtube_links.txt', 'r') as f:
    links = f.readlines()

# Loop through the links and download each video
for link in links:
    try:
        # Download the video using yt-dlp
        stripped_link = link.split("v=")[-1].replace("\n", '')
        # os.makedirs(f'youtube_videos/{stripped_link}')
        os.system(f'dependencies\yt-dlp.exe --ffmpeg-location "dependencies\ffmpeg-7.1-essentials_build\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe" --remux-video mp4 --paths "youtube_videos/{stripped_link}" --output "{stripped_link}.mp4" {link}')

        # Print a success message
        print(f'Successfully downloaded {link}')

    except Exception as e:
        # Print an error message if something went wrong
        print(f'Error downloading {link}: {e}')
