import threading
import logging

from subscripts.humidity import DHT22
from subscripts.pressure import BMP280
from subscripts.wind_speed import wind_speed
from subscripts.wind_direction import wind_direction
from subscripts.create_folder import CreateFolder


threads = []
classes = [DHT22, BMP280, wind_speed, wind_direction]
def thread_function(cls, cur_f_path):
    obj = cls()
    method = getattr(obj, f"method{classes.index(cls) + 1}", None)
    if callable(method):
        method(cur_f_path)

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
    for cls in classes:
        thread = threading.Thread(target=thread_function, args=(cls,cur_folder_path))
        threads.append(thread)
        thread.start() # 启动线程
        logging.info('============='+cls.__name__+' data start to record!=============')

    for thread in threads:
        thread.join()  # 阻塞主进程，直到所有线程都完成

