import random
from coin import Coin
from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

class Goofy:

	def generate_goofy_key(self):
		key = RSA.generate(2048)
		s = open('goofysk.pem','w')
		s.write(key.exportKey('PEM'))
		s.close()
		p= open('goofypk.pem','w')
		p.write(key.publickey().exportKey('PEM'))
		p.close()

	def read_goofy_key(self):
		privkey = RSA.importKey(open('goofysk.pem').read())
		pubkey = RSA.importKey(open('goofypk.pem').read())
		return privkey, pubkey

	def create_coin(self):
		self.generate_goofy_key()
		coin_id = str(random.getrandbits(256))
		message = 'Create coin %s'%coin_id
		coin_signature = self.sign_coin(message)
		coin = Coin(message,coin_signature)
		return coin 

	def sign_coin(self,message):
		privkey,pubkey = self.read_goofy_key()
		h = SHA.new()
		h.update(message)
		signer = PKCS1_PSS.new(privkey)
		signature = signer.sign(h)
		return signature
	

if __name__=='__main__':
	goofy = Goofy()
	coin = goofy.create_coin()
	print coin.message









