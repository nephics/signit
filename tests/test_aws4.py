"""Test signing of AWS query strings using the AWS Signature Version 4 algorithm

See:
   http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html

License: MIT License
Copyright (c) 2015-2017 Nephics AB
"""

from __future__ import print_function

import hashlib
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from signit import verify


access = 'AKIAIOSFODNN7EXAMPLE'
secret = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'

request = """GET
/test.txt
X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20130524%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20130524T000000Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host
host:examplebucket.s3.amazonaws.com

host
UNSIGNED-PAYLOAD"""

signed_request = hashlib.sha256(request).hexdigest()

if signed_request != '3bfa292879f6447bbcda7001decf97f4a54dc650c8942174ae0a9121cf58ad04':
    raise Exception('Request signature mismatch')

string2sign = """AWS4-HMAC-SHA256
20130524T000000Z
20130524/us-east-1/s3/aws4_request
{}""".format(signed_request)

date = '20130524'
region = 'us-east-1'
service = 's3'

ok = verify('aeeed9bbccd4d02ee5c0109b86d86835f995330da4c265957d157751f604d404',
            'AWS4' + secret, date, region, service, 'aws4_request', string2sign)

if not ok:
    raise Exception('Signature mismatch')

print('Signature match')
