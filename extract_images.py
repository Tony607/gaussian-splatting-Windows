import subprocess
import sys
import os

def get_video_duration(file_path):
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {file_path}'
    duration_str = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    return float(duration_str)

def extract_images(file_path, output_dir, num_images=100):
    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    duration = get_video_duration(file_path)
    frame_rate = duration / num_images
    output_file_pattern = os.path.join(output_dir, '%06d.jpg')
    cmd = f'ffmpeg -i {file_path} -vf "fps=(1/{frame_rate})" {output_file_pattern}'
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_images.py <path_to_mov_file> <output_directory>")
        sys.exit(1)

    file_path = sys.argv[1]
    output_dir = sys.argv[2]
    extract_images(file_path, output_dir)
