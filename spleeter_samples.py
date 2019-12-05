# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 18:51:03 2018

@author: Harry Ahlas
"""


import os
import wave
import struct
import random
import numpy as np
from numpy import array

import matplotlib.pyplot as plt

os.chdir("C:\\Development\\github\\GAN-tests")

wrd=wave.open("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-06.wav","r")

# Need to improve speed of import.  See http://www.cameronmacleod.com/blog/reading-wave-python
def read_whole(filename):
    wav_r = wave.open(filename, 'r')
    ret = []
    while wav_r.tell() < wav_r.getnframes():
        decoded = struct.unpack("<h", wav_r.readframes(1))
        ret.append(decoded)
    return ret

# Import training samples
drum_train_01 = read_whole("Audio\drum_train-01.wav")
drum_train_02 = read_whole("Audio\drum_train-02.wav")
drum_train_03 = read_whole("Audio\drum_train-03.wav")
drum_train_04 = read_whole("Audio\drum_train-04.wav")
drum_train_05 = read_whole("Audio\drum_train-05.wav")
drum_train_06 = read_whole("Audio\drum_train-06.wav")
drum_train_07 = read_whole("Audio\drum_train-07.wav")
'''
drum_train_08 = read_whole("Audio\drum_train-08.wav")
drum_train_09 = read_whole("Audio\drum_train-09.wav")
drum_train_10 = read_whole("Audio\drum_train-10.wav")
drum_train_11 = read_whole("Audio\drum_train-11.wav")
drum_train_12 = read_whole("Audio\drum_train-12.wav")
drum_train_13 = read_whole("Audio\drum_train-13.wav")
drum_train_14 = read_whole("Audio\drum_train-14.wav")
drum_train_15 = read_whole("Audio\drum_train-15.wav")
drum_train_16 = read_whole("Audio\drum_train-16.wav")
drum_train_17 = read_whole("Audio\drum_train-17.wav")
drum_train_18 = read_whole("Audio\drum_train-18.wav")
drum_train_19 = read_whole("Audio\drum_train-19.wav")
drum_train_20 = read_whole("Audio\drum_train-20.wav")
drum_train_21 = read_whole("Audio\drum_train-21.wav")
drum_train_22 = read_whole("Audio\drum_train-22.wav")
drum_train_23 = read_whole("Audio\drum_train-23.wav")
drum_train_24 = read_whole("Audio\drum_train-24.wav")
drum_train_25 = read_whole("Audio\drum_train-25.wav")
drum_train_26 = read_whole("Audio\drum_train-26.wav")
drum_train_27 = read_whole("Audio\drum_train-27.wav")
drum_train_28 = read_whole("Audio\drum_train-28.wav")
drum_train_29 = read_whole("Audio\drum_train-29.wav")
drum_train_30 = read_whole("Audio\drum_train-30.wav")
drum_train_31 = read_whole("Audio\drum_train-31.wav")
drum_train_32 = read_whole("Audio\drum_train-32.wav")
'''

drum_test_01 = read_whole("Audio\drum_test-01.wav")
drum_test_02 = read_whole("Audio\drum_test-02.wav")
drum_test_03 = read_whole("Audio\drum_test-03.wav")
drum_test_04 = read_whole("Audio\drum_test-04.wav")
drum_test_05 = read_whole("Audio\drum_test-05.wav")
drum_test_06 = read_whole("Audio\drum_test-06.wav")
drum_test_07 = read_whole("Audio\drum_test-07.wav")
drum_test_08 = read_whole("Audio\drum_test-08.wav")
drum_test_09 = read_whole("Audio\drum_test-09.wav")


train_list = [drum_train_01,
              drum_train_02,
              drum_train_03,
              drum_train_04,
              drum_train_05,
              drum_train_06,
              drum_train_07]

# Length of biggest training sample
train_list_maxlength = len(max(train_list, key = len))

test_list = [ drum_test_01,
              drum_test_02,
              drum_test_03,
              drum_test_04,
              drum_test_05,
              drum_test_06,
              drum_test_07,
              drum_test_08,
              drum_test_09]

background_train_full = read_whole("Audio/background_train_full.wav")

# Input min and max lengths of audio sizes for sample generation
min_audio_file_seconds = 10
max_audio_file_seconds = 30
min_background_section_seconds = 3
max_background_section_seconds = 10
min_empty_section_seconds = 0
max_empty_section_seconds = 10


number_of_audio_files = 5

# Start loop

for loop_number in range(1, number_of_audio_files):
    print(loop_number)
    audio_file_number = loop_number
    audio_file_number_text = "{:04d}".format(audio_file_number)
    
    # Length of current audio file
    current_audio_file_seconds = random.randint(min_audio_file_seconds, max_audio_file_seconds)
    current_audio_file_samples = current_audio_file_seconds * 44100
    
    
    # Create background noise. Append to noise until length of current_audio_file_seconds is met    
    current_audio_file_background = []   
    background_section_start = 0 #samples, not seconds
    #create_background_section_continue_flag = True
    #loop
    
    
    # go through while loop until background audio is long enough
    while len(current_audio_file_background) <= current_audio_file_samples:
        
        # select length of this section
        background_section_seconds = random.randint(min_background_section_seconds, max_background_section_seconds)
        background_section_samples = background_section_seconds * 44100
        
        # start point of background platter to choose from
        background_platter_start = random.randint(0, len(background_train_full) - background_section_samples)
        # end point of background platter to choose from
        background_platter_end = background_platter_start + background_section_samples
        
        # end point
        background_section_end = background_section_start + background_section_samples 
        current_audio_file_background.extend(background_train_full[background_platter_start:background_platter_end])
        background_section_start = background_section_end + 1
    
    # Trim to appropriate length
    current_audio_file_background = current_audio_file_background[0:current_audio_file_samples]
    
    
    
    
    sound_output=wave.open(("audio_files_split/audio_file_background_" + audio_file_number_text + ".wav"),'w')
    sound_output.setparams((1, 2, 44100, 0, 'NONE', 'not compressed')) # was 1,2... but used get_params for this file
    f = (array(current_audio_file_background))
    f = f.astype('int16')
    f = f.reshape(current_audio_file_samples)#100000)
    for i in range(0, len(f)):
            value = f[i]
            packed_value = struct.pack('h', value)
            sound_output.writeframes(packed_value)
    sound_output.close()
    
    
    # to get parameters #notused
    wav_r = wave.open("Audio/background_train_full.wav", 'r')
    wav_r.getparams()
    
    # if len(current_audio_file_background) >= current_audio_file_seconds * 44100 then 
    # subset it and take only the seconds that are needed
    # create_background_section_continue_flag = False
    
    # end loop
        
    
    ############new section
    #select random amount of time between 3-10 seconds of background noise
    #				* if less than total time then find another random amount and add
    #				* repeat until time limit exceeded.    
    
    
    
    # Create hits only audio. Add until length of current_audio_file_seconds is met    
    current_audio_file_hits = []   
    #hits_section_start = 0 #samples, not seconds
    
    # Start with empty section
    empty_section_seconds = random.randint(min_empty_section_seconds * 100, max_empty_section_seconds * 100) / 100
    empty_section_samples = [0] * int(empty_section_seconds * 44100)
    current_audio_file_hits.extend(empty_section_samples)
        
    # go through while loop until hits audio plus the length of the longest sample is less than the desired length
    while len(current_audio_file_hits) + train_list_maxlength  <= current_audio_file_samples:
        
        # Create random hit sample
        random_sample = random.choice(train_list)
        random_sample = [i[0] for i in random_sample]
        
        # select length of this section
        empty_section_seconds = random.randint(min_empty_section_seconds * 100, max_empty_section_seconds * 100) / 100
        empty_section_samples = [0] * int(empty_section_seconds * 44100)
    
        ## start point of background platter to choose from
        #background_platter_start = random.randint(0, len(background_train_full) - background_section_samples)
        ## end point of background platter to choose from
        #background_platter_end = background_platter_start + background_section_samples
        
        # end point
        #hits_section_end = background_section_start + background_section_samples 
        current_audio_file_hits.extend(random_sample + empty_section_samples)
        #background_section_start = background_section_end + 1
    
    # Trim to appropriate length
    current_audio_file_hits = current_audio_file_hits[0:current_audio_file_samples]
    
    # Print hits (drums)
    sound_output=wave.open(("audio_files_split/audio_file_hits_" + audio_file_number_text + ".wav"),'w')
    sound_output.setparams((1, 2, 44100, 0, 'NONE', 'not compressed')) # was 1,2... but used get_params for this file
    
    g = (array(current_audio_file_hits))
    g = g.astype('int16')
    g = g.reshape(current_audio_file_samples)#100000)
        
    for i in range(0, len(g)):
            value = g[i]
            packed_value = struct.pack('h', value)
            sound_output.writeframes(packed_value)
    sound_output.close()
    
    # Create mixture
    h = [f[i] + g[i] for i in range(current_audio_file_samples)] 
    
    # Print mixture
    sound_output=wave.open(("audio_files_split/audio_file_mixture_" + audio_file_number_text + ".wav"),'w')
    sound_output.setparams((1, 2, 44100, 0, 'NONE', 'not compressed')) # was 1,2... but used get_params for this file
    
    for i in range(0, len(h)):
            value = h[i]
            packed_value = struct.pack('h', value)
            sound_output.writeframes(packed_value)
    sound_output.close()
    
# End loop    





# select random sample
random_sample = random.choice(train_list)

use test_list  and train_list 



# waverdwave.py

import matplotlib.pyplot as plt
from random import randint
import keras
#from keras.datasets import mnist
from keras.models import Model, Sequential
from keras.layers import Input, Dense, Conv1D, MaxPooling1D, UpSampling1D, Flatten, Reshape
from keras import regularizers




sample_length = 10000
total_rows = 5000
train_rows = 4000
#n_features = highest_number + 1 # NOTE: no number can be larger than 60.  So for kick it would be ~27k??
n_steps_in =  sample_length #15  #6
n_steps_out = sample_length #15 #3



drum_train_01 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-01.wav")
drum_train_02 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-02.wav")
drum_train_03 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-03.wav")
drum_train_04 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-04.wav")
drum_train_05 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-05.wav")
drum_train_06 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-06.wav")
drum_train_07 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-07.wav")

percussion_list = [drum_train_01,
                   drum_train_02,
                   drum_train_03,
                   drum_train_04,
                   drum_train_05,
                   drum_train_06,
                   drum_train_07]

drum_test_01 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-01.wav")
drum_test_02 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-02.wav")
drum_test_03 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-03.wav")
drum_test_04 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-04.wav")
drum_test_05 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-05.wav")
drum_test_06 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-06.wav")
drum_test_07 = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_test-07.wav")


percussion_list_test = [drum_test_01,
                   drum_test_02,
                   drum_test_03,
                   drum_test_04,
                   drum_test_05,
                   drum_test_06,
                   drum_test_07]

background_train_full = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\\background_train_full.wav")
###########need to create new test files
#
#
#test_full = read_whole("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\\background_test_00.wav")

def generate_background(n_samples, background_music):
    background_train_full_length = len(background_train_full)
    background_start = randint(0, background_train_full_length - sample_length)
    background = background_train_full[background_start:(background_start + 10000)]
    background = [background[j][0] for j in range (len(background))]
    return background

background_test = generate_background(1, background_train_full)

def generate_percussion(sound_list):
    percussion = percussion_list[randint(0,(len(percussion_list) - 1))]
    percussion = [percussion[j][0] for j in range (len(percussion))]
    percussion += [0] * int(sample_length - len(percussion))
    #percussion = np.asarray(percussion)
    return percussion
                
percussion_test = generate_percussion(percussion_list)

def get_dataset(n_in, n_out, sound_list_name, background_train_list, n_samples):
        X1, y = list(), list()
#        X1, y = array(), array()
        for _ in range(n_samples):
                # generate source sequence
                background_generated = generate_background(1, background_train_list)
                percussion_generated = generate_percussion(sound_list_name)
                # define padded target sequence
                source = [background_generated[i]+percussion_generated[i] for i in range(len(background_generated))]
                #note: can add noise to target below, see old file
                target = percussion_generated
                target = target[:n_out] #just in case i decide to change lengths later
                # create padded input target sequence
#                target_in = [0] + target[:-1]
                # encode
#                src_encoded = to_categorical([source], num_classes=cardinality)
#                tar_encoded = to_categorical([target], num_classes=cardinality)
#                tar2_encoded = to_categorical([target_in], num_classes=cardinality)
#                # store
                X1.append(source)
#                X2.append(tar2_encoded)
                y.append(target)
#        X1 = np.squeeze(array(X1), axis=1) 
#        X2 = np.squeeze(array(X2), axis=1) 
#        y = np.squeeze(array(y), axis=1)
        X1 = array(X1)
        y = array(y)         
        return X1, y

X1, y = get_dataset(n_steps_in, n_steps_out, percussion_list, background_train_full, total_rows )
print(X1.shape, y.shape)


# from conv_decoder.py

x_train = X1[0:train_rows,]
y_train = y[0:train_rows,]
x_test = X1[train_rows:,]
y_test = y[train_rows:,]
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

# Get min value and increase all data by that amount
min_value = float(min(x_train.min(), y_train.min(), x_test.min(), y_test.min()))

x_train = x_train + - min_value
y_train = y_train + - min_value
x_test = x_test + - min_value
y_test = y_test + - min_value

# Scales the training and test data to range between 0 and 1.
max_value = float(max(x_train.max(), y_train.max(), x_test.max(), y_test.max()))
x_train = x_train.astype('float32') / max_value
y_train = y_train.astype('float32') / max_value
x_test = x_test.astype('float32') / max_value
y_test = y_test.astype('float32') / max_value

x_train.shape, x_test.shape, y_train.shape, y_test.shape
# ((60000, 28, 28), (10000, 28, 28))

x_train = x_train.reshape((len(x_train), sample_length, 1))
y_train = y_train.reshape((len(y_train), sample_length, 1))
x_test = x_test.reshape((len(x_test), sample_length, 1))
y_test = y_test.reshape((len(y_test), sample_length, 1))

x_train.shape, x_test.shape, y_train.shape, y_test.shape

# New, check...no need for noise
x_train_noisy = x_train 
x_train_noisy = np.clip(x_train_noisy, 0., 1.)

x_test_noisy = x_test
x_test_noisy = np.clip(x_test_noisy, 0., 1.)


row_num = 1
plt.plot(x_train_noisy[row_num])
plt.plot(y_train[row_num])


plt.plot(x_test_noisy[row_num])
plt.plot(y_test[row_num])

filters = 32

# Begin model
autoencoder = Sequential()

# Encoder Layers  (conv filters was 32, now 4)
autoencoder.add(Conv1D(filters, 3, activation='relu', padding='same', input_shape=x_train.shape[1:]))
autoencoder.add(MaxPooling1D(2, padding='same'))
autoencoder.add(Conv1D(filters, 3, activation='relu', padding='same'))
autoencoder.add(MaxPooling1D(2, padding='same'))

# Decoder Layers
autoencoder.add(Conv1D(filters, 3, activation='relu', padding='same'))
autoencoder.add(UpSampling1D(2))
autoencoder.add(Conv1D(filters, 3, activation='relu', padding='same'))
autoencoder.add(UpSampling1D(2))
autoencoder.add(Conv1D(1, 3, activation='sigmoid', padding='same'))

autoencoder.summary()



autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
autoencoder.fit(x_train_noisy, y_train,
                epochs=25,
                batch_size=10, #128,
                validation_data=(x_test_noisy, x_test))

import datetime
print(datetime.datetime.now())

final_input, final_target = get_dataset(n_steps_in, n_steps_out, percussion_list_test, background_train_full, 20)

final_input = final_input + - min_value
final_target = final_target + - min_value


final_input = final_input.astype('float32') / max_value
final_target = final_target.astype('float32') / max_value

final_input = final_input.reshape((len(final_input), sample_length, 1))
final_target = final_target.reshape((len(final_target), sample_length, 1))


final_input.shape, final_target.shape




final_input_denoised = autoencoder.predict(final_input)

final_input_denoised = final_input_denoised + .028315127


row_num = 0
plt.plot(final_input_denoised[row_num], color = "blue")  # Prediction
plt.plot(final_target[row_num], color = "orange")         # target
plt.plot(final_input[row_num], color = "red")     # original

window = list(range(sample_length))[1200:1250]
plt.plot(final_input_denoised[row_num][window], color = "blue")  # Prediction
plt.plot(final_target[row_num][window], color = "orange")         # target





import wave
import struct
import random

sound_output=wave.open("C:/Development/Python/encoder_decoder/encoder_decoder_sounds/Audio/output/final_input_denoised.wav",'w')
sound_output.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))
f = final_input_denoised[0]
f_median = np.median(final_input_denoised[0])
f = (final_input_denoised[0] - f_median ) * max_value   * .94
f = f.astype('int16')
f = f.reshape(10000)
for i in range(0, len(f)):
        value = f[i]
        packed_value = struct.pack('h', value)
        sound_output.writeframes(packed_value)
sound_output.close()

sound_output=wave.open("C:/Development/Python/encoder_decoder/encoder_decoder_sounds/Audio/output/final_input.wav",'w')
sound_output.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))
f = (final_input[0]  * max_value  + min_value ) * .94
f = f.astype('int16')
f = f.reshape(10000)
for i in range(0, len(f)):
        value = f[i]
        packed_value = struct.pack('h', value)
        sound_output.writeframes(packed_value)
sound_output.close()

sound_output=wave.open("C:/Development/Python/encoder_decoder/encoder_decoder_sounds/Audio/output/final_target.wav",'w')
sound_output.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))
f = (final_target[0]  * max_value  + min_value ) * .94
f = f.astype('int16')
f = f.reshape(10000)
for i in range(0, len(f)):
        value = f[i]
        packed_value = struct.pack('h', value)
        sound_output.writeframes(packed_value)
sound_output.close()

sound_output=wave.open("C:/Development/Python/encoder_decoder/encoder_decoder_sounds/Audio/output/background_testxxx3.wav",'w')
sound_output.setparams((1, 1, 44100, 0, 'NONE', 'not compressed'))
f = (array(background_train_full[1:100000]))#  * max_value  + min_value ) * .94
f = f.astype('int16')
f = f.reshape(100000)
for i in range(0, len(f)):
        value = f[i]
        packed_value = struct.pack('h', value)
        sound_output.writeframes(packed_value)
sound_output.close()






ifile = wave.open("C:\Development\Python\encoder_decoder\encoder_decoder_sounds\Audio\drum_train-01.wav")
ofile = wave.open("C:/Development/Python/encoder_decoder/encoder_decoder_sounds/Audio/output/final_input_denoised.wav", "w")
ofile.setparams(ifile.getparams())

sampwidth = ifile.getsampwidth()
fmts = (None, "=B", "=h", None, "=l")
fmt = fmts[sampwidth]
dcs  = (None, 128, 0, None, 0)
dc = dcs[sampwidth]

outputwave = []

f = (final_input_denoised[0]  * max_value  + min_value ) * .94
f = f.astype('int16')
f = f.reshape(10000)
for i in range(len(f)):
#    iframe = ifile.readframes(1)
#
#    iframe = struct.unpack(fmt, iframe)[0]
#    
#    iframe -= dc
#
#    inputwave.append(iframe)
#    
#    oframe = iframe / 2;
    oframe = f[i]
    oframe += dc
    oframe = struct.pack(fmt, oframe)
    ofile.writeframes(oframe)

ifile.close() 
ofile.close()



plt.plot(inputwave[3000:3100], color = "red")
plt.plot(drum_train_01[3000:3100], color = "blue")