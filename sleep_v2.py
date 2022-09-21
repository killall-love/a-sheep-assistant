import struct
import base64
import random
import urllib3
import requests

# 初始化 requests
session = requests.session()
session.headers = {
    "content-type": "application/json;charset=utf-8",
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
# 移除Https警告
urllib3.disable_warnings()

# 刷取类型 1 是话题 2 是羊群 默认羊群
rank_state = 2
# 过关时间默认是 5 分钟 所以（5 * 60） 可修改为 1
rank_time = 5*60
# 请输入你刷取的次数
nums = 10
# 请输入你的Token
token = ""


# 获取getMatchPlayInfo参数


def getMatchPlayInfo(token):
    url = f'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?t={token}'
    session.get(url)
    url = f'https://cat-match.easygame2021.com/sheep/v1/game/map_info_ex?matchType=3&t={token}'
    res = session.get(url)
    map_md5 = res.json()['data']['map_md5'][1]
    res = requests.get(
        url=f"https://cat-match-static.easygame2021.com/maps/{map_md5}.txt", verify=False).json()
    levelData = res['levelData']
    p = []
    for h in range(len(sum(levelData.values(), []))):  # 生成操作序列
        p.append({'chessIndex': 127 if h > 127 else h,
                 'timeTag': 127 if h > 127 else h})
    data = struct.pack('BB', 8, 3)
    for i in p:
        c, t = i.values()
        data += struct.pack('BBBBBB', 34, 4, 8, c, 16, t)
    return base64.b64encode(data)


# 羊群模式
def game_over_ex(i):
    res = session.get(
        url=f"https://cat-match.easygame2021.com/sheep/v1/game/update_user_skin?skin=1&t={token}", verify=False).json()
    if str(res['err_code']) == "0":
        print(f"羊群数量操作成功\r\n操作次数：{i + 1}")
    else:
        print(f"羊群数量操作失败\r\n操作次数：{i + 1}")
# 话题模式


def topic_game_over(i):
    res = session.get(
        url=f"https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over?rank_score=1&rank_state=1&rank_time={rank_time}&rank_role={rank_state}&skin=1&t={token}", verify=False).json()
    if str(res['err_code']) == "0":
        print(f"话题数量操作成功\r\n操作次数：{i + 1}")
    else:
        print(f"话题数量操作失败\r\n操作次数：{i + 1}")


# 第一次刷取


def first():
    res = session.post(url=f"https://cat-match.easygame2021.com/sheep/v1/game/game_over_ex?t={token}", json={
        "rank_score": 1,
        "rank_state": 1,
        "rank_time": rank_time + random.randint(20, 80),
        "rank_role": 1,
        "skin": 1,
        "MatchPlayInfo": str(getMatchPlayInfo(token))
    }, verify=False).json()
    return str(res['err_code']) == "0"

# 批量操作


def batch():
    for i in range(nums):
        try:
            game_over_ex(i) if rank_state == 2 else topic_game_over(i)
        except Exception as e:
            print(f"{ '羊群数量' if rank_state == 2 else '话题数量' }操作失败\r\n操作次数：{i + 1}")

# 游戏结束后


def game_over_data():
    url = f'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?t={token}'
    res = session.get(url).json()
    if str(res['err_code']) == "0" and res['data']['today_state'] == 1:
        print(
            f"\r\n\r\n操作成功\r\n羊群：{d_c_old} -----  {res['data']['daily_count']}\r\n话题：{t_c_old} -----  {res['data']['topic_count']}")
    else:
        print(f"数据操作失败")


if __name__ == '__main__':
    # 获取基础参数
    url = f'https://cat-match.easygame2021.com/sheep/v1/game/personal_info?t={token}'
    res = session.get(url).json()
    d_c_old = res['data']['daily_count']
    t_c_old = res['data']['topic_count']
    if str(res['err_code']) == "0" and res['data']['today_state'] == 1:
        print(f"当前用户\r\n羊群：{d_c_old}\r\n话题：{t_c_old}\r\n\r\n")
        if first():
            batch()
    else:
        print("数据操作失败")

    game_over_data()

    
    
# 当前用户
# 羊群：65834
# 话题：19393


# 羊群数量操作成功
# 操作次数：1
# 羊群数量操作成功
# 操作次数：2
# 羊群数量操作成功
# 操作次数：3
# 羊群数量操作成功
# 操作次数：4
# 羊群数量操作成功
# 操作次数：5
# 羊群数量操作成功
# 操作次数：6
# 羊群数量操作成功
# 操作次数：7
# 羊群数量操作成功
# 操作次数：8
# 羊群数量操作成功
# 操作次数：9
# 羊群数量操作成功
# 操作次数：10


# 操作成功
# 羊群：65834 -----  65844
# 话题：19393 -----  19393
    
    
    
    
    
    
    
    
    
    
