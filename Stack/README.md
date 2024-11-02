## Stack

A **stack** is an abstract data type that serves as a collection of elements
with two main operations: _Push_ (which adds an element to the collection),
and _Pop_ (which removes the most recently added element).

Additionally, a _Peek_ operation can, without modifying the stack,
return the value of the last element added.
The name stack is an analogy to a set of physical items stacked one atop
another, such as a stack of plates.
As with a stack of physical objects, this structure makes it easy
to take an item off the top of the stack, but accessing a datum deeper
in the stack may require removing multiple other items first.

The order in which elements are added to or removed from a stack is described
as last in, first out, referred to by the acronym LIFO.

Considered a sequential collection, a stack has one end which is the only
position at which the push and pop operations may occur, the top of the stack,
and is fixed at the other end, the bottom. A stack may be implemented as,
for example, a singly linked list with a pointer to the top element.
A stack may be implemented to have a bounded capacity.
If the stack is full and does not contain enough space to accept
another element, the stack is in a state of stack overflow.

A stack is needed to implement depth-first search (DFS).