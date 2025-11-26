from http.server import SimpleHTTPRequestHandler, HTTPServer

html_content = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Welcome to Jenkins</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        /* Global Styles */
        body {
            margin: 0;
            padding: 0;
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f0ad4e, #d9534f); /* Jenkins-inspired warm colors */
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            overflow: hidden;
        }

        /* Card */
        .card {
            background: rgba(0,0,0,0.3);
            backdrop-filter: blur(15px);
            padding: 60px 80px;
            border-radius: 25px;
            text-align: center;
            box-shadow: 0 0 30px rgba(0,0,0,0.4);
            position: relative;
            animation: float 6s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }

        h1 {
            font-size: 3.5rem;
            margin-bottom: 20px;
            color: #fff;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.4);
        }

        p {
            font-size: 1.4rem;
            opacity: 0.9;
            margin-bottom: 30px;
        }

        .jenkins-logo {
            width: 80px;
            height: 80px;
            margin-bottom: 20px;
            animation: rotate 10s linear infinite;
        }

        @keyframes rotate {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .status {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 50px;
            background: #5cb85c;
            color: #fff;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .footer {
            position: absolute;
            bottom: 20px;
            font-size: 0.9rem;
            opacity: 0.7;
        }
    </style>
</head>
<body>
    <div class='card'>
        <img class="jenkins-logo" src="https://www.jenkins.io/images/logos/jenkins/jenkins.png" alt="Jenkins Logo">
        <h1>Welcome to Jenkins!</h1>
        <p>Your Python server is running and ready for CI/CD automation.</p>
        <div class="status">Server Status: <strong>Running</strong></div>
        <div class="footer">Powered by Python & Jenkins</div>
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
    server = HTTPServer(("0.0.0.0", 3000), Handler)
    print("Serving on http://0.0.0.0:3000 ...")
    server.serve_forever()
    