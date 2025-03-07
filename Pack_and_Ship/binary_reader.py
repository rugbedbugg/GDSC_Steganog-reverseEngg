file = "release_UPXdecompressed"

with open(file, "rb") as f:
	output = f.read()

pretty_output = output.decode("ascii", errors="ignore")

print(pretty_output)
