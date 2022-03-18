"""A simple Python script to download videos"""
import pytube


def main():
    url = 'https://www.youtube.com/watch?v=hFgaAtgY29Q&ab_channel=GamersCathedral'
    youtube = pytube.YouTube(url)
    youtube.streams.filter(resolution='720p').first().download()

main()