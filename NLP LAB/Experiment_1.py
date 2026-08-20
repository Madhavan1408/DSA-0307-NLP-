import re

text = "Contact us at support@example.com or sales@example.org. Call 9876543210 or 044-28451212. Visit https://www.example.com for more info. Order ID: AB1234, CD5678."

email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
phone_pattern = r'\b\d{10}\b|\b\d{3,4}-\d{6,8}\b'
url_pattern = r'https?://[^\s]+'
order_pattern = r'\b[A-Z]{2}\d{4}\b'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
urls = re.findall(url_pattern, text)
orders = re.findall(order_pattern, text)
print("Text:", text)
print("\nEmails found:", emails)
print("\nPhone numbers found:", phones)
print("\nURLs found:", urls)
print("\nOrder IDs found:", orders)

match = re.search(r'support@\w+\.\w+', text)
if match:
    print("\nFirst support email match:", match.group())

replaced = re.sub(r'\d{10}', 'XXXXXXXXXX', text)
print("\nAfter masking phone numbers:", replaced)
