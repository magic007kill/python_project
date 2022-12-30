class A:

    def test(self):
        print("--A--test方法")

    def demo(self):
        print("--A--demo方法")


class B:

    def demo(self):
        print("--B--demo方法")

    def test(self):
        print("--B--test方法")


class C(B, A):
   # 多继承的父类中如果有名字相同的方法或属性，只能调用一个
   # 由继承的顺序决定，如上，调用的是B的方法
    pass

# 创建子类对象
c = C()
c.test()
c.demo()

# 使用C.__mro__方法来确定C类对象调用方法的顺序
print(C.__mro__)
