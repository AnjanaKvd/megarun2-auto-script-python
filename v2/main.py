from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
if len(devices) == 0:
    print('No device attached')

device = devices[0]

def capture_screen():
    image = device.screencap()
    return image

def save_screen(image):
    with open(f'images/screen.png', 'wb') as f:
        f.write(image)

def main():
    while True:
        image = capture_screen()
        save_screen(image)