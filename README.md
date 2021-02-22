# GAN-tests
Test scripts for GAN models

* *spleeter_info.md* has functioning split, though results are not impressive after a short train.  Need to do a better train.
	* [ ] Try more samples
* *mnistgan_test.ipynb* Implementation of Deep Convolutional Generative Adversarial Network.
	* Based on [https://github.com/eriklindernoren/Keras-GAN/blob/master/dcgan/dcgan.py](https://github.com/eriklindernoren/Keras-GAN/blob/master/dcgan/dcgan.py)
	* Process:
		1 DCGAN
		2 build_discriminator - sequential model. Compiled, not trainable
		3 build_generator - sequential model. The generator takes noise as input and generates imgs  Trainable, then compiled
		4 train
	* RESOLVED - Appears to work on google colab but may need to fix this issue: <code>/usr/local/lib/python3.6/dist-packages/keras/engine/training.py:493: UserWarning: Discrepancy between trainable weights and collected trainable weights, did you set `model.trainable` without calling `model.compile` after ?
  'Discrepancy between trainable weights and collected trainable'</code>.
		* Note: this issue does not appear to mess up the output.
	* COMPLETE - Unprocess/dummy down the code so a model object is returned.  
		* *mnistgan_test_with_class.ipynb* is the original file that runs on a single command.* Cleanup:
		* Original code had an issue with loading the images from the images folder.  Somehow it is working but need to figure out the way the image storage/retrieval happens. 

* *DrumDenoiserGAN.ipynb* Implementation of Deep Convolutional Generative Adversarial Network to denoise audio for drum replacement.
	* COMPLETE - Update to import audio files
	* COMPLETE - Move *Untitled0_v05f_detailsearch.ipynb* to *DrumDenoiserGAN.ipynb*.
		* Image creator/saver needs work
	* COMPLETE - Figure out how to adjust for latent_dim. Original process may be taking smaller images. If so, we may need to remove latent_dim.
	* COMPLETE -  Look at spleeter...reg doesnt work, try jupyter notebook on colab
	##**Next steps: **musdb
	##**Next steps: **spleeter
	* COMPLETE - look at https://github.com/deezer/spleeter/blob/master/configs/musdb_train.csv
	* COMPLETE - use C:\Development\Python\encoder_decoder\conv_decoder_with_real_samples.py as template
		* C:\Development\github\GAN-tests\spleeter_samples.py
	* COMPLETE - split files in that order, create blanks for other categories
		* COMPLETE - get list of train, test, and validation samples
		* COMPLETE - tom samples
			* COMPLETE - C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_sample-14.wav (01 through 32)
			test is through 9, train is through 7
			* COMPLETE - add to github
		* COMPLETE - get list of background noise
				* COMPLETE - C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\background_train_full.wav
				* COMPLETE - add to github		
			* figure out how to cut up background and crossfade
			* if simple enough then add to code below
		* COMPLETE - process
			* COMPLETE - pick random amount of time, between 10, 30 seconds
			* COMPLETE - create background noise for time period
				* COMPLETE - select random amount of time between 3-10 seconds of background noise
				* COMPLETE - if less than total time then find another random amount and add
				* COMPLETE - repeat until time limit exceeded.
				* COMPLETE - save as sample000n_other.wav
			* COMPLETE - pick random time between 0, 10 seconds 
				* COMPLETE -pick random train sample
				* COMPLETE -add 0 values for that amount of time prior to sample
				* COMPLETE -repeat process.
				* COMPLETE -if new amount of time plus the previous sample(s) is < 2 seconds before end time then add blank space till end of time limit
				* COMPLETE -otherwise repeat and append
				* COMPLETE -save as sample000n_drums.wav
			* COMPLETE - Combine
			* COMPLETE - save as sample000n_mixture.wav
		* COMPLETE - create multiple samples using loop
	* COMPLETE - create train csv
		* COMPLETE - Get lengths of songs
		* COMPLETE - locate and copy version from spleeter
		* COMPLETE - add names
		* COMPLETE - Update locations
	* Open train session in spleeter
		* COMPLETE - Research this error: <code>(spleeter-cpu) C:\Development\github\spleeter>spleeter train -p C:/Development/github/GAN-tests/spleeter_configs/musdb_config.json -d
usage: spleeter train [-h] [-a AUDIO_ADAPTER] [-p PARAMS_FILENAME] [--verbose]
                      -d AUDIO_PATH
spleeter train: error: argument -d/--data: expected one argument</code>
		* Research error: <code>INFO:spleeter:Loading audio b'C:/Development/github/GAN-tests/audio_files_split\\train/Invisible Familiars - Disturbing Wildlife/mixture.wav' from 99.2498865 to 119.2498865
WARNING:spleeter:ffprobe error (see stderr output for detail)
INFO:spleeter:Loading audio b'C:/Development/github/GAN-tests/audio_files_split\\train/Music Delta - Hendrix/mixture.wav' from 0.0 to 20.0
WARNING:spleeter:ffprobe error (see stderr output for detail)
INFO:spleeter:Loading audio b'C:/Development/github/GAN-tests/audio_files_split\\train/Johnny Lokke - Whisper To A Scream/mixture.wav' from 117.6633105 to 137.6633105</code>
	* run train session (refer to spleeter_start.txt)
	* evaluate results
		* Create new files for evaluation using training samples
		* Run on new one - STAR HERE - LOCATE OUTPUT, SEE IF 2 CHANNEL OUTPUT WORKED
		* Repeat above for testing samples
	* see documentation for training	
	* **Next steps: ** UPDATE V2 TO INCLUDE CODE FROM OTHER GIT, FIGURE OUT ERROR
		* COMPLETE - SEE IF SWITHCING CONV1D2 FROM 64 TO SOMETHING ELSE CHANGES THE GAPS!!
		* Why is it only generating changes roughly every 64?
		* COMPLETE - Increase samples to 700
		* **may be an issue with : x_train_noisy[0, :,0]*
			 * Try using something like this with the : in the middle: <code>get_variance(x_train_noisy[0, :,0])
			 ia = x_train_noisy[0, :,0]
slide_array = np.append(0, ia[0:-1])
output_array = ia - slide_array
output_array.shape</code>
		* If still issues then look at structure of models and reevaluate. Maybe look at old cnn or lstm that worked better for ideas.
			* Could be issue with reshape on generator
		* If improvement, then further increase in samples?
		* Additional sample increase?
		* Adjust parameters
			* Change Adam to .00001 and .8?
		* Also need to reuse periodic image generator, only for periodic audio generation

* **Demucs**
	* see *stempegscripts/README.md* for info including stem building and running
	* In short, the process works on both pc and colab. However, FB recommends not even trying to train on a different data set.  When I tried to train using *demucs _attempt.ipynb* I got this error at the end: 
		* <code>Experiment musdb=demucs batch_size=1
Number of training samples adjusted to 451924
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "/usr/local/lib/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/content/demucs/demucs/__main__.py", line 271, in <module>
    main()
  File "/content/demucs/demucs/__main__.py", line 210, in main
    world_size=args.world_size)
  File "/content/demucs/demucs/train.py", line 38, in train_model
    loader = DataLoader(dataset, batch_size=batch_size, num_workers=workers, shuffle=True)
  File "/usr/local/lib/python3.7/site-packages/torch/utils/data/dataloader.py", line 262, in __init__
    sampler = RandomSampler(dataset, generator=generator)  # type: ignore
  File "/usr/local/lib/python3.7/site-packages/torch/utils/data/sampler.py", line 104, in __init__
    "value, but got num_samples={}".format(self.num_samples))
ValueError: num_samples should be a positive integer value, but got num_samples=0</code>

* Potential steps:
	* Run 2d image GAN successfully
	* Understand wtf is going on there
	* Convert script to 1d
	* Update code to run on audio instead of images
		* Pull in audio creation source code
	* Update noise generator to work with sound, or simply skip and use audio already created.
	
