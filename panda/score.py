import pandas as pd
import matplotlib.pyplot as plt

# 创建示例数据
data = {
    '學號': ['001', '002', '003', '004', '005'],
    '成績': [85, 92, 78, 88, 90]
}

# 创建DataFrame对象
df = pd.DataFrame(data)

# 绘制柱状图
plt.bar(df['學號'], df['成績'])

# 设置图形标题和坐标轴标签
plt.title('學號與成績')
plt.xlabel('學號')
plt.ylabel('成績')

# 显示图形
plt.show()
