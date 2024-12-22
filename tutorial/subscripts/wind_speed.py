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


class wind_speed():
    # 构建Modbus RTU指令帧
    def build_read_frame(self, device_address, function_code, start_address, data_length):
        frame = struct.pack('>B B H H', device_address, function_code, start_address, data_length)
        crc = calculate_crc(frame)
        frame += struct.pack('<H', crc)  # 添加CRC校验，低位在前
        return frame

    # 解析应答帧，读取风速数据
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

        # 提取风速值
        wind_speed_value = struct.unpack('>H', response[3:5])[0]  # 风速为2字节无符号整数
        wind_speed = wind_speed_value / 10.0  # 根据协议，转换为实际值（单位m/s）
        return wind_speed

    # 读取风速数据函数
    def read_wind_speed(self, serial_port, cur_folder_path, device_address=0x01, function_code=0x03, start_address=0x00, data_length=0x01):
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

            # 解析风速数据
            wind_speed = self.parse_response(response)
            #print("Wind speed: {0:0.3f} m/s".format(wind_speed))
            ws = "{0:0.3f}".format(wind_speed)
            if ws is not None:
                # 保存
                with open(cur_folder_path+"/wind_speed_data.txt", "a") as file:
                    cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                    file.write(cur_time)
                    file.write(',')
                    file.write(str(ws))
                    file.write(',m/s')
                    file.write('\n')
                    file.flush()
            else:
                logging.info("can not receive wind speed data, check the connection!")

            # 关闭串口
            ser.close()
        except Exception as e:
            logging.info("Error: "+str(e))

    def method3(self, cur_folder_path):
        serial_port = "/dev/ttyUSB0"
        logging.info('=============Wind Speed data start to record!=============')
        while True:
            self.read_wind_speed(serial_port, cur_folder_path)
            time.sleep(2)
