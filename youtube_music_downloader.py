from pytube import YouTube
import os

while(True):
    print("\nYouTube Music Downloader\n")
    print("Do you want to download a music?")
    option = input("[y] YES, [n] NO: ").lower()

    if option == 'y':
        path = os.getcwd()
        path = path.replace("\\","\\\\")
        
        try:
            os.mkdir('Songs')
        except FileExistsError:
            pass
        
        songs = []
        for filename in os.listdir('Songs'):
            filename = filename.strip()
            filename = filename[:-4]
            songs.append(filename)
        
        link = input("\nEnter the youtube music video link: ")
        yt = YouTube(link)
        
        song_title = yt.title.replace('.','')
        song_title = song_title.replace('\\','')
        song_title = song_title.replace('/','')
        song_title = song_title.replace(':','')
        song_title = song_title.replace('*','')
        song_title = song_title.replace('?','')
        song_title = song_title.replace('|','')
        song_title = song_title.replace('"','')
        song_title = song_title.replace("'",'')
        song_title = song_title.replace('>','')
        song_title = song_title.replace('<','')
    
        if song_title in songs:
            print("\nThis song already exists in the 'Songs' folder.")
        else:
            if yt.check_availability == None:
                print("\nThe music video is not available.")
            else:
                yd = yt.streams.get_audio_only()
                yd.download('Songs')
                print("\nThe song", yd.title, "was downloaded and added to 'Songs' folder.")
                
    elif option == 'n':
        break
    else:
        print("\nInvalid option.")