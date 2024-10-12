import Constants
from DataAction import getHd


def setData():
    Constants.JSESSIONID = input("请输入 JSESSIONID: ")
    Constants.HD_ID = input("请输入要抢的活动ID：")


if __name__ == "__main__":
    setData()
    getHd()
