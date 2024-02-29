# TCP/IP and HTTP Networking Project

This project demonstrates basic networking concepts using Python, focusing on TCP/IP communication and HTTP requests. It includes a simple TCP server and client that communicate over sockets, a multithreaded version of the server for handling multiple connections simultaneously, and an HTTP client that sends GET requests.

## Project Structure

- `server.py`: A basic TCP server that accepts client connections and echoes received messages.
- `client.py`: A TCP client that connects to the server and sends messages.
- `threaded_server.py`: An enhanced version of `server.py` that uses threading to handle multiple client connections concurrently.
- `http_client.py`: A simple HTTP client that sends a GET request to a specified server and displays the response.

## How to Run

### Running the TCP Server and Client

1. **Start the Server:**

- `python server.py`

Or, for the multithreaded server:

- `python threaded_server.py`

2. **Run the Client:**

- `python client.py`


### Running the HTTP Client

Ensure your target server is running and accepts HTTP requests on the correct port, then:

- `python http_client.py`


This command sends an HTTP GET request to the server and prints the response.

## Requirements

- Python 3.x
- Basic understanding of TCP/IP and HTTP protocols

## Contributing

Feel free to fork this project and submit pull requests for any enhancements, bug fixes, or improvements you develop.

## License

This project is open-source and available under the MIT License.
