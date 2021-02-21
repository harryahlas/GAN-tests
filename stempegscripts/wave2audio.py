
import stempeg


filenamex = "D:/Development/github/GAN-tests/audio_files_split/audio_file_mixture_0002.wav"
S, rate = stempeg.read_stems(filenamex, stem_id=0)
stempeg.write_audio("test.mp4", S, rate)

