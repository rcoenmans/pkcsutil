# PEM to PKCS12 conversion utility 
A simple PEM to PKCS12 (PFX) conversion utility written in Python.

## Usage
You can run `pkcsutil` from the command prompt. Provide the path/filename of the certificate file, private key (both PEM encoded) and the output file. You will also need to provide the passphrase for the private key which will also be used to password-protect the output file. 
```console
python pkcsutil.py --cert C:\path\to\cert.pem 
                   --key C:\path\to\key.pem 
                   --passphrase PassPhraseOfPrivateKey 
                   --out C:\path\to\cert.pfx
```

## Testing
In order to run the tests you will need a valid private key and certificate file.
```
pkcsutil
|-- minica-key.pem
|-- minica.pem
|-- pkcsutil_test.py
|-- pkcsutil.py

python -m pytest pkcsutil_test.py
```