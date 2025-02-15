# BMP280 iic address.
BMP280_I2C_ADDRESS = 0x76        # SDO = 0
# Registers value
BMP280_ID_Value = 0x58           # BMP280 ID
BMP280_RESET_VALUE = 0xB6
# BMP280 Registers definition
BMP280_TEMP_XLSB_REG = 0xFC      # Temperature XLSB Register
BMP280_TEMP_LSB_REG = 0xFB       # Temperature LSB Register
BMP280_TEMP_MSB_REG = 0xFA       # Temperature LSB Register
BMP280_PRESS_XLSB_REG = 0xF9     # Pressure XLSB  Register
BMP280_PRESS_LSB_REG = 0xF8      # Pressure LSB Register
BMP280_PRESS_MSB_REG = 0xF7      # Pressure MSB Register
BMP280_CONFIG_REG = 0xF5         # Configuration Register
BMP280_CTRL_MEAS_REG = 0xF4      # Ctrl Measure Register
BMP280_STATUS_REG = 0xF3         # Status Register
BMP280_RESET_REG = 0xE0          # Softreset Register
BMP280_ID_REG = 0xD0             # Chip ID Register
# calibration parameters
BMP280_DIG_T1_LSB_REG = 0x88
BMP280_DIG_T1_MSB_REG = 0x89
BMP280_DIG_T2_LSB_REG = 0x8A
BMP280_DIG_T2_MSB_REG = 0x8B
BMP280_DIG_T3_LSB_REG = 0x8C
BMP280_DIG_T3_MSB_REG = 0x8D
BMP280_DIG_P1_LSB_REG = 0x8E
BMP280_DIG_P1_MSB_REG = 0x8F
BMP280_DIG_P2_LSB_REG = 0x90
BMP280_DIG_P2_MSB_REG = 0x91
BMP280_DIG_P3_LSB_REG = 0x92
BMP280_DIG_P3_MSB_REG = 0x93
BMP280_DIG_P4_LSB_REG = 0x94
BMP280_DIG_P4_MSB_REG = 0x95
BMP280_DIG_P5_LSB_REG = 0x96
BMP280_DIG_P5_MSB_REG = 0x97
BMP280_DIG_P6_LSB_REG = 0x98
BMP280_DIG_P6_MSB_REG = 0x99
BMP280_DIG_P7_LSB_REG = 0x9A
BMP280_DIG_P7_MSB_REG = 0x9B
BMP280_DIG_P8_LSB_REG = 0x9C
BMP280_DIG_P8_MSB_REG = 0x9D
BMP280_DIG_P9_LSB_REG = 0x9E
BMP280_DIG_P9_MSB_REG = 0x9F