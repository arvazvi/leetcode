package main

type Node struct {
	Key   int
	Value int
	Prev  *Node
	Next  *Node
}

func NewNode(key, value int) *Node {
	return &Node{Key: key, Value: value}
}

type List struct {
	size int
	Head *Node
	Tail *Node
}

func NewList() *List {
	return &List{}
}

func (l *List) Append(n *Node) {
	if l.Head == nil && l.Tail == nil {
		l.Head = n
		l.Tail = n
	} else if l.Head == l.Tail {
		l.Head.Next = n
		l.Head = n
		l.Head.Prev = l.Tail
	} else {
		l.Head.Next = n
		n.Prev = l.Head
		l.Head = n
	}
	l.size++
}

func (l *List) PopLeft() *Node {
	evicted := l.Tail
	if evicted == nil {
		return nil
	}
	l.Tail = evicted.Next
	if l.Tail == nil {
		l.Head = nil
	} else {
		l.Tail.Prev = nil
	}
	evicted.Next = nil
	l.size--
	return evicted
}

func (l *List) PopRight() *Node {
	evicted := l.Head
    if evicted == nil {
        return nil
    }
	l.Head = evicted.Prev
	if l.Head == nil {
		l.Tail = nil
	} else {
		l.Head.Next = nil
	}
	evicted.Prev = nil
	l.size--
	return evicted
}

func (l *List) Pop(n *Node) *Node {
	if l.Head == nil && l.Tail == nil {
		return nil
	}

	if l.Head == l.Tail && l.Head == n {
		l.Head = nil
		l.Tail = nil
		n.Next = nil
		n.Prev = nil
		return n
	}

	if n == l.Head {
		return l.PopRight()
	}
	if n == l.Tail {
		return l.PopLeft()
	}
	n.Prev.Next = n.Next
	n.Next.Prev = n.Prev
	n.Next = nil
	n.Prev = nil
	l.size--
	return n
}

func (l *List) MoveToFront(node *Node) {
	l.Append(l.Pop(node))
}

type LRU struct {
	capacity int
	size     int
	Cache       map[int]*Node
	List        *List
}

func NewLRU(capacity int) *LRU {
	return &LRU{capacity: capacity, List: NewList(), Cache: make(map[int]*Node)}
}

func (lru *LRU) Get(key int) int {
	n, ok := lru.Cache[key]
	if !ok {
		return -1
	}

	lru.List.MoveToFront(n)
	return n.Value
}

func (lru *LRU) Put(key, value int) {
	n, ok := lru.Cache[key]
	if ok {
		n.Value = value
		lru.List.MoveToFront(n)
	} else {
		if lru.size+1 > lru.capacity {
			evicted := lru.List.PopLeft()
			delete(lru.Cache, evicted.Key)
			lru.Cache[key] = NewNode(key, value)
			lru.List.Append(lru.Cache[key])
		} else {
			lru.Cache[key] = NewNode(key, value)
			lru.List.Append(lru.Cache[key])
			lru.size++
		}
	}
}
