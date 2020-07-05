"""
11. Create a variable, filename. Assuming that it has a three-letter
extension, and using slice operations, find the extension. For
README.txt, the extension should be txt. Write code using slice
operations that will give the name without the extension. Does your
code work on filenames of arbitrary length?
"""
filename = str(input("Enter a file name with extension:")) or "README.txt"
extensionRemover = slice(0, -4)
extensionRemovedName = filename[extensionRemover]
print("Original FileName:", filename)
print("Actual filename:", extensionRemovedName)

# The code does not work on arbitrary length if the extension is of different length.
filename2 = "Assignment.docx"
extensionRemovedName2 = filename2[extensionRemover]
print("Original FileName 2:", filename2)
# The filename fails to omit the "." which shows it is not suitable for arbitrary length.
print("Actual filename 2:", extensionRemovedName2)

