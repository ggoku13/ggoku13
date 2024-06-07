import odrive
from odrive.enums import *

# Подключение к ODrive
print("Подключение к ODrive...")
odrv0 = odrive.find_any()

print("ODrive подключен!")

# Калибровка моторов
print("Калибровка мотора 0...")
odrv0.axis0.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while odrv0.axis0.current_state != AXIS_STATE_IDLE:
    pass
print("Мотор 0 калиброван!")

print("Калибровка мотора 1...")
odrv0.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while odrv0.axis1.current_state != AXIS_STATE_IDLE:
    pass
print("Мотор 1 калиброван!")

# Переключение в режим управления скоростью (velocity control mode)
odrv0.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL
odrv0.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

odrv0.axis0.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL
odrv0.axis1.controller.config.control_mode = CONTROL_MODE_VELOCITY_CONTROL

# Установка скорости
target_velocity_axis0 = 10000  # Скорость для оси 0 (в единицах count/s)
target_velocity_axis1 = 10000  # Скорость для оси 1 (в единицах count/s)

odrv0.axis0.controller.input_vel = target_velocity_axis0
odrv0.axis1.controller.input_vel = target_velocity_axis1

print(f"Ось 0 установлена на скорость {target_velocity_axis0} count/s")
print(f"Ось 1 установлена на скорость {target_velocity_axis1} count/s")

# Ожидание 10 секунд перед остановкой
import time
time.sleep(10)

# Остановка моторов
odrv0.axis0.controller.input_vel = 0
odrv0.axis1.controller.input_vel = 0

print("Моторы остановлены!")

# Переключение в состояние IDLE для безопасности
odrv0.axis0.requested_state = AXIS_STATE_IDLE
odrv0.axis1.requested_state = AXIS_STATE_IDLE

print("ODrive переведён в состояние IDLE.")
