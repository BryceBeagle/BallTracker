from time import sleep

from communication import CommunicationProtocol as com
from helpers       import robot

bot = com.Device('COM5')

def wait():
    while bot.getMoving(): sleep(.01)

base, main, scnd = robot.move(40, 130, 105)
bot.setServo(0, base)
bot.setServo(1, main)
bot.setServo(2, scnd)

# for x in range(10):
#     base, main, scnd = robot.move(-25, 150, 20)
#     bot.setServo(0, base)
#     bot.setServo(1, main)
#     bot.setServo(2, scnd)
#     sleep(1)
#     base, main, scnd = robot.move(-25, 200, 20)
#     bot.setServo(0, base)
#     bot.setServo(1, main)
#     bot.setServo(2, scnd)
#     sleep(1)
#     base, main, scnd = robot.move( 25, 200, 20)
#     bot.setServo(0, base)
#     bot.setServo(1, main)
#     bot.setServo(2, scnd)
#     sleep(1)
#     base, main, scnd = robot.move( 25, 150, 20)
#     bot.setServo(0, base)
#     bot.setServo(1, main)
#     bot.setServo(2, scnd)
#     sleep(1)