# takes multiple pictures with options

# imports necessary dependencies
from picamera import PiCamera
from optparse import OptionParser

parser = OptionParser()
usage = "usage: %prog [options]"
parser.add_option("-n", "--number", type="string", help="supply number of pictures to take", dest="captures", default=1)

# creates a camera object to take pictures or videos with
camera = PiCamera()

camera.capture_sequence(['/home/pi/image%s.jpg' % i for i in range(captures)])
