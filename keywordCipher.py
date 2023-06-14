alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generateSubstitutes(keyword: str, alphabests: str) -> str:
  return keyword + ''.join([x for x in alphabets if x not in keyword])

def keyWordCiphering(text: str, substitutes: str) -> str:
  text = ''.join(text.split()).upper()
  return ''.join([substitutes[alphabets.index(ch)] for ch in text])

print(keyWordCiphering('Rose', generateSubstitutes('THURSDAY', alphabets)))