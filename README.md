# fractal9: a stack-oriented golfing language

fractal9 is an esoteric, stack-oriented language made for code golfing. It's similar to Jelly, Vyxal, and Pyth with some elements of Forth.

Fractal9 is not intended to be a knockoff of the esoteric language Fractal- it's completely different.

## Example code:
```
Hello, ∘ world! ≽ ≽ ≽
```

## Explanation:
`Hello,`: Pushes the string "Hello," onto the stack
`∘`: Pushes a space character onto the stack
`world!`: Pushes the string "world!" onto the stack
`≽ ≽ ≽`: Each `≽` pops the top value and prints it as a string

It outputs `Hello, world!`
