import requests

URL = 'https://api.github.com/repos/CP1404/demos/issues'

response = requests.get(URL)
issues = response.json()
print(issues)
print(type(issues))
for issue in issues:
    print(issue['number'], issue['title'])


# demo_text = """{"number": 1, "title": "demo", "state": "open" }"""
#
# thing = json.loads(demo_text)  # loading with jason
# print(thing)
# print(type(thing))
# print(thing['title'])
# thing['title'] = thing['title'].upper()
# print(thing['title'])
#
# text = json.dumps(thing)
# print(text)
# print(type(text))

