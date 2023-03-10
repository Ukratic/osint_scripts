from pytube import YouTube
import argparse

#parse argument : link to download
parser = argparse.ArgumentParser(description='Download youtube video')
parser.add_argument('link', type=str, help='link to download')
args = parser.parse_args()

yt = YouTube(args.link)
# download the highest resolution possible
yt.streams.get_highest_resolution().download()
# print the link back when done
print("downloaded", args.link)