from PIL import Image
from ppadb.client import Client as AdbClient
from img_converter import convert
from cpp_solver_wrapper import cpp_solver


def place(x, y, digit):
    device.shell(f'input tap {92 + 111 * x} {510 + dy + 111 * y}')
    device.shell(f'input tap {79 + 116 * (digit - 1)} {2040}')


client = AdbClient(host='127.0.0.1', port=5037)
client.remote_connect('192.168.1.3', 5555)
device = client.device('192.168.1.3:5555')
result = device.screencap()

with open("screen.png", "wb") as fp:
    fp.write(result)

board, to_place, dy = convert(Image.open('screen.png'))

res = cpp_solver(board)

for i in to_place:
    place(i % 9, i // 9, res[i])
# левый верхний на картинке, правый нижний на рамке (в редакторе)
