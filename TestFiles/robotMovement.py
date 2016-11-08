from time import sleep

from communication import CommunicationProtocol as com

robot = com.Device('COM5')

def wait():
    while robot.getMoving(): sleep(.01)

while True:
    robot.setXYZ(-2.5, 15, 8, 500)
    sleep(1)
    robot.setXYZ(-2.5, 20, 8, 500)
    sleep(1)
    robot.setXYZ( 2.5, 20, 8, 500)
    sleep(1)
    robot.setXYZ( 2.5, 15, 8, 500)
    sleep(1)
