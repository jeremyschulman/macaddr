# macaddr

As a network engineer you many have to deal with MAC address values.  In some
cases a network operating system wants the MAC address in a particular format. 
The following are common formats:

    * aa:bb:cc:dd:ee:ff
    * aabb-ccdd-eeff
    * aabb.ccdd.eeff

As well as their upper-case variants, AA:BB:CC:DD:EE:FF for example.

This package provides the `MacAddress` class definition and a supporting `format`
method that allows you to develop programs using a MAC address in different formats.

# Installation
```shell
pip install macaddr
```
# Usage

By default the MacAddress is formated in the "2 byte colon separated" format.


```python
from macaddr import MacAddress

mac = MacAddress("aabb.ccdd.eeff")
print(mac)
```
```shell
aa:bb:cc:dd:ee:ff
```

You can obtain differnt formats using the `format` method.

```python
from macaddr import MacAddress

mac = MacAddress("aabb.ccdd.eeff")
print(mac.format(size=4, sep='-', to_case=str.upper))
```
```shell
AABB-CCDD-EEFF
```

The `format` method values are cached so that repeated calls to `format` with
the same arguments return the cached value.  For example, if you had a network
of 1000 devices, 500 of them required the "2-colon" format and 500 of them
required the "4-dot" format, then these two formats are only computed twice.