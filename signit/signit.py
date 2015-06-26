"""Simple cryptographically signing and signature verification using HMAC-256

License: MIT License
Copyright (c) 2015-2017 Nephics AB
"""

import base64
import hmac
import hashlib


if type('') is not type(b''):
	unicode_type = str
else:
	unicode_type = unicode


_enc = lambda s: s.encode() if isinstance(s, unicode_type) else s


def _hmac_sha256(key, s):
	return hmac.new(key=_enc(key), msg=_enc(s), digestmod=hashlib.sha256)


def _sign(key, s, *args):
	"""HMAC-SHA256 signed hash of one or more strings signed with key string.
	"""
	signed_hash = _hmac_sha256(key, s)
	for value in args:
		signed_hash = _hmac_sha256(signed_hash.digest(), value)
	return signed_hash


def sign(key, s, *args):
	"""Hex digest of the HMAC-SHA256 signature of one or more strings
	signed with key string.
	"""
	return _sign(key, s, *args).hexdigest()


def sign_b64(key, s, *args):
	"""Base 64 encoded digest of the HMAC-SHA256 signature of
	one or more strings signed with key string.
	"""
	return base64.b64encode(_sign(key, s, *args).digest())


def verify(h, key, s, *args):
	"""Verify that hash string h is the hex digest of the
	HMAC-SHA256 signature of one or more strings signed with key string.
	"""
	return h == sign(key, s, *args)


def verify_b64(h, key, s, *args):
	"""Verify that hash string h is the base 64 encoded digest of the
	HMAC-SHA256 signature of one or more strings signed with key string.
	"""
	return h == sign_b64(key, s, *args)
