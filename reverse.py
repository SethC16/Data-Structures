def reverse_ll(ll):
    """
    Receive a LinkedList as an input, and returns a reversed order LL 

    Steps:
    1. Each node needs to point at the previous node
    2. Head and Tail pointers need to be flipped

    Cases:
    1. If the LL is empty return the original that is passed in
    reverse_ll(LinkedList())
    return the empty list

    reverse_ll(Lin)
    """
    # If LL is empty, return LL
    if ll.head is None:
        return ll

    # If LL has one node
    if ll.head is ll.tail:
        return ll

    # If LL has more than one node
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        # store a pointer to the current next value
        next_node = current.get_next()

        # switch current's next pointer to the previous
        current.set_next(previous)

        # increment logic
        previous = current
        current = next_node
        
    ll.head, ll.tail = ll.tail, ll.head