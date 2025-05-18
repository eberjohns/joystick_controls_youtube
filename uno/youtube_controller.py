import serial
import pyautogui
import time

# --- Configuration ---
SERIAL_PORT = 'COM3'  # Replace with your Arduino's serial port
BAUD_RATE = 9600
SERIAL_TIMEOUT = 1  # Seconds to wait for serial data

# --- Key mappings for YouTube ---
KEY_LEFT = 'left'
KEY_RIGHT = 'right'
KEY_UP = 'pageup'     # Adjust for volume up
KEY_DOWN = 'pagedown'   # Adjust for volume down
KEY_PLAY_PAUSE = 'space'

# --- Delay for repeated key presses (in seconds) ---
REPEAT_DELAY = 0.1

def simulate_key_press(key):
    try:
        pyautogui.press(key)
        print(f"Simulated key press: {key}")
    except pyautogui.FailSafeException:
        print("Pyautogui failsafe triggered. Move mouse to a corner to stop.")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=SERIAL_TIMEOUT)
    time.sleep(2)
    print(f"Serial port opened successfully on {SERIAL_PORT} at {BAUD_RATE}!")
    last_direction = None
    last_press_time = 0

    while True:
        if ser.in_waiting > 0:
            try:
                data = ser.readline().decode('utf-8').strip()
                print(f"Received from Arduino: {data}")
                current_time = time.time()

                if data == "LEFT":
                    simulate_key_press(KEY_LEFT)
                    last_direction = "LEFT"
                    last_press_time = current_time
                elif data == "RIGHT":
                    simulate_key_press(KEY_RIGHT)
                    last_direction = "RIGHT"
                    last_press_time = current_time
                elif data == "UP":
                    simulate_key_press(KEY_UP)
                    last_direction = "UP"
                    last_press_time = current_time
                elif data == "DOWN":
                    simulate_key_press(KEY_DOWN)
                    last_direction = "DOWN"
                    last_press_time = current_time
                elif data == "PRESS":
                    simulate_key_press(KEY_PLAY_PAUSE)
                    last_direction = "PRESS"
                    last_press_time = current_time

            except UnicodeDecodeError:
                print("Error decoding serial data.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        time.sleep(0.01)

except serial.SerialException as e:
    print(f"Error opening serial port {SERIAL_PORT}: {e}")
except KeyboardInterrupt:
    print("\nScript stopped by user.")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serial port closed.")
