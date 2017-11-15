class Student(object): # 类名的括号里写继承的类，如果没有则写object，这是所有类都要继承的类

    school = '清华大学' # 直接在类中定义的属性为类属性，归Student类所有，所有实例都可以访问到，但是与java的静态变量不同，如果一个实例改变了school的值，那么这个新值就生效，且只对这一个实例生效

    def __init__(self, name, score): # 只要是class中定义的函数，第一个参数都要写self，并且调用时第一个参数都不必传
                                     # __init__ 是特殊函数，在创建类时会调用，相当于java的构造函数
        self.__name = name # 可以直接self.新的变量名，注意，两个下划线开头的变量名为私有变量，不允许外部访问，但可以通过get和set方法访问和赋值
        self.__score = score # 以两个下划线开头且以两个下划线结尾的变量为特殊变量，特殊变量不是私有变量，允许外部访问，因此起变量名时不要起成这种特殊变量的格式

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score') # 手动抛出异常

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 61) # 会自动调用 __init__ 函数，第一个self不必传，剩下的两个参数都要传
print('bart.get_name() =', bart.get_name())
bart.set_score(64)
print('bart.get_score() =', bart.get_score())
print('DO NOT use bart._Student__name:', bart._Student__name) # 之所以说 __name 是私有变量，是因为python将私有变量自动重命名为 _Student__name，因此 bart.__name 是获取不到的。
                                                              # 但是不同的python版本可能重命名的格式不同，因此强烈建议不要这么读取。
bart.__name = 'New Name'
print('bart.get_name()=',bart.get_name()) # bart.__name 赋值的其实不是私有变量，因为私有变量已经被重命名，因此这是新建的一个变量，所以 get_name() 方法的返回结果仍然不变。

bart2 = Student('Tian Rong', 100)
bart2.school = '北京大学'  # school 是类变量，但是bart2这个实例对类变量进行了赋值，则相当于新建了一个school变量
print('bart2.school=',bart2.school) # 实例属性优先级比类属性高，因此会输出新值
print('bart.school=',bart.school)  # 因为bart2.school是一个新的变量，因此bart的类变量不会受其影响，值不变
print('Student.school=',Student.school) # 类属性不会被任何实例所影响，值不变
del bart2.school # 将bart2的实例变量删掉，则再次访问 bart2.school，则访问的是类变量
print('bart2.school=',bart2.school)