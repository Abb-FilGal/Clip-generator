import os
import pytube

# Create a directory to save the videos in, if it doesn't already exist
if not os.path.exists('youtube_videos'):
    os.makedirs('youtube_videos')

# Open the text file containing the YouTube links
with open('youtube_links.txt', 'r') as f:
    links = f.readlines()

# Loop through the links and download each video
for link in links:
    try:
        # Create a YouTube object from the link
        youtube = pytube.YouTube(link)

        # Get the first video stream available
        stream = youtube.streams.first()

        # Set the filename to the video title
        filename = youtube.title + '.mp4'

        # Download the video to the 'youtube_videos' directory
        stream.download(os.path.join('youtube_videos', filename))

        # Print a success message
        print(f'Successfully downloaded {youtube.title}')

    except Exception as e:
        # Print an error message if something went wrong
        print(f'Error downloading {link}: {e}')
