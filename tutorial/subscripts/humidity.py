class DHT22():
    def __init__(self):
        pass

    def get_humidity(self, cur_folder_path):
        DHT_SENSOR=Adafruit_DHT.DHT22
        DHT_PIN=18
        humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        last_temperature = 0.0
        last_humidity = 0.0
        try:
            print("Temp: {0:0.1f} °C    Humidity: {1:0.1f} % ".format(temp, humidity))
            last_temperature = "{0:0.3f}".format(temp)
            last_humidity = "{0:0.3f}".format(humidity)
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
                    file.write(str(last_temperature))
                    file.write(',°C,')
                    file.write(str(last_humidity))
                    file.write(',%')
                    file.write('\n')
                    file.flush()
            else:
                logging.info("can not receive humidity data, check the connection!")
    def method1(self, cur_folder_path):
        while True:
            self.get_humidity(cur_folder_path)