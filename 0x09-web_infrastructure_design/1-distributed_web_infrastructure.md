Description

This is a distributed web infrastructure designed to alleviate traffic on the primary server by offloading some of the load to a replica server, managed by a load balancer.
Specifics About This Infrastructure

    Load Balancer Distribution Algorithm:
    The HAProxy load balancer uses the Round Robin distribution algorithm, which allocates requests to each server in turn based on their weights. This approach ensures an even distribution of processing time among servers and allows dynamic adjustment of server weights.

    Load-Balancer Setup:
    The HAProxy load balancer facilitates an Active-Passive setup. In this configuration, only one node is active at a time, handling all requests, while the other node remains passive, ready to take over if the active node fails. This contrasts with an Active-Active setup, where multiple nodes share the workload, improving throughput and response times.

    Database Primary-Replica (Master-Slave) Cluster:
    In this setup, one server acts as the Primary (master), handling all read/write operations, while the Replica (slave) server handles only read operations. The Replica server syncs data with the Primary server whenever a write operation occurs.

    Difference Between Primary and Replica Nodes:
    The Primary node handles all write operations, while the Replica node processes read operations, reducing the read load on the Primary node.

Issues With This Infrastructure

    Multiple Single Points of Failure (SPOF):
    If the Primary MySQL database server fails, no changes can be made to the site. Additionally, the load balancer and the application server connecting to the primary database are SPOFs.

    Security Issues:
    Without SSL certificates, data transmitted over the network is vulnerable to interception. The absence of firewalls means unauthorized IPs cannot be blocked.

    Lack of Monitoring:
    There is no system in place to monitor the status and health of the servers, leaving administrators unaware of potential issues.
