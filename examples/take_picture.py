# very simple script that just takes one picture
from picamera import PiCamera

# creates a camera object to take pictures or videos with
camera = PiCamera()

# captures to the pi user's home directory
# change the quoted path to capture somewhere else
camera.capture('/home/pi/capture.jpg')
