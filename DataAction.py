import time
from json import JSONDecodeError

import Constants
import RequestHelper


def addBm():
    while (True):
        getBmResult = RequestHelper.sendPostRequest(
            Constants.BASE_URL + '/ext/hd/hdfb/cn.huosoft.ek.hd.Hdbm.addBm.biz.ext')
        if getBmResult.status_code == 200:
            if getBmResult.json()['result'] == "1":
                print("报名成功！请返回二课网站查询,感谢使用！再见！")
                break
            if getBmResult.json()['result'] == "2":
                print("已经报名过当前活动！")
            elif getBmResult.json()['result'] == "4":
                print("报名人数已满！")
            elif getBmResult.json()['result'] == "5":
                print("已报名,等待主办方审核！")
            elif getBmResult.json()['result'] == "5":
                print("根据系统规则，近两个月内缺席报名活动2次（或以上），暂时禁止活动报名！")
            else:
                print("报名失败！")

        else:
            print("网络错误，正在重试！！")
    time.sleep(0.1)


def getHd():
    getHdInfor = RequestHelper.sendPostRequest(
        Constants.BASE_URL + '/ext/hd/hdfb/cn.huosoft.ek.hd.Hdfb.getHdfbsqByFbsqid.biz.ext')
    if getHdInfor.status_code == 200:
        try:
            hdInfo = getHdInfor.json()
            print('响应内容:', hdInfo)
            key = input('您要抢课的活动名称是：' + hdInfo['hdfbsq']['hdfbbt'] + "如要开始抢课请输入y:")
            if key == 'y':
                addBm()
            else:
                print("输入错误,请重新开始！")
        except KeyError:
            print("活动不存在")
        except JSONDecodeError:
            print("身份令牌失效或过期，请检查！")
        except:
            print("未知错误！")

    else:
        print(f'请求失败，状态码: {getHdInfor.status_code},请检查网络')
