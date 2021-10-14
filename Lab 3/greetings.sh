#adapted from https://learn.adafruit.com/speech-synthesis-on-the-raspberry-pi/speak-easier-flite
echo $1
flite -voice slt -t $1
