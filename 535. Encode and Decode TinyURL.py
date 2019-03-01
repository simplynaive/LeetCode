class Codec:
    def __init__(self):
        self.urls = []
        self.i = -1

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        self.i += 1
        return "http://tinyurl.com/" + str(self.i)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return str(self.urls[int(shortUrl.split('/')[-1]) - 1])


if __name__ == "__main__":
    codec = Codec()
    print(codec.encode('http://tinyurl.com/asdvasd'))
    print(codec.decode('http://tinyurl.com/1'))

# JAVA
# public
#
#
# class Codec {
# Map < Integer, String > map = new HashMap <> ();
# int i = 0;
#
# // Encodes a URL to a shortened URL.
# public String encode(String longUrl) {
# map.put(i, longUrl);
#
#
# return "http://tinyurl.com/" + i + +;
# }
#
# // Decodes
# a
# shortened
# URL
# to
# its
# original
# URL.
#     public
# String
# decode(String
# shortUrl) {
# return map.get(Integer.parseInt(shortUrl.replace("http://tinyurl.com/", "")));
# }
# }