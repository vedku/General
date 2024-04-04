from pytube import Playlist
import time

def download_playlist(playlist_url, path='C:/Users/YourUsername/Desktop/'): #modify the path
    playlist = Playlist(playlist_url)
    print(f'Found {len(playlist.videos)} videos in the playlist.')
    
    for video in playlist.videos:
        try:
            print(f'Downloading: {video.title}')
            video.streams.get_highest_resolution().download(output_path=path)
            print(f'Finished downloading: {video.title}')
            time.sleep(5)  #anti rate limit
        except Exception as e:
            print(f'Failed to download {video.title}: {e}')

if __name__ == '__main__':
    playlist_url = 'YOUR_PLAYLIST_URL_HERE'  #replace with your url
    download_playlist(playlist_url, path='C:/Users/YourUsername/Desktop/')  #modify the path

