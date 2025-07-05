import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

PINS = [board.D7, board.D10, board.D9, board.D8, board.D0] 

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder = EncoderHandler()
encoder.pins = ((board.D3, board.D4, board.D5, False),)
keyboard.modules.append(encoder)

def handle_encoder(keyboard, encoder_index, direction):
    if direction > 0:
        keyboard.tap_key(KC.VOLU)
    else:
        keyboard.tap_key(KC.VOLD)

keyboard.encoder_handler = handle_encoder
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D, KC.LCTRL]
]

if __name__ == ‘__main__’:
    print(“hello world“)
    keyboard.go()