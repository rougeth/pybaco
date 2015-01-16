pybaco
======

Python Base Converter - Converts any base to any base

**Installing**
```
$ pip install pybaco
```

**Usage**
``` python
from string import digits
from pybaco import Baco, base2, base10, base16

b = Baco(18, base10)
# You need to pass the alphabet you want to convert, in this case, '01' (binary)
b.convert(base2) # 10010

# Shortcuts
Baco.to_bin(18) # 10010
Baco.to_oct(18) # 22
Baco.to_hex(15) # f
Baco.to_36(123456789) # 21i3v9
Baco.to_62(123456789) # 8M0kX

# Specifing the origin base
Baco.to_bin(15, base16) # 1111
Baco.to_62('abc', base16) # ik

```
