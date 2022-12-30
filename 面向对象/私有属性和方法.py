class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，可以访问对象的私有属性
        print("%s的年龄是%d" % (self.name, self.__age))


xiaohua = Women("小花")
# 私有属性，在外界不能被直接访问
print(xiaohua.__age)
# 私有方法，同样不允许在外界访问
xiaohua.__secret()