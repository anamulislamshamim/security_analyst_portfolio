My company that offers web design services, graphic design, and social media marketing solutions to small businesses. My organization recently experienced a DDoS attack, which compromised the internal network for two hours until it was resolved. <br>
# 
During the attack, my organization’s network services suddenly stopped responding due to an incoming flood of ICMP packets. Normal internal network traffic could not access any network resources. The incident management team responded by blocking incoming ICMP packets, stopping all non-critical network services offline, and restoring critical network services. <br>
# 
The company’s cybersecurity team then investigated the security event. They found that a malicious actor had sent a flood of ICMP pings into the company’s network through an unconfigured firewall. This vulnerability allowed the malicious attacker to overwhelm the company’s network through a distributed denial of service (DDoS) attack. <br>
# 
To address this security event, the network security team implemented: <br>
# 
A new firewall rule to limit the rate of incoming ICMP packets <br>
# 
Source IP address verification on the firewall to check for spoofed IP addresses on incoming ICMP packets <br>
# 
Network monitoring software to detect abnormal traffic patterns <br>
# 
An IDS/IPS system to filter out some ICMP traffic based on suspicious characteristics <br>
# 
As a cybersecurity analyst, my tasked with using this security event to create a plan to improve company’s network security, following the National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF). 