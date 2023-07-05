def insert(heap_list, number):
    heap_list.append(number)
    pos = len(heap_list) - 1
    parent_id = (pos - 1) // 2
    while pos > 0 and heap_list[parent_id] < number:
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
                if heap_list[pos] < heap_list[right_pos]:
                    heap_list[pos], heap_list[right_pos] = heap_list[right_pos], heap_list[pos]
                else:
                    break
            elif right_pos >= size:
                if heap_list[pos] < heap_list[left_pos]:
                    heap_list[pos], heap_list[left_pos] = heap_list[left_pos], heap_list[pos]
                else:
                    break
            else:
                if heap_list[pos] < max(heap_list[right_pos], heap_list[left_pos]):
                    if heap_list[right_pos] > heap_list[left_pos] and heap_list[pos] < heap_list[right_pos]:
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


max_heap = []
for i in range(int(input())):
    data = list(map(int, input().split()))
    if data[0] == 0:
        insert(max_heap, data[1])
    elif data[0] == 1:
        extract(max_heap)
