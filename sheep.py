import requests

# 刷取类型 1 是话题 2 是羊群 默认羊群
rank_state = 2
# 过关时间默认是 5 分钟 所以（5 * 60） 可修改为 1
rank_time = 5*60

# 小程序OpenId
openId = "xxxxxxxxxxxxxxxxxxxxxxx"

# 通过OpenId 生成Token
res = requests.post(url="https://cat-match.easygame2021.com/sheep/v1/user/login_oppo", json={
    "uid": openId,
    "nick_name": "baidu",
    "avatar": "https://www.baidu.com/favicon.ico",
    "sex": 1
}, headers={
    "Content-Type": "application/json",
    "Host": "cat-match.easygame2021.com",
    "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/14/page-frame.html",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_HK",
}).json()

# 直接使用Token刷 使用Token请注释上面的 生成Token
# 并注释掉 token = str(res['data']['token'])
# token="你的Token"

token = str(res['data']['token'])
res = requests.get(url=f"https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state=1&rank_time={rank_time}&rank_role={rank_state}&skin=34&t={token}", headers={
    "Content-Type": "application/json",
    "Host": "cat-match.easygame2021.com",
    "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/14/page-frame.html",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_HK",
    "T": token
}).json()

if str(res['err_code']) == "0":
    print("操作成功\r\n头像和名称已发生变化\r\n移除小程序重新登录即可正常")
else:
    print("操作失败")
