import moviepy.editor as mp

def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    return my_clip

if __name__ == "__main__":
    file_path = r'路径'
    my_clip = extract_audio(file_path)
    my_clip.audio.write_audiofile(f'name.mp3')
