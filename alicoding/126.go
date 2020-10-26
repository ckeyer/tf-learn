package main

import "fmt"

func main() {
	var (
		wallet = []int{10, 9, 9, 9}
		wuts   = []int{5, 2, 6, 1, 2, 4}
	)

	jiecheng(wallet)
	jiecheng(wuts)
}

func jiecheng(arr []int) [][]int {
	pailie(12)
	return nil
}

func pailie(n int) [][]int {
	arrLen := 1
	for i := 1; i <= n; i++ {
		arrLen *= i
	}

	// arr := make([][]int, 0, arrLen)

	fmt.Println(n, arrLen)

	return nil
}
