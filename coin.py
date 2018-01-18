from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA


class Coin(object):
	def __init__(self, message, signature):
		self.message = message
		self.signature = signature

	def verify_coin(self):
		try:
			goofy_public_key = RSA.importKey(open('goofypk.pem').read())
			sha_hash = SHA.new()
			sha_hash.update(self.message)
			verifier = PKCS1_PSS.new(goofy_public_key)
			if verifier.verify(sha_hash, self.signature):
				print "The signature is authentic."
			else:
				print "The signature is not authentic."
		except:
			print "An error occured"

