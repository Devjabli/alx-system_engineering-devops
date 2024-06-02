Description

This is a basic web infrastructure hosting a website accessible via www.foobar.com. It lacks firewalls and SSL certificates for network protection. All components (database, application server) share the server's resources (CPU, RAM, and SSD).
Specifics About This Infrastructure

    What a Server Is:
    A server is a computer, either hardware or software, that provides services to other computers, known as clients.

    The Role of the Domain Name:
    A domain name offers a user-friendly alias for an IP address. For instance, the domain name www.wikipedia.org is easier to remember than 91.198.174.192. This mapping is managed by the Domain Name System (DNS).

    The Type of DNS Record for www.foobar.com:
    www.foobar.com uses an A record, which can be verified by running dig www.foobar.com. The results may vary, but this infrastructure uses an A record. An Address Mapping record (A Record) stores a hostname and its corresponding IPv4 address.

    The Role of the Web Server:
    The web server, either software or hardware, handles requests via HTTP or HTTPS and responds with the requested resource's content or an error message.

    The Role of the Application Server:
    The application server installs, operates, and hosts applications and associated services for users, IT services, and organizations, enabling the delivery of high-end consumer or business applications.

    The Role of the Database:
    The database maintains a collection of organized information that can be easily accessed, managed, and updated.

    Server-Client Communication:
    Communication between the client and server occurs over the internet through the TCP/IP protocol suite.

Issues With This Infrastructure

    Multiple Single Points of Failure (SPOF):
    If the MySQL database server goes down, the entire site would be unavailable.

    Downtime During Maintenance:
    Performing maintenance on any component requires shutting it down or turning off the server. With only one server, this results in website downtime.

    Scalability Issues:
    The infrastructure cannot easily scale with increased traffic since all components reside on a single server. The server may quickly run out of resources or slow down under heavy load.
