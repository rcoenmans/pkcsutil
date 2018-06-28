# PEM to PKCS12 conversion utility 
A simple PEM to PKCS12 conversion utility written in Python.

## Usage
```console
python pkcsutil.py --key C:\path\to\key.pem --cert C:\path\to\cert.pem --out C:\path\to\cert.pfx
```

## Testing
```console
python -m pytest pkcsutil_test.py
```