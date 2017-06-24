"""
A simple Client Server application in python 3.5. This application consist of two parts Server application
"ServerApplication.py" and Client Application " ClientApplication.py"
The server echo whatever it receives from client.

In order to see the client/server interactions, launch the following server script in one console:
$python ClientServerApplication.py --port=9900
You will see the output like this:
Starting up echo server on localhost port 9900
Waiting to receive message from client

Now run ClientApplication.py from another terminal:

$python ClientApplication.py --port 9900
Connecting to localhost port 9900
Sending Test message. This will be echoed
Received: Test message. Th
Received: is will be echoe
Received: d
Closing connection to the server

"""
import socket
import sys
import argparse
host = 'localhost'
def echo_client(port):
    """ A simple echo client """
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the server
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    try:
        # Send data
        message = "Test message. This will be echoed"
        print("Sending %s" % message)
        sock.sendall(message)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print("Received: %s" % data)
    except socket.errno as e:
        print("Socket error: %s" %str(e))
    except Exception as e:
        print("Other exception: %s" %str(e))
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)