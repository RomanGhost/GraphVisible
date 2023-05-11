from geometric import *
import config

f1 = Figure()
f1.appendPoint(Point(1, 7))
f1.appendPoint(Point(1, 10))
f1.appendPoint(Point(2, 8))
f1.appendPoint(Point(2, 9))
f1.appendPoint(Point(3, 10))
f1.appendPoint(Point(3, 5))

f1.appendException(Line(Point(1.4, 9.2), Point(3.1, 10.2)))
f1.appendException(Line(Point(1.99, 8.01), Point(1, 12)))

f2 = Figure()
f2.appendPoint(Point(7, 5))
f2.appendPoint(Point(7, 7))
f2.appendPoint(Point(10, 7))
f2.appendPoint(Point(10, 3))
f2.appendPoint(Point(9, 3))
f2.appendPoint(Point(9, 6))
f2.appendPoint(Point(8, 6))
f2.appendPoint(Point(8, 5))

f2.appendException(Line(Point(8.001, 5.999), Point(8.5, 2)))

f3 = Figure()
f3.appendPoint(Point(3, 3))
f3.appendPoint(Point(3, 4))
f3.appendPoint(Point(7, 4))
f3.appendPoint(Point(7, 2))
f3.appendPoint(Point(4, 2))
f3.appendPoint(Point(4, 3))

f3.appendException(Line(Point(3.9, 2.9), Point(3, 2)))

f4 = Figure()
f4.appendPoint(Point(7, 11))
f4.appendPoint(Point(11, 11))
f4.appendPoint(Point(10, 8))

f5 = Figure()
f5.appendPoint(Point(11, 1))
f5.appendPoint(Point(11, 4))
f5.appendPoint(Point(13, 4))
f5.appendPoint(Point(13, 1))

f6 = Figure()
f6.appendPoint(Point(13, 8))
f6.appendPoint(Point(12, 9))
f6.appendPoint(Point(12, 10))
f6.appendPoint(Point(13, 11))
f6.appendPoint(Point(14, 10))
f6.appendPoint(Point(14, 9))

f7 = Figure()
f7.appendPoint(Point(11, 5))
f7.appendPoint(Point(13, 5))
f7.appendPoint(Point(13, 7))

f8 = Figure()
f8.appendPoint(Point(14, 2))
f8.appendPoint(Point(14, 3))
f8.appendPoint(Point(17, 3))
f8.appendPoint(Point(17, 2))

f9 = Figure()
f9.appendPoint(Point(15, 9))
f9.appendPoint(Point(18, 9))
f9.appendPoint(Point(17, 8))
f9.appendPoint(Point(17, 6))

f9.appendException(Line(Point(17.1, 7.9), Point(18, 7)))

f10 = Figure()
f10.appendPoint(Point(15, 5))
f10.appendPoint(Point(15, 6))
f10.appendPoint(Point(16, 6))
f10.appendPoint(Point(16, 5))

f11 = Figure()
f11.appendPoint(Point(18, 3))
f11.appendPoint(Point(19, 6))

f_test = Figure()
f_test.appendPoint(Point(7, 10))
f_test.appendPoint(Point(8, 5))
f_test.appendPoint(Point(11, 6))
f_test.appendPoint(Point(13, 4))
f_test.appendPoint(Point(14, 11))
figures = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11]
# figures = [f_test]
# figures = [f1, f2, f3, f4, f5, f6, f7, f8]
start_point = Point(6, 8)
finish_point = Point(14, 6)

str_points = ""
str_diagonals = ""
str_lines = ""

for f in figures:
    for p in f.points:
        str_points += f"{p};"

    for r in f.ribs:
        str_lines += f"{r};"

    for d in f.createDiagonals():
        str_diagonals += f"{d};"

print("Data get!")

print("Clear")
with open(config.cache_line, "w") as f:
    f.write('')

print("Write to file...")
with open(config.cache_line, "a") as file:
    file.write(f"{start_point}, {finish_point}\n")
    file.write(str_points[:-1])
    file.write('\n')

    file.write(str_lines[:-1])
    file.write('\n')

    file.write(str_diagonals[:-1])
    file.write('\n')


print("Write is done")
