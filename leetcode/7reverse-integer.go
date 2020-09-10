package main

import "fmt"

func main() {
	{
		ret := 1
		for i := 0; i < 31; i++ {
			ret *= 2
		}
		fmt.Println(ret)
	}
	fmt.Println((1 << 31) * -1)
	fmt.Println((0x1 << 30))
	fmt.Println(1463847412)
	fmt.Println(1534236469)

	for _, x := range []int{23, 12, 234, -124, 1534236469, -2147483412, -2147483648} {
		fmt.Println(x, reverse(x))
	}

}

func reverse(x int) int {
	lessZero := 1
	if x == 0 || x >= (1<<31)-1 || x <= (1<<31)*-1 {
		return 0
	} else if x < 0 {
		lessZero = -1
		x *= -1
	}

	ret := 0
	for i := 0; x > 0; i++ {
		yushu := x % 10
		ret = ret*10 + yushu
		x /= 10
	}
	ret *= lessZero
	if ret >= (1<<31)-1 || ret <= (1<<31)*-1 {
		return 0
	}

	return ret
}
