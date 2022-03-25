# coding=utf-8


class Account:
    __interest_rate = 0.0668  # 类变量利率__interest_rate

    def __init__(self, owner, amount):
        self.owner = owner  # 公有实例变量owner
        self.__amount = amount  # 私有实例变量__amount

    # 类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.__interest_rate * amt

    def __get_info(self):
        return "{0} 金额:{1} 利率:{2}。".format(self.owner, self.__amount, Account.__interest_rate)

    def desc(self):
        print(self.__get_info())


interest = Account.interest_by(12000.0)  # 类方法可通过"类名.类方法"形式访问
print('计算利息:{0:.4f}'.format(interest))
# print('利率:{0}'.format(Account.__interest_rate))
account = Account('Tony', 800000.0)
account.interest_by(800000)
account.desc()
