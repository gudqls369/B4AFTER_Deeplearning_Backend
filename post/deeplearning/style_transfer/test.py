import os
import cv2
from image_transfer import *


def deeplearning():
    os.system("style_transfer image/cat1.png model/cryingwoman.jpg -s 256 -i 100")
    
# deeplearning()

def test():
    img = dl()
    cv2.imwrite("model/result.png", img)
    
test()