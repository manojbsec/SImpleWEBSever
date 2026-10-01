from http.server import HTTPServer, BaseHTTPRequestHandler

REG_NO = "26011811"
NAME = "MANOJ B"

content = f"""<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <h3>Register No: {REG_NO} &nbsp;|&nbsp; Name: {NAME}</h3>
    <table border="1" cellpadding="8" cellspacing="0">
        <tr><th>Layer</th><th>Protocols</th></tr>
        <tr><td>Application</td><td>HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, DHCP, Telnet, SSH, SNMP, TFTP</td></tr>
        <tr><td>Transport</td><td>TCP, UDP, SCTP</td></tr>
        <tr><td>Internet (Network)</td><td>IP (IPv4/IPv6), ICMP, ARP, IGMP, IPsec</td></tr>
        <tr><td>Network Access (Link)</td><td>Ethernet, Wi-Fi (802.11), PPP, Frame Relay</td></tr>
    </table>
</body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ("127.0.0.1", 8000)
httpd = HTTPServer(server_address, MyHandler)
print("My webserver is running at http://127.0.0.1:8000 ...")
httpd.serve_forever()