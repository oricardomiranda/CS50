import re
import sys

def main():
    html = input("HTML: ")
    video_id = parse(html)
    if video_id:
        print(video_id)
    else:
        print("No YouTube Video ID found in the input.")

def parse(s):
    if frame := re.search(r"<iframe src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)\"></iframe>", s):
        return f"https://youtu.be/{frame.group(1)}"

if __name__ == "__main__":
    main()