import marshal,zlib,base64
exec(zlib.decompress(base64.b64decode("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")))
