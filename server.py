import os
import json
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 8088
HISTORY_DIR = 'history'

USERS = {
    '2418480104001': 'Cuong@26121998',
    '2418480104005': 'Nhut@123'
}

class EPTHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes')
        # Disable caching for API responses
        if self.path.startswith('/api/'):
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def send_range_content(self, filepath, file_size, range_header):
        try:
            val = range_header.strip()
            if not val.startswith('bytes='):
                super().do_GET()
                return
            
            range_str = val[6:]
            parts = range_str.split('-')
            
            if parts[0] and parts[1]:
                start = int(parts[0])
                end = int(parts[1])
            elif parts[0]:
                start = int(parts[0])
                end = file_size - 1
            elif parts[1]:
                start = max(0, file_size - int(parts[1]))
                end = file_size - 1
            else:
                start = 0
                end = file_size - 1

            if start >= file_size or start > end:
                self.send_response(416)
                self.send_header('Content-Range', f'bytes */{file_size}')
                self.send_header('Accept-Ranges', 'bytes')
                self.end_headers()
                return

            end = min(end, file_size - 1)
            content_length = end - start + 1

            self.send_response(206)
            self.send_header('Content-Type', self.guess_type(filepath))
            self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
            self.send_header('Content-Length', str(content_length))
            self.send_header('Accept-Ranges', 'bytes')
            self.send_header('Cache-Control', 'public, max-age=3600')
            self.end_headers()

            with open(filepath, 'rb') as f:
                f.seek(start)
                remaining = content_length
                chunk_size = 64 * 1024
                while remaining > 0:
                    read_len = min(chunk_size, remaining)
                    data = f.read(read_len)
                    if not data:
                        break
                    self.wfile.write(data)
                    remaining -= len(data)
        except (ConnectionResetError, BrokenPipeError):
            pass
        except Exception as e:
            pass

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

        filepath = self.translate_path(self.path)
        if os.path.isfile(filepath):
            range_header = self.headers.get('Range')
            if range_header:
                file_size = os.path.getsize(filepath)
                self.send_range_content(filepath, file_size, range_header)
                return
            
        super().do_GET()

    def do_HEAD(self):
        filepath = self.translate_path(self.path)
        if os.path.isfile(filepath):
            file_size = os.path.getsize(filepath)
            range_header = self.headers.get('Range')
            if range_header and range_header.startswith('bytes='):
                try:
                    val = range_header.strip()[6:]
                    parts = val.split('-')
                    start = int(parts[0]) if parts[0] else 0
                    end = int(parts[1]) if len(parts) > 1 and parts[1] else file_size - 1
                    end = min(end, file_size - 1)
                    length = end - start + 1
                    self.send_response(206)
                    self.send_header('Content-Type', self.guess_type(filepath))
                    self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
                    self.send_header('Content-Length', str(length))
                    self.send_header('Accept-Ranges', 'bytes')
                    self.end_headers()
                    return
                except:
                    pass
        super().do_HEAD()

if __name__ == '__main__':
    if not os.path.exists(HISTORY_DIR):
        os.makedirs(HISTORY_DIR)
        
    print(f"Server is starting on http://localhost:{PORT}")
    print(f"Users configured: {list(USERS.keys())}")
    httpd = ThreadingHTTPServer(('', PORT), EPTHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
