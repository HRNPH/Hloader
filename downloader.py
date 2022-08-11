from pytube import YouTube

def YTDownloader(download_link):     
    url =YouTube(str(download_link))
    video = url.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('./downloaded')
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210) 