# TCP/IP and HTTP Networking Project

This Python-based project is an exploration into the foundational aspects of network programming, focusing on the TCP/IP model for creating robust client-server applications and understanding the HTTP protocol for web communication. Through practical implementation, this project demonstrates key networking concepts, the creation of networked applications, and the intricacies of web requests.

## Key Concepts Covered

- **TCP/IP Communication**: Utilizing the Transmission Control Protocol (TCP) and Internet Protocol (IP) to establish a reliable connection between a client and a server. This includes setting up sockets, listening for incoming connections, and handling data transmission.
- **Multithreading in Server Applications**: Enhancing the server to handle multiple client connections simultaneously without blocking, through the use of Python's `threading` module.
- **HTTP Protocol**: Crafting and sending HTTP requests manually using TCP sockets to understand the structure of web requests and responses, including methods, headers, and the message body.
- **Software Design Patterns**: Implementing the client-server model and exploring asynchronous programming patterns to improve the efficiency and reliability of networked applications.

## Project Structure

- `server.py`: Implements a basic TCP server that can accept connections, read incoming messages, and echo them back to the client.
- `client.py`: A simple TCP client capable of connecting to the server, sending messages, and receiving responses.
- `threaded_server.py`: An extension of `server.py` that uses threading to handle multiple clients concurrently, showcasing how to scale network applications.
- `http_client.py`: Demonstrates how to manually create an HTTP GET request, send it to a web server, and process the response, highlighting the workings of the web at a low level.

## Running the Project

### TCP Server and Client

1. **Start the Server**:


- `python server.py`

For handling multiple connections:

- `python threaded_server.py`

2. **Run the Client:**

- `python client.py`


### Running the HTTP Client

Ensure your target server is running and accepts HTTP requests on the correct port, then:

- `python http_client.py`


This command sends an HTTP GET request to the server and prints the response.

## Learning Outcomes

- Gained hands-on experience with network programming, understanding how data is transmitted over the internet.
- Learned how to use Python's `socket` and `threading` libraries to build networked applications.
- Deepened understanding of the HTTP protocol and how web applications communicate over the network.

## Requirements

- Python 3.x
- Basic understanding of TCP/IP and HTTP protocols

## Contributing

Feel free to fork this project and submit pull requests for any enhancements, bug fixes, or improvements you develop.

## License

This project is open-source and available under the MIT License.
