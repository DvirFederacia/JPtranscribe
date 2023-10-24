# JPtranscribe
This script is intended to work with locally deployed whisper via whisper web ui, for installation guide for that pls refer to [Whisper WebUI with a VAD for more accurate non-English transcripts (Japanese) · openai/whisper · Discussion #397 · GitHub](https://github.com/openai/whisper/discussions/397)
first you need to install gradio_client
```
pip install gradio_client
```
## set up automation with qBitTorrent
![[Pasted image 20231024130354.png]]
## or run the script manually on a specified folder:
```
python {path to JPtranscribe.py} --path {path to the folder}
```
![[Pasted image 20231024130433.png]]
this script will search through every sub folder of the given path(if the given path is a video file then it will just transcribe it) and transcribe every video file that doesn't have a matching .ja.srt or .srt or .ja.ass or .ass subtitle file

if you don't want this behavior, for example, you want to find subtitle yourself for anime that already finished airing which you can download in bulk(which means it will be a multifile torrent, and thus the %F will be a folder path instead of a video file), and only want automated transcription for currently airing anime(which you will download as single video file), you can just delete the "else" part of this function, so it will only transcribe if the given path is a video file.
![[Pasted image 20231024131352.png]]  
and you can edit what extension you want to transcribe by editing this part
![[Pasted image 20231024131638.png]]
