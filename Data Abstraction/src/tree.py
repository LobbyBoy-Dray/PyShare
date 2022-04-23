# tree的本质[value, list, list, ...]
# 例: [3, [1], [2, [1], [1]]]

# tree的constructor
def tree(label, branches=[]):
        for branch in branches:
                assert is_tree(branch)
        return [label] + list(branches)

# tree的selector: 获取tree的root label
def label(tree):
        return tree[0]

# tree的selector: 获取tree的branches
def branches(tree):
        return tree[1:]

def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
                return False
        for branch in branches(tree):
                if not is_tree(branch):
                        return False
        return True

def is_leaf(tree):
        return not branches(tree)




def count_leaves(t):
    """Returns the number of leaf nodes in T."""
    if is_leaf(t):
        return 1

    result = 0
    for branch in branches(t):
        result += count_leaves(branch)

    return result



def print_tree(t, indent=0):
    """Print a tree in a specific formatting."""
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent+1)


def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t for which the labels along the path sum to total."""
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths(b, total-label(t)) for b in branches(t)])

        if label(t) == total:
                found = 1
        else:
                found = 0












