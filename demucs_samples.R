# This script, along with demucs_samples.py, creates samples for use with demucs

library(reticulate)
library(tidyverse)
library(tuneR)

# Build samples
source_python("demucs_samples.py")

library(tidyverse)
library(tuneR)

# Get template for musdb csv
musdb_template <- read_csv("https://github.com/deezer/spleeter/blob/master/configs/musdb_train.csv?raw=true", n_max = 20)
musdb_test <- musdb_template[0,]

audio_folder <- "D:\\Development\\github\\GAN-tests\\audio_files_split_demucs\\"

# Start loop
for (i in (16:29)) {
  print(i)
  # 4 digit number
  i4digit <- sprintf("%04d", i)
  
  # Read in mix path to get audio information
  audio <- readWave(paste0(audio_folder, "audio_file_mixture_", i4digit, ".wav"), header=TRUE)
  audio_length <- audio$samples / audio$sample.rate
  
  # construct soundless audio sample
  soundless_audio <-  Wave(left = seq(0, 0, length = audio$samples), 
                           samp.rate = audio$sample.rate, 
                           bit = audio$bits)
  
  # Write soundless audio that will be used for vocals, and bass paths
  writeWave(soundless_audio, paste0(audio_folder, "audio_file_soundless_audio_", i4digit, ".wav"))
  
  # add row to musdb file  
  musdb_test <- musdb_output %>% 
    add_row(mix_path = paste0(audio_folder, "audio_file_mixture_", i4digit, ".wav"),
            vocals_path = paste0(audio_folder, "audio_file_soundless_audio_", i4digit, ".wav"),
            drums_path = paste0(audio_folder, "audio_file_hits_", i4digit, ".wav"),
            bass_path = paste0(audio_folder, "audio_file_soundless_audio_", i4digit, ".wav"),
            other_path = paste0(audio_folder, "audio_file_background_", i4digit, ".wav"),
            duration = audio_length
    )
  
}
write.csv(musdb_test, "musdb_test.csv")
