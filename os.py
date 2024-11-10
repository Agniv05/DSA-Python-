import os

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)

# Close the file


# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)


# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']


# Create a new directory
os.mkdir("newdir")


# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']


# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()

f = open('myfile.txt', 'r')
contents = f.read()
print(contents)


# Readlines
f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)

# Writelined
f = open('myfile.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

with open('file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)

  # Read the next 5 bytes
  data = f.read(5)


with open('file.txt', 'r') as f:
  # Read the first 10 bytes
  data = f.read(10)

  # Save the current position
  current_position = f.tell()

  # Seek to the saved position
  f.seek(current_position)

  with open('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)

#  When you open a file in Python using the open function,
#  you can specify the mode in which you want to open the 
#  file. If you specify the mode as 'w' or 'a', the file 
#  is opened in write mode and you can write to the file.
#  However, if you want to truncate the file to a specific 
#  size, you can use the truncate function.

with open('sample.txt', 'r') as f:
  print(f.read())

