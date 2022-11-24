import cv2
import numpy as np

def dl(image_path):
    _CUR_DIR = 'C:/Users/gudql/Desktop/B4AFTER_Deeplearning/B4AFTER_Deeplearning_Backend/post/deeplearning/style_transfer'

    net = cv2.dnn.readNetFromTorch(_CUR_DIR + '/models/instance_norm/la_muse.t7')

    path = "media\\" + str(image_path)

    img = cv2.imread(_CUR_DIR + '/image/cat1.png')

    h, w, c = img.shape

    img = cv2.resize(img, dsize=(500, int(h / w * 500)))

    MEAN_VALUE = [103.939, 116.779, 123.680]
    blob = cv2.dnn.blobFromImage(img, mean=MEAN_VALUE)

    net.setInput(blob)
    output = net.forward()

    output = output.squeeze().transpose((1, 2, 0))
    output += MEAN_VALUE

    output = np.clip(output, 0, 255)
    output = output.astype('uint8')
    
    return output
