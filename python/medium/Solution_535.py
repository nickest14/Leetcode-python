# 535. Encode and Decode TinyURL

class Codec:
    def __init__(self):
        self.encode_map = {}
        self.decode_map = {}
        self.base = 'https:/tiny.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.encode_map:
            return self.encode_map[longUrl]
        else:
            shortUrl = self.base + str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = shortUrl
            self.decode_map[shortUrl] = longUrl
            return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map.get(shortUrl, "")


url = 'https://leetcode.com/problems/design-tinyurl'
codec = Codec()
ans = codec.decode(codec.encode(url))
print(ans)
