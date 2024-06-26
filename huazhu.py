"""
new Env("微信小程序-华住签到")
cron 0 7 * * *
环境变量名称 huazhu_cookies

仅用于测试和学习研究，禁止用于商业用途，不能保证其合法性，准确性，完整性和有效性，请根据情况自行判断；您必须在下载后的24小时内从计算机或手机中完全删除以上内容。
如果任何单位或个人认为该项目的脚本可能涉嫌侵犯其权利，则应及时通知并提供身份证明，所有权证明，我们将在收到认证文件后删除相关脚本。
"""

import datetime
import json
import traceback
import requests

import ApiRequest
import mytool
from notify import send

title = '微信小程序-华住签到'
tokenName = 'huazhu_cookies'


class huazhu(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Client-Platform': 'WEB-APP',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'DNT': '1',
            'Origin': 'https://campaign.huazhu.com',
            'Referer': 'https://campaign.huazhu.com/',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67',
            'User-Token': 'null',
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'Cookie': data,
        }

    def login(self):
        data = {
            'state': '1',
            'day': str(datetime.date.today().day),
        }
        try:
            rj = self.sec.post('https://hweb-mbf.huazhu.com/api/signIn', data=data).json()
            if rj['businessCode'] == "1000":
                msg = f"签到成功, 获得{rj['content']['point']}积分!"
            else:
                # json内容到msg
                msg = f"签到失败\n" + json.dumps(rj)
            print(msg)
            send(title, msg)
        except:
            traceback.print_exc()
            pass
        pass

if __name__ == "__main__":
    # if mytool.getlistCk(f'{tokenName}') == None:
    #     print(f'请检查你的变量名称 {tokenName} 是否填写正确')
    #     exit(0)
    # else :
    #     for i in mytool.getlistCk(f'{tokenName}'):
    #         (i).login()
    ApiRequest.ApiMain(['login']).run(tokenName, huazhu)