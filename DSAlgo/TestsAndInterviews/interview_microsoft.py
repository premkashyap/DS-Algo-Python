from SinglyLinkedList import * 

def process_expression(expression):
    expression+='@'
    operand1=None
    operand2=None
    current_operand = ''
    current_operator= None
    for c in expression:
        if c not in ('+', '-', '@'):
            current_operand+=c
        else:
            if operand1 is None:
                operand1 = current_operand
            else:
                operand2 = current_operand
                if operand1 is not None and operand2 is not None and current_operator is not None:
                    operand1 = eval('int('+ str(operand1)+')' + current_operator+ 'int('+ operand2+')')
            current_operand=''
            current_operator =c
    print(operand1)

def sort_singly_linkedlist_of012(lst):
    list0, list1, list2 = SinglyLinkedList(), SinglyLinkedList(), SinglyLinkedList()
    current_node = lst.head
    while current_node is not None:
        if current_node.data == 0:
            list0.insert_end(current_node)
        elif current_node.data ==1:
            list1.insert_end(current_node)
        else:
            list2.insert_end(current_node)
        current_node =current_node.next_node
    list1.insert_node_end(list2.head)
    list0.insert_node_end(list1.head)
    return list0


if __name__ == '__main__':
    #process_expression('2+5-4')
    print(sort_singly_linkedlist_of012(SinglyLinkedList.create_from_list([1,0,0,1,2,2,1,1,0])))