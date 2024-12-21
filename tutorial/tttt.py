import logging
import time
from datetime import datetime

import adafruit_dht
import board


class DHT22():
    def get_humidity(self, cur_folder_path):
        dht = adafruit_dht.DHT22(board.D4)
        last_temperature = 0.0
        last_humidity = 0.0
        try:
            last_temperature = dht.temperature
            last_humidity = dht.humidity
        except RuntimeError as e:
            logging.error(f'Reading from DHT failure: {e.args}')
        finally:
            if last_temperature and last_humidity is not None:
                # 保存
                with open(cur_folder_path + "/temperature_and_pressure_data.txt",
                          "a") as file:
                    cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    file.write(cur_time)
                    file.write(',')
                    file.write(last_temperature)
                    file.write(',t,')
                    file.write(last_humidity)
                    file.write(',%,')
                    file.write('\n')
                    file.flush()
            else:
                logging.info("can not receive humidity data, check the connection!")
    def method1(self, cur_folder_path):
        while True:
            self.get_humidity(cur_folder_path)