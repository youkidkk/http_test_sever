import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get("content-length"))
        req_body = json.loads(self.rfile.read(content_len).decode("utf-8"))

        res_body = {**req_body, "res": "res value"}
        self.send_response(200)
        self.send_header("Content-type", "application/json;charset=utf-8")
        self.end_headers()
        body_json = json.dumps(res_body, sort_keys=False, indent=4, ensure_ascii=False)
        self.wfile.write(body_json.encode("utf-8"))


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 3000
    httpd = HTTPServer((host, port), MyHandler)
    httpd.serve_forever()
