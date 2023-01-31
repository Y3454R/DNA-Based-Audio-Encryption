from cryptography.fernet import Fernet
import matplotlib.pyplot as plt
from scipy.io import wavfile

key = Fernet.generate_key()
fernet = Fernet(key)

with open('key.key', 'wb') as keyfile:
    keyfile.write(key)

with open('dog.wav', 'rb') as audio:
    original = audio.read() 

fs, input = wavfile.read('dog.wav')
plt.plot(input)

encrypted = fernet.encrypt(original)

with open('encrypted check.mp3', 'wb') as audio:
    audio.write(encrypted)

with open('encrypted check.mp3', 'rb') as audio:
    encrypted_file = audio.read()

decrypted = fernet.decrypt(encrypted_file)

with open('decrypted check.mp3', 'wb') as audio:
    audio.write(decrypted)

