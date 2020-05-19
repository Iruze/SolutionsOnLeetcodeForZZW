"""
python3, 利用异或性质:

如果a ^ b = c, 则a ^ c = b, b ^ c = a:
"""

class Codec:
    def __init__(self):
        # 取素数
        self.BASE = 1999

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        ret = ['' for _ in range(len(longUrl))]
        for i, c in enumerate(longUrl):
            ret[i] = chr(self.BASE ^ ord(c))
        return ''.join(ret)

        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # 这四行跟encode一样，除了改longUrl为shortUrl
        ret = ['' for _ in range(len(shortUrl))]
        for i, c in enumerate(shortUrl):
            ret[i] = chr(self.BASE ^ ord(c))
        return ''.join(ret)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
