package main

import (
	"fmt"
	"sort"
)

var (
	countArr = []int{}
)

func main() {
	in := [][]int{
		[]int{4, 1, 5, 3},
		[]int{3, 2, 7, 7},
		[]int{6, 5, 2, 8},
		[]int{8, 9, 4, 5},
	}
	soluSub(in, 0, 0, 4)

	fmt.Println()
	sort.Ints(countArr)

	for i, v := range countArr {
		fmt.Println(i+1, v)
	}

}

func soluSub(arr [][]int, i, j, count int) {
	fmt.Println(i, j, count)
	rightCount, downCount := count, count
	isDown, isRight := false, false
	if i < len(arr)-1 {
	} else {
		isDown = true
	}
	if j < len(arr[0])-1 {
	} else {
		isRight = true
	}
	if isRight && isDown {
		countArr = append(countArr, downCount)
		fmt.Println("Over", rightCount, downCount)
	}

	if !isDown {
		downCount += arr[i+1][j]
		soluSub(arr, i+1, j, downCount)
	}
	if !isRight {
		rightCount += arr[i][j+1]
		soluSub(arr, i, j+1, rightCount)
	}

	return
}
