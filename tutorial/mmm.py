import threading
import logging

from subscripts.humidity import DHT22
from subscripts.pressure import BMP280
from subscripts.wind_speed import wind_speed
from subscripts.wind_direction import wind_direction
from subscripts.create_folder import CreateFolder


def thread_dht(cur_f_path):
    dht = DHT22()
    dht.method1(cur_f_path)

def thread_bmp(cur_f_path):
    bmp = BMP280()
    bmp.method2(cur_f_path)

def thread_ws(cur_f_path):
    ws = wind_speed()
    ws.method3(cur_f_path)

def thread_wd(cur_f_path):
    wd = wind_direction()
    wd.method4(cur_f_path)

def init_logging(root_path):
    logger = logging.getLogger()
    logger.setLevel('DEBUG')
    BASIC_FORMAT = '%(asctime)s - %(levelname)-5s - %(filename)-15s: line %(lineno)d - %(message)s'
    DATE_FORMATE = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(BASIC_FORMAT, DATE_FORMATE)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(filename=root_path+'/result/log_recording.log', mode='a', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

if __name__ == "__main__":
    root_path = '/usr/local/project/ISEC2024-Final-Project/'
    cf = CreateFolder(root_path)
    cf.initialize()
    cur_folder_path = cf.get_current_storage_path()
    init_logging(root_path)
    logging.info('create storage dir:' + cur_folder_path)

    logging.info('=============start to record the sensor data=============')
    thread1 = threading.Thread(target=thread_dht, args=(cur_folder_path,))
    thread2 = threading.Thread(target=thread_bmp, args=(cur_folder_path,))
    thread3 = threading.Thread(target=thread_ws, args=(cur_folder_path,))
    thread4 = threading.Thread(target=thread_wd, args=(cur_folder_path,))

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Wait for threads to complete
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
