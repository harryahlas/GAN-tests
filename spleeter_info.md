# Successful Spleeter Train
Was working with not so great results but it did function.  After adding additional train/test data something is breaking.
[ ] need to fix above. My guess is it is one of these:
   durations are incorrect somewhere
   some other error on the csv files
   the wrong wav files are there. not sure how to solve that without reuploading everything.

*spleeter.ipynb* works.  These are the steps as I recall.  It started with demucs but moved to spleeter after I was unable to train demucs on new data.
1. Create samples using *spleeter_samples.py*. Note there is a better file called *spleeter_more_samples.py*
1. Save audio samples to train and/or test folders on colab in *gdrive/MyDrive/Development/spleeter*.  I don't think it matters which folder you save to. 
1. Update *spleeter_configs/colab* folder.  The csvs should have the locations as they would appear on colab/drive.
   1. musdb_config.json
   1. musdb_train.csv
   1. musdb_validation.csv
1. Save files above to *gdrive/MyDrive/Development/spleeter* 
1. Run *spleeter.ipynb*
1. **Next step:** run this with *spleeter_more_samples.py*

################# Original notes below

<code>git clone https://github.com/Deezer/spleeter
conda env create -f spleeter/conda/spleeter-cpu.yaml
activate spleeter-cpu
pip install museval
pip install spleeter
spleeter separate -i 156e-wVoxedit1.wav -p spleeter:2stems -o output  ### note that this needs to have no spaces in filename

conda env create -f C:\Development\github\spleeter\conda\spleeter-cpu.yaml

(older conda)
activate <envname>

cd C:\Development\github\spleeter
conda activate spleeter-cpu
spleeter separate -i spleeter/audio_example.mp3 -p spleeter:2stems -o output

#### split file
cd C:\Development\github\spleeter
activate spleeter-cpu
spleeter separate -i spleeter/audio_file_mixture_0017.wav -p 

cd C:\Development\github\spleeter
conda env create -f spleeter/conda/spleeter-cpu.yaml
spleeter separate -i 156e-wVoxedit1.wav -p spleeter:2stems -o output
spleeter separate -i 156e-wVoxedit1.wav -p spleeter:2stems -o output

#### 12/6/2019
cd C:\Development\github\spleeter
activate spleeter-cpu
ERROR HERE: spleeter train -p C:/Development/github/GAN-tests/spleeter_configs/musdb_config.json -d C:/Development/github/GAN-tests/audio_files_split

2/20/2021 - trying this after updating musdb_train.csv and musdb_validate.csv:
ERROR HERE: spleeter train -p D:/Development/github/GAN-tests/spleeter_configs/musdb_config.json -d D:/Development/github/GAN-tests/audio_files_split


### demucs start
pip install musdb
cd C:\Development\github\demucs
conda env update -f environment-cpu.yml

2)
#comment out pip installs in environment-cpu.yml
cd C:\Development\github\demucs
conda env update -f environment-cpu.yml

xtra --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org

</code>
