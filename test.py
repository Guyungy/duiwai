import requests

# 你的飞书 API 认证信息
APP_ID = "cli_a7254e9691fb500d"
APP_SECRET = "lXcKvOnSaXLew8DrroqLwd6NGY3f225h"
APP_TOKEN = "Lht8biN7Bawz7UsGJupcXDBKnDd"
TABLE_ID = "tblFx5LyEsmiaJ9C"

# 获取 tenant_access_token
def get_tenant_access_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    headers = {"Content-Type": "application/json"}
    data = {"app_id": APP_ID, "app_secret": APP_SECRET}
    response = requests.post(url, json=data, headers=headers)
    return response.json().get("tenant_access_token")

# 添加记录
def add_record():
    token = get_tenant_access_token()
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/tables/{TABLE_ID}/records"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json; charset=utf-8"
    }

    # 这里是你要添加的数据
    payload = {
        "fields": {
            "描述": "测试描述内容",
            "标签": ["科技", "新闻"],  # 多选字段
            "发布时间": 1674206443000,  # 毫秒级时间戳
            "URL": {"text": "测试链接", "link": "https://example.com"},
            "点赞": 100,  # 数字字段
            "收藏": 50,
            "转发": 10,
            "文案": "这是一段测试文案"
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    print("新增记录返回:", response.json())

# 运行新增记录
add_record()
