from http.server import SimpleHTTPRequestHandler, HTTPServer

html_content = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Welcome</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
        }
        .card {
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(12px);
            padding: 50px 60px;
            border-radius: 20px;
            text-align: center;
        }
        h1 { font-size: 3rem; }
        p { font-size: 1.25rem; opacity: .9; }
    </style>
</head>
<body>
    <div class='card'>
        <h1>Welcome!</h1>
        <p>Python is serving this modern welcome page.</p>
    </div>
</body>
</html>
"""

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode())

if __name__ == "__main__":
    server = HTTPServer(("localhost", 3000), Handler)
    print("Serving on http://localhost:3000 ...")
    server.serve_forever()
    