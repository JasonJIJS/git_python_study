print("test", "test1", sep=" ")
print("test" + "test1")

print("%s %d" %('test',10))

a= 0.123456789
print("{0:.2f}, {0:.5f}".format(a))

print("{:2d}".format(3))
print("{:02d}".format(3))
print("{:>5d}".format(12))
print("{:.3f}".format(3))
print("{:,}".format(3000000))
print("{:2e}".format(925000000))
print("{:.1%}".format(0.33))
print("{0:#x}, {1:#o}, {2:#b}".format(16,8,2))

