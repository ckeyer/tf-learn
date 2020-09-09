package main

import "fmt"

func main() {
	var (
		a = "123"
		b = "456"
	)
	fmt.Println(a, b, multiply(a, b))

	fmt.Println(byte2Int("3"))
	fmt.Println(smallInt2String(124))
	fmt.Println(singalMultsingal("4", "9"))
	fmt.Println(`singalAdd("4", "9")`, singalAdd("4", "9"))
	fmt.Println(`singalAdd("4", "9", "9")`, singalAdd("4", "9", "9"))

	fmt.Println(`add("4", "9")`, add("4", "9"))
	fmt.Println(`add("9876543210", "2")`, add("9876543210", "2"))

	fmt.Println(`singalMultLarge("2", "33335555")`, 2*33335555)
	fmt.Println(`singalMultLarge("2", "33335555")`, singalMultLarge("2", "33335555"))
	fmt.Println(`singalMultLarge("2", "33335555")`, singalMultLarge("2", "33335555"))

	fmt.Println(`multiply("2", "33335555")`, multiply("2", "33335555"))
	fmt.Println(`("2", "33335555")`, 2*33335555)
	fmt.Println(`multiply("0", "33335555")`, multiply("0", "33335555"))
	fmt.Println(`("22", "33335555")`, 22*33335555)

}
func multiply(num1 string, num2 string) (ret string) {
	if len(num1) < len(num2) {
		num1, num2 = num2, num1
	}
	var (
		bLen = len(num2)
	)
	for j := 0; j < bLen; j++ {
		partSum := singalMultLarge(string(num2[len(num2)-j-1]), num1) + fillZero(j)
		ret = add(ret, partSum)
	}
	return ret
	trimIdx := 0
	for i, n := range ret {
		if n == '0' {
			trimIdx = i + 1
		} else {
			break
		}
	}
	if trimIdx == len(ret) {
		return "0"
	}
	return ret[trimIdx:]
}

func singalMultLarge(aSig, bLar string) (ret string) {
	if aSig == "0" {
		return "0"
	}
	bLen := len(bLar)

	for i := 0; i < bLen; i++ {
		ret = add(ret, singalMultsingal(string(bLar[bLen-i-1]), aSig)+fillZero(i))
	}
	return
}

func singalMultsingal(a, b string) string {
	n := byte2Int(a) * byte2Int(b)
	return smallInt2String(n)
}

func add(a, b string) string {
	if len(a) > len(b) {
		b = fillZero(len(a)-len(b)) + b
	} else if len(a) < len(b) {
		a = fillZero(len(b)-len(a)) + a
	}
	var (
		aLen = len(a)
		ret  = ""
		tmp  = "0" // 进位
	)
	for i := 0; i < aLen; i++ {
		part1 := singalAdd(string(a[aLen-i-1]), string(b[aLen-i-1]), tmp)
		ret = string(part1[len(part1)-1]) + ret
		if len(part1) > 1 {
			tmp = string(part1[:len(part1)-1])
		} else {
			tmp = "0"
		}
	}
	if tmp != "0" {
		ret = tmp + ret
	}

	return ret
}

func singalAdd(abc ...string) string {
	count := 0
	for _, n := range abc {
		count += byte2Int(n)
	}
	return smallInt2String(count)
}

func byte2Int(num string) int {
	return int([]byte(num)[0] - '0')
}

func smallInt2String(n int) string {
	ret := ""
	for {
		if n <= 9 {
			return string(byte(n+int('0'))) + ret
		}
		y := n % 10
		ret = string(byte(y+int('0'))) + ret
		n = n / 10
	}
	return ret
}

func fillZero(n int) (ret string) {
	for i := 0; i < n; i++ {
		ret += "0"
	}
	return
}
