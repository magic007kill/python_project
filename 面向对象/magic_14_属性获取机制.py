class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象地数量
    count = 0

    def __init__(self, name):
        self.name = name
        # 让类属性地值加1
        Tool.count += 1


# 1.创建工具对象
tool1 = Tool("锤子")
tool2 = Tool("扳手")
tool3 = Tool("改锥")
# 2.输出工具对象地总数
# print(Tool.count)，推荐使用——类名.属性这种方式
print("工具对象总数%d" % tool2.count)