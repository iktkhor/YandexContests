# def heapify(array):
#     centre = len(array) // 2 + 1 if len(array) % 2 == 1 else len(array) / 2
#     for i in range(centre)


def insert(heap_list, number):
    heap_list.append(number)
    pos = len(heap_list) - 1
    parent_id = (pos - 1) // 2
    while pos > 0 and heap_list[parent_id] > number:
        heap_list[parent_id], heap_list[pos] = heap_list[pos], heap_list[parent_id]
        pos = parent_id
        parent_id = (pos - 1) // 2


def extract(heap_list):
    if len(heap_list) > 1:
        print(heap_list[0])
        heap_list[0] = heap_list[-1]
        heap_list.pop()
        size = len(heap_list)
        pos = 0
        left_pos = 2 * pos + 1
        right_pos = 2 * pos + 2
        while left_pos < size or right_pos < size:
            if left_pos >= size:
                if heap_list[pos] > heap_list[right_pos]:
                    heap_list[pos], heap_list[right_pos] = heap_list[right_pos], heap_list[pos]
                else:
                    break
            elif right_pos >= size:
                if heap_list[pos] > heap_list[left_pos]:
                    heap_list[pos], heap_list[left_pos] = heap_list[left_pos], heap_list[pos]
                else:
                    break
            else:
                if heap_list[pos] > min(heap_list[right_pos], heap_list[left_pos]):
                    if heap_list[right_pos] < heap_list[left_pos] and heap_list[pos] > heap_list[right_pos]:
                        heap_list[pos], heap_list[right_pos] = heap_list[right_pos], heap_list[pos]
                        pos = right_pos
                    else:
                        heap_list[pos], heap_list[left_pos] = heap_list[left_pos], heap_list[pos]
                        pos = left_pos
                else:
                    break
            left_pos = 2 * pos + 1
            right_pos = 2 * pos + 2

    elif len(heap_list) == 1:
        print(heap_list[0])
        heap_list.pop()
    else:
        print('CANNOT')


min_heap = []
with open('input.txt') as text:
    for line in text:
        command = line.split()[0]
        if command == '':
            break
        if command == 'CLEAR':
            min_heap.clear()
        elif command == 'EXTRACT':
            extract(min_heap)
        else:
            num = line.split()
            insert(min_heap, int(num[1]))


# int(input())
# for num in list(map(int, input().split())):
#     insert(min_heap, num)
# while len(min_heap) > 0:
#     extract(min_heap)
