import base64
from time import sleep
import winsound
# Play Windows exit sound.
with open('click.wav','rb') as f:
  wav = f.read()

data = '''Hello there Nina.

def foo(bar):
  return bar
  
foo(123)

Now is the time
for all good people
to come to the aid
of their planet.



'''
winsound.PlaySound('click.wav', winsound.SND_FILENAME)

for letter in list(data):
  s = str(letter)
  if s.isalpha():
    if s.islower():
      delay = 0.01
    else:
      delay = 0.05
  elif s.isdigit():
    delay = 0.020
  else:
    delay = 0.55

  sleep(delay)

  print(letter, end="", flush=True)

  winsound.PlaySound(wav, winsound.SND_MEMORY)



# winsound.PlaySound('click.wav', winsound.SND_FILENAME)

