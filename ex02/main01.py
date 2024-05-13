
def count_letters():
  RECEIVED = input("Informe a palavra:")
  uppercase = [key for key in RECEIVED if key == key.upper()]
  lowercase = [key for key in RECEIVED if key != key.upper()]
  return (len(uppercase), len(lowercase))

print(count_letters())

def count_oddAndPair(*args):
  pair = [k for k in args if k % 2 == 0]
  odd = [k for k in args if k % 2 != 0]
  return f"Existem {len(pair)} números pares e existem {len(odd)} ímpares"

print(count_oddAndPair(21920,92,12,2,24,3,553,3,63,73,73,3,3,3,3))