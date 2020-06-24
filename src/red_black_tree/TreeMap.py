import time
from enum import Enum


# 节点颜色
class TreeColor(Enum):
    RED = 0
    BLACK = 1


# 红黑树节点
class TreeNode(object):
    __slots__ = ('key', 'value', 'color', 'left', 'right', 'parent')

    def __init__(self, key: int, value):
        self.color = TreeColor.RED
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.value = value


# 获取父节点
def parentOf(node: TreeNode):
    if node is not None:
        return node.parent
    else:
        return None


# 获取兄弟节点
def brotherOf(node: TreeNode):
    node_parent = parentOf(node)
    if node_parent is None:
        return None
    elif node_parent.right == node:
        return node_parent.left
    else:
        return node_parent.right


# 红黑平衡树结构
class TreeMap(object):
    __slots__ = ('balance', 'rootNode', '_step')

    def __init__(self):
        self._step = 0
        self.rootNode = None
        self.balance = False

    def put(self, key: int, value):
        self._insertNode(TreeNode(key, value))

    def remove(self, key: int):
        return self._removeNode(key)

    def get(self, key: int):
        current_node = self.rootNode
        if current_node is None:
            return None
        self._step = 0
        while True:
            self._step += 1
            if current_node.key == key:
                # print("checkNodeCount=" + str(self._step))
                return current_node.value
            elif key > current_node.key:
                if current_node.right is None:
                    return None
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    return None
                else:
                    current_node = current_node.left

    def _isRoot(self, node: TreeNode):
        return node == self.rootNode

    # 移除节点
    def _removeNode(self, remove_key: int):
        remove_node = None
        replace_node = None
        remove_value = None
        # 寻找删除节点
        current_node = self.rootNode
        while True:
            if current_node is None:
                return None
            else:
                if current_node.key == remove_key:
                    remove_node = current_node
                    break
                elif current_node.key > remove_key:
                    current_node = current_node.left
                    continue
                else:
                    current_node = current_node.right
                    continue
        remove_value = remove_node.value
        # 寻找删除节点的代替节点，可能多次定位删除节点
        while True:
            if remove_node.left is not None:
                current_node = remove_node.left
                while True:
                    if current_node.right is not None:
                        current_node = current_node.right
                        continue
                    else:
                        remove_node.key = current_node.key
                        remove_node.value = current_node.value
                        remove_node = current_node
                        break
            elif remove_node.right is not None:
                current_node = remove_node.right
                while True:
                    if current_node.left is not None:
                        current_node = current_node.left
                        continue
                    else:
                        remove_node.key = current_node.key
                        remove_node.value = current_node.value
                        remove_node = current_node
                        break
            else:
                replace_node = remove_node
                break
        # print("replace node " + str(replace_node.key) + ":" + str(replace_node.value))
        #   调整红黑树平衡状态
        self.fixAfterDeletion(replace_node)
        self._dropNode(replace_node)
        return remove_value

    # 插入节点
    def _insertNode(self, add_node: TreeNode):
        if self.rootNode is None:
            self.rootNode = add_node
            add_node.color = TreeColor.BLACK
        else:
            current_node = self.rootNode
            # 寻找插入位置,并插入
            while True:
                if current_node.key == add_node.key:
                    current_node.value = add_node.value
                    break
                elif current_node.key > add_node.key:
                    if current_node.left is None:
                        current_node.left = add_node
                        add_node.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                        continue
                else:
                    if current_node.right is None:
                        current_node.right = add_node
                        add_node.parent = current_node
                        break
                    else:
                        current_node = current_node.right
                        continue
        self.fixAfterInsert(add_node)

    # 对节点做左旋操作
    def rotateLeft(self, current_node: TreeNode):
        if current_node is None:
            return
        current_right = current_node.right
        if current_right is None:
            return
        if current_node.parent is not None:
            if current_node.parent.left == current_node:
                current_node.parent.left = current_right
            else:
                current_node.parent.right = current_right
        current_right.parent = current_node.parent
        current_node.right = current_right.left
        if current_right.left is not None:
            current_right.left.parent = current_node
        current_right.left = current_node
        current_node.parent = current_right

        if current_node == self.rootNode:
            self.rootNode = current_right

    # 对节点做右旋操作
    def rotateRight(self, current_node: TreeNode):
        if current_node is None:
            return
        current_left = current_node.left
        if current_left is None:
            return
        if current_node.parent is not None:
            if current_node.parent.left == current_node:
                current_node.parent.left = current_left
            else:
                current_node.parent.right = current_left
        current_left.parent = current_node.parent
        current_node.left = current_left.right
        if current_left.right is not None:
            current_left.right.parent = current_node
        current_left.right = current_node
        current_node.parent = current_left

        if current_node == self.rootNode:
            self.rootNode = current_left

    # 从树中丢弃节点
    def _dropNode(self, node):
        # print("drop node value: " + str(node.key))
        parent = parentOf(node)
        if parent is not None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            node.parent = None
        if self._isRoot(node):
            self.rootNode = None

    #   移除节点后，调整红黑树平衡状态，移除节点为黑色节点
    def fixAfterDeletion(self, node: TreeNode):
        remove_flag_node = node
        # case1 移除的节点是红色节点，直接移除
        # case2 移除节点是根节点
        if remove_flag_node.color is TreeColor.RED or self._isRoot(remove_flag_node):
            self._dropNode(remove_flag_node)
            return
        # print("remove node:" + str(remove_flag_node.key))
        # 移除的节点是黑色节点
        while True:
            parent: TreeNode = parentOf(remove_flag_node)
            brother: TreeNode = brotherOf(remove_flag_node)
            brother_left: TreeNode = brother.left
            brother_right: TreeNode = brother.right
            if parent is not None and brother is not None:
                if brother.color is TreeColor.BLACK:
                    brother_left_is_red = brother_left is not None and brother_left.color is TreeColor.RED
                    brother_right_is_red = brother_right is not None and brother_right.color is TreeColor.RED
                    if brother_left_is_red or brother_right_is_red:
                        # case 3
                        if parent.left == remove_flag_node:
                            # case 3L
                            # print("case 3L")
                            if brother_right is None:
                                self.rotateRight(brother)
                                brother_left.color = brother.color  # Black
                            else:
                                brother_right.color = brother.color  # Black
                            self.rotateLeft(parent)
                        else:
                            # case 3R
                            # print("case 3R")
                            if brother_left is None:
                                self.rotateLeft(brother)
                                brother_right.color = brother.color  # Black
                            else:
                                brother_left.color = brother.color  # Black
                            self.rotateRight(parent)
                        # 交换旋转后父节点和兄弟节点颜色
                        temp_color = brother.color
                        brother.color = parent.color
                        parent.color = temp_color
                        break
                    else:
                        # case 4
                        # print("case 4")
                        if parent.color is TreeColor.RED:
                            # case 4 PR
                            # print("case 4 PR")
                            parent.color = brother.color
                            brother.color = TreeColor.RED
                            break
                        else:
                            # case 4 PB
                            # print("case 4 PB")
                            brother.color = TreeColor.RED
                            remove_flag_node = parent
                            if self._isRoot(parent):
                                break
                            else:
                                continue
                else:  # brother.color is TreeColor.RED
                    # case 5
                    # print("case 5")
                    # if parent.left == remove_flag_node:
                    #     # case 5L
                    #     # print("case 5L")
                    #     brother.color = TreeColor.BLACK
                    #     self.rotateLeft(parent)
                    #     brother_left.color = TreeColor.RED
                    # else:
                    #     # case 5R
                    #     # print("case 5R")
                    #     brother.color = TreeColor.BLACK
                    #     self.rotateRight(parent)
                    #     brother_right.color = TreeColor.RED
                    # break
                    brother.color = TreeColor.BLACK
                    if parent.left == remove_flag_node:
                        # case 5L
                        # print("case 5L")
                        self.rotateLeft(parent)
                        parent.color = TreeColor.RED
                    else:
                        # case 5R
                        # print("case 5R")
                        self.rotateRight(parent)
                        parent.color = TreeColor.RED
                    continue

    #  插入元素之后，调整红黑树平衡状态
    def fixAfterInsert(self, node: TreeNode):
        current_node = node
        while True:
            if parentOf(current_node) is None:
                return
            current_parent = parentOf(current_node)
            current_uncle = brotherOf(current_parent)
            current_grandpa = parentOf(current_parent)
            if current_parent is not None and current_parent.color is TreeColor.BLACK:
                # print("case break")
                break
            # case 5/6
            if current_parent is not None and current_parent.color == TreeColor.RED:
                if current_uncle is not None and current_uncle.color == TreeColor.RED:
                    if current_grandpa is not None and current_grandpa.color == TreeColor.BLACK:
                        # if current_parent.parent == current_grandpa.left and current_node == current_parent.right:
                        #     print("case5L")
                        #     # case 5L
                        #     self.rotateLeft(current_parent)
                        # elif current_parent.parent == current_grandpa.right and current_node == current_parent.left:
                        #     print("case5R")
                        #     # case 5R
                        #     self.rotateRight(current_parent)
                        # print("case5")
                        current_parent.color = TreeColor.BLACK
                        current_uncle.color = TreeColor.BLACK
                        current_grandpa.color = TreeColor.RED
                        if self._isRoot(current_grandpa):
                            current_grandpa.color = TreeColor.BLACK
                            break
                        else:
                            # self.fixAfterInsert(current_parent)
                            current_node = current_grandpa
                            continue
            # case 2/3
            if current_parent is not None and current_parent.color == TreeColor.RED:
                if current_uncle is None or current_uncle.color == TreeColor.BLACK:
                    if current_grandpa is not None:
                        # if current_parent == current_grandpa.left and current_node == current_parent.right:
                        #     print("case3L")
                        #     # case 3L
                        #     self.rotateLeft(current_parent)
                        # elif current_parent == current_grandpa.right and current_node == current_parent.left:
                        #     print("case3R")
                        #     # case 3R
                        #     self.rotateRight(current_parent)
                        # print("case2")
                        if current_parent.left == current_node:
                            # case 2L
                            self.rotateRight(current_grandpa)
                        else:
                            # case 2R
                            self.rotateLeft(current_grandpa)
                        current_grandpa.color = TreeColor.RED
                        current_parent.color = TreeColor.BLACK
                        break
            # case 1
            if current_grandpa is None:
                if current_parent is not None and current_parent.color == TreeColor.RED:
                    # print("case1")
                    current_parent.color = TreeColor.BLACK
                    break

    def doTraversal(self):
        self._Traversal(self.rootNode)

    # 二叉树前序遍历
    def _Traversal(self, current_node: TreeNode):
        if not checkTreeNodeReference(current_node):
            print("checkTreeNodeReference Fail")
        if current_node is None:
            print("finish")
        else:
            print(str(current_node.value) + "_" + str(current_node.color.name))
            if current_node.left is not None:
                self._Traversal(current_node.left)
            if current_node.right is not None:
                self._Traversal(current_node.right)

    def doMidTraversal(self):
        self._MidTraversal(self.rootNode)

    # 二叉树中序遍历
    def _MidTraversal(self, current_node: TreeNode):
        if current_node is None:
            print("finish")
        else:
            if not (current_node.left is None):
                self._MidTraversal(current_node.left)
            print(str(current_node.value) + "_" + str(current_node.color.name))
            if not (current_node.right is None):
                self._MidTraversal(current_node.right)


def checkTreeNodeReference(current: TreeNode):
    parent = parentOf(current)
    left = current.left
    right = current.right
    if parent is not None:
        if parent.left is not current and parent.right is not current:
            return False
    if left is not None:
        if left.parent is not current:
            return False
    if right is not None:
        if right.parent is not current:
            return False
    return True
