import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

if_input_x_y = 0
if if_input_x_y:
    x_name = input()
    y_name = input()
else:
    x_name = "T"
    y_name = "R_{T}"

# 生成随机数据
np.random.seed(0)
x = np.array([17.8, 26.9, 37.7, 48.2, 58.8, 69.3])#np.linspace(0, 10, 100)
y = np.array([3.554, 3.687, 3.827, 3.969, 4.105, 4.246])#2 * x + 1 + np.random.normal(0, 2, 100)

# 计算线性回归
# 斜率，截距，R值，P值，错误
slope, intercept, r_value, p_value, std_err = linregress(x, y)

# 计算过程量
x_sum = np.sum(x) # x的和
x_mean = np.mean(x) # x的平均值
x_squared_sum = np.sum(x**2) # x的平方和
x_squared_mean = np.mean(x**2) # x的平方平均值
x_delta_squared_sum = np.sum((x-x_mean)**2) # x与平均值的差距的平方和
x_variance_sample = np.var(x, ddof=1) # 样本方差
x_dev_sample = np.std(x, ddof=1) # 样本标准差
#总体方差，总体标准差

y_sum = np.sum(y)
y_mean = np.mean(y)
y_squared_sum = np.sum(y**2)
y_squared_mean = np.mean(y**2)
y_delta_squared_sum = np.sum((y-y_mean)**2)
y_variance_sample = np.var(y, ddof=1) # 样本方差
y_dev_sample = np.std(y, ddof=1) # 样本标准差

x_mul_y_mean = np.mean(x * y) # xy的平均值

#x相关
print("-------------------------x相关---------------------------")
print(f"∑x:\n   \\sum_{{i=1}}^{{n}}{x_name} = {x_sum}")
print(f"x的平均数:\n  \\overline{{{x_name}}} = {x_mean}")
print(f"∑(x^2):\n  \\sum_{{i=1}}^{{n}}{x_name}^2 = {x_squared_sum}")
print(f"x 的平方平均数:\n  \\overline{{{x_name}^2}} = {x_squared_mean}")
print(f"∑(Δx^2):\n  \\sum_{{i=1}}^{{n}}\\Delta {x_name}^2 = {x_delta_squared_sum}")
print(f"x的样本方差:\n  \\sigma_{{{x_name}}} = \\frac{{\\sum_{{i=1}}^{{n}}\\Delta {x_name}^2}}{{n-1}} = {x_dev_sample}")
print(f"x的样本标准差:\n  \\sigma_{{{x_name}}} = \\sqrt{{\\frac{{\\sum_{{i=1}}^{{n}}\\Delta {x_name}^2}}{{n-1}}}} = {x_dev_sample}")

#y相关
print("-------------------------y相关---------------------------")
print(f"∑y:\n  \\sum_{{i=1}}^{{n}}{y_name} = {y_sum}")
print(f"y的平均数:\n  \\overline{{{y_name}}} = {y_mean}")
print(f"∑(y^2):\n  \\sum_{{i=1}}^{{n}}{y_name}^2 = {y_squared_sum}")
print(f"y 的平方平均数:\n  \\overline{{{y_name}^2}} = {y_squared_mean}")
print(f"∑(Δy^2):\n  \\sum_{{i=1}}^{{n}}\\Delta {y_name}^2 = {y_delta_squared_sum}")
print(f"y的样本方差:\n  \\sigma_{{{y_name}}} = \\frac{{\\sum_{{i=1}}^{{n}}\\Delta {y_name}^2}}{{n-1}} = {y_dev_sample}")
print(f"y的样本标准差:\n  \\sigma_{{{y_name}}} = \\sqrt{{\\frac{{\\sum_{{i=1}}^{{n}}\\Delta {y_name}^2}}{{n-1}}}} = {y_dev_sample}")

#xy相关
print("-------------------------xy相关---------------------------")
print(f"xy的平均数:\n  \\overline{{{x_name}{y_name}}} = {x_mul_y_mean}")

# 输出线性回归的参数
print("-----------------------回归方程相关-------------------------")
print(f"斜率a:\n  a = \\frac{{\\overline{{{x_name}{y_name}}}-\\overline{{{x_name}}}\\cdot\\overline{{{y_name}}}}}{{\\overline{{{{{x_name}}}^2}}-(\\overline{{{x_name}}})^2}} = {slope}")
print(f"截距b:\n  b = \\overline{{{y_name}}}-a\\overline{{{x_name}}} = {intercept}")
print(f"相关系数R:\n  R = \\frac {{L_{{xy}}}} {{\\sqrt{{L_{{xx}}\\cdot L_{{yy}} }} }} = {r_value}")
#print(f"p 值 (p_value): {p_value}")
#print(f"标准误差 (std_err): {std_err}")

# 输出回归方程
print(f"回归方程:\n  {y_name} = {slope:.6f}{x_name} + {intercept:.6f}")

# 绘制数据和回归直线
plt.scatter(x, y, label='data') # scatter: 散开，散布
plt.plot(x, slope * x + intercept, color='red', label='Regression Line') # plot: 绘制(曲线)
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.legend() # legend: 图例
plt.title('linregress')
plt.show()