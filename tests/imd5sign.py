import Wii
import sys

for elem in sys.argv:
    Wii.IMD5(elem).add(elem)
