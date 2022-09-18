# a-sheep-assistant
羊了个羊助手，羊了个羊一键闯关，本项目仅用于学习研究使用，请勿将本项目的任何内容用于商业或非法目的，否则后果自负。

### 支持小程序 Token刷取
#### token是抓取后直接提交
### 支持小程序 openid刷取
#### openId是生成Token实现刷取

### 支持小程序 uid刷取
*****2022年09月17日*****
#### uid生成openId -> openId通过（oppo/~~ios~~ 设备接口）生成Token实现刷取 （uid理论抖音和微信通刷）
*****2022年09月18日*****
#### ~~IOS 接口废弃~~
刷取完成后 昵称会默认显示 '默认用户' 移除小程序 重新进入 即可恢复

# 原理分享
## 首先UID是内部维护的一个id
## openid是第三方平台登录的标识

### uid获取token实际上是通过user_info接口获取用户信息，里面包含了openid
### 在通过OPPO/~~iOS~~的设备登录方式 通过openid登录获取Token
### 获取token就直接刷了

## 刷接口需要token 登录不需要token uid获取openid的token哪里来?
### 程序的一个bug把 通过自己的token可以获取任何人的用户信息 是不是很意外
### 比如A用户的Token B用户的uid 
#### 使用A的token获取b的信息 在任何层面这都是不通的 不应该能获取的
### 可笑的是他是可以的 所以这一切就串起来了

###### 用自己的token和别人的uid获取别人的openid 
###### 在通过渠道登录接口通过openid实现登录
###### 然后获取token实现刷次数


