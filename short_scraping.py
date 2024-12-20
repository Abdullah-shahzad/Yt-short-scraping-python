import subprocess

def download_youtube_short(video_url, output_file):
    try:
        # Run yt-dlp command
        result = subprocess.run(
            ["yt-dlp", "-o", output_file, video_url],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Video downloaded successfully as {output_file}")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")
        print(e.stderr)



if __name__ == "__main__":
    video_url1 = "https://www.youtube.com/shorts/FsV4QtjSi1I"
    output_file1 = "output.mp4"
    download_youtube_short(video_url1, output_file1)
