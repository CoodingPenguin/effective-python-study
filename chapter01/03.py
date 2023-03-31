# BETTER WAW 3. bytes와 str의 차이를 알아두라

a = b'h\x65llo'
print(list(a))  # [104, 101, 108, 108, 111]
print(a)        # b'hello'


b = 'a\u0300 propos'
print(list(b))  # ['a', '̀', ' ', 'p', 'r', 'o', 'p', 'o', 's']
print(b)        # à propos


def to_str(bytes_or_str: bytes | str) -> str:
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_str(b'foo')))             # 'foo'
print(repr(to_str('bar')))              # 'bar'
print(repr(to_str(b'\xed\x95\x9c')))    # '한' (UTF-8에서 한글은 3바이트)


def to_bytes(bytes_or_str: bytes | str) -> bytes:
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

print(repr(to_bytes(b'foo')))   # b'foo'
print(repr(to_bytes('bar')))    # b'bar'
print(repr(to_bytes('한글')))    # b'\xed\x95\x9c\xea\xb8\x80'


print(b'one' + b'two')  # b'onetwo'
print('one' + 'two')    # onetwo
# print(b'one' + 'two') # TypeError: can't concat str to bytes


assert b'red' > b'blue'
assert 'red' > 'blue'
# assert 'red' > b'blue'    # TypeError: '>' not supported between instances of 'str' and 'bytes'


print(b'foo' == 'foo')  # False


print(b'red %s' % b'blue')  # b'red blue'
print('red %s' % 'blue')    # red blue
# print(b'red %s' % 'blue')   # TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'str'