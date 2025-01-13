# from PIL import Image
# import numpy as np
# import os
#
#
# def convert_img(img):
#     img = Image.open(img).convert("RGB")
#     img = img.resize((288, 288))
#     img = np.array(img)
#     img = np.transpose(img, (2, 0, 1)) / 255
#     img = np.expand_dims(img, 0).astype(np.float32)
#     return img.flatten().tolist()
#
# os.environ['CLASSPATH'] = ".:lib/onnx.jar:" + os.environ.get('CLASSPATH', '')
# from jnius import autoclass
#
#
# Util = autoclass('org.example.MyUtil')
# util = Util()
# img_arr = convert_img("hua2.jpg")
# # print(len(img_arr))
# # print(3*288*288)
# ret = util.parseImg(img_arr, "EfficientNet_B2.onnx")
# print(np.argmax(ret[0]))
