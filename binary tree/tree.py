class _Node:
    def __init__(self, key, data, left=None, right=None):
        if type(key).__name__ != 'int':
            raise ValueError
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self, data=None):
        """ Takes 'dict' as data. Only 'int' can be a key """
        self.head = None
        self.size = 0
        if data is not None:
            self.append(data)

    def append(self, data):
        """ Adds element to the tree. Takes 'dict' as data. Can take 'dict' with many values."""
        if type(data).__name__ == 'dict':
            values = list(data)
            if len(values) == 0 or not all(isinstance(x, int) for x in values):
                raise TypeError
            if self.head is None:
                self.head = _Node(values[0], data[values[0]])
                self.size += 1
                values.remove(values[0])
            if len(values) > 0:
                for i in range(len(values)):
                    temp = self.head
                    while temp is not None:
                        if temp.key > values[i]:
                            if temp.left is None:
                                temp.left = _Node(values[i], data[values[i]])
                                self.size += 1
                                break
                            else:
                                temp = temp.left
                        elif temp.key < values[i]:
                            if temp.right is None:
                                temp.right = _Node(values[i], data[values[i]])
                                self.size += 1
                                break
                            else:
                                temp = temp.right
                        else:
                            raise ValueError
        else:
            raise TypeError

    def __len__(self):
        return self.size

    def _see_next(self, temp, list):
        if temp is None:
            return
        self._see_next(temp.left, list)
        list.append(f'{temp.key}: {temp.data}')
        self._see_next(temp.right, list)

    def _see(self):
        temp = self.head
        if temp is None:
            str = "{}"
        else:
            list = []
            self._see_next(temp, list)
            str = "{"
            for i in list:
                str += i + ', '
            else:
                str = str[:-2]
                str += '}'
        return str

    def __str__(self):
        return self._see()

    def clear(self):
        self.head = None

    def get(self, key):
        if type(key).__name__ != 'int':
            raise TypeError
        temp = self.head
        return self._get(key, temp)

    def _get(self, key, temp):
        if temp is None:
            raise KeyError
        if temp.key == key:

            return temp.data
        else:
            if key < temp.key:
                return self._get(key, temp.left)
            else:
                return self._get(key, temp.right)

    def __getitem__(self, key):
        return self.get(key)

    def erase(self, key):
        if type(key).__name__ != 'int':
            raise TypeError
        if len(self) is 0:
            raise ValueError
        temp = self.head
        if temp.key == key:
            if len(self) == 1:
                self.head = None
                self.size = 0
            else:
                if self.head.left is not None and self.head.right is None:
                    self.head.data = self.head.left.data
                    self.head.ley = self.head.left.key
                    self.head.right = self.head.left.right
                    self.head.left = self.head.left.left
                else:
                    self.head.data = self.head.right.data
                    self.head.key = self.head.right.key
                    self.head.left = self.head.right.left
                    self.head.right = self.head.right.right
                self.size -= 1
            return
        self._erase(key, temp, temp)

    def _erase(self, key, temp, prev):
        if temp is None:
            raise ValueError
        elif temp.key == key:
            if temp.left is None and temp.right is None:
                if prev.left and prev.left.key == key:
                    prev.left = None
                else:
                    prev.right = None
                self.size -= 1
            elif temp.left is not None and temp.right is not None:
                if temp.right.left is None:
                    temp.data = temp.right.data
                    temp.key = temp.right.key
                    temp.right = temp.right.right
                    self.size -= 1
                else:
                    tempM = temp.left
                    prev = temp
                    while tempM.left is not None:
                        tempM = tempM.left
                    temp.data = tempM.data
                    temp.key = tempM.key
                    self._erase(tempM.key, tempM, prev)
            else:
                if temp.left is not None:
                    temp.data = temp.left.data
                    temp.key = temp.left.key
                    temp.right = temp.left.right
                    temp.left = temp.left.left
                else:
                    temp.data = temp.right.data
                    temp.key = temp.right.key
                    temp.left = temp.right.left
                    temp.right = temp.right.right
                self.size -= 1

        elif temp.key > key:
            self._erase(key, temp.left, temp)
        elif temp.key < key:
            self._erase(key, temp.right, temp)
