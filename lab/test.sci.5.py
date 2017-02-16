import requests
import sci
import json

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')

print page.content

tags = sci.html_tags(page.content)

# print json.dumps(tags)

# print json.dumps(sci.html_tree(tags))