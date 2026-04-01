# DNSHE Auto Renew 

每月自动续期 DNSHE 免费子域名。

本项目是一个基于 GitHub Actions 的自动化脚本，旨在利用 **DNSHE 免费域名 API**  实现子域名的自动续期
##  功能特性

* **全自动续期**：每月 1 日自动执行续期操作 。
* **多域名支持**：自动遍历账户下所有子域名进行批量续期 。
* **安全合规**：采用 GitHub Secrets 管理密钥，不在代码中硬编码敏感信息 。

---

##  快速上手

### 第一步：获取 API 密钥

1. 登录 [DNSHE](https://my.dnshe.com/) 。


2. 进入 **“免费域名”** 页面 。


3. 在底部的 **“API 管理”** 卡片中点击 **“创建 API 密钥”** 。


4. 妥善保存获取到的 `API Key` 和 `API Secret` 。


### 第三步：配置 GitHub 仓库

1. **Fork 本仓库** 或将脚本及工作流文件上传至您的私有仓库。
2. 进入仓库设置：**Settings** -> **Secrets and variables** -> **Actions**。
3. 点击 **New repository secret**，依次添加以下变量：

| 变量名称 | 说明 | 示例 |
| --- | --- | --- |
| `DNSHE_API_KEY` | DNSHE 的 API Key | `cfsd_xxxxxxxxxx` |
| `DNSHE_API_SECRET` | DNSHE 的 API Secret | `yyyyyyyyyyyy` |


### 第四步：启用自动化

1. 点击仓库顶部的 **Actions** 选项卡。
2. 在左侧选择 **"DNSHE Domain Auto Renew"** 工作流。
3. 点击 **Run workflow** 手动触发一次，验证配置是否正确。

### 第五步：启用邮件通知
1.全局邮件通知设置（控制所有通知的接收方式）
点击右上角头像 → 选择“Settings”（设置）。
在左侧菜单中点击“Notifications”（通知）。
在“Email”（邮件）部分，确保你已添加并验证了接收通知的邮箱地址。
选择“Receive notifications by email”（通过邮件接收通知）的频率：
All activity：接收所有活动通知（不推荐，邮件量大）。
Only for threads that I’m watching or participating in：仅接收你关注或参与的讨论通知（推荐）。
Never：从不接收邮件通知。

2.按仓库设置邮件通知（精细化控制）
进入目标仓库页面。
点击页面右上角的“Watch”（关注）按钮。
在下拉菜单中选择：
Watching：接收该仓库所有活动的邮件通知。
Custom：自定义接收哪些事件的通知（如 Issues、Pull Requests、Releases 等）。
Ignoring：不接收任何通知。


3.通过 GitHub Actions 触发自定义邮件通知
在 .github/workflows/ 目录下编辑你的 YAML 文件（如 dnshe-renew.yml）。
使用 actions/setup-python 和 python 脚本发送邮件，或集成第三方邮件服务（如 SendGrid、Mailgun）。
或者使用 GitHub Actions 的 mail 动作。


##  运行计划

* **执行频率**：每月 1 日北京时间 08:00。
* **速率限制**：脚本遵循 API 默认的 60 请求 / 分钟限制 。
* **错误处理**：若续期失败，推送消息中将包含具体的错误原因（如认证失败、资源不存在等） 。



##  安全建议

* **密钥保护**：切勿将 `API Secret` 上传至公开代码库 。
* **定期轮换**：建议定期在 DNSHE 后台使用 `regenerate` 操作更新密钥以增强安全性 。
* **最小权限**：建议仅为该脚本配置必要的 API 访问权限 。


---


##  致谢

本项目得以实现，特别感谢以下平台与技术的支持：

* **[DNSHE](https://www.dnshe.com/)**：提供简单、快速、免费的域名注册服务及免费域名 API 服务，支持全类型 DNS 记录解析、DNS 记录管理及自动化续期功能。

---
