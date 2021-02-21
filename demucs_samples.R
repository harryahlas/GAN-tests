# This script, along with demucs_samples.py, creates samples for use with demucs

library(reticulate)
library(tidyverse)
library(tuneR)

# Build samples
source_python("demucs_samples.py")


# Get template for musdb csv
musdb_template <- read_csv("https://github.com/deezer/spleeter/blob/master/configs/musdb_train.csv?raw=true", n_max = 20)

# test samples
musdb_test <- musdb_template[0,]

audio_folder_test <- "D:\\Development\\github\\GAN-tests\\audio_files_split_demucs\\"

# Start loop
for (i in (16:29)) {
  print(i)
  # 4 digit number
  i4digit <- sprintf("%04d", i)
  
  # Read in mix path to get audio information
  audio <- readWave(paste0(audio_folder_test, "audio_file_mixture_", i4digit, ".wav"), header=TRUE)
  audio_length <- audio$samples / audio$sample.rate
  
  # construct soundless audio sample
  soundless_audio <-  Wave(left = seq(0, 0, length = audio$samples), 
                           samp.rate = audio$sample.rate, 
                           bit = audio$bits)
  
  # Write soundless audio that will be used for vocals, and bass paths
  writeWave(soundless_audio, paste0(audio_folder_test, "audio_file_soundless_audio_", i4digit, ".wav"))
  
  # add row to musdb file  
  musdb_test <- musdb_test %>% 
    add_row(mix_path = paste0(audio_folder_test, "audio_file_mixture_", i4digit, ".wav"),
            vocals_path = paste0(audio_folder_test, "audio_file_soundless_audio_", i4digit, ".wav"),
            drums_path = paste0(audio_folder_test, "audio_file_hits_", i4digit, ".wav"),
            bass_path = paste0(audio_folder_test, "audio_file_soundless_audio_", i4digit, ".wav"),
            other_path = paste0(audio_folder_test, "audio_file_background_", i4digit, ".wav"),
            duration = audio_length
    )
  
}
write.csv(musdb_test, "musdb_test.csv")


# train samples
musdb_train <- musdb_template[0,]

audio_folder_train <- "D:\\Development\\github\\GAN-tests\\audio_files_split\\"

# Start loop
for (i in (1:17)) {
  if (i == 12) {next}
  print(i)
  # 4 digit number
  i4digit <- sprintf("%04d", i)
  
  # Read in mix path to get audio information
  audio <- readWave(paste0(audio_folder_train, "audio_file_mixture_", i4digit, ".wav"), header=TRUE)
  audio_length <- audio$samples / audio$sample.rate
  
  # construct soundless audio sample
  soundless_audio <-  Wave(left = seq(0, 0, length = audio$samples), 
                           samp.rate = audio$sample.rate, 
                           bit = audio$bits)
  
  # Write soundless audio that will be used for vocals, and bass paths
  writeWave(soundless_audio, paste0(audio_folder_train, "audio_file_soundless_audio_", i4digit, ".wav"))
  
  # add row to musdb file  
  musdb_train <- musdb_train %>% 
    add_row(mix_path = paste0(audio_folder_train, "audio_file_mixture_", i4digit, ".wav"),
            vocals_path = paste0(audio_folder_train, "audio_file_soundless_audio_", i4digit, ".wav"),
            drums_path = paste0(audio_folder_train, "audio_file_hits_", i4digit, ".wav"),
            bass_path = paste0(audio_folder_train, "audio_file_soundless_audio_", i4digit, ".wav"),
            other_path = paste0(audio_folder_train, "audio_file_background_", i4digit, ".wav"),
            duration = audio_length
    )
  
}
write.csv(musdb_train, "musdb_train.csv")


## put a loop on stempegtest.py and run
system("python D:/Development/github/GAN-tests/stempegscripts/wave2audio.py")



## old
system("C:/Users/hahla/miniconda3/Scripts/activate.bat")
system("C:/Users/hahla/miniconda3/python.exe D:/Development/github/GAN-tests/stempegscripts/wave2audio.py")
system("C:\\Users\\hahla\\miniconda3\\Scripts\\activate.bat")
system("help")
system("python D:/Development/github/GAN-tests/stempegtest/stempegtest2.py")
system("python D:/Development/github/GAN-tests/stempegtest/stempegtest.py")
system(c("help","help"))
system("exit")

system("conda help")
system("C:/Users/hahla/miniconda3/Scripts/activate.bat")









musdb_train[1,1]
repl_python()

py_config()[1]
system(paste0(py_config()[1], " ", getwd(), "/stempegtest/stempegtest.py"))
source_python("stempegtest/stempegtest.py")

#works in conda: 
#conda run C:/Users/hahla/miniconda3/python.exe D:/Development/github/GAN-tests/stempegtest/stempegtest.py

%windir%\System32\cmd.exe "/K" C:\Users\hahla\miniconda3\Scripts\activate.bat C:\Users\hahla\miniconda3

system("C:\\Users\\hahla\\miniconda3\\Scripts\\activate.bat")
system("help")
system("python D:/Development/github/GAN-tests/stempegtest/stempegtest2.py")
system("python D:/Development/github/GAN-tests/stempegtest/stempegtest.py")
system(c("help","help"))
system("exit")

system("conda help")
system("C:/Users/hahla/miniconda3/Scripts/activate.bat")

