import numpy as np
import cv2
import urllib.request
import matplotlib.pyplot as plt
print("OpenCV-Python Version %s" % cv2.__version__)

image_link = input('> enter image link : ')
try:
    req = urllib.request.urlopen(image_link)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    # display an image using matplotlib
    # plt.imshow(img) shown an image with wrong colorspace
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

    cv2.imwrite('image.png',image)

except:
    print('error')
    quit()
