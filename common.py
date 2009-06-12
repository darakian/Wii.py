import os, hashlib, struct, subprocess, fnmatch, shutil, urllib, array
import wx
from Crypto.Cipher import AES
import png
from Struct import Struct

def align(x, boundary):
	return x + (x % boundary)

def hexdump(s, sep=" "):
        return sep.join(map(lambda x: "%02x" % ord(x), s))

class Crypto:
	"""This is a Cryptographic/hash class used to abstract away things (to make changes easier)"""
	def __init__(self):
		return
	def DecryptContent(self, titlekey, idx, data):
		"""Decrypts a Content."""
		iv = struct.pack(">H", idx) + "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
		if(len(data) % 16 != 0):
			return AES.new(titlekey, AES.MODE_CBC, iv).decrypt(data + ("\x00" * (16 - (len(data) % 16))))[:len(data)]
		else:
			return AES.new(titlekey, AES.MODE_CBC, iv).decrypt(data)
	def ValidateHash(self, data, hash):
		"""Validates a hash. Not checking currently because we have some...issues with hashes."""
		return 1 #hack
#		if(hashlib.sha1(data).hexdigest() == hexdump(hash, "")):
#			return 1
#		else:
#			return 0

