class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def show(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values) if values else "порожній список")


def reverse(lst):
    """Реверс списку: змінюємо посилання next кожного вузла на протилежне."""
    prev = None
    current = lst.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    lst.head = prev


def insertion_sort(lst):
    """Сортування вставками: переставляємо вузли у новий відсортований список."""
    sorted_head = None
    current = lst.head
    while current:
        next_node = current.next
        if sorted_head is None or current.data < sorted_head.data:
            current.next = sorted_head
            sorted_head = current
        else:
            place = sorted_head
            while place.next and place.next.data < current.data:
                place = place.next
            current.next = place.next
            place.next = current
        current = next_node
    lst.head = sorted_head


def merge_sorted(list_a, list_b):
    """Об'єднує два відсортовані списки в один відсортований."""
    result = LinkedList()
    a = list_a.head
    b = list_b.head
    while a and b:
        if a.data <= b.data:
            result.append(a.data)
            a = a.next
        else:
            result.append(b.data)
            b = b.next
    while a:
        result.append(a.data)
        a = a.next
    while b:
        result.append(b.data)
        b = b.next
    return result


def main():
    lst = LinkedList()
    for value in [5, 2, 9, 1, 7]:
        lst.append(value)
    print("Початковий список:")
    lst.show()

    reverse(lst)
    print("Після реверсу:")
    lst.show()

    insertion_sort(lst)
    print("Після сортування:")
    lst.show()

    other = LinkedList()
    for value in [0, 3, 4, 8]:
        other.append(value)
    print("Другий відсортований список:")
    other.show()

    print("Об'єднаний список:")
    merge_sorted(lst, other).show()


if __name__ == "__main__":
    main()
