import serial
import pyautogui
import time

# --- Configuration ---
SERIAL_PORT = 'COM3'  # Replace with your Arduino's serial port (e.g., /dev/ttyACM0 on Linux, /dev/cu.usbmodemXXXX on macOS)
BAUD_RATE = 9600
SERIAL_TIMEOUT = 1  # Seconds to wait for serial data

# --- Key mappings for YouTube ---
# adjust these keys however desired to change the use
KEY_LEFT = 'left'
KEY_RIGHT = 'right'
KEY_UP = 'up'
KEY_DOWN = 'down'
KEY_PLAY_PAUSE = 'space'

def simulate_key_press(key):
    try:
        pyautogui.press(key)
        print(f"Simulated key press: {key}")
    except pyautogui.FailSafeException:
        print("Pyautogui failsafe triggered. Move mouse to a corner to stop.")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=SERIAL_TIMEOUT)
    time.sleep(2)  # Give time for serial port to initialize
    print(f"Serial port opened successfully on {SERIAL_PORT} at {BAUD_RATE}!")
except serial.SerialException as e:
    print(f"Error opening serial port {SERIAL_PORT}: {e}")
    exit()

try:
    while True:
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode('utf-8').strip()
                print(f"Received from Arduino: {data}")
                if data == "LEFT":
                    simulate_key_press(KEY_LEFT)
                elif data == "RIGHT":
                    simulate_key_press(KEY_RIGHT)
                elif data == "UP":
                    simulate_key_press(KEY_UP)
                elif data == "DOWN":
                    simulate_key_press(KEY_DOWN)
                elif data == "PRESS":
                    simulate_key_press(KEY_PLAY_PAUSE)
            except UnicodeDecodeError:
                print("Error decoding serial data.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nScript stopped by user.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")