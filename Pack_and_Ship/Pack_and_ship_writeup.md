# Introduction
This is in continuation with the "Hidden Pixels" task. We are provided with a executable file. Opening the file with a text editor reveals to us that the file has been packed with UPX.

![release_packed_with_UPX.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/release_packed_with_UPX.png)

Kali Purple comes pre-installed with ```upx-ucl```, the exact tool used to to pack this executable and can also be used to unpack it. A quick read through its manual by typing ```upx-ucl -h``` gives enough information to write a command to unpack the file.

![unpacking_release.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/unpacking_release.png)

Upon reopening the uncompressed executable with a text editor we get to see some sort of code refering to entering a password. 

![unpacked_release_in_text.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/unpacked_release_in_text.png)

Lets try running the executable to see how it behaves

![running_uncompressed_release.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/running_uncompressed_release.png)

My best guess is to look into its source code, as this is the only logical thing to do, but not in the way that I did. I wrote a script to output the hex equivalent of the binary file. Lord knows what I was expecting.

![tried_to_read_the_binary_and_almost died.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/tried_to_read_the_binary_and_almost%20died.png)

Yeah... thats not very nice on the eyes. Although with a little bit of effort we can see the mention of an ```obfuscated password``` and ```obfuscated flag```. We will need a better format to read this file.

### 1. UTF-8
* * *
```
file = "release_UPXdecompressed"

with open(file, "rb") as f:
        output = f.read()

pretty_output = output.decode("utf-8", errors="ignore")

print(pretty_output)
```
Running the above code we get the following output

![binary_utf_8_version.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/binary_utf_8_version.png)

### 2. ASCII
* * *
```
file = "release_UPXdecompressed"

with open(file, "rb") as f:
        output = f.read()

pretty_output = output.decode("ascii", errors="ignore")

print(pretty_output)
```
Similarly we try ASCII as well

![binary_ascii_version.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/binary_ascii_version.png)

### 3. Assembly Language
* * *
Both of them look almost readable but not clear enough. Good for me I learnt assembly language. Lets try to disassemble the program. Linux again comes with a built-in functionality to disassemble a program. The command is
``` objdump -d release_UPXdecompressed | less ```

The ```less``` at the end of the command hlpe

[the_answer_is_assembly.mp4](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/the_answer_is_assembly.mp4)

This is what we were looking. Notice that we can again see a few lines written with comments like obfuscated flag and obfuscated password. It is difficult to analyze the program like this so we will convert this into the equivalent C code. this should finally do the trick. We use the pre-installed tool called ```Ghidra``` to interactively analyse the diassembled code.

![ghidra_analysis.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/ghidra_analysis.png)

We get this very cool looking interface to work with. On the right is the equivalent C code which we can understand better than the aseembly code in the middle. Our task now is to find out the password and the flag. But first we have reverse engineer this obfuscated C code. This is what the code looks like right now.

![obfuscated_decompiled_C_version.png](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/obfuscated_decompiled_C_version.png)

We can make this code better by renaming variables into meaningful ones. After a painstakingly long session, I came up with this

![reverse_engineered_code.jpeg](https://github.com/rugbedbugg/GDSC_Steganog-reverseEngg/blob/master/Pack_and_Ship/documented_media/reverse_engineered_code.jpeg)

Now the code is much clearer. We can see that there is a reference to the ```FLAG``` variable. One mention of this is where there is the instruction 

```LEA INPUT_MATCH->FLAG [RBP -0x]```
