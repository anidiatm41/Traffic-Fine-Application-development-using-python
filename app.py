from hashfunction import MyHashTable
from policenode import Node, add_node, in_order, reorder_tree_on_fine_amt, post_order, pre_order, add_node_amt, check_bonus


class Record:

    def __init__(self,polid,licno,fineamt):
        self.polid = polid
        self.licno = licno
        self.fineamt = fineamt

    def __str__(self):
        return "Police Id = {}, LicNo = {} , Fine Amount = {}".format(self.polid,self.licno,self.fineamt)


record_list = []
updated_list = [] 
violator_hash = None


def readfile():
    f = open("inputPS3.txt", "r")

    for x in f:
        array = x.split(" / ")
        record = Record(array[0],array[1],array[2])
        record_list.append(record)

    f.close()

def initializeHash():
    hash = MyHashTable(10)
    return hash

def printViolators():

    violator_hash = initializeHash()
    
    i = 0
    for record in record_list:
        if violator_hash.get(record.licno) is None:
            # print("License not present")
            violator_hash.set(record.licno, i+1)
        else:
            # print("License present")
            violator_hash.set(record.licno, violator_hash.get(record.licno)+1)

    f = open("violators.txt", "w")
    f.write("--------------------------Violators----------------------\n")
    for key in violator_hash.keys:
        if key is not None:
            f.write("{},{}\n".format(key,violator_hash.get(key)))
    f.close()

    destroyHash(violator_hash)

def destroyHash(hash_table):
    hash_table.keys = None
    hash_table.values = None
    hash_table = None

def destroyPoliceTree(root_node):
    if root_node.left:
        destroyPoliceTree(root_node.left)
    elif root_node.right:
        destroyPoliceTree(root_node.right)
    else:
        root_node = None

def insertByPoliceId():
    root_node = Node(record_list[0].polid, record_list[0].fineamt)
    add_node(None, root_node)
    i = 1
    while i < len(record_list):
        node = Node(record_list[i].polid, record_list[i].fineamt)
        add_node(root_node, node)
        i = i+1

    in_order(root_node)
    update_the_list(root_node)
    destroyPoliceTree(root_node)

    
def update_the_list(node):
    updated_list.append(node)
    if node.left:
        update_the_list(node.left)
    if node.right:
        update_the_list(node.right)


def reorderByFineAmount():
    root_node = Node(updated_list[0].police_id, updated_list[0].fine_amt)
    add_node_amt(None, root_node)
    i = 1
    while i < len(updated_list):
        node = Node(updated_list[i].police_id, updated_list[i].fine_amt)
        add_node_amt(root_node, node)
        i = i + 1

    pre_order(root_node)
    destroyPoliceTree(root_node)

def printBonusPoliceman():
    total_bonus_amount = 0

    root_node = Node(updated_list[0].police_id, updated_list[0].fine_amt)
    add_node_amt(None, root_node)
    i = 1
    while i < len(updated_list):
        node = Node(updated_list[i].police_id, updated_list[i].fine_amt)
        add_node_amt(root_node, node)
        i = i + 1
        
    for node in updated_list:
        total_bonus_amount = int(total_bonus_amount) + int(node.fine_amt)

    print("Total Fine amount = {}".format(total_bonus_amount))
    f = open("bonus.txt","w")
    f.write("--------------------------Bonus----------------------\n")
    check_bonus(root_node, total_bonus_amount,f)
    f.close()

readfile()
printViolators()
insertByPoliceId()
reorderByFineAmount()
printBonusPoliceman()



