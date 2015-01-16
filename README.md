pybaco
======

Python Base Converter


* Converts any base to any base
* Provides some shortcuts, like:
    * to_bin
    * to_oct
    * to_hex
    * to_36
    * to_62

``` python
from string import digits
from pybaco import Baco

b = Baco(number=18, alphabet=digits)
# You need to pass the alphabet you want to convert, in this case, '01' (binary)
b.convert('01') # 10010

# Shortcuts
Baco.to_bin(18) # 10010
Baco.to_oct(18) # 22
Baco.to_hex(15) # f
Baco.to_36(123456789) # 21i3v9
Baco.to_62(123456789) # 8M0kX
```
