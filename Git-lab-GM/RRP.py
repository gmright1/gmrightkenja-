class Node: 

def __init__(self,key): 

self.left = None #left to the node

self.right = None# right of the node

self.val = key 

def insert(root,node): #inserting the node into the BST

if root is None: #if the node is only one

root = node 

else: 

if root.val < node.val: #if root value is less then move the node as right to the Root 

if root.right is None: 

root.right = node 

else: 

insert(root.right, node) 

else: 

if root.left is None: 

root.left = node #if root value is greater then move the node as left to the Root

else: 

insert(root.left, node) #recursion

def inorder(root): 

if root: 

inorder(root.left) 

print(root.val) 

inorder(root.right)

def deletenode(root,d):# d is for the node which we want to delete

if root is None:

return root

if d < root.val:

root.left = deletenode(root.left,d)#recursion method

if d > root.val:

root.right = deletenode(root.right,d) 

def search(root,key): 

if root is None or root.val == key: 

return root 

if root.val < key: 

return search(root.right,key) 

return search(root.left,key)

root=raw_input("Enter Root Element:\t")

r = Node(root)

while True:

ch=input("\n1.Insert Element\n2.Show Tree\t \n3.Search the Word \n4.Delete the Word From the Tree")

if ch==1:

val=raw_input("Enter Word to be inserted:\t")

insert(r,Node(val))

if ch==2:

print "Your Tree in INORDER :\n"

inorder(r)

if ch==3:

	ke=raw_input("Enter the Key To select")

	print search(r,ke)

if ch==4:

	d=raw_input("Enter the Node to be Deleted")

	deletenode(r,Node(d))

if ch==5:

	print ("Dont Visit Again")

	break;

		

