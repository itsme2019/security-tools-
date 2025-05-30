#!/usr/bin/env python3
"""
Basic Port Scanner
Author: Khalil Zarrouk - Cybersecurity Officer
"""

import socket
import threading
from datetime import datetime
import sys

def scan_port(target, port):
    try:
        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        # Attempt connection
        result = sock.connect_ex((target, port))
        
        if result == 0:
            try:
                # Try to grab banner
                sock.send(b'GET / HTTP/1.1\r\n\r\n')
                banner = sock.recv(1024).decode().strip()
                print(f"Port {port}: OPEN - {banner[:50]}...")
            except:
                print(f"Port {port}: OPEN")
        
        sock.close()
        
    except socket.gaierror:
        print(f"Could not resolve {target}")
    except Exception as e:
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 port_scanner.py <target>")
        sys.exit(1)
    
    target = sys.argv[1]
    print(f"Scanning {target}...")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)
    
    # Common ports
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995]
    
    threads = []
    for port in ports:
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("-" * 50)
    print(f"Scan completed: {datetime.now()}")

if __name__ == "__main__":
    main()