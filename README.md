# JPtranscribe
This script is intended to work with locally deployed whisper via whisper web ui, for installation guide for that please refer to [Whisper WebUI with a VAD for more accurate non-English transcripts (Japanese) · openai/whisper · Discussion #397 · GitHub](https://github.com/openai/whisper/discussions/397)
first you need to install gradio_client
```
pip install gradio_client
```
## set up automation with qBitTorrent
![image](https://github.com/DvirFederacia/JPtranscribe/assets/52207204/55813f1a-57f3-4e25-b98d-17df92bdd09d)

## or run the script manually on a specified folder:
```
python {path to JPtranscribe.py} --path {path to the folder}
```
this script will search through every sub folder of the given path(if the given path is a video file then it will just transcribe it) and transcribe every video file that doesn't have a matching .ja.srt or .srt or .ja.ass or .ass subtitle file

if you don't want this behavior, for example, you want to find subtitle yourself for anime that already finished airing which you can download in bulk(which means it will be a multifile torrent, and thus the %F will be a folder path instead of a video file), and only want automated transcription for currently airing anime(which you will download as single video file), you can just delete the "else" part of this function, so it will only transcribe if the given path is a video file.
```python
def get_all_video_files(dir_path):
    """Recursively get all video files in a directory, excluding videos that already have subtitles."""
    video_files = []
    if is_video_file(dir_path) and not subtitle_exists_for_video(dir_path):
        video_files.append(dir_path)
#    else:
#        for root, _, files in os.walk(dir_path):
#            for file in files:
#                file_path = os.path.join(root, file)
#                if is_video_file(file_path) and not subtitle_exists_for_video(file_path):
#                    video_files.append(file_path)
                
    return video_files
```
and you can edit what extension you want to transcribe by editing this part
```python
def is_video_file(file_path):
    """Check if a file is a video by its extension."""
    video_extensions = [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"] #edit this
    _, ext = os.path.splitext(file_path)
    return ext.lower() in video_extensions
```
