class Node:

    def __init__(self):
        pass

    def __init__(self, police_id, fine_amt):
        self.police_id = police_id
        self.fine_amt = fine_amt
        self.violations = 1
        self.left = None
        self.right = None


def add_node(root, node):
    if root is None:
        root = node
    else:
        if root.police_id == node.police_id:
            # print("Print value Id :{} and Fine: {} + + {}".format(root.police_id, root.fine_amt, node.fine_amt))
            root.fine_amt = int(root.fine_amt) + int(node.fine_amt)
            root.violations = int(root.violations) + 1
            # print("Root fine amount now {}".format(root.fine_amt))

        elif root.police_id < node.police_id:
            if root.right is None:
                root.right = node
            else:
                if root.right.police_id == node.police_id:
                    root.right.fine_amt = int(root.right.fine_amt) + int(node.fine_amt)
                    root.right.violations = int(root.right.violations) + 1
                else:
                    add_node(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                if root.left.police_id == node.police_id:
                    root.left.fine_amt = int(root.left.fine_amt) + int(node.fine_amt)
                    root.left.violations = int(root.left.violations) + 1
                else:
                    add_node(root.left, node)

def add_node_amt(root, node):
    if root is None:
        root = node
    else:
        if root.fine_amt < node.fine_amt:
            if root.right is None:
                root.right = node
            else:
                add_node_amt(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                add_node_amt(root.left, node)

def in_order(root):
    if root:
        in_order(root.left)
        print(" Police Id = {}, Amount = {} Violations = {}".format(root.police_id, root.fine_amt, root.violations))
        in_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(" Police Id = {}, Amount = {} Violations = {}".format(root.police_id, root.fine_amt, root.violations))


def pre_order(root):
    if root:
        print(" Police Id = {}, Amount = {} Violations = {}".format(root.police_id, root.fine_amt, root.violations))
        pre_order(root.left)
        pre_order(root.right)


def check_bonus(root, total_amount,file_stream):
    if root:
        percentage  = (float(root.fine_amt) / float(total_amount)) * 100
        #print("Percentage of POlice = {} Percent = {} fine n= {}".format(root.police_id, percentage, root.fine_amt))
        if percentage > 80:
            #print("Bonus Eligible = {}, Violations = {}".format(root.fine_amt, root.violations))
            file_stream.write("{},{},{}\n".format(root.police_id, root.fine_amt, root.violations))
        else:
            print("Not Eligible")
        check_bonus(root.left, total_amount,file_stream)
        check_bonus(root.right, total_amount,file_stream)


def reorder_tree_on_fine_amt(root):
    print("Node Fine amount {} Id {} ".format(root.fine_amt, root.police_id))
    if root.left:
        if root.fine_amt < root.left.fine_amt:
            print("Root fine amt {} Left fine amt {} ".format(root.fine_amt, root.left.fine_amt))
            # root = root.left
            reorder_tree_on_fine_amt(root.left)
        else:
            print("Root is greater than left")
    else:
        print "root doesn't have any left"

    if root.right:
        if root.fine_amt > root.right.fine_amt:
            print("Root fine amt {} right fine amt {}".format(root.fine_amt,root.right.fine_amt))
            # root = root.right
            reorder_tree_on_fine_amt(root.right)
        else:
            print("Root is lesser than right")
    else:
        print "root doesn't have any right"


