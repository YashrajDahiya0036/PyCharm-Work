import speedtest

speed = speedtest.Speedtest()


while True:
    download_speed = speed.download()
    upload_speed = speed.upload()
    print(download_speed, upload_speed)
