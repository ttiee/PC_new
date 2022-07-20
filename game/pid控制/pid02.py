from pid_class import PID

import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline, make_interp_spline


def test_pid():
    # PID中的超参数
    P = 1.2
    I = 1
    D = 0.001
    # 循环次数
    L = 50
    pid = PID(P, I, D)
    pid.SetPoint = 0.0
    pid.sample_time = 0.01

    feedback = 0

    feedback_list = []
    time_list = []
    setpoint_list = []
    for i in range(1, L):
        pid.update(feedback)
        output = pid.output

        if pid.SetPoint > 0:
            # 更新feedback
            feedback += (output - (1 / i))

            # 目前只是为了观察
        if i > 9:
            pid.SetPoint = 1

        if i > 30:
            pid.SetPoint = 1.2

        time.sleep(0.02)

        # 为了绘制曲线，记录相应的数值
        feedback_list.append(feedback)
        setpoint_list.append(pid.SetPoint)
        time_list.append(i)

    time_sm = np.array(time_list)
    # 在指定的间隔内返回均匀间隔的数字
    time_smooth = np.linspace(time_sm.min(), time_sm.max(), 300)
    # 拟合一条曲线 - 拟合后，曲线才能绘制出来
    feedback_smooth = make_interp_spline(time_list, feedback_list)(time_smooth)

    plt.plot(time_smooth, feedback_smooth, color='r')
    # 拟合目标变化句
    plt.plot(time_list, setpoint_list, color='b')
    plt.xlim((0, L))
    plt.ylim((min(feedback_list) - 0.5, max(feedback_list) + 0.5))
    plt.xlabel('time (s)')
    plt.ylabel('PID')
    plt.title('TEST PID')

    plt.ylim((1 - 0.5, 1 + 0.5))

    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    test_pid()