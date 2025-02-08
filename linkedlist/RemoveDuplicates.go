package removeduplicates

type Node struct {
	data int
	next *Node
}

func newNode(data int) *Node {
	return &Node{data: data, next: nil}
}

func createLinkedList(dataArray []int) *Node {
	genesisNode := &Node{}
	previousNode := genesisNode
	for _, data := range dataArray {
		previousNode.next = newNode(data)
		previousNode = previousNode.next
	}
	return genesisNode.next
}

func countLinkedList(headNode *Node) int {
	listLength := 0
	node := headNode
	for node != nil {
		listLength++
		node = node.next
	}
	return listLength
}
