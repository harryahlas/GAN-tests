# GAN-tests
Test scripts for GAN models

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
	* **Next steps: Figure out how to adjust for latent_dim**. Original process may be taking smaller images. If so, we may need to remove latent_dim.

	
* Potential steps:
	* Run 2d image GAN successfully
	* Understand wtf is going on there
	* Convert script to 1d
	* Update code to run on audio instead of images
		* Pull in audio creation source code
	* Update noise generator to work with sound, or simply skip and use audio already created.
	