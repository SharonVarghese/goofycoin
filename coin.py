class Coin(object):
    def __init__(self, message, signature):
        self.message = message 
        self.signature = signature

    def verify_coin(self):
        try: 
        	goofy_public_key = RSA.importKey(open('goofypk.pem').read())
     		h = SHA.new()
			h.update(message)
          verifier = PKCS1_PSS.new(goofy_public_key)
			if verifier.verify(h, self.signature):
				print "The signature is authentic."
			else:
				print "The signature is not authentic."
		except:
			print "An error occured"

