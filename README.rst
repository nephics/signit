===================================================================================
Signit - Simple cryptographically signing and signature verification using HMAC-256
===================================================================================

With signit you can authenticate strings with a cryptographically signature using HMAC-SHA256. To sign and/or validate a string, you need a pre-shared secret key.

The algorithm is the same as the one used for authenticating AWS requests (`AWS Signature Version 4`_). An example of signing an AWS request is included in the test folder.


Example usage
-------------

Here is an example of creating a hexdigest signature from signing two strings with a secret key::

  import signit

  secret_key = 'wfAlWbCePXJopHhB'
  msg1 = 'A test message'
  msg2 = 'Another test message'

  signature = signit.sign(secret_key, msg1, msg2)

  print('signature =', signature)

  ok = signit.verify(signature, secret_key, msg1, msg2)

  print('ok =', ok)


Running this program in Python 3 results in the following output::

  signature = f0e1e79ce3d672d807c02558fd7dc394aef5b93f4b735a5d246b562ce761c953
  ok = True

As seen from the function definitions, you can pass any number of strings to sign/validate::

  sign(key, s, *args)

  verify(h, key, s, *args)


The package also contains variants of sign and verify for creating signatures as Base64 encoded hash values (instead of hexdigest)::

  sign_b64(key, s, *args)

  verify_b64(h, key, s, *args)


License
-------

The MIT License (MIT)

Copyright (c) 2015 Jacob Sondergaard

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


.. _AWS Signature Version 4: http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html
