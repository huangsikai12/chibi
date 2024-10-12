import sys

import Constants
from DataAction import getHd

# Designed by 黄斯恺
def setData():
    Constants.JSESSIONID = input("请输入 JSESSIONID: ")
    Constants.HD_ID = input("请输入要抢的活动ID：")

if __name__ == "__main__":
    try:
        setData()
    except:
        print("\n程序退出！")
        sys.exit()
    getHd()
