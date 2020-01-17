import os
import numpy as np
import matplotlib.pylab as plt
import matplotlib.image as mpimg
import PIL.Image as Image

directory = "./PreventPic/"

#sess = tf.compat.v1.Session()

test_image_ones = []

num = 0
for imgname in os.listdir(directory):
    print(imgname)
    image = Image.open(directory + imgname)
    print(directory + imgname)
    #image.show()
    image.save('2/' + str(num) + '.png')
    num += 1
    #img = image.open(f)
    #img.save(str(sum) + '.jpg')
    #arr = np.asarray(img, dtype=np.float32)
    #print(img.size, arr.shape)
    #print(arr)
    #test_image_ones.append(arr)
'''
test_image_ones = np.array(test_image_ones)
print(test_image_ones.shape)
print(type(test_image_ones))
print(test_image_ones)
'''