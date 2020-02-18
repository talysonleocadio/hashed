from hashlib import sha1


def _convert_from_string_to_byte(unicode_string):
    return unicode_string.encode()


def sha1_hex_digest(string):
    byte_obj = _convert_from_string_to_byte(string)
    return sha1(byte_obj).hexdigest()
