import time


class PID:
    """
    PID算法实现
    """

    def __init__(self, P=0.2, I=0.0, D=0.0, current_time=None):
        """
        :param P: P算法超参数
        :param I: I算法超参数
        :param D: D算法超参数
        :param current_time: 当前时刻
        """

        self.Kp = P
        self.Ki = I
        self.Kd = D

        # 采样时间段
        self.sample_time = 0.00
        self.current_time = current_time if current_time is not None else time.time()
        self.last_time = self.current_time

        self.clear()

    def clear(self):
        """
        清理系数
        """
        self.SetPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0

        self.int_error = 0.0
        # 最大的波动值
        self.I_max_modify = 20.0

        self.output = 0.0

    def update(self, feedback_value, current_time=None):
        """
        math::
             u(k) = K_pe_k + K_i\sum_{j=0}^ke(j)\Delta t + K_d\frac{e(k) - e(k-1)}{\Delta t}
        """
        # 误差
        error = self.SetPoint - feedback_value

        self.current_time = current_time if current_time is not None else time.time()
        # 间隔时间
        delta_time = self.current_time - self.last_time

        if delta_time >= self.sample_time:
            self.ITerm += error * delta_time

            # 限制积分项ITerm最大与最小值
            if (self.ITerm < -self.I_max_modify):
                self.ITerm = -self.I_max_modify
            elif (self.ITerm > self.I_max_modify):
                self.ITerm = self.I_max_modify

            self.DTerm = 0.0

            if delta_time > 0:
                self.DTerm = (error - self.last_error) / delta_time

            # 更新时间
            self.last_time = self.current_time
            self.last_error = error
            # PID结果
            self.output = (self.Kp * error) + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)