import logging
from datetime import datetime
import Adafruit_DHT
import time


class DHT22():
    def __init__(self):
        pass

    def get_humidity(self, cur_folder_path):
        DHT_SENSOR=Adafruit_DHT.DHT22
        DHT_PIN=18
        try:
            humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            #print("Temp: {0:0.1f} °C    Humidity: {1:0.1f} % ".format(temp, humidity))
            #logging.info("Temp: {0:0.1f} °C    Humidity: {1:0.1f} % ".format(temp, humidity))
            if humidity is None or temp is None:
                logging.info('Humidity or Temp data is None, check the hardware connection!!!')
                last_temperature = 0.00
                last_humidity = 0.00
            else:
                last_temperature = "{0:0.3f}".format(temp)
                last_humidity = "{0:0.3f}".format(humidity)
        except RuntimeError as e:
            logging.error(f'Reading from DHT failure: {e.args}, Check hardware connection!')
        finally:
            if last_temperature and last_humidity is not None:
                # 保存
                with open(cur_folder_path + "/temperature_and_humidity_data.txt", "a") as file:
                    cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    file.write(cur_time)
                    file.write(',')
                    file.write(str(last_temperature))
                    file.write(',°C,')
                    file.write(str(last_humidity))
                    file.write(',%')
                    file.write('\n')
                    file.flush()
            else:
                logging.info("can not receive humidity data, check the connection!")
    def method1(self, cur_folder_path):
        logging.info('=============DHT22 data start to record!=============')
        while True:
            self.get_humidity(cur_folder_path)
            time.sleep(0.5)