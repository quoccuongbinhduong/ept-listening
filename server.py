import os
import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 8088
HISTORY_DIR = 'history'

USERS = {
    '2418480104001': 'Cuong@26121998',
    '2418480104005': 'Nhut@123'
}

class EPTHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching for API responses
        if self.path.startswith('/api/'):
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_POST(self):
        if self.path == '/api/login':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(body)
                user = data.get('user', '')
                pwd = data.get('pass', '')
                
                if user in USERS and USERS[user] == pwd:
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
                else:
                    self.send_response(401)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": False, "error": "Sai thông tin đăng nhập!"}).encode('utf-8'))
            except Exception as e:
                self.send_response(400)
                self.end_headers()
            return
            
        elif self.path == '/api/sync':
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            try:
                data = json.loads(body)
                user = data.get('user')
                state = data.get('state')
                app = data.get('app', '')
                
                if user and state is not None:
                    if not os.path.exists(HISTORY_DIR):
                        os.makedirs(HISTORY_DIR)
                    filename = f"{user}_{app}.json" if app else f"{user}.json"
                    filepath = os.path.join(HISTORY_DIR, filename)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(state, f, ensure_ascii=False)
                        
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True}).encode('utf-8'))
                else:
                    self.send_response(400)
                    self.end_headers()
            except Exception as e:
                self.send_response(400)
                self.end_headers()
            return

        # Fallback for standard POST
        super().do_POST()

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        
        if parsed_path.path == '/api/sync':
            query = urllib.parse.parse_qs(parsed_path.query)
            user = query.get('user', [None])[0]
            app = query.get('app', [''])[0]
            
            if user:
                filename = f"{user}_{app}.json" if app else f"{user}.json"
                filepath = os.path.join(HISTORY_DIR, filename)
                if os.path.exists(filepath):
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                else:
                    data = {}
                    
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
            return
            
        # Serve index.html as default
        if self.path == '/':
            self.path = '/index.html'
            
        super().do_GET()

if __name__ == '__main__':
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)
        
    print(f"Server is starting on http://localhost:{PORT}")
    print(f"Users configured: {list(USERS.keys())}")
    httpd = HTTPServer(('', PORT), EPTHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
