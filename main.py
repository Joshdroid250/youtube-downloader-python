from pytubefix import YouTube

input_url = input("agregar link de descarga: ")
yt = YouTube(input_url)
print(f'El titulo de video a descargar es: {yt.title}')
print(f'Escoge que video descargar: {yt.streams.filter(file_extension='mp4')}')

try:
    stream = yt.streams.get_by_itag(input("Ingresa el itag del video a descargar: "))
    stream.download()   # Download the video
    print("Download completed successfully")
except Exception as e:
    print(f"An error occurred: {e}")