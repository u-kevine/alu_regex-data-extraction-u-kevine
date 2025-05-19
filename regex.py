import re

# Sample string to test on
text = """
Contact me at user@example.com
Visit https://www.example.com or https://subdomain.example.org/page.
Call (123) 456-7890 or 123-456-7890 or 123.456.7890.
Credit card: 1234 5678 9012 3456, 1234-5678-9012-3456.
Price: $19.99, $1,234.56, and $1234567.89 are listed.
"""
#  Email address regex
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
emails = re.findall(email_pattern, text)

#  URL regex
url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, text)

#  Phone number regex
phone_pattern = r'(\(\d{3}\)\s\d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})'
phones = re.findall(phone_pattern, text)

#  Credit card number regex
credit_card_pattern = r'(\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4})'
cards = re.findall(credit_card_pattern, text)

#  Currency amounts regex
currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})'
currencies = re.findall(currency_pattern, text)

#  Print results
print("Emails found:", emails)
print("URLs found:", urls)
print("Phone numbers found:", phones)
print("Credit card numbers found:", cards)
