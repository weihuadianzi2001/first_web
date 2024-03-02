import cv2
import numpy as np
with open('D:/shijuan/old/test.txt', 'r') as f:
  test_img_path=[]
  N = 0
  for line in f:
    test_img_path.append(line.strip())
  for image_path in test_img_path:
        print(image_path)
        N =N+1
        img = cv2.imread(image_path)
        new = np.clip(1.4057577998008846*img-38.33089999653017, 0, 255).astype(np.uint8)
        cv2.imwrite('D:/shijuan/new/{N}.png', new)