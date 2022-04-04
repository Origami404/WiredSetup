import mitmproxy.http
from mitmproxy import ctx

# 辅助变量: 需要修改的 HTTP 响应的 MIME 类型
target_mime = {
    'text/html', 'text/javascript', 
    'text/css', 'application/json',
    'application/javascript',
}


# 辅助变量: 需要替换的字符串
replacements = {
    b'http://10.1.1.1:9000': b'https://ak.origami404.top',
    b'http://10.1.1.1:9001': b'https://ak.origami404.top/api',
}


# 辅助函数: 根据 MIME 头判断是否应该修改这个响应 
def is_proper_mime(ct: str) -> bool:
    # 有些框架的 MIME 类型会类似这样: "text/css; charset=utf-8"
    # 所以需要做下面的处理
    return ct.split(';')[0] in target_mime


# Addon 的主体部分, 定义了当发生特点事件时动作
class Interceptor:
    # 当 mitmproxy 拦截到一个响应时
    def response(self, flow: mitmproxy.http.HTTPFlow):
        # 获得响应本身
        response = flow.response
        if not response:
            return

        # 根据响应的 MIME 头先筛选一次, 防止脚本对很多 jpg/png 等二进制文件也做替换
        if ct := response.headers['Content-Type']:
            if is_proper_mime(ct) and response.content:
                # 依次修改想要修改的字符串
                for old, new in replacements.items():
                    response.content = response.content.replace(old, new)


# 注册 Interceptor
addons = [ Interceptor() ]