#!/usr/bin/env python3
"""Send code to Maya over the command port."""

import socket
import sys

def send_to_maya(code):
    """Send Python code to Maya's command port."""
    port = 7001
    host = 'localhost'

    try:
        # Connect to Maya command port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))

        # Send the Python code
        message = f"python(\"{code}\")"
        sock.sendall(message.encode('utf-8'))

        # Receive response
        response = sock.recv(4096).decode('utf-8')
        print(response)

    except ConnectionRefusedError:
        print("Error: Cannot connect to Maya command port.")
        print("Make sure Maya is running and the command port is open.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        code = sys.argv[1]
        send_to_maya(code)
    else:
        print("Usage: python3 send_to_maya.py '<python_code>'")
        print("Example: python3 send_to_maya.py 'import importlib; importlib.reload(set_dresser)'")
