import serial
import struct

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

# 构建Modbus RTU指令帧
def build_read_frame(device_address, function_code, start_address, data_length):
    frame = struct.pack('>B B H H', device_address, function_code, start_address, data_length)
    crc = calculate_crc(frame)
    frame += struct.pack('<H', crc)  # 添加CRC校验，低位在前
    return frame

# 解析应答帧，读取风速数据
def parse_response(response):
    if len(response) < 7:
        print("错误：应答数据长度不正确")
        return None

    # 校验CRC
    data = response[:-2]
    received_crc = struct.unpack('<H', response[-2:])[0]
    calculated_crc = calculate_crc(data)
    if received_crc != calculated_crc:
        print("错误：CRC校验失败")
        return None

    # 提取风速值
    wind_speed_value = struct.unpack('>H', response[3:5])[0]  # 风速为2字节无符号整数
    wind_speed = wind_speed_value / 10.0  # 根据协议，转换为实际值（单位m/s）
    return wind_speed

# 读取风速数据函数
def read_wind_speed(serial_port, device_address=0x01, function_code=0x03, start_address=0x00, data_length=0x01):
    try:
        # 打开串口
        ser = serial.Serial(serial_port, baudrate=4800, bytesize=8, parity='N', stopbits=1, timeout=1)
        print("串口已打开:", serial_port)

        # 构建读取指令帧
        request_frame = build_read_frame(device_address, function_code, start_address, data_length)
        print("发送读取帧:", request_frame.hex(' '))

        # 发送指令
        ser.write(request_frame)

        # 接收应答帧
        response = ser.read(7)  # 应答帧长度为7字节
        print("接收到应答帧:", response.hex(' '))

        # 解析风速数据
        wind_speed = parse_response(response)
        if wind_speed is not None:
            print(f"当前风速值: {wind_speed} m/s")
            # 保存到文件
            with open("wind_speed_data.txt", "a") as file:
                file.write(f"风速值: {wind_speed} m/s\n")
            print("风速数据已保存到文件 'wind_speed_data.txt'")
        else:
            print("未能解析风速值")

        # 关闭串口
        ser.close()
    except Exception as e:
        print("发生错误:", str(e))

# 主函数
if __name__ == "__main__":
    # 根据你的系统串口修改 serial_port
    serial_port = "COM7"  # Windows下的串口，如 COM3；Linux下可用 /dev/ttyUSB0
    while True:
        read_wind_speed(serial_port)
