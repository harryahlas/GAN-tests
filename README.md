# GAN-tests
Test scripts for GAN models

* *mnistgan_test.ipynb*
	* Based on [https://github.com/eriklindernoren/Keras-GAN/blob/master/aae/aae.py](https://github.com/eriklindernoren/Keras-GAN/blob/master/aae/aae.py)
	* Appears to work on google colab
	* Cleanup:
		* Original code had an issue with loading the images from the images folder.  Somehow it is working but need to figure out the way the image storage/retrieval happens. 
* Potential steps:
	* Run 2d image GAN successfully
	* Understand wtf is going on there
	* Convert script to 1d
	* Update code to run on audio instead of images
		* Pull in audio creation source code
	* Update noise generator to work with sound, or simply skip and use audio already created.
	