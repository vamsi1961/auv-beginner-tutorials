import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense ,Conv2D ,Conv2DTranspose ,Dropout ,BatchNormalization ,Input ,MaxPooling2D ,concatenate,UpSampling2D
from tensorflow.keras.models import Model
import timeit
from tensorflow.keras.optimizers import Adam



def conv_model(hidden_size = (256,256,3)):

    input_layer = Input((256,256,3))
    conv_1 = Conv2D(hidden_size * 1,(3,3),activation = "relu" ,padding = "same")(input_layer)
    conv_1 = Conv2D(hidden_size * 1,(1,1),activation = "relu" ,strides=(2,2))(conv_1)

    conv_2 = Conv2D(hidden_size * 2,(3,3),activation = "relu" ,padding = "same")(conv_1)
    conv_2 = Conv2D(hidden_size * 2,(1,1),activation = "relu" ,strides=(2,2))(conv_2)

    conv_3 = Conv2D(hidden_size * 4,(3,3),activation = "relu" ,padding = "same")(conv_2)
    conv_3 = Conv2D(hidden_size * 4,(1,1),activation = "relu" ,strides=(2,2))(conv_3)

    conv_4 = Conv2D(hidden_size * 8,(3,3),activation = "relu" ,padding = "same")(conv_3)
    conv_4 = Conv2D(hidden_size * 8,(1,1),activation = "relu" ,strides=(2,2))(conv_4)

    conv_m = Conv2D(hidden_size * 32,(3,3),activation = "relu" ,padding = "same")(conv_4)
    conv_m = Conv2D(hidden_size * 32,(1,1),activation = "relu" ,strides=(2,2))(conv_m)

    de_conv_4 = Conv2DTranspose(hidden_size * 8, (3, 3), strides=(2, 2), padding="same")(conv_m)
    de_conv_4 = concatenate([de_conv_4 , conv_4])
    de_conv_4 = Conv2D(hidden_size * 8, (3, 3), activation="relu", padding="same")(de_conv_4)
    de_conv_4 = Conv2D(hidden_size * 8, (3, 3), activation="relu", padding="same")(de_conv_4)

    de_conv_3 = Conv2DTranspose(hidden_size * 4, (3, 3), strides=(2, 2), padding="same")(de_conv_4)
    de_conv_3 = concatenate([de_conv_3 , conv_3])
    de_conv_3 = Conv2D(hidden_size * 4, (3, 3), activation="relu", padding="same")(de_conv_3)
    de_conv_3 = Conv2D(hidden_size * 4 ,(3, 3), activation="relu", padding="same")(de_conv_3)

    de_conv_2 = Conv2DTranspose(hidden_size * 2, (3, 3), strides=(2, 2), padding="same")(de_conv_3)
    de_conv_2 = concatenate([de_conv_2 , conv_2])
    de_conv_2 = Conv2D(hidden_size * 2, (3, 3), activation="relu", padding="same")(de_conv_2)
    de_conv_2 = Conv2D(hidden_size * 2, (3, 3), activation="relu", padding="same")(de_conv_2)

    de_conv_1 = Conv2DTranspose(hidden_size * 2, (3, 3), strides=(2, 2), padding="same")(de_conv_2)
    #de_conv_1 = concatenate([de_conv_1 , conv_1])
    de_conv_1 = Conv2D(hidden_size * 2, (3, 3), activation="relu", padding="same")(de_conv_1)
    de_conv_1 = Conv2D(hidden_size * 2 ,(3, 3), activation="relu", padding="same")(de_conv_1)

    output_layer = Conv2D(3, (1,1), padding="same", activation="sigmoid")(de_conv_1)

    model = Model(inputs = [input_layer] ,outputs = [output_layer])
    return model

model = conv_model(32)
model.load_weights("enh_menco_0.3L1_0.7ssim_3c_underwater_imagenet.h5")


def loss_fn(y_true,y_pred):
    mae = tf.keras.losses.MeanAbsoluteError()
    k = mae(y_true, y_pred)
    k = (k/(256*256))
    ssim = tf.image.ssim(y_true *255 , y_pred * 255, max_val = 255, filter_size=11, filter_sigma=1.5, k1=0.01, k2=0.03)
    m = (1-ssim)/2

    return ((0.3*k) + (0.7*m)) 


model.compile(optimizer = Adam(lr = 0.0001),loss = loss_fn ,metrics = [tf.keras.metrics.MeanSquaredError()])

def get_result(image ,plot = True):

    image = image.reshape((-1,256,256 ,3))
    image_ = ((image/255.0))
    raw_result = model.predict(image_)
    result = raw_result.reshape((128,128,3))
    return raw_result


start = timeit.default_timer()
img = cv2.imread("red.jpeg")
img = cv2.resize(img,(256,256))
print(img.shape)
print(model)
result1 = get_result(img ,plot = False)
print(result1.shape)
#cv2.imshow("result1",result1)
cv2.imshow("img",img)
stop = timeit.default_timer()
print('Time: ', stop - start)
cv2.waitKey(0)