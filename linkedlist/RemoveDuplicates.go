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

func RemoveDuplicates(headNode *Node) *Node {
	if headNode == nil {
		return headNode
	}
	dataMap := make(map[int]bool)
	currentNode := headNode
	dataMap[headNode.data] = true
	for currentNode.next != nil {
		if dataMap[currentNode.next.data] {
			currentNode.next = currentNode.next.next
		} else {
			dataMap[currentNode.next.data] = true
			currentNode = currentNode.next
		}
	}
	return headNode
}

func WithoutBuffer(headNode *Node) *Node {
	currentNode := headNode
	for currentNode != nil && currentNode.next != nil {
		if currentNode.data == currentNode.next.data {
			currentNode.next = currentNode.next.next
		} else {
			runner := currentNode.next
			for runner.next != nil {
				if currentNode.data == runner.next.data {
					runner.next = runner.next.next
				} else {
					runner = runner.next
				}
			}
			currentNode = currentNode.next
		}
	}
	return headNode
}
