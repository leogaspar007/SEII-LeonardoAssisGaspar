# f = open("test.txt", "r")
# f = open("test.txt", "w")
# f = open("test.txt", "a")
# f = open("test.txt", "r+")
# print(f.name)
# print(f.mode)
# f.close()

# with open("test.txt", "r") as f:
#     pass

#     f_contents = f.read()
#     print(f_contents)

#     f_contents = f.readlines()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents)
#     f_contents = f.readline()
#     print(f_contents)

#     f_contents = f.readline()
#     print(f_contents, end='')
#     f_contents = f.readline()
#     print(f_contents, end='')

#     for line in f:
#         print(line, end='')

#     f_contents = f.read()
#     print(f_contents, end='')

#     f_contents = f.read(100)
#     print(f_contents, end='')
#     f_contents = f.read(100)
#     print(f_contents, end='')
#     f_contents = f.read(100)
#     print(f_contents, end='')

#     size_to_read = 100
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents)
#         f_contents = f.read(size_to_read)

#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#     f.seek(0)
#     f_contents = f.read(size_to_read)
#     print(f_contents, end='')
#     print(f.tell())
#     while len(f_contents) > 0:
#         print(f_contents, end='*')
#         f_contents = f.read(size_to_read)
# print(f.mode)
# print(f.closed)
# print(f.read())

# with open("test.txt", "r") as f:
#     f.write("Test")

# with open("test2.txt", "w") as f:
#     pass
#     f.write("Test")
#     f.seek(0)
#     f.write("Test")
#     f.seek("R")

# with open("test.txt", "r") as rf:
#     with open("test_copy.txt", "w") as wf:
#         for line in rf:
#             wf.write(line)

# with open("bronx.jpg", "r") as rf:
#     with open("Foto de perfil.jpeg", "w") as wf:
#         for line in rf:
#             wf.write(line)

# with open("bronx.jpg", "rb") as rf:
#     with open("Foto de perfil.jpeg", "wb") as wf:
#         for line in rf:
#             wf.write(line)

with open("Foto de perfil.jpeg", "rb") as rf:
    with open("Foto de perfil_copy.jpeg", "wb") as wf:
        chunk_size = 4096
    rf_chunk = rf.read(chunk_size)
    while len(rf_chunk) > 0:
        wf.write(rf_chunk)
        rf_chunk = rf.read(chunk_size)
