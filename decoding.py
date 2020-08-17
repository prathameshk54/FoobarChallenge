import base64

MESSAGE = '''
EFIfHgIRCxpdV1JbVE8GHwASHAlfS1IPBA0eCwhJBRdGVFJBSgAAHEsWBhAITE1SSQxIFh0TABtG TV9TT0cdCAcJDwgQAgwJXFJGFQsJBAAFDUMWBQFLS1tSSRxAHB0CHw0FSklTT1wSCRcFHxJVTlMO VwEAEg1GQUVUDkEcTFVWS0YFBwcPVw8=
'''

KEY = 'kulkarni.prathamesh.s'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
	result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))
