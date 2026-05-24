import http.server
import socketserver
import urllib.request
from urllib.parse import unquote

PORT = 8000

class LocalProxyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Intercept calls made to our custom /api/yf endpoint
        if self.path.startswith('/api/yf?url='):
            target_url = unquote(self.path.split('?url=')[1])
            
            # Mask the request with a standard browser User-Agent so Yahoo doesn't block it
            req = urllib.request.Request(target_url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            
            try:
                with urllib.request.urlopen(req) as response:
                    data = response.read()
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(data)
            except Exception as e:
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(f'{{"error": "{str(e)}" }}'.encode())
        else:
            # Serve regular files (like screener.html) normally
            super().do_GET()

print(f"Starting robust local server at http://localhost:{PORT}")
socketserver.TCPServer(("", PORT), LocalProxyHandler).serve_forever()