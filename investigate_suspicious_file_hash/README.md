# I am a level one security operations center (SOC) analyst at a financial services company. I have received an alert about a suspicious file being downloaded on an employee's computer. 
# 
# I investigate this alert and discover that the employee received an email containing an attachment. The attachment was a password-protected spreadsheet file. The spreadsheet's password was provided in the email. The employee downloaded the file, then entered the password to open the file. When the employee opened the file, a malicious payload was then executed on their computer. 
# 
# I retrieve the malicious file and create a SHA256 hash of the file. I might recall from a previous course that a hash function is an algorithm that produces a code that can't be decrypted. Hashing is a cryptographic method used to uniquely identify malware, acting as the file's unique fingerprint. 
# 
# Now that I have the file hash, I will use VirusTotal to uncover additional IoCs that are associated with the file.

# ** SHA256 file hash: 54e6ea47eb04634d3e87fd7787e2136ccfbcc80ade34f246a12cf93bab527f6b **

# After I've explored the sections in the VirusTotal report, I will uncover additional IoCs that are associated with the file according to the VirusTotal report.
# 
# Identify three indicators of compromise (IoCs) that are associated with this file hash using the tabs in the VirusTotal report. Then, enter the IoCs into their respective sections in the Pyramid of Pain template.
# 
# Indicators of compromise are valuable sources of information for security professionals because they are used to identify malicious activity. I can choose to identify any three of the six types of IoCs found in the Pyramid of Pain: 
# 
# Hash value: Hashes convert information into a unique value that can't be decrypted. Hashes are often used as unique references to files involved in an intrusion. In this activity, I used a SHA256 hash as the artifact for this investigation. Find another hash that's used to identify this malware and enter it beside the Hash values section in the Pyramid of Pain template. I can use the Details tab to help I identify other hashes.
# 
# IP address: Find an IP address that this malware contacted and enter it beside the IP addresses section in the Pyramid of Pain template. I can locate IP addresses in the Relations tab under the Contacted IP addresses section or in the Behavior tab under the IP Traffic section.
# 
# Domain name: Find a domain name that this malware contacted and enter it beside the Domain names section in the Pyramid of Pain template. I can find domain name information under the Relations tab. I might encounter benign domain names. Use the Detections column to identify domain names that have been reported as malicious.
# 
# Network artifact/host artifact: Malware can create network-related or host-related artifacts on an infected system. Find a network-related or host-related artifact that this malware created and enter it beside the Network/host artifacts section in the Pyramid of Pain template. I can find this information from the sandbox reports under the Behavior tab or from the Relations tab.
# 
# Tools: Attackers can use tools to achieve their goal. Try to find out if this malware has used any tool. Then, enter it beside the Tools section in the Pyramid of Pain template.
# 
# Tactics, techniques, and procedures (TTPs): TTPs describe the behavior of an attacker. Using the sandbox reports from the Behavior tab, find the list of tactics and techniques used by this malware as identified by MITRE ATT&CK® and enter it beside the TTPs section in the Pyramid of Pain template.