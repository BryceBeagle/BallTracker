from scipy.optimize import fsolve
import math
import numpy as np

def move(x, y, z):

    z += 40

    if y == 0: theta1 = math.copysign(90, x)
    else:      theta1 = math.degrees(math.atan(x / y))

    # x -= 34.788 * math.sin(theta1)
    # y -= 34.788 * math.cos(theta1)

    print(x, y)

    a1 = 89.214
    a2 = 148
    a3 = 160
    a4 = 20.3
    a5 = 35

    # m      = horizontal length of extension after taking angle into account
    # q      = distance from p(theta2) to end effector
    # phi    = angle    from p(theta2) to end effector
    # theta2 = angle of first arm above horizontal
    # theta3 = angle of second arm below horizontal

    m     = math.sqrt(x**2 + y**2) - (a4 + a5)
    q     = math.sqrt(m**2 + (z - a1)**2)

    alpha = math.acos((a3**2 - a2**2 - q**2) / (-2 * a2 * q))
    phi   = math.atan((z - a1) / m)

    theta2 = alpha + phi
    theta3 = math.degrees(math.acos((m - a2 * math.cos(theta2)) / a3))
    theta2 = math.degrees(theta2)

    print(theta1)
    print(theta2)
    print(theta3)

    # if theta1 == -90: base = 180
    # else:             base = (90 - theta1) % 180

    base = 90 - ((.0005 * theta1**2) + (0.9212*theta1) + 3.3804)
    main = (theta2 + 20) % 180
    scnd =  theta3       % 180

    # base *= .95
    #
    # print(base)
    # print(main)
    # print(scnd)

    return base, main, scnd