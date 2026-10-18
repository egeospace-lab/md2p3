# PPT: Web Engineering Fundamentals

# Understanding the Modern Web Ecosystem

## Preliminary Definitions

### Networking

- **Protocols:** A protocol is a set of rules that governs how data is exchanged between computers. The most common examples are HTTP (HyperText Transfer Protocol) and HTTPS (secure HTTP), which define how browsers and servers communicate.
- **Schemes:** A scheme is the part of a URL that specifies which protocol is being used. For example, `https://` indicates secure HTTP.
- **Host:** The host identifies the server, either by domain name (e.g., `egeospace.in`) or IP address.
- **Port:** A port is a number that identifies a specific service on a host. For example, `:443` is the default port for HTTPS.
- **Origin:** The origin is defined as the combination of scheme, host, and port. It is a key concept in browser security. Example: `https://egeospace.in:443`
- **Site:** A site is broader than origin, usually defined as scheme + registrable domain (ignoring subdomains). Example:
    - `https://shop.egeospace.in` → Site: `https://egeospace.in`
    - `https://blog.egeospace.in` → Site: `https://egeospace.in`

### Request and Response

- **Request:** A request is a message sent by the client (browser) to the server asking for a resource.
- **Methods:** Methods define the type of action a request performs:
    - **GET**: Retrieve data.
    - **POST**: Send data.
    - **PUT/PATCH**: Update data.
    - **DELETE**: Remove data.
- **Payload:** The payload is the body of a request, containing data sent to the server (e.g., JSON form data).
- **Preflight Requests:** Special requests (using the HTTP OPTIONS method) sent by browsers before the actual request, to check if the server allows cross‑origin access.
- **Response:** A response is the server’s reply to a request, containing data, HTML, or status codes.

### Additional Concepts

- **Credentials:** Authentication information (like cookies, tokens, or HTTP auth headers) that may be included in requests to prove identity.
- **Latency:** The time delay between sending a request and receiving a response.
- **Bandwidth:** The maximum amount of data that can be transmitted over a network in a given time.
- **Throughput:** The actual rate at which data is successfully transferred over the network. It represents real‑world achieved performance, not just the theoretical maximum.
- **Path:** The path specifies the location of a resource on the server, such as `/products/list`.
- **Query String:** A query string passes data to the server using key‑value pairs. For example, `?id=123&sort=asc`.
- **Fragment:** A fragment refers to a section within a page, indicated by `#`, such as `#section3`.

## Modern Front‑end Engineering

### The Front‑end as the Product Experience

- The front‑end is the user’s direct interface with the application.
- It defines how users perceive and interact with the product.
- Design, usability, and responsiveness are critical success factors.
- A polished front‑end builds trust and engagement with users.
- Accessibility ensures inclusivity across diverse user groups.
- The front‑end is often the deciding factor in product adoption.

### The Front‑end as an Application Runtime

- Modern front‑ends are not just static pages but dynamic runtimes.
- JavaScript enables logic execution directly in the browser.
- Frameworks like React, Angular, and Vue provide structured runtimes.
- Client‑side rendering allows applications to feel fast and interactive.
- APIs connect front‑ends to back‑end services seamlessly.
- This runtime capability makes the browser a powerful application platform.

### The Front‑end as a Rapidly Evolving Discipline

- Front‑end technologies evolve faster than most other fields in IT.
- New frameworks and libraries emerge regularly, reshaping best practices.
- Standards like HTML, CSS, and JavaScript are continuously updated.
- Developers must adapt to trends like responsive design and progressive web apps.
- Tooling ecosystems (bundlers, linters, CI/CD) enhance productivity.
- Continuous learning is essential to remain competitive in front‑end engineering.

## Modern Back‑end Engineering

### The Back‑end as the Core Logic and Data Layer

- The back‑end handles business logic and data management.
- It processes requests from the front‑end and returns structured responses.
- Databases store and retrieve information efficiently.
- Back‑end frameworks simplify building APIs and services.
- Security and validation are enforced at this layer.
- Without a strong back‑end, applications cannot function reliably.

### The Back‑end as a Scalability and Reliability Foundation

- Back‑ends must scale to handle growing user demand.
- Techniques like load balancing distribute traffic across servers.
- Reliability is achieved through redundancy and failover systems.
- Cloud platforms provide elastic scaling for modern applications.
- Monitoring ensures issues are detected before they impact users.
- Scalability and reliability are key to sustaining business growth.

### The Back‑end as an Integration Hub for Services

- Back‑ends connect applications to external services and APIs.
- Payment gateways, authentication providers, and analytics tools integrate here.
- Microservices architectures allow modular integration.
- Middleware manages communication between different systems.
- Back‑ends often orchestrate workflows across multiple services.
- This integration capability makes back‑ends the central nervous system of applications.

## The Web as an Application Platform

### A Universal Installation‑free Runtime

- The web runs directly in browsers without installation.
- Users access applications instantly via URLs.
- This universality reduces friction compared to native apps.
- Updates are deployed centrally, reaching all users immediately.
- Progressive Web Apps (PWAs) extend web capabilities to offline and mobile.
- The web’s installation‑free nature drives global accessibility.

### A Distributed Cloud‑connected Platform

- Web applications leverage cloud infrastructure for distribution.
- Content Delivery Networks (CDNs) bring data closer to users.
- APIs connect applications to global services seamlessly.
- Cloud hosting ensures scalability and resilience.
- Distributed systems reduce latency and improve performance.
- The web is inherently designed for global reach and connectivity.

### A Secure and Continuously Evolving Environment

- Security protocols like HTTPS and TLS protect user data.
- Browsers enforce sandboxing to isolate applications.
- Regular updates patch vulnerabilities across the ecosystem.
- Standards bodies continuously evolve web specifications.
- Privacy regulations shape how data is handled online.
- The web remains a dynamic, secure environment for innovation.

# Evolution of the Web

---

## Web 1.0: The Static, Read‑only Web

### Hyperlinked Documents and Browsing

- Web 1.0 was primarily about static HTML documents linked together.
- Users navigated by clicking hyperlinks to move between pages.
- Browsers displayed content without much interactivity.
- Information was presented in a one‑way, read‑only format.
- Websites acted like digital brochures or libraries.
- This era laid the foundation for global information sharing.

### Centralised Content Publishing

- Content was created and controlled by a small number of publishers.
- Websites were hosted on central servers managed by organisations.
- Users consumed information but rarely contributed.
- Publishing required technical knowledge and infrastructure.
- Authority and credibility were concentrated in established institutions.
- This centralisation limited diversity of voices online.

### Limited Interactivity and Early Constraints

- User interaction was minimal, often limited to reading text.
- Forms and guestbooks were among the few interactive features.
- Bandwidth and slow connections restricted multimedia use.
- Browsers had limited capabilities for dynamic content.
- Personalisation was almost non‑existent.
- These constraints defined the early web as static and passive.

## Web 2.0: The Interactive User‑generated Web

### From Pages to Applications

- Web 2.0 transformed websites into dynamic applications.
- JavaScript and AJAX enabled real‑time updates without page reloads.
- Interfaces became interactive and responsive.
- Applications like Gmail and Facebook showcased this shift.
- The web evolved into a platform for productivity and communication.
- This marked the beginning of the “app‑like” web experience.

### User‑generated Content and Social Interfaces

- Platforms empowered users to create and share content.
- Blogs, wikis, and social media became dominant.
- Communities formed around shared interests and contributions.
- The web became participatory rather than publisher‑driven.
- Social interfaces encouraged collaboration and engagement.
- This era democratized content creation globally.

### Rich Interactivity and Personalised Experiences

- Web 2.0 introduced multimedia, animations, and interactive widgets.
- Personalisation tailored content to individual users.
- Recommendation engines shaped user experiences.
- APIs allowed integration of services across platforms.
- Mobile devices accelerated interactive web adoption.
- The web became immersive, adaptive, and user‑centric.

## Web 3.0: Decentralised, Trust‑minimised, and User‑owned Experiences

### Core Principles of Web 3.0

- Web 3.0 emphasises decentralisation and user ownership.
- Trust is minimised through cryptographic verification.
- Data sovereignty shifts control back to individuals.
- Peer‑to‑peer networks replace centralised servers.
- Transparency and immutability are key principles.
- The vision is a fairer, user‑empowered internet.

### Blockchain and Smart Contract Interactions

- Blockchain provides a distributed ledger for transactions.
- Smart contracts automate agreements without intermediaries.
- Applications run on decentralised infrastructure (dApps).
- Financial services evolve into decentralised finance (DeFi).
- Ownership of digital assets is verifiable and transferable.
- This technology underpins trustless interactions online.

### Wallet‑based Authentication and User Ownership

- Users authenticate using cryptographic wallets instead of passwords.
- Wallets store digital identities and assets securely.
- Ownership of data and content is tied to the user’s wallet.
- Platforms cannot easily revoke or censor user access.
- Wallets enable seamless participation in decentralised ecosystems.
- This model redefines digital identity and control.

# Transport Protocols

---

## TCP/IP

### TCP – Reliable Transport for Web Applications

- TCP ensures reliable communication by guaranteeing delivery of data packets.
- It establishes a connection before transmitting information (handshake process).
- Packets are sequenced and reassembled in the correct order.
- Lost or corrupted packets are retransmitted automatically.
- This reliability makes TCP ideal for web browsing, email, and file transfers.
- The trade‑off is slightly higher latency compared to faster protocols.

### IP – Addressing and Routing Basics

- IP provides unique addresses for devices on a network.
- It defines how packets are routed from source to destination.
- Routers use IP addresses to forward data across networks.
- IPv4 uses 32‑bit addresses, while IPv6 expands to 128‑bit for scalability.
- IP does not guarantee delivery; it simply handles addressing and routing.
- Combined with TCP, it forms the backbone of internet communication.

### How TCP/IP Powers HTTP and HTTPS

- HTTP and HTTPS rely on TCP/IP for transport.
- TCP ensures reliable delivery of web requests and responses.
- IP handles addressing so clients can reach servers globally.
- HTTPS adds encryption via TLS on top of TCP/IP.
- Together, these layers enable secure and consistent web communication.
- Without TCP/IP, the web’s request–response model would not function.

## UDP

### UDP – Lightweight, Fast Transport

- UDP is a connectionless protocol, sending packets without handshakes.
- It prioritises speed over reliability, with no retransmission of lost packets.
- Packets may arrive out of order or be dropped entirely.
- This simplicity reduces overhead and latency.
- It is well‑suited for real‑time applications like streaming and gaming.
- Developers must handle reliability at the application level if needed.

### Common Use Cases for UDP

- Video and audio streaming rely on UDP for low latency.
- Online gaming uses UDP for fast, continuous updates.
- DNS queries use UDP for quick lookups.
- VoIP calls depend on UDP for real‑time communication.
- Broadcast and multicast transmissions often use UDP.
- These use cases value speed and timeliness over guaranteed delivery.

## Applied Transport Protocols

### Trade‑offs Between TCP and UDP

- TCP offers reliability, ordering, and error correction.
- UDP offers speed, simplicity, and lower latency.
- TCP is better for applications requiring accuracy, like banking or browsing.
- UDP is better for real‑time applications where delays are worse than errors.
- Choosing between them depends on application requirements.
- Many modern systems combine both for different tasks.

### Other Transport Protocols

- SCTP (Stream Control Transmission Protocol) supports multi‑streaming and multi‑homing.
- QUIC, developed by Google, combines reliability with low latency over UDP.
- QUIC underpins HTTP/3, the latest web communication standard.
- DCCP (Datagram Congestion Control Protocol) manages congestion for streaming.
- Each protocol addresses specific limitations of TCP or UDP.
- The ecosystem continues to evolve to meet modern application needs.

# Domain Name System (DNS)

---

## Overview of DNS

### Core Concepts of DNS

- DNS translates human‑readable domain names into machine‑readable IP addresses.
- It acts like the “phonebook” of the internet.
- Every domain name corresponds to one or more IP addresses.
- DNS queries resolve these mappings to connect users to websites.
- Without DNS, users would need to remember numeric IP addresses.
- This system makes the web accessible and user‑friendly.

### Domain Names and Hierarchy

- Domain names are structured hierarchically with dots separating levels.
- The rightmost part (e.g., `.com`, `.org`) is the top‑level domain (TLD).
- The next level identifies the organisation or service (e.g., `egeospace.in`).
- Subdomains (e.g., `blog.egeospace.in`) provide further granularity.
- This hierarchy ensures scalability and organisation of the namespace.
- It allows millions of domains to coexist without conflict.

### Root Servers and Delegation

- Root servers are the highest authority in the DNS hierarchy.
- They direct queries to the appropriate TLD servers.
- TLD servers then delegate queries to authoritative servers for specific domains.
- This delegation process ensures efficient resolution.
- Root servers are globally distributed for resilience.
- They form the backbone of the DNS infrastructure.

### DNS Records and TTL

- DNS records define specific information about a domain.
- Common types include A (IPv4 address), AAAA (IPv6 address), MX (mail server), and CNAME (alias).
- Each record has a Time‑to‑Live (TTL) value.
- TTL determines how long a record is cached before refreshing.
- Short TTLs allow rapid updates, while long TTLs reduce query load.
- Records and TTLs balance flexibility with performance.

## DNS Resolution Process

### Process Overview

- DNS resolution begins when a user enters a domain name.
- The query is sent to a DNS resolver, often provided by the ISP.
- The resolver checks its cache for existing records.
- If not found, it queries root servers, then TLD servers, then authoritative servers.
- The authoritative server provides the final IP address.
- The resolver returns this address to the user’s device.

### Recursive vs Iterative Resolution

- Recursive resolution means the resolver handles the entire query chain.
- The client receives only the final answer.
- Iterative resolution means the resolver returns referrals step by step.
- The client may need to query multiple servers directly.
- Recursive resolution is more common for end‑users.
- Iterative resolution is often used by DNS infrastructure components.

### Caching and Performance

- DNS caching stores resolved addresses temporarily.
- Browsers, operating systems, and resolvers all maintain caches.
- Caching reduces repeated queries and speeds up access.
- It also lowers the load on DNS servers.
- TTL values control how long caches remain valid.
- Effective caching improves both performance and reliability.

### Common Issues

- DNS propagation delays occur when records are updated but caches still hold old data.
- Misconfigured records can cause websites to be unreachable.
- DNS spoofing or poisoning can redirect users to malicious sites.
- Slow DNS servers can increase page load times.
- Outages at major DNS providers can disrupt large parts of the internet.
- Monitoring and redundancy help mitigate these risks.

# Web Communication

---

## HTTP Methods

### GET – Retrieving Resources

- GET requests are used to fetch data from a server.
- They are safe and idempotent, meaning repeated requests don’t change server state.
- Responses typically include HTML, JSON, or other content formats.
- Query parameters can be added to refine the request.
- GET requests are cached by browsers and proxies for efficiency.
- They form the backbone of most web page loading operations.

### POST – Creating or Submitting Data

- POST requests send data to the server for processing.
- They are commonly used for form submissions and API calls.
- Unlike GET, POST modifies server state by creating or updating resources.
- Data is included in the request body, not the URL.
- POST requests are not cached by default.
- They are essential for interactive applications requiring user input.

### PUT and PATCH – Updating Resources

- PUT replaces an entire resource with new data.
- PATCH applies partial updates to an existing resource.
- Both methods are idempotent when used correctly.
- They are widely used in RESTful APIs for resource management.
- PUT is ideal for full replacements, while PATCH is more efficient for small changes.
- These methods ensure structured and predictable updates.

### DELETE – Removing Resources

- DELETE requests remove resources from the server.
- They are idempotent, meaning repeated requests have the same effect.
- Security controls often restrict DELETE operations.
- Responses confirm whether the deletion was successful.
- DELETE is critical for managing data lifecycle in applications.
- It ensures resources are cleaned up when no longer needed.

### Other Methods and Their Use Cases

- HEAD retrieves metadata without the full resource body.
- OPTIONS checks which methods are supported by a server.
- CONNECT establishes a tunnel, often for HTTPS.
- TRACE echoes the request for diagnostic purposes.
- These methods support specialised use cases beyond CRUD operations.
- They enhance flexibility and transparency in communication.

## Communication Process Mechanisms

### Request–Response Cycle

- The web is built on a client–server request–response model.
- Clients send requests, and servers return responses.
- Each cycle is independent and stateless.
- Responses include status codes to indicate success or failure.
- Headers provide metadata about the request and response.
- This cycle underpins all web interactions.

### Statelessness and Session Management

- HTTP is inherently stateless, meaning each request is independent.
- Servers do not remember previous interactions by default.
- Sessions are introduced to maintain continuity for users.
- Cookies and tokens store session identifiers.
- Session management enables features like login persistence.
- Balancing statelessness with session needs is key to scalability.

### Content Negotiation and Data Formats

- Content negotiation allows servers to deliver data in preferred formats.
- Clients specify acceptable formats via headers (e.g., JSON, XML, HTML).
- Servers respond with the best match based on availability.
- This ensures compatibility across diverse clients.
- Data formats define how information is structured and exchanged.
- JSON has become the dominant format for APIs due to simplicity.

### Caching and Performance Optimisation

- Caching stores frequently accessed data to reduce repeated requests.
- Browsers, proxies, and CDNs all implement caching strategies.
- Cache headers (e.g., `Cache-Control`, `ETag`) guide behaviour.
- Effective caching improves speed and reduces server load.
- Performance optimisation relies heavily on smart caching.
- Poor caching strategies can lead to stale or inconsistent data.

## TLS

### Overview and Purpose of TLS

- TLS (Transport Layer Security) secures communication over the web.
- It encrypts data to prevent eavesdropping and tampering.
- TLS ensures confidentiality, integrity, and authenticity.
- It underpins HTTPS, the secure version of HTTP.
- Without TLS, sensitive data like passwords would be exposed.
- TLS is essential for user trust and compliance.

### Certificates and Trust Chains

- TLS relies on digital certificates issued by Certificate Authorities (CAs).
- Certificates verify the identity of websites.
- Browsers trust CAs to validate authenticity.
- Trust chains link certificates back to a root authority.
- Invalid or expired certificates trigger browser warnings.
- Certificates are critical for secure communication.

### TLS Handshake

- The TLS handshake establishes a secure connection between client and server.
- It negotiates encryption algorithms and session keys.
- Certificates are exchanged to verify identities.
- Once complete, all communication is encrypted.
- The handshake adds slight latency but ensures security.
- Modern optimisations reduce handshake overhead.

### Modern TLS Practices

- TLS 1.3 is the latest version, offering improved speed and security.
- Forward secrecy ensures past communications remain secure even if keys are compromised.
- Strong cipher suites prevent vulnerabilities.
- Automated certificate management simplifies renewals.
- Security best practices require disabling outdated versions like TLS 1.0.
- Continuous updates keep TLS resilient against evolving threats.