import requests
import re

# Step 1: Load the dataset
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
response = requests.get(url)
# print(response.text)
text = response.text

# Optional: split into lines
lines = text.splitlines()

# Step 2: Apply regex on each message (ignoring header)
for line in lines[1:]:
    label, message = line.split('\t', 1)

    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', message)
    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', message)
    all_caps = re.findall(r'\b[A-Z]{2,}\b', message)
    amounts = re.findall(r'\$\d+(?:\.\d{2})?', message)
    phones = re.findall(r'\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)*\d{3,4}[-.\s]?\d{3,4}\b', message)

    if emails or phones or urls or all_caps or amounts:
        # print(f"Message: {message}")
        if emails: print(f"  📧 Emails: {emails}")
        # if urls: print(f"  🌐 URLs: {urls}")
        # if all_caps: print(f"  🔠 ALL CAPS: {all_caps}")
        # if amounts: print(f"  💰 Amounts: {amounts}")
        # if phones: print(f"  ☎️ Phones: {phones}")
        # print("-" * 80)


# import re
# text = "Hello 123, Python 456!"
# pattern = r"\d+"
# result = re.sub(pattern, "[NUMBER]", text)
#
# print(result)