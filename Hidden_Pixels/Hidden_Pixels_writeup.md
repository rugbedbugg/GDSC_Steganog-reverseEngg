# Introduction
This challenge consists of us trying to extract information from a ```.bmp``` image file
Analysing the properties of the image tells us a few things. Here are checksums we get from the ```Properties``` tab of the file.

**MD5 checksum**: 9f9e265a87a6ed024e6c7fc4289fbc74
**SHA256 checksum**: 53c7ddbf269ea3dcb2c22e73c09a0f597fb302677a59c846102a206a9db72b90e
**SHA1 checksum**: d01beb8627c5427c482593ee30568eb75258e2c6
**CRC32 checksum**: 88a74491

We were also provided with the **SHA256** checksum of the as a part of the challenge
```SHA256: 53c7ddbf269ea3dcb2c22e73c09a0f597fb302677a59c846102a206a9db72b9e```

We can run them through a simple program to check for dissimilarities
```
expected = "53c7ddbf269ea3dcb2c22e73c09a0f597fb302677a59c846102a206a9db72b90e"

received = "53c7ddbf269ea3dcb2c22e73c09a0f597fb302677a59c846102a206a9db72b9e"

mismatch = 0
longer = max([expected, received])
for i in range(len(longer)):
        if (i != 0) & (expected[i] != received[i]):
                print(f"Hash mismatch at char {i+1}")
                mismatch = 1
if mismatch:
        print("Original hash and received hash don't match. The file you received may be been tampered with.")

print(f"Received: {received}")
print(f"Expected: {expected}")
```

## Output:
![hash_match_output.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Hidden_Pixels/hash_match_output.png)

The received and expected hashes dont match the one recieved along with the challenge has one byte less character than the expected 32 bytes (1 byte or 8 bits for each character).

As we have discrepancies we should search for more information using scripts:

```
import os

# Define the file path
file_path = "output.bmp"

# Get file properties
file_properties = {
    "File_Size (bytes): ": os.path.getsize(file_path),
    "File_Type: ": os.popen(f'file "{file_path}"').read().strip(),,
	"SHA256 Hash:": os.popen(f'SHA256 checksum "{file_path}"').read().split()
}

for property in file_properties:
	print(property, file_properties[property])
```

## Output:
![more_info.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Hidden_Pixels/more_info.png)
This time the script did not find the SHA256 checksum of the file.

## Another approach (Steganography)

We have a bitmap image file with some noise at the top of the image. Maybe there is some hidden data in this image. We can try tools like ```steghide``` or ```outguess``` on Linux to extract this data but both dont support ```.bmp```. This led me think of possible file conversions. I looked it up online as got to know that ```.png``` and ```.bmp``` file are lossless in nature and hence donot loose the encoded message within them.

Naturally my next idea was to convert the ```.bmp``` file to a ```.png``` file to see we could extract data from there but turns out even PNG is not supported by many steganograpgy tools. 

![output.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Hidden_Pixels/output.png)

Although I read that ```.jpeg``` files has lossy encoding I decided to give it a shot and converted the ```.png```  file into a ```.jpeg``` file. Surprisingly, the image cleared up to show a still obfuscated but visible second part of the image.

It seems like the noise was added on top of the image.

![output.jpeg](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Hidden_Pixels/output.jpeg)

The image somehow now looks ready for extracting the encoded data, judging from the uniform stripes in the noise. Lets see what happens.

![steg_hide_needs_passphrase.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Hidden_Pixels/steg_hide_needs_passphrase.png)

It needs a passphrase, ofcourse. I tried using the missing character of the received SHA sum , i.e. ```0``` but that didnt work. I tried all the checksums I found from the file but they didnt work either. Maybe this is related to the other challenge, as suggested by the word ```CTF```. 
