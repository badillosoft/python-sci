import requests
import sci
import json

content = """
<!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		<div>
			<div>
				<a href="url1"/>
				<a href="url2">
				<a href="url3">Contenido</a>
			</div>
			<a href="url4"/>
			<a href="url5">
			<a href="url6">Contenido</a>
		</div>
		<div>
			<div>
				<a href="url7"/>
				<a href="url8">
				<a href="url9">Contenido</a>
			</div>
			<a href="url10"/>
			<a href="url11">
			<a href="url12">Contenido</a>
		</div>
	</body>
</html>
"""

tags = sci.html_tags(content)

# print json.dumps(tags)

print json.dumps(sci.html_tree(tags))