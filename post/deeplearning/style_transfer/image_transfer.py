import cv2
import numpy as np

def img_transfer(model_type, image_file):
    
    model_path = "post/deeplearning/style_transfer/media/" + model_type

    net = cv2.dnn.readNetFromTorch(model_path)

    image_path = "post/deeplearning/style_transfer/media/" + str(image_file)

    img = cv2.imread(image_path)

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
    
    name1 = model_type[model_type.index('/')+1:]
    
    image_name = str(image_file)
    
    name2 = image_name[image_name.index('/')+1:]
    
    cv2.imwrite(f"post/deeplearning/style_transfer/media/after_image/{name1}+{name2}", output)
    
    return output

