package main

import "fmt"

const lsb16Mask int = 65535

const gAFactor, gAMultiple int = 16807, 4
const gBFactor, gBMultiple int = 48271, 8
const remainder int = 2147483647

func match(a, b int) bool {
	return (a & lsb16Mask) == (b & lsb16Mask)
}

func generator(start, factor, divisor int, judge chan<- int) {
	for {
		start = (start * factor) % remainder

		for (start % divisor) != 0 {
			start = (start * factor) % remainder
		}

		judge <- start
	}
}

func main() {
	generatorA := make(chan int, 25)
	generatorB := make(chan int, 25)

	go generator(512, gAFactor, gAMultiple, generatorA)
	go generator(191, gBFactor, gBMultiple, generatorB)

	total := 0
	// Main thread acts as the judge
	for i := 0; i < 5000000; i++ {
		numberA := <-generatorA
		numberB := <-generatorB

		if match(numberA, numberB) {
			total++
		}
	}

	fmt.Println(total)

	// Channels auto closed by go runtime, therefore no cleanup required.
}
