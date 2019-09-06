class _Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class List:
    def __init__(self, data=None):
        self.size = 0
        if data is None:
            self.head = None
        elif type(data).__name__ == 'list':
            for i in data:
                self.append(i)
            self.size = len(data)
        elif type(data).__name__ == 'List':
            if data.head is not None:
                self.head = _Node(data.head.data, data.head.next)
                self.size = data.size
        else:
            self.head = _Node(data)
            self.size = 1

    def append(self, data):
        """ appends data to the end of the List. 'list' appends like an object. To ecah object from      """
        if self.size == 0:
            self.head = _Node(data)
            self.size += 1
        elif self.size > 0:
            for i in self:
                pass
            else:
                i.next = _Node(data)
                self.size += 1

    def getList(self):
        temp = self.head
        for i in range(self.size):
            print(temp.data)
            temp = temp.next

    def __iter__(self):
        temp = self.head
        while temp is not None:
            yield temp
            temp = temp.next

    def pop(self):
        """ deletes last element and returns it"""
        temp = None
        if self.size > 0:
            if self.size == 1:
                temp = self.head.data
                self.head = None
            else:
                for i in self:
                    if i.next.next is None:
                        temp = i.next.data
                        i.next = None
            self.size -= 1
            return temp

    def insert(self, data, index):
        """ inserts data by index. first arg is data, second - index """
        try:
            index = int(index)
        except ValueError:
            raise ValueError

        if index >= 0 and index <= self.size:
            if index == 0:
                temp = self.head
                self.head = _Node(data, temp)
            else:
                count = 0
                for i in self:
                    if count == index - 1:
                        temp = i.next
                        i.next = _Node(data, next=temp)
                        break
                    count += 1
            self.size += 1
        else:
            raise IndexError

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        """ overload of [] operator """
        if self.size > 0:
            if index >= 0 and index < self.size:
                count = 0
                for i in self:
                    if index == count:
                        return i.data
                    count += 1
            else:
                raise IndexError
        else:
            raise IndexError

    def reverse(self):
        """ returns new reversed list """
        temp = List()
        for i in self:
            temp.insert(i.data, 0)
        return temp

    def __str__(self):
        if len(self):
            str = "["
            for i in self:
                str += f'{i.data}, '
            else:
                str = str[:-2]
                str += ']'
            return str
        else:
            return '[]'

    def extend(self, list):
        """ add list of values to the end of the list """
        if type(list).__name__ == 'List':
            if len(list) is 0:
                pass
            elif self is list:
                temp = []
                for i in self:
                    temp.append(i.data)
                for i in temp:
                    self.append(i)

            elif len(self) is 0:
                self.head = _Node(list.head.data)
                for i in list:
                    self.append(i.data)
            else:
                for i in list:
                    self.append(i.data)
        elif type(list).__name__ == 'list':
            if len(self) is 0:
                for i in list:
                    self.append(i)
            else:
                for i in list:
                    self.append(i)
        else:
            print("'list' or 'List' were expected")
            raise TypeError

    def clear(self):
        self.head = None
        self.size = 0

    def __add__(self, list):
        temp = List()
        temp.extend(self)
        temp.append(list)

        return temp
