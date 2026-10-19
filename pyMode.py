import pyperclip
capter_name = input('What is The Capter Name?: ')
template = \
f'I am learning {capter_name} from Automate The boring stuff with python book, 2e, Help me in this'
pyperclip.copy(template)
print('Copied to clipboard!')

