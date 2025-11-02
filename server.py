#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple HTTP Server for Droidify Redirector
خادم HTTP بسيط لـ Droidify Redirector
"""

import http.server
import socketserver
import os
import sys
import io
from urllib.parse import urlparse, unquote

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to support .well-known directory"""
    
    def end_headers(self):
        # Add CORS headers for assetlinks.json
        if self.path.endswith('.json'):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        # Security headers
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()
    
    def do_GET(self):
        # Handle .well-known directory
        if self.path.startswith('/.well-known'):
            file_path = self.path[1:]  # Remove leading /
            if os.path.exists(file_path):
                self.path = file_path
            else:
                self.send_error(404, "File not found")
                return
        
        # Handle /app/ route
        if self.path == '/' or self.path == '':
            # Redirect to /app/
            self.send_response(301)
            self.send_header('Location', '/app/')
            self.end_headers()
            return
        
        # Default handling
        super().do_GET()

def main():
    PORT = 8000
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if port is already in use
    try:
        with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
            local_ip = get_local_ip()
            print("=" * 60)
            print("Droidify Redirector Server")
            print("=" * 60)
            print(f"\n[OK] Server is running!")
            print(f"\n[*] Access from THIS device:")
            print(f"    http://localhost:{PORT}/app/")
            print(f"    http://127.0.0.1:{PORT}/app/")
            print(f"\n[*] Access from OTHER devices on same network:")
            print(f"    http://{local_ip}:{PORT}/app/")
            print(f"\n[*] Test links (use your network IP from other devices):")
            print(f"    http://{local_ip}:{PORT}/app/?id=com.example.app")
            print(f"    http://{local_ip}:{PORT}/app/?id=com.example.app&repo_address=https://repo.example.com/repo")
            print(f"\n[*] Make sure:")
            print(f"    - Both devices are on the same WiFi/network")
            print(f"    - Firewall allows port {PORT}")
            print(f"    - Use the network IP: {local_ip}")
            print(f"\n[*] Press Ctrl+C to stop the server")
            print("=" * 60)
            
            httpd.serve_forever()
    except OSError:
        print(f"[ERROR] Port {PORT} is already in use!")
        print(f"[TIP] Try using a different port or stop the process using port {PORT}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n[STOPPED] Server stopped by user")
        sys.exit(0)

def get_local_ip():
    """Get local IP address"""
    import socket
    try:
        # Connect to a remote address to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if __name__ == "__main__":
    main()

