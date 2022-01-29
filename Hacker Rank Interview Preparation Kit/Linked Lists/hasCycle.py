def hasCycle(head):
    seen = set()
    curr = head
    while curr:
        if curr in seen:
            return True
        seen.add(curr)
        curr = curr.next
    return False