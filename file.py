f=open("test.txt",'r')
print(f.read())
print(f.readline())
print(f.fileno())
print(f.isatty())
print(f.readable())
print(f.readlines())
f.seek(6)
print(f.readline())
print(f.seekable())
print(f.tell())
z=open('test.txt','a')
z.truncate(20)
z.close()
z=open('test.txt','r')
print(z.read())
g=open('test.txt','a')
g.write("see you later")
f.close()
g=open("test.txt",'r')
print(g.read())
print(f.writable())
