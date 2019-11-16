import datetime
import numpy as np

Week = datetime.datetime.now().isoweekday()
M = datetime.datetime.now().month
D = datetime.datetime.now().day
if D == 1:
    aims = float(input('请更新月目标'))
    sche = 0 #月达成归零
    A = [aims,0,0]
    np.save('out',A)
#[月度目标，理论月度达成，实际月度达成]
[aims,ideal,true] = np.load('out.npy')
print('请核对下列数字是否正确\n月度目标:{} 昨日理论达成:{} 昨日实际达成:{}\n如果正确请继续，错误请退出'.format(aim, ideal, true))

try:
    num1 = int(input('请输入今日营业额：'))
    num2 = float(input('请输入上周今日营业额：'))
    num3 = float(input('请输入今日目标：'))
    num4 = float(input('请输入今日转换率：'))
    num5 = float(input('请输入昨日转换率：'))
    num6 = int(input('请输入客流：'))
    num7 = int(input('请输入客单价：'))
except ValueError:
    print('要输入数字哦！——来自亲爱的路的提醒')
    exit()   
#开始计算
true = num1+true #月至今实际营业额
ideal = ideal+num3 #月至今理论营业额
result1 = num1/num3-1 #营业额VS目标
result2 = num1/num2-1 #周环比
result3 = num4-num5 #转换率日环比
result4 = true/aims #月至今达成率
result5= (true-ideal)/aims #月营业额VS目标
A = [aims,ideal,true]
np.save('out',A)
[aims,ideal,true] = np.load('out.npy')
print('请核对下列数字是否正确\n月度目标:{} 今日理论达成:{} 今日实际达成:{}\n如果正确请继续，错误请退出'.format(aim, ideal, true))
print('武汉南国泛悦汇\n{}.{} 星期{}\n营业额：{}\nVS目标：{:.0%}\n转化率：{:.0%}、环比昨日{:.0%}\n客流：{}\n客单价：{}\n月至今营业额：{}\nVS目标：{:.0%}\n月至今达成率：{:.0%}\n上周：{}、周环比：{:.0%}'.format(M, D, Week, num1, result1, num4, result3, num6, num7, true, result5, result4, num2, result2))