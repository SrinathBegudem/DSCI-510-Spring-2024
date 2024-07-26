# Lab 10
# Replace "WRITE CODE HERE" with your python code and remove the "pass" statement


# ----------------- Question 1 -----------------

import re

def redact_phone_numbers(text):
    
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    
    redacted_text = re.sub(pattern, '[REDACTED]', text)
    return redacted_text

text = "Call me at 123-456-7890 or 098-765-4321 tomorrow."
print(redact_phone_numbers(text))

# ----------------- Question 2 -----------------

import re

def validate_passwords(passwords):
    
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\d!@#$%^&*()]{8,}$'
    
    results = []
   
    for password in passwords:
        
        is_valid = bool(re.match(pattern, password))
        results.append(is_valid)
    return results



# invoke the function with relevant args of your choice
example_passwords = ["StrongPass1!", "weak", "12345", "AnotherStrongPass2@"]
print(validate_passwords(example_passwords))


# ----------------- Question 3 -----------------
from urllib.parse import urlparse

def extract_host_from_url(urls):
    
    hostnames = []
    
    for url in urls:
        try:
            
            parsed_url = urlparse(url)
            
            hostname = parsed_url.netloc
            
            hostnames.append(hostname)
        except:
            
            hostnames.append('')
    return hostnames



# invoke the function with relevant args of your choice
example_urls = ["https://www.example.com/page", "http://subdomain.example.org", "www.malformed-url.com", "https://bit.ly/xyz123"]
print(extract_host_from_url(example_urls))

