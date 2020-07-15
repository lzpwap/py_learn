import time

from TreeMap import TreeMap

tree_map = TreeMap()
hash_map = dict()
tree_map.balance = True

# print("add4-----------------------")
# tree_map.put(4, "4")
# print("add5-----------------------")
# tree_map.put(5, "5")
# print("add1-----------------------")
# tree_map.put(1, "1")
# print("add2-----------------------")
# tree_map.put(2, "2")
# print("add6-----------------------")
# tree_map.put(6, "6")
# print("add3-----------------------")
# tree_map.put(3, "3")
# print("add7-----------------------")
# tree_map.put(7, "7")

# print("add1-----------------------")
# tree_map.put(1, "1")
# print("add2-----------------------")
# tree_map.put(2, "2")
# print("add3-----------------------")
# tree_map.put(3, "3")
# print("add4-----------------------")
# tree_map.put(4, "4")
# print("add5-----------------------")
# tree_map.put(5, "5")
# print("add6-----------------------")
# tree_map.put(6, "6")
# print("add7-----------------------")
# tree_map.put(7, "7")
# print("add8-----------------------")
# tree_map.put(8, "8")
# print("add100-----------------------")
# tree_map.put(100, "100")

timeStart = time.time()
for i in range(10000000):
    # print("add" + str(i) + "-----------------------")
    hash_map[i] = str(i)
timeEnd = time.time()
print("dict insert use Time=" + str(timeEnd - timeStart))

timeStart = time.time()
for i in range(10000000):
    if hash_map[i] != str(i):
        print("dict value error")
timeEnd = time.time()
print("dict get use Time=" + str(timeEnd - timeStart))

# timeStart = time.time()
# for i in range(10000000):
#     # print("add" + str(i) + "-----------------------")
#     tree_map.put(i, str(i))
# timeEnd = time.time()
# print("treeMap insert use Time=" + str(timeEnd - timeStart))
# #
# timeStart = time.time()
# for i in range(10000000):
#     # print("add" + str(i) + "-----------------------")
#     tree_map.get(i)
# timeEnd = time.time()
# print("treeMap find use Time=" + str(timeEnd - timeStart))



# print("remove------------------0")
# tree_map.remove(0)
# print("remove------------------1")
# tree_map.remove(1)
# print("remove------------------2")
# tree_map.remove(2)
# print("remove------------------3")
# tree_map.remove(3)
# print("remove------------------4")
# tree_map.remove(4)
# print("remove------------------5")
# tree_map.remove(5)


# print("中序遍历------------------")
# tree_map.doMidTraversal()
print("前序遍历-----------------")
# tree_map.doTraversal()

tree_map.get(10000000)
print("check")

# print("查找值100")
# print(tree_map.get(100))
# print("查找值1")
# print(tree_map.get(1))
# print("查找值2")
# print(tree_map.get(2))
# print("查找值3")
# print(tree_map.get(3))
# print("查找值4")
# print(tree_map.get(4))
# print("查找值7")
# print(tree_map.get(7))
# print("查找值999")
# print(tree_map.get(999))