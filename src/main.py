from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt


# 已知量
omega1 = 10
l1 = 50
l2 = 150
l3 = 150
l4 = 200
theta1 = 0.01


if __name__ == "__main__":
    # 根据theta1计算出theta2和theta3
    resTheta2 = []
    resTheta3 = []
    resTheta1 = []

    def func1(x):
        return [
            l1*np.cos(theta1)+l2*np.cos(x[0])-l3*np.cos(x[1])-l4,
            l1*np.sin(theta1)+l2*np.sin(x[0])-l3*np.sin(x[1])
        ]
        pass

    while theta1 < np.pi*2:
        root = fsolve(func1, [0, 0])
        if root[0] > 3 or root[1] > 3:
            theta1 += 0.01
            continue
        elif theta1 <= np.pi:
            resTheta2.append(root[0])
            resTheta3.append(root[1])
            pass
        elif theta1 > np.pi:
            resTheta3.append(np.pi+root[0])
            resTheta2.append(np.pi+root[1])
            pass
        resTheta1.append(theta1)
        theta1 += 0.01
        pass
    plt.scatter(resTheta1, resTheta2)
    plt.scatter(resTheta1, resTheta3)
    plt.show()

    # 速度分析：根据 theta2 和 theta3 计算 omega2 和 omega3

    resOmega2 = []
    resOmega3 = []
    for i in range(len(resTheta1)):

        def func2(x):
            return [
                x[0]*l2*np.cos(resTheta2[i])
                + omega1*l1 * np.cos(theta1)
                - x[1]*l3*np.cos(resTheta3[i]),

                omega1*l1 * np.sin(theta1)
                + x[0]*l2*np.sin(resTheta2[i])
                - x[1]*l3*np.sin(resTheta3[i])
            ]
            pass

        root = fsolve(func2, [0, 0])
        resOmega2.append(root[0])
        resOmega3.append(root[1])
        pass
    plt.scatter(resTheta1, resOmega2)
    plt.scatter(resTheta1, resOmega3)
    plt.show()

    # 加速度分析：根据 theta2, theta3, omega2, omega3 计算 alpha2, alpha3
    pass
