import board
import analogio
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time

# --- Configuration ---
joy_x = analogio.AnalogIn(board.GP26) # Physical Pin 31
joy_y = analogio.AnalogIn(board.GP27) # Physical Pin 32
joy_button = digitalio.DigitalInOut(board.GP17) # Physical Pin 22
joy_button.direction = digitalio.Direction.INPUT
joy_button.pull = digitalio.Pull.UP # Internal pull-up for the button

keyboard = Keyboard(usb_hid.devices)

# Threshold for joystick movement (adjust based on your observation by debugging, 0-65535 range)
THRESHOLD_ANALOG = 10000 # Start with a larger dead zone (e.g., 10000-15000)
CENTER_ANALOG = 32767

# Debounce for button
BUTTON_DEBOUNCE_MS = 250 # For faster game response, try 50-100ms

# --- State Variables for Continuous Hold ---
# Keep track of which key is currently being held down by the joystick movements
currently_pressed_movement_key = None
last_button_press_time = 0

print("Starting Continuous Hold YouTube/Game Controller...")
print(f"Initial THRESHOLD_ANALOG: {THRESHOLD_ANALOG}, CENTER_ANALOG: {CENTER_ANALOG}")

while True:
    x_val = joy_x.value
    y_val = joy_y.value
    button_pressed = not joy_button.value

    current_time_ms = time.monotonic_ns() // 1_000_000

    # --- Determine current joystick action ---
    action_key_to_press = None

    if x_val < (CENTER_ANALOG - THRESHOLD_ANALOG):
        action_key_to_press = Keycode.LEFT_ARROW
    elif x_val > (CENTER_ANALOG + THRESHOLD_ANALOG):
        action_key_to_press = Keycode.RIGHT_ARROW
    elif y_val < (CENTER_ANALOG - THRESHOLD_ANALOG):
        action_key_to_press = Keycode.UP_ARROW # For games, you might want Keycode.PAGE_UP or specific keys
    elif y_val > (CENTER_ANALOG + THRESHOLD_ANALOG):
        action_key_to_press = Keycode.DOWN_ARROW # For games, you might want Keycode.PAGE_DOWN or specific keys

    # --- Handle Key Press/Release for Movement ---
    if action_key_to_press != currently_pressed_movement_key:
        # If a new movement key should be pressed, or joystick moved to center (None)
        if currently_pressed_movement_key is not None:
            # Release the old key if one was held
            keyboard.release(currently_pressed_movement_key)
            print(f"Released: {currently_pressed_movement_key}")
        
        if action_key_to_press is not None:
            # Press the new key
            keyboard.press(action_key_to_press)
            print(f"Pressed: {action_key_to_press}")
        
        currently_pressed_movement_key = action_key_to_press

    # --- Joystick Button (Center Press) ---
    if button_pressed and (current_time_ms - last_button_press_time > BUTTON_DEBOUNCE_MS):
        keyboard.press(Keycode.SPACE) # Spacebar for Play/Pause in YouTube, or Jump/Action in games
        keyboard.release(Keycode.SPACE)
        last_button_press_time = current_time_ms
        print("PRESS (Button)")

    # Small delay to prevent busy-waiting and reduce CPU usage
    time.sleep(0.01) # 10 milliseconds, controls how often the loop checks
