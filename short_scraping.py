import subprocess
import time

def download_youtube_short(video_url, output_file):
    try:
        start_time = time.time()
        # Run yt-dlp command
        result = subprocess.run(
            ["yt-dlp", "-o", output_file, video_url],
            check=True,
            capture_output=True,
            text=True
        )

        elapsed_time = time.time() - start_time
        print(f"Video downloaded successfully as {output_file}")
        print(result.stdout)
        print(f"Execution time: {elapsed_time:.2f} seconds")


    except subprocess.CalledProcessError as e:
        print(f"Error downloading video: {e}")
        print(e.stderr)




if __name__ == "__main__":
    video_url1 = "https://www.youtube.com/shorts/LW1-ZfkqEJc"
    output_file1 = "output.mp4"
    download_youtube_short(video_url1, output_file1)
