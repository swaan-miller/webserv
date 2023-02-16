import os

print("HTTP/1.1 200 OK" + "\r")
print("Content-Type: text/html\r\n\r\n")
print("<!doctype html>")
print("<html>")
print("<head>")
print("<title>Environment variables</title>")
print("<style>")
print("body {")
print("background-image: linear-gradient(to right, rgb(241, 202, 252) , white);")
print("font-family: 'Courier New', Courier, monospace;")
print("}")
print("</style>")
print("</head>")
print("<body>")
for k, v in os.environ.items():
	print(k, "=", v)
	print("<br>")
print("</body>")
print("</html>")