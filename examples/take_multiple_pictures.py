# takes multiple pictures with options

# imports necessary dependencies
from picamera import PiCamera
from optparse import OptionParser

# declares objects to use later
camera = PiCamera()
parser = OptionParser()

# gives usage information and adds options for script
usage = "usage: %prog [options]"
parser.add_option("-n", "--number", help="supply number of pictures to take", dest="captures", default=1)

# parses the arguments and stores them in tuples
(opts, args) = parser.parse_args()

# captures images in a sequence based on a user supplied value
camera.capture_sequence(['/home/pi/image%s.jpg' % i for i in range(int(captures))])
