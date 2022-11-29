import cv2
import numpy as np

def img_transfer(model_type, image_file):
    # 모델 파일 불러오기
    model_path = "post/deeplearning/style_transfer/media/" + model_type
    net = cv2.dnn.readNetFromTorch(model_path)

    # 변환할 이미지 파일 불러오기
    image_path = "post/deeplearning/style_transfer/media/" + str(image_file)
    img = cv2.imread(image_path)

    # 이미지 변환 작업
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
    
    # 결과물 파일 저장 및 경로, 이름 설정
    name1 = model_type[model_type.index('/')+1:]
    
    image_name = str(image_file)
    
    name2 = image_name[image_name.index('/')+1:]
    
    cv2.imwrite(f"post/deeplearning/style_transfer/media/after_image/{name1}+{name2}", output)
    
    return output

