"""接收页面 POST 过来的 dataURL 图片并存盘，用于逐帧检查画面。

用法：python -I frame_sink.py <输出目录>
页面里调用 dump('a.jpg', [1, 5, 9, 13])，图片会存到 <输出目录>/a.jpg，再用 Read 工具查看。
"""
import base64
import http.server
import os
import sys

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'


class Handler(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', '*')

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length'])).decode()
        name = os.path.basename(self.path.strip('/')) or 'frame.jpg'
        with open(os.path.join(OUT, name), 'wb') as f:
            f.write(base64.b64decode(data.split(',', 1)[1]))
        self.send_response(200)
        self._cors()
        self.end_headers()
        self.wfile.write(b'ok')

    def log_message(self, *args):
        pass


http.server.HTTPServer(('127.0.0.1', 8799), Handler).serve_forever()
