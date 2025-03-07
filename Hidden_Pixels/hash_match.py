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
