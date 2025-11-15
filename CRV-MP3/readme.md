# CRV-MP3
The Honda CR-V media player circa 2009 is very picky about the MP3 formats it can play, and it can't play M4A files at all. This software transcodes MP3 and M4A files to an MP3 format suitable for use on the MP3 player on a 2009 Honda CR-V. It likely works with the MP3 players in other Honda cars of about the same age, but obviously I can't test it.

To use the software, you'll need to install FFMPEG and LAME on your system. FFMEG is used to decode M4A files, and LAME is used to encode MP3 files (you might need to download the MP3 encoding engine for LAME). On OSX, the best way to install these packahes is using brew, so for example brew lame.

The CRV-MP3 script is designed to work on OSX, so it points to usr folders that contain the FFMPEG and LAME executables. If you're using a Windows machine, you'll have to point to the appropriate folders on your system. 

The software reads in MP3 and M4A files in the Original folder, transcodes them, and writes the transcoded files to a Recoded folder. M4A files are coded to MP3 and MP3 files are recoded to an MP3 format the CR-V media player can handle.

Here's an example of how to use the software.
* Install FFMPEG and LAME (you may need to install the LAME MP3 engine).
* Check the crv-mp3 file and make sure the constants FFMPEG2 and LAME point to the correct folder on your system (they're correctly set up for OSX).
* Create an Original folder in the same folder as the crv-mp3.py file.
* Copy your MP3 and M4A files to the Original folder. Here's an example of some albums on my machine:

       crv_mp3.py

       Original

          Christmas
  
             02 God Rest Ye Merry Gentlemen.mp3
  
             02 All I Want for Christmas Is You (2005).mp3
    
             18 Christmas In Hollis.mp3
    
             02 Driving Home for Christmas.mp3
    
             1-01 Happy Christmas (War Is Over).m4a
    
             1-02 Wonderful Christmastime 1.m4a
    
             01 Fairytale Of New York.mp3
    
             10 2000 Miles.m4a
    
             08 Hazy shade of winter.mp3
  
          Alanis Morissette
  
             Jagged Little Pill
    
                04 Hand In My Pocket.m4a

* Now, execute the script:

    python crv-mp3.py

* At the end of the process, you should see:

       crv_mp3.py

       Original

          Christmas
  
             02 God Rest Ye Merry Gentlemen.mp3
  
             02 All I Want for Christmas Is You (2005).mp3
    
             18 Christmas In Hollis.mp3
    
             02 Driving Home for Christmas.mp3
    
             1-01 Happy Christmas (War Is Over).m4a
    
             1-02 Wonderful Christmastime 1.m4a
    
             01 Fairytale Of New York.mp3
    
             10 2000 Miles.m4a
    
             08 Hazy shade of winter.mp3
  
          Alanis Morissette
  
             Jagged Little Pill
    
                04 Hand In My Pocket.m4a
                
       Recoded
       
          Christmas
  
             02 God Rest Ye Merry Gentlemen.mp3
  
             02 All I Want for Christmas Is You (2005).mp3
    
             18 Christmas In Hollis.mp3
    
             02 Driving Home for Christmas.mp3
    
             1-01 Happy Christmas (War Is Over).mp3
    
             1-02 Wonderful Christmastime 1.mp3
    
             01 Fairytale Of New York.mp3
    
             10 2000 Miles.mp3
    
             08 Hazy shade of winter.mp3
  
          Alanis Morissette
  
             Jagged Little Pill
    
                04 Hand In My Pocket.mp3
                
* The MP3 files may look the same, but they might have been been transcoded to a different sampling rate, bit rate, or audio mode.
