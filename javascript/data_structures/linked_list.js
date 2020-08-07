class Linked_List {
    constructor() {
        /*  The constructor initializes the linked list with
            an empty head and tail object. This two objects 
            represent the first and last element of the linked list.
            Each element in the linked list has a property "value"
            containing the value stored and a property "next" containing the 
            next element in the list
        */
        this.head = null;
        this.tail = null;
    }

    append(value) {
        /*  This function receives a value to append at the end of the linked 
            list. To achieve so we have to create a new node with the value
            passed and "null" for the "next" property because it is the last
            element in the list.
        */
        const newNode = { value: value, next: null };

        //  Connecting previous tail to the newNode only if a tail is already 
        //  present. Which means if at least one element is inside the list.
        //  Otherwise the list is empty and we set the head to be the newNode.
        if (this.tail) {
            this.tail.next = newNode;
        } else {
            this.head = newNode;
        }

        //  In the end we set the current tail to newNode.
        this.tail = newNode
    }

    prepend(value) {
        /* This function receives a value to add at the beginning of the linked
            list. The procedure is similar to the append function but in this case
            we must populate the "next" property of the newNode to be connected with
            the previous head of the list.
        */
        const newNode = { value: value, next: this.head };

        this.head = newNode;

        //  We also check if we had previously an empty list, therefore not having any tail
        //  in that case we also set the tail as the newNode
        if (!this.tail) {
            this.tail = newNode;
        }
    }

    find(value) {
        /*  This function finds all the elements with a certain value and returns them as an array */
        //  First check if the list is empty
        if (!this.head) {
            return;
        }

        let foundValues = [];
        let currentNode = this.head;

        while (currentNode) {
            if (currentNode.value === value) {
                foundValues.push(currentNode);
            }
            currentNode = currentNode.next;
        }

        if (foundValues.length === 0) {
            return null;
        } else {
            return foundValues;
        }
    }

    findOne(value) {
        /*  This function finds the first element with a certain value and returns it */
        //  First check if the list is empty
        if (!this.head) {
            return;
        }

        let currentNode = this.head;

        while (currentNode) {
            if (currentNode.value === value) {
                return currentNode;
            }
            currentNode = currentNode.next;
        }

        return null;
    }

    insertAfterAll(value, afterValue) {
        /*  This function insert an extra node, with "value" = afterValue, after each found occurrance of elements with "value" equal
            to the user input "value".
        */
        const existingNodes = this.find(value);

        if (!existingNodes) {
            return null;
        }

        existingNodes.map(node => {
            const newNode = { value: afterValue, next: node.next };
            node.next = newNode
        })
    }

    insertAfterOne(value, afterValue) {
        /*  This function insert an extra node, with "value" = afterValue, after the first found occurrance of elements with "value" equal
            to the user input "value".
        */
        const existingNode = this.findOne(value);

        if (!existingNode) {
            return null;
        }

        const newNode = { value: afterValue, next: existingNode.next };
        existingNode.next = newNode
    }

    delete(value) {
        /*  This function deletes all the elements with the corresponding received property value "value".
            To do so, the list is examined and once an element is to be deleted, the connection from the
            previous node is modified so to skip the node to be deleted. In this way the node will never 
            be referenced again and it is lost in memory and, eventually, will be garbage collected.

            Special cases are to be considered for the head and the tail nodes.
        */
        //  First check if the list is empty, because then there is no element to delete
        if (!this.head) {
            return null;
        }

        //  Here we check if the node to be deleted is the head. This loop will continue deleting the head
        //  also if subsequent head are also to be deleted, until we have one node as head node that does not 
        //  have to be deleted.
        while (this.head && this.head.value === value) {
            this.head = this.head.next;
        }

        let currentNode = this.head;

        //  Notice that the check starts from the second node therefore it is needed the previous  
        //  extra check for the "value" of the head node. Also we want to move to the next element
        //  only if also the updated "next" does not need to be deleted
        while (currentNode.next) {
            if (currentNode.next.value === value) {
                if (currentNode.next === this.tail) {
                    //  In case the tail has to be deleted, we need to reset the tail to the last existing node,
                    //  which is the last node in the loop (currentNode)
                    this.tail = currentNode;
                }
                currentNode.next = currentNode.next.next;
            } else {
                currentNode = currentNode.next;
            }
        }
    }

    deleteOne(value) {
        /*  This function deletes the fisrt element found with the corresponding value.
            It is achieved with the usage of a flag.
        */
        let deletedFlag = false;

        while (this.head && this.head.value === value && !deletedFlag) {
            this.head = this.head.next;
            return true;
        }

        let currentNode = this.head;

        while (currentNode.next && !deletedFlag) {
            if (currentNode.next.value === value) {
                if (currentNode.next === this.tail) {
                    this.tail = currentNode;
                }
                currentNode.next = currentNode.next.next;
                return true;
                console.log("HElloo");
            } else {
                currentNode = currentNode.next;
            }
        }

    }

    toArray() {
        /*  This function returns the full content of the linked list as an array 
            of all the elements of the linked list elements.
            
            It works by starting from the head node and iterating over the whole list 
            until it finds an empty (null) node. At each iteration it appends the 
            element to the array and, in the end it returns the filled array.
        */
        const elements = [];

        let currentNode = this.head;
        while (currentNode) {
            elements.push(currentNode);
            currentNode = currentNode.next;
        }

        return elements;
    }
}

// TESTING 
const linkedList1 = new Linked_List();

linkedList1.prepend("Prepended Element");
linkedList1.prepend("Prepended Element");
linkedList1.append(1);
linkedList1.append("Hello");
linkedList1.append(32.34);
linkedList1.append(true);
linkedList1.append({ val1: 3, val2: 4 });
linkedList1.append(1);
linkedList1.append(1);
console.log(linkedList1.toArray());

linkedList1.insertAfterAll("Prepended Element", 555);
console.log(linkedList1.toArray());

module.exports = Linked_List;