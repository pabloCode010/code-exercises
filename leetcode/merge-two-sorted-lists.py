# MERGE TWO SORTED LISTS
# https://leetcode.com/problems/merge-two-sorted-lists/

# Se le proporcionan los encabezados de dos listas vinculadas ordenadas list1y list2.
# Combine las dos listas en una lista ordenada . La lista debe hacerse empalmando los nodos de las dos primeras listas.
# Devuelve el encabezado de la lista enlazada fusionada
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        merge_list = list1
        prev = None
        
        while list2:
            current = prev or merge_list

            while current and (list2.val > current.val):
                prev = current
                current = current.next

            if current is merge_list:
                merge_list = list2
                list2 = list2.next
                merge_list.next = current

            elif current is None:
                prev.next = list2
                list2 = None

            else:
                prev.next = list2
                list2 = list2.next
                prev.next.next = current

        return merge_list

def print_list(list: ListNode):
    while list:
        print(list.val, end=" -> ")
        list = list.next
    print(list)

def list_to_linked_list(lst):
    if not lst:
        return None

    # Crea el primer nodo de la lista vinculada
    head = ListNode(lst[0])
    current = head

    # Agrega los nodos restantes
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

list1 = list_to_linked_list([9, 9, 1, 3, 5])
list2 = list_to_linked_list([-5,-3,0,7,8,8])
print_list(list1)
print_list(list2)

merge = Solution().mergeTwoLists(list1, list2)

print_list(merge)
