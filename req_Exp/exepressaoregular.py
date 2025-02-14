texto = '''
Joao Maria da silva barbosa
joao antonio maria
joao cardoso
'''
import re


print(re.findall(r'joao', texto))
print(re.sub(r'Joao','felipe', texto))
print(re.sub(r'joao', 'felipe', texto))


texto2 = '''
<p> frase 1</p> <p> frase 2 </p> <p> qualquer coisa </p> <div></div>'''

print(re.findall (r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto2))