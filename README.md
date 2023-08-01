# mywebsite

1. WSGI
   Web Server Getway Interface is designed for handling synchronous web applications,
   where each request is processed one at a time,
   and the server waits for the application to generate the response before moving on to the next request.
 
2. ASGI
   Asynchronous Server Gateway Interface is an evolution of WSGI that introduces support for asynchronous programming
   and real-time communication. ASGI allows web applications to handle asynchronous tasks,
   where multiple requests can be processed concurrently without the need for separate threads or processes.
   
3. Django Channels
   Django Channels is an extension to the Django web framework
   that enables the handling of real-time web protocols, such as WebSockets, alongside traditional HTTP requests.
   
4. WebSockets
   WebSocket is a communication protocol that enables bidirectional, full-duplex communication channels
   over a single TCP connection. It provides a way for web browsers and servers to establish
   a persistent, real-time connection, allowing them to exchange data in both directions continuously. 
   WebSocket is designed to overcome some of the limitations of traditional HTTP,
   which follows a request-response model and does not allow continuous communication between clients and servers.
   
5. WebSocket connection (Client and Server side)
    required components and steps:
   1. WebSocket server URL(for handshake)
   2. WebSocket object(JS)
   3. Event Listeners
   4. Sending Messages
   5. Handling User actions
   6. Handling Server responses
      
7. Consumers
    Consumers are Python classes responsible for handling WebSocket connections and other asynchronous events.
    WebSocket consumers define methods to handle events such as connection open, message received, and connection close.
    They allow you to write custom logic to process WebSocket messages and perform real-time operations.
    
8. Routing
    Routing is a mechanism to map incoming messages, such as WebSocket connections or other asynchronous events, to their corresponding consumers.
    The routing configuration defines how different channels or URLs are associated with specific consumers.

9. AuthMiddlewareStack
10. path VS re_path
