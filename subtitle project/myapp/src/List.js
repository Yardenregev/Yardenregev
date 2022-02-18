class Node {
    constructor (id,value,is_term,time_stamp,search,next = null) {
        this.id = id;//2
        this.value = value;//"world"
        this.is_term = is_term;//"term"
        this.time_stamp = time_stamp;//"00:20:15"
        this.search = search;
        this.next = next;
    }
}



class List{
    constructor (){
        this.head = null;
        this.tail = null;
        this.count = 0;
    }



    //Insert first node
    InsertFirst(value,is_term,time_stamp)
    {
        this.head = new Node(this.count,value,is_term,time_stamp,this.head);
        this.count++;
    }


    //Insert last node
    InsertLast(value,is_term,time_stamp)
    {
        let new_node = new Node(this.count,value,is_term,time_stamp,null);
        if (this.tail != null)
        {
                    this.tail.next = new_node;
        }
        this.tail = new_node;
        this.count++;
    }

    //Pop first
    PopFirst()
    {
        this.head = this.head.next;
        this.count --;
    }

    //Pop last
    PopLast()
    {
        let current = this.head;
        while (current.next != this.tail)
        {
            current = current.next;
        }
        current.next = null;
        this.tail = current;
        this.count --;
    }

    //Make word term at index
    MakeTermAtIndex(index)
    {
        if (index < 0 || index >= this.count)
        {
            alert("Invalid index");
            return;
        }
        let current = this.head;
        while(current.id != index)
        {
            current = current.next;
        }
        current.is_term = "term";
    }

    //Make not term at index
    MakeNotTermAtIndex(index)
    {
        if (index < 0 || index >= this.count)
        {
            alert("Invalid index");
            return;
        }
        let current = this.head;
        while(current.id != index)
        {
            current = current.next;
        }
        current.is_term = "";
    }

    //edit time stamp at index
    EditTimeStampAtIndex(index,new_time_stamp)
    {
        if (index < 0 || index >= this.count)
        {
            alert("Invalid index");
            return;
        }
        let current = this.head;
        while(current.id != index)
        {
            current = current.next;
        }
    }

    //Check if list is empty
    IsEmpty()
    {
        if(this.tail == null && this.head == null)
        {
            return 1;
        }
        return 0;
    }

    //Print list data
    PrintList(){
        let current = this.head;
        while (current != null) {
            console.log(current.value);
            current = current.next;
        }
    }

}