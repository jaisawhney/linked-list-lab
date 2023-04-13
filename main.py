from DoublyLinkedList import DoublyLinkedList

# Example:  12 ↔️ 200 ↔️ 19 ↔️ 49

dll = DoublyLinkedList()
dll.append(10)
dll.update(10, 50)

print(dll.head.data)
dll.append(12)
print(dll.head.next)
print(dll.head.next.previous.data)

dll.remove(50)
print(dll.find(50))
dll.append(50)

dll.insert(20, 1)
print(dll.find(20))
