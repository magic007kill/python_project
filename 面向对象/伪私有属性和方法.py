class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，可以访问对象的私有属性
        print("%s的年龄是%d" % (self.name, self.__age))


xiaohua = Women("小花")
# 伪私有属性，可以如下访问
print(xiaohua._Women__age)
# 伪私有方法，可以如下访问
xiaohua._Women__secret()