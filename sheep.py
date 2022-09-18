import requests

# 初始化 requests
session = requests.session()
session.headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Host": "cat-match.easygame2021.com",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_HK",
}

# 刷取类型 1 是话题 2 是羊群 默认羊群
rank_state = 2
# 过关时间默认是 5 分钟 所以（5 * 60） 可修改为 1
rank_time = 5*60
# 请输入你刷取的次数
nums = 1

# 请输入你的游戏UID
uid = ""

# ***********************UID**START****************************

res = session.get(
    url=f"https://cat-match.easygame2021.com/sheep/v1/game/user_info?uid={uid}&t=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ0NzgwMTAsIm5iZiI6MTY2MzM3NTgxMCwiaWF0IjoxNjYzMzc0MDEwLCJqdGkiOiJDTTpjYXRfbWF0Y2g6bHQxMjM0NTYiLCJvcGVuX2lkIjoiIiwidWlkIjo0ODUwNDY1MCwiZGVidWciOiIiLCJsYW5nIjoiIn0.IEjNoHJiJPqlh86DqDS3-SMTwErTCatQF6ykZk4o-Yc", verify=False).json()
openId = res['data']['wx_open_id']
nick_name = res['data']['nick_name']
avatar = res['data']['avatar']
# ***********************UID**END****************************

# 小程序OpenId
# 如果想使用 openId 刷取 请注释  UID**START -> UID**END 并取消注释  （ # openId = "xxxxxxxxxxxxxxxxxxxxxxx" ）
# openId = "xxxxxxxxxxxxxxxxxxxxxxx"

# 两种方式获取 openId -> token

# 方式一
# 通过OpenId 生成Token  OPPO 手机

# ***********************生成Token**START****************************
res = session.post(url="https://cat-match.easygame2021.com/sheep/v1/user/login_oppo", json={
    "uid": openId,
    "nick_name": nick_name,
    "avatar": avatar,
    "sex": 1
}).json()
token = str(res['data']['token'])
# ***********************生成Token**END****************************

# 方式二 （2022-09-18 已废弃）
# 通过OpenId 生成Token  IOS 设备

# ***********************生成Token**START****************************
# 
# res = session.post(url="https://cat-match.easygame2021.com/sheep/v1/user/login_tourist", verify=False, json={
#     "uuid": openId,
# }).json()
# token = str(res['data']['token'])
# ***********************生成Token**END****************************

# 直接使用Token刷 使用Token请注释上面的 生成Token
# 并注释掉 token = str(res['data']['token'])
# 如果想使用 Token刷取 请注释  生成Token**START -> 生成Token**END 并取消注释  （ # token="你的Token" ）
# token="你的Token"

for i in range(nums):
    try:
        res = session.get(
            url=f"https://cat-match.easygame2021.com/sheep/v1/game/{'game_over' if rank_state == 2 else 'topic_game_over'}?rank_score=1&rank_state=1&rank_time={rank_time}&rank_role={rank_state}&skin=1&t={token}", verify=False).json()
        if str(res['err_code']) == "0":
            print(f"{ '羊群数量' if rank_state == 2 else '话题数量' }操作成功\r\n操作次数：{i + 1}")
        else:
            print(f"{ '羊群数量' if rank_state == 2 else '话题数量' }操作失败\r\n操作次数：{i + 1}")
    except Exception as e:
        print(f"{ '羊群数量' if rank_state == 2 else '话题数量' }操作失败\r\n操作次数：{i + 1}")
