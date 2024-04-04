from pytube import Playlist

def download_playlist(playlist_url, path='Downloads/'): #replace with your path
    playlist = Playlist(playlist_url)

    for video in playlist.videos:
        print(f'Downloading: {video.title}')
        video.streams.get_highest_resolution().download(output_path=path)
        print(f'Finished downloading: {video.title}')

if __name__ == '__main__':
    playlist_url = 'pass'  #your url here
    download_playlist(playlist_url)
