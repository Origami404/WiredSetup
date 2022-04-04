# Wired Setup

通过一串奇奇怪怪的软件将位于内网的服务暴露到公网上, 适用于 HITsz 等使用深信服 VPN 的学校.

具体架构/原理参考这篇博客: [访问校内服务的错误方法]().

这是一个用作示范的仓库, 直接使用此仓库里的配置不会暴露任何校内服务至公网.

本项目使用 AGPL license 发布, 并且恳请使用者再三考虑使用其的 **安全风险**.

## 使用方法 

首先, 构建出运行所需的两个镜像:

```
docker-compose build
```

然后, 运行下面的命令登录 easyconnect 以获取真正的 `easyconn` 文件. **这个文件与你的 easy connect 账号密码具有同等效力, 请妥善保管!**

```bash
docker run --device /dev/net/tun --cap-add NET_ADMIN -ti -v "$PWD/easyconn:/root/.easyconn" -e EC_VER=7.6.3 hagb/docker-easyconnect:cli
```

随后, 在 `conf.toml` 里填写你需要转发的服务的内网网址跟端口, 支持多个服务, 只要写多块不同名字的配置就可以了.

```toml
[servers.<名字, 可以乱起>]
proxy = "socks5://easyconn:1080"  # 不用改, docker-compose 里设好的
listen_host = "0.0.0.0"           # 不用改, docker-compose 里设好的
listen_port = 10001               # 容器对外提供服务的端口, 可以改, 但要注意配合好 docker-compose
upstream_host = "10.1.1.1"        # 校内服务的地址, 需要改
upstream_port = 9000              # 校内服务的端口, 需要改
upstream_ssl = false              # 是否对上游使用 SSL(HTTPS), 一般都不需要
```

如果你反代的服务比较简单, 就是一个静态页面, 可以直接在 docker-compose 里注释掉所有的跟 `mitmproxy` 有关的 services. 否则, 你可以照葫芦画瓢改改 `run.py` 使其符合你的需求.

最后, 我的这套配置文件里不包含 [caddy-docker-proxy](https://github.com/lucaslorentz/caddy-docker-proxy) 的 services, 你可能需要自己设一个, 配置可以参考本仓库里的 `docker-compose.yml`. 你也可以直接躺平, 将 rsocks/mitmproxy 的端口暴露到公网并通过 HTTP 访问.

## 感谢 

没有下面的开源软件, 就没有这套配置. 如果这套配置帮助到了您, 请给它们点 stars!

- [easyconnect-docker](https://github.com/Hagb/docker-easyconnect)
- [rsocks](https://github.com/tonyseek/rsocks) 
- [mitmproxy](https://github.com/mitmproxy/mitmproxy)
- [caddy-docker-proxy](https://github.com/lucaslorentz/caddy-docker-proxy)