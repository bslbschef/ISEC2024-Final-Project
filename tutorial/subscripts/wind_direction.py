import logging
from datetime import datetime
import serial
import struct
import time


# CRC16校验计算函数
def calculate_crc(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc
def angle_to_wind_direction(angle):
    wind_directions = [
        (348.75, 11.25, "北风"),
        (11.25, 33.75, "北东北风"),
        (33.75, 56.25, "东北风"),
        (56.25, 78.75, "东东北风"),
        (78.75, 101.25, "东风"),
        (101.25, 123.75, "东东南风"),
        (123.75, 146.25, "东南风"),
        (146.25, 168.75, "南东南风"),
        (168.75, 191.25, "南风"),
        (191.25, 213.75, "南西南风"),
        (213.75, 236.25, "西南风"),
        (236.25, 258.75, "西西南风"),
        (258.75, 281.25, "西风"),
        (281.25, 303.75, "西西北风"),
        (303.75, 326.25, "西北风"),
        (326.25, 348.75, "北西北风"),
    ]
    for start, end, direction in wind_directions:
        if start <= angle < end or (start > end and (angle >= start or angle < end)):  # 跨0度的情况
            return direction
    return "unknown wind direction! check list!"

class wind_direction():
    # 构建Modbus RTU指令帧
    def build_read_frame(self, device_address, function_code, start_address, data_length):
        frame = struct.pack('>B B H H', device_address, function_code, start_address, data_length)
        crc = calculate_crc(frame)
        frame += struct.pack('<H', crc)  # 添加CRC校验，低位在前
        return frame

    # 解析应答帧，读取风向数据
    def parse_response(self, response):
        if len(response) < 7:
            logging.info("Error: The length of the response data is incorrect.")
            return None

        # 校验CRC
        data = response[:-2]
        received_crc = struct.unpack('<H', response[-2:])[0]
        calculated_crc = calculate_crc(data)
        if received_crc != calculated_crc:
            logging.info("Error: CRC check failed.")
            return None

        # 提取风向值
        wind_direction_value = struct.unpack('>H', response[3:5])[0]  # 风向为2字节无符号整数
        wind_direction = wind_direction_value / 10.0  # 根据协议，转换为实际值（单位m/s）
        return wind_direction

    # 读取风向数据函数
    def read_wind_direction(self, serial_port, cur_folder_path, device_address=0x01, function_code=0x03, start_address=0x00, data_length=0x01):
        try:
            # 打开串口
            ser = serial.Serial(serial_port, baudrate=4800, bytesize=8, parity='N', stopbits=1, timeout=1)
            #logging.info('serial port is opening: '+serial_port)

            # 构建读取指令帧
            request_frame = self.build_read_frame(device_address, function_code, start_address, data_length)
            #logging.info('send the reading frame: ' + request_frame.hex(' '))

            # 发送指令
            ser.write(request_frame)

            # 接收应答帧
            response = ser.read(7)  # 应答帧长度为7字节
            #logging.info('receive the responding frame: ' + response.hex(' '))

            # 解析风向数据
            wind_direction = self.parse_response(response)
            #print("Wind direction: {0:0.3f} °".format(wind_direction))
            wd = "{0:0.3f}".format(wind_direction)
            if wd is not None:
                # 保存
                with open(cur_folder_path+"/wind_direction_data.txt", "a") as file:
                    cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    cur_dir = angle_to_wind_direction(wind_direction)
                    file.write(cur_time)
                    file.write(',')
                    file.write(str(wd))
                    file.write(',°,')
                    file.write(cur_dir)
                    file.write(',十六方位角')
                    file.write('\n')
                    file.flush()
            else:
                logging.info("can not receive wind speed data, check the connection!")

            # 关闭串口
            ser.close()
        except Exception as e:
            logging.info("Error: "+str(e))

    def method4(self, cur_folder_path):
        serial_port = "/dev/ttyUSB1"
        logging.info('=============Wind Direction data start to record!=============')
        while True:
            self.read_wind_direction(serial_port, cur_folder_path)
            time.sleep(1)
