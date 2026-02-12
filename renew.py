import os
import sys
import requests
from datetime import datetime

# 从环境变量读取密钥（安全！）
API_KEY = os.getenv("DNSHE_API_KEY")
API_SECRET = os.getenv("DNSHE_API_SECRET")

if not API_KEY or not API_SECRET:
    print("❌ 请设置 DNSHE_API_KEY 和 DNSHE_API_SECRET")
    sys.exit(1)

BASE_URL = "https://api005.dnshe.com/index.php?m=domain_hub"
HEADERS = {
    "X-API-Key": API_KEY,
    "X-API-Secret": API_SECRET,
    "Content-Type": "application/json"
}

def log(msg):
    print(f"[{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC] {msg}")

def main():
    log("🚀 开始检查域名续期...")
    try:
        resp = requests.get(f"{BASE_URL}&endpoint=subdomains&action=list", headers=HEADERS, timeout=15)
        data = resp.json()
        if not data.get("success"):
            log(f"❌ 获取列表失败: {data.get('error', 'Unknown')}")
            return
        subdomains = data.get("subdomains", [])
    except Exception as e:
        log(f"💥 请求异常: {e}")
        return

    renewed = 0
    for sd in subdomains:
        if sd.get("status") != "active":
            continue
        full_domain = sd["full_domain"]
        sd_id = sd["id"]
        log(f"🔄 尝试续期: {full_domain}")
        try:
            resp = requests.post(
                f"{BASE_URL}&endpoint=subdomains&action=renew",
                headers=HEADERS,
                json={"subdomain_id": sd_id},
                timeout=15
            )
            if "application/json" in resp.headers.get("content-type", ""):
                result = resp.json()
                if result.get("success"):
                    log("✅ 续期成功！")
                    renewed += 1
                else:
                    log(f"⚠️ 被拒: {result.get('error') or 'Unknown'}")
            else:
                log("ℹ️ 暂不可续期")
        except Exception as e:
            log(f"💥 续期异常: {e}")

    log(f"🏁 完成，成功续期 {renewed} 个域名。")

if __name__ == "__main__":
    main()
