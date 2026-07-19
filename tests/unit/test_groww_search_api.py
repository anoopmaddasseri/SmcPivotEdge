import urllib.request
import json

url = "https://api.groww.in/v1/api/search/v3/query/global/st_query?query=KAYNES&web=true"
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
})
try:
    with urllib.request.urlopen(req, timeout=5) as r:
        data = json.loads(r.read().decode())
        print("SUCCESS")
        print(json.dumps(data, indent=2)[:1000])
except Exception as e:
    print("FAILED:", e)
