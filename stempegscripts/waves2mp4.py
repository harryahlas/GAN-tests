
import stempeg

# 0 - The mixture,
# 1 - The drums,
# 2 - The bass,
# 3 - The rest of the accompaniment,
# 4 - The vocals.

stems_folder = "D:/Development/github/GAN-tests/audio_files_split/audio_files_001"
S, rate = stempeg.read_stems(stempeg.example_stem_path())


filename_mix = "D:/Development/github/GAN-tests/audio_files_split/audio_file_mixture_0002.wav"
filename_drums = "D:/Development/github/GAN-tests/audio_files_split/audio_file_hits_0002.wav"
filename_bass = "D:/Development/github/GAN-tests/audio_files_split/audio_file_soundless_audio_0002.wav"
filename_other = "D:/Development/github/GAN-tests/audio_files_split/audio_file_background_0002.wav"
filename_vocals = "D:/Development/github/GAN-tests/audio_files_split/audio_file_soundless_audio_0002.wav"

S_filename_mix, rate = stempeg.read_stems(filename_mix, stem_id=0)

S_filename_drums, rate = stempeg.read_stems(filename_drums, stem_id=0)

S_filename_bass, rate = stempeg.read_stems(filename_bass, stem_id=0)

S_filename_other, rate = stempeg.read_stems(filename_other, stem_id=0)

S_filename_vocals, rate = stempeg.read_stems(filename_vocals, stem_id=0)


# convert to stereo, yuck
S_filename_mix = np.column_stack((S_filename_mix, S_filename_mix))
S_filename_drums = np.column_stack((S_filename_drums, S_filename_drums))
S_filename_bass = np.column_stack((S_filename_bass, S_filename_bass))
S_filename_other = np.column_stack((S_filename_other, S_filename_other))
S_filename_vocals = np.column_stack((S_filename_vocals, S_filename_vocals))


# works
stems = {
  "mix": S_filename_mix,
  "drums": S_filename_drums,
  "bass": S_filename_bass,
  "other": S_filename_other,
  "vocals": S_filename_vocals
}

# Write as multiple files
stempeg.write_stems(
 ("output", ".mp4"),
 stems,
 sample_rate=rate,
 writer=stempeg.FilesWriter(
        multiprocess=True,
        output_sample_rate=44100,
        stem_names=["mix", "drums", "bass", "other", "vocals"]
    )
)    
 
stempeg.write_stems(
 ("output.mp4"),
 stems,
 sample_rate=rate,
 writer=stempeg.StreamsWriter(
        #multiprocess=True,
        output_sample_rate=44100#,
       # stem_names=["mix", "drums", "bass", "other", "vocals"]
    )
)    


stempeg.write_stems(
 ("output.mp4"),
 stems,
 sample_rate=rate,
 writer=stempeg.StreamsWriter(
        #multiprocess=True,
        output_sample_rate=44100,
        stem_names=["mix", "drums", "bass", "other", "vocals"]
    )
)    
 


stems = np.array([S_filename_mix,
S_filename_drums,
S_filename_bass,
S_filename_other,
S_filename_vocals])
  
 
stempeg.write_audio(
 ("output.mp4"),
 stems,
 sample_rate=rate,
 
)    
    



# error
stempeg.write_stems(
("output", ".mp4"),
stems,
sample_rate=rate,
writer=stempeg.FilesWriter(
       multiprocess=True,
       output_sample_rate=44100,
       stem_names=["mix", "drums", "bass", "other", "vocals"]
   )
)
# error ^

S, rate = stempeg.read_stems(filenamex, stem_id=0)



stempeg.write_audio("test.mp4", S, rate)

