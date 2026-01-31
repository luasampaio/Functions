import requests
import io

response = requests.get("https://lucianasampaio.wordpress.com/")

print('Status code:', response.status_code)
print('↓↓ Header ↓↓')
print(response.headers)

print('\n↓↓ Content ↓↓')
print(response.content)