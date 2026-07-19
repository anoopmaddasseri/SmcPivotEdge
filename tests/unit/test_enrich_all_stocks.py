import json
import urllib.request
import urllib.parse
import concurrent.futures
import time
import sys

input_file = r"../../nse-all-stocks.js"
output_file = r"../../nse-all-stocks.js"

# Load current stocks
try:
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Clean JS comments and prefix
    lines = [line for line in content.splitlines() if not line.strip().startswith("//")]
    content_clean = "\n".join(lines)
    json_str = content_clean.replace("window.ALL_NSE_STOCKS = ", "").strip()
    if json_str.endswith(";"):
        json_str = json_str[:-1].strip()
        
    stocks = json.loads(json_str)
except Exception as e:
    print("Failed to load nse-all-stocks.js:", e)
    sys.exit(1)

print(f"Loaded {len(stocks)} stocks. Preparing to resolve sectors/industries...")

def resolve_industry(stock):
    symbol = stock["symbol"]
    search_url = f"https://query2.finance.yahoo.com/v1/finance/search?q={urllib.parse.quote(symbol + '.NS')}&quotesCount=1&newsCount=0"
    req = urllib.request.Request(search_url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    })
    
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=4) as response:
                data = json.loads(response.read().decode())
                quotes = data.get("quotes", [])
                if quotes:
                    q = quotes[0]
                    # Retrieve clean sector and industry name
                    stock["industry"] = q.get("industryDisp") or q.get("industry") or q.get("sectorDisp") or q.get("sector") or "Equity"
                    stock["sector"] = q.get("sectorDisp") or q.get("sector") or "Equity"
                else:
                    stock["industry"] = "Equity"
                    stock["sector"] = "Equity"
                return stock
        except Exception as e:
            if attempt == 2:
                stock["industry"] = "Equity"
                stock["sector"] = "Equity"
                return stock
            time.sleep(0.5)
    return stock

start_time = time.time()
completed = []

print("Running batch resolution for all stocks...")
# Limit parallel requests slightly to avoid rate limit bans while staying fast
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
    futures = {executor.submit(resolve_industry, s): s for s in stocks}
    for count, fut in enumerate(concurrent.futures.as_completed(futures), 1):
        completed.append(fut.result())
        if count % 200 == 0:
            print(f"Resolved {count} / {len(stocks)} stocks...")

end_time = time.time()
print(f"Completed all {len(stocks)} stocks in {end_time - start_time:.2f} seconds.")

# Write updated list back to the file
try:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("// Comprehensive list of all NSE stocks with sector and industry classifications\n")
        f.write("window.ALL_NSE_STOCKS = ")
        json.dump(completed, f, indent=2)
        f.write(";\n")
    print("Successfully wrote updated file to:", output_file)
except Exception as e:
    print("Failed to write output file:", e)
