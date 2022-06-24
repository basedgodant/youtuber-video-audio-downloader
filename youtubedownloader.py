from youtube_dl import YoutubeDL

downloader = YoutubeDL({'format':'bestaudio'})

while True:
    try:
        print('Youtube Downloader'.center(40, '_'))
        LINK = input('Enter youtube url :  ')
        downloader.extract_info(LINK)

    except Exception:
        print("Couldn't download the audio")

    finally:
        option = int(input('1 = Another Link \n Anything Else = Exit \n : '))

        if option!=1:
            break