from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None
    lst= list_repr.split(' -> ')
    lst=lst[:-1]
    res=Node(int(lst[-1]))
    for el in lst[-2::-1]:
        res=Node(int(el), res)
    return res
