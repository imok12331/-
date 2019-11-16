import numpy as np
try:
    aims = int(input('请输入月度目标：'))
    ideal = int(input('请输入昨日本月理论达成：'))
    true = int(input('请输入昨日本月实际达成：'))
except ValueError:
    print('要输入数字哦！——来自亲爱的路的提醒')
    exit()
A = [aims,ideal,true]
np.save('out',A)
print('校正完成，请运行magical.py\n输入以下命令 python magical.py')