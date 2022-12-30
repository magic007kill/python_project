class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象地数量
    count = 0

    @ classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d" % cls.count)

    def __init__(self, name):
        self.name = name
        # 让类属性地值加1
        Tool.count += 1



# 1.创建工具对象
tool1 = Tool("锤子")
tool2 = Tool("扳手")
tool3 = Tool("改锥")
# 2.输出工具对象地总数
Tool.show_tool_count()
