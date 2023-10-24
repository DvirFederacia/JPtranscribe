from gradio_client import Client
import os
import shutil
import argparse

parser = argparse.ArgumentParser(description="Transcribe video files.")
parser.add_argument('--path', type=str, help="Path to the video file.")
args = parser.parse_args()

import os

def is_video_file(file_path):
    """Check if a file is a video by its extension."""
    video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"]
    _, ext = os.path.splitext(file_path)
    return ext.lower() in video_extensions

def subtitle_exists_for_video(video_path):
    """Check if a subtitle file with the same name exists for the given video."""
    base_name = os.path.basename(video_path)
    video_name_without_ext = os.path.splitext(base_name)[0]
    subtitle_path = os.path.join(os.path.dirname(video_path), video_name_without_ext + ".srt")
    subtitle_path_ja = os.path.join(os.path.dirname(video_path), video_name_without_ext + ".ja.srt")
    subtitle_path_ass = os.path.join(os.path.dirname(video_path), video_name_without_ext + ".ass")
    subtitle_path_ass_ja = os.path.join(os.path.dirname(video_path), video_name_without_ext + ".ja.ass")
    return os.path.exists(subtitle_path) or os.path.exists(subtitle_path_ass) or os.path.exists(subtitle_path_ja) or os.path.exists(subtitle_path_ass_ja)

def get_all_video_files(dir_path):
    """Recursively get all video files in a directory, excluding videos that already have subtitles."""
    video_files = []
    if is_video_file(dir_path) and not subtitle_exists_for_video(dir_path):
        video_files.append(dir_path)
    else:
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                if is_video_file(file_path) and not subtitle_exists_for_video(file_path):
                    video_files.append(file_path)
                
    return video_files


def transcribe(video_file_path:str):
    client = Client("http://127.0.0.1:7860/")
    result = client.predict(
                    "medium",	# str (Option from: ['tiny', 'base', 'small', 'medium', 'large', 'large-v2']) in 'Model' Dropdown component
                    "Japanese",	# str
                    "",	# str in 'URL (YouTube, etc.)' Textbox component
                    [video_file_path],	# List[str] (List of filepath(s) or URL(s) to files) in 'Upload Files' File component
                    "",	# str (filepath on your computer (or URL) of file) in 'Microphone Input' Audio component
                    "transcribe",	# str (Option from: ['transcribe', 'translate']) in 'Task' Dropdown component
                    "silero-vad",	# str (Option from: ['none', 'silero-vad', 'silero-vad-skip-gaps', 'silero-vad-expand-into-gaps', 'periodic-vad']) in 'VAD' Dropdown component
                    5,	# int | float in 'VAD - Merge Window (s)' Number component
                    30,	# int | float in 'VAD - Max Merge Size (s)' Number component
                    False,	# bool in 'Word Timestamps' Checkbox component
                    False,	# bool in 'Word Timestamps - Highlight Words' Checkbox component
                    False,	# bool in 'Diarization' Checkbox component
                    2,	# int | float in 'Diarization - Speakers' Number component
                    api_name="/predict"
    )
    print(result)
    srt_path = result[0][0]
    # Extract the directory and the base name of the video
    video_directory = os.path.dirname(video_file_path)
    video_basename = os.path.basename(video_file_path)
    video_name_without_ext = os.path.splitext(video_basename)[0]

    # Construct the new SRT file name
    new_srt_name = video_name_without_ext + ".srt"

    # Full path to the new SRT file
    new_srt_path = os.path.join(video_directory, new_srt_name)

    # Copy the SRT file and rename it
    shutil.copy(srt_path, new_srt_path)

video_files = get_all_video_files(args.path)
for video in video_files:
    transcribe(video)