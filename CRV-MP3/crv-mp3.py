#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:57:17 2018

@author: mikewoodward

The 2009 Honda CRV has an MP3 player that only plays some types of MP3 files.
It doesn't play M4A files. This script will convert MP3 and M4A files to a 
format that the 2009 CRV can play.
The files to be transcoded are in the Original folder and the output files
are in the Recoded folder.

"""

import glob
from shutil import copyfile
import subprocess
import os
from mutagen.mp3 import MP3, BitrateMode


# %%===========================================================================
# Constants
# =============================================================================
#FFMPEG = ("""/usr/local/bin/ffmpeg -i """
#          """"{0}" -codec:a libmp3lame -b:a 128k -ar 44100 """
#          """-joint_stereo 1 -f mp3 "{1}" """)

# The constants below point to the folders that contain the FFMPEG and 
# LAME executables. If you're on a Windows machine, you'll need to change
# them..

# Script to run the FFMPEG decoder. The wav file is resampled to 44.1 kHz.
FFMPEG2 = ("""/usr/local/bin/ffmpeg -i """
           """"{0}" -acodec pcm_s16le -ar 44100 "{1}" """)

# Script to run the lame mp3 encoder. Note the encoded bit rate is set to
# 128 kbit/s at a sampling rate of 44.1 kHz. q0 is the best quality encoding.
LAME = """/usr/local/bin/lame "{0}" "{1}" -q0 -b128 --resample 44.1"""

# These are the MP3 CBR bitrates I believe the CRV MP3 player can support
CBRBITRATES = [32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000,
               160000, 192000, 224000, 256000, 320000]

# %%===========================================================================
# Functions
# =============================================================================
def get_names():
    
    """Get the nmes of all the files to transcode or copy."""
    
    # Get all folders below Original
    folders = glob.glob('./Original/**/', recursive=True)
    folders.sort()
    
    files_list = []
    
    # Cycle through every folder
    for folder in folders:
        print(folder)
        
        abs_folder = os.path.abspath(folder)
        
        # We only want the m4a or mp3 files
        files_list.extend(glob.glob(abs_folder + '/*.mp3'))
        files_list.extend(glob.glob(abs_folder + '/*.m4a'))  
        
    files_list.sort()
    
    return files_list

# %%
def get_rename(names):
    
    """Set the new names of the files."""
 
    rename = []
    
    for name in names:

        filename, file_extension = os.path.splitext(name)            
        filename = filename.replace('/Original/', '/Recoded/')            

        rename.append({'old': name, 
                       'old type': file_extension,
                       'new':filename + '.mp3',
                       'basename': name.split('/')[-1]})
        
    return rename
   
# %%   
def recode(rename):
    
    """Transcode or copy the mp3/m4a files."""
    
    for entry in rename:

        # Create a new folder for the output audio if it doesn't already exist
        folder = os.path.dirname(entry['new'])
        if not os.path.isdir(folder):
            os.makedirs(folder)
            
        # Delete the copied or transcoded file if it already exists
        if os.path.isfile(entry['new']):
            os.remove(entry['new'])
        
        # If the source file is an mp3
        if entry['old type'] == '.mp3': 
        
            audio = MP3(entry['old']) 
            
            # Find out if we need to recode the file and then recode it
            if (audio.info.bitrate_mode == BitrateMode.VBR or 
                audio.info.bitrate_mode == BitrateMode.ABR or
                audio.info.bitrate_mode == BitrateMode.UNKNOWN or
                audio.info.bitrate not in CBRBITRATES or
                audio.info.mode == 0):
                lame_string = LAME.format(entry['old'], entry['new'])
                subprocess.run(lame_string, shell=True, check=True)
            else:
                # Copy the file without changing it
                copyfile(entry['old'], entry['new'])    

        # The file is an m4a
        else:
            try:
                ffmpeg_string = FFMPEG2.format(entry['old'], 
                                               entry['new'][0:-4] + '.wav') 
                # Decode to wav
                subprocess.run(ffmpeg_string, shell=True, check=True)  
                
                lame_string = LAME.format(entry['new'][0:-4] + 
                                          '.wav', entry['new'])
                # Recode to mp3
                subprocess.run(lame_string, shell=True, check=True)  
                
                # Remove the wav file
                os.remove(entry['new'][0:-4] + '.wav')
                                
            except BaseException as error:
                print(ffmpeg_string)
                raise error

# %%===========================================================================
# Main
# =============================================================================
if __name__ == '__main__':
    
    print("**********\n*CR-V MP3*\n**********")
    print("""Transcodes MP3 and M4A files to a format that can be """
          """played on the MP3 player in a 2009 Honda CR-V.""")
    print('If you have a lot of M4A files, transcoding can take a while.')
    print("Put the files to encode in the Original folder.")
    print("The transcoded files will be in the Recoded folder.")
    
    print("Getting file names")
    names = get_names()
    print("Setting up renames")
    rename = get_rename(names)
    print("Recoding")
    recode(rename)
        