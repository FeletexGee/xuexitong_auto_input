#-*-coding:utf-8-*-#
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()
#读入文件，完成读取后立即释放文件I/O流
with open('input.in','r',-1,'utf-8') as file:
    input_data=file.read()
#选择速率
indicate=True
while (indicate==True):
    speed_arg=int(input("选择速率（输入数字编号）：\n1-正常速率\n2-快速\n3-极速"))
    if (speed_arg==1):
        interval=0.1
        indicate=False
    elif (speed_arg==2):
        interval=0.05
        indicate=False
    elif (speed_arg==3):
        interval=0.01
        indicate=False
    else:
        print("非法参数!请重新输入")
#警告信息
for i in range(5,0,-1):
    print("还有",i,"秒开始模拟输入，请完成窗口切换。")
    time.sleep(1)
#愉快输入
time_start=time.time()
for j in range(0,len(input_data)+1):
    time.sleep(interval)
    keyboard.type(input_data[j:j+1])
time_end=time.time()
print("输入任务结束，耗时"+"{:3}".format((time_end-time_start))+"秒")