import order_vector
import read_json
import lstm_cond_wgan_2 as GAN
import numpy as np

# excel --- json
def get_multiple_days_json():
    print('Start transfer excel to json:')
    order_vector.order_aggregation_multiple_days()
# json --- npy
def  get_multiple_days_npy(filename):
    print('Start transfer json to npy:')
    np.save(filename + ".npy", read_json.read_multiple_days_data())

#Train Q-GAN
def Q_GAN_Train():
    gan = GAN.lstm_cond_gan(orderLength=240)
    gan.fit()
    gan.predict()

#Train Z_O_GAN
def Z_O_GAN_Train():
    gan = GAN.lstm_cond_gan_01()
    gan.fit()
    gan.predict()


if __name__ == '__main__':
    get_multiple_days_json()
    get_multiple_days_npy('data')
    # Train Zero_one GAN
    Z_O_GAN_Train()
    # TRain Quantity GAN
    #Q_GAN_Train()
