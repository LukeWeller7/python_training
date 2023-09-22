# APIs - Notes and Revision

## What are API's 

- **Application Programming Interface** - it is a type of application that allows two software components to communicate with each other, sending information depending on the definitions and functions.

### How are they Used?

- APIs are used such so a client side software can request certain sets of data from a server sided software, the server will send over the requested information over to the client.

### Why are they so popular?

- APIs are so popular because they allow these softwares to communicate with each other in real-time, allowing information to be sent between servers quicker through automation, this provides easier to use softwares for the user.

### Flowchart Digram showing how APIs work

![](C:\Users\lukew\PycharmProjects\DevOps_Training\python_fundamentals\notes\flowchart_API.png)
Diagram 1. Flowchart showing the process of API request.

Diagram 1. above shows a flowchart of how an API works for a user requesting data from a server. First the client send a request to the API stating where to find the database and what information to get. The API processes the request, checking it's validity. If invalid, an error will return to User. If not, the API with communicate with the server, which then retrieves the data from it's database. This information is sent back to the User/Client and an API Response is given.

### What is REST API?

- **Representation State Transfer** - a software architecture that provides conditions and guidelines on how APIs should work. Initally created to manage complex communication, it is now mainly used for high-performance through high traffic communication giving stronger reliability.

### What makes an API RESTful?

- RESTful API is an interfacr that two computer systems use to communicate their data, this data transfer is secure and exchanged over the internet. This allows businesses to communicate with other internal, external, and third-party applications.

```
Client
--->
HTTP Methods
--->
API - translate the request the client wants into the way the Server can understand
--->
HTTP Request
--->
Server
--->
Your Data
--->
API - Translates the data collected from the server database into a suitable format for the client 
--->
JSON - How the client wants the data
--->
Client
```

# HTTP

### What does HTTP stand for?

- **Hypertext Transfer Protocol**

### What is HTTP?

- It is a application-layer protocol that is used to transmit hypermedia documents, such as HTML. Designed to transfer information between network devices.

### What is HTTP used for?

- It is used to load in webpages using hypertext links

### What is HTTPS?

- **Hypertext Transfer Protocol Secure** - same as HTTP, but is a secure version. Provides encrypted data

### Explain HTTP request structure

- **Verb** - What is the action you want the API to perform
  - **Get** - 
  - **Post** - 
  - **Put** - 
  - **Patch** - 
  - **Delete** - 
- **URL** - The location of data you want to retrieve
- **Version** - HTTP Version
- **Header** - Content-type, Date (Information that needs to be sent to Sever)
- **Body**



### Explain HTTP response structure

- **Response code** - how does the server response?
  - 200: Response
  - 400: Bad Request
  - 401: Unauthorised
  - 404: Not Found
  - 500: Server down??
- **HTTP Version**


### What is statelessness?

- The server doesn't store any data about the client's previous request.

Stateless - Customers are dealt with at same time
```
http://ourservice/customer/1
http://ourservice/customer/2
```
Stateful - Nextcustomer has to wait for Customer_1
```
http://ourservice/customer/1
http://ourservice/nextcustomer
```

### What is caching?

- Store data that is used ofter/recently so you don't need to do as much work



