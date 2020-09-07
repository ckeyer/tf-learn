package main

import "fmt"

func main() {
	input := [][]byte{
		{'5', '3', '.', '.', '7', '.', '.', '.', '.'},
		{'6', '.', '.', '1', '9', '5', '.', '.', '.'},
		{'.', '9', '8', '.', '.', '.', '.', '6', '.'},
		{'8', '.', '.', '.', '6', '.', '.', '.', '3'},
		{'4', '.', '.', '8', '.', '3', '.', '.', '1'},
		{'7', '.', '.', '.', '2', '.', '.', '.', '6'},
		{'.', '6', '.', '.', '.', '.', '2', '8', '.'},
		{'.', '.', '.', '4', '1', '9', '.', '.', '5'},
		{'.', '.', '.', '.', '8', '.', '.', '7', '9'},
	}

	printSudoku(input)

	solveSudoku(input)

	printSudoku(input)

	printColume(getSudokuOptions(input, 0, 8))
}

func printSudoku(board [][]byte) {
	fmt.Println("----begin")
	defer fmt.Println("----end")
	for _, v := range board {
		printColume(v)
	}
}

func printColume(sli []byte) {
	for _, it := range sli {
		fmt.Printf("%s ", string(it))
	}
	fmt.Println("")
}

func solveSudoku(board [][]byte) {
	sk := newSudoku(board)
	sk.iter(0, 0)
	sk.printGuess()
}

type sudoku struct {
	opt  map[int]map[int][]byte
	idxs map[int]map[int]int
}

func newSudoku(board [][]byte) *sudoku {
	ret := &sudoku{
		opt:  map[int]map[int][]byte{},
		idxs: map[int]map[int]int{},
	}
	for i, rows := range board {
		ret.opt[i] = map[int][]byte{}
		ret.idxs[i] = map[int]int{}
		for j, col := range rows {
			ret.idxs[i][j] = 0
			if col != '.' {
				ret.opt[i][j] = []byte{col}
			} else {
				ret.opt[i][j] = getSudokuOptions(board, i, j)
			}
		}
	}
	return ret
}

func (s *sudoku) printGuess() {
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			col := s.idxs[i][j]
			fmt.Printf("%v ", string(s.opt[i][j][col]))
		}
		fmt.Println("")
	}
	fmt.Println("check: ", s.check())
}

func (s *sudoku) check() bool {
	{
		for i := 0; i < 9; i++ {
			exiRow := map[byte]struct{}{}
			exiCol := map[byte]struct{}{}
			for j := 0; j < 9; j++ {
				v := s.opt[i][j][s.idxs[i][j]]
				if _, ok := exiRow[v]; ok {
					return false
				} else {
					exiRow[v] = struct{}{}
				}

				vCol := s.opt[j][i][s.idxs[j][i]]
				if _, ok := exiCol[vCol]; ok {
					// return false
				} else {
					exiCol[vCol] = struct{}{}
				}
			}
		}
	}
	return true
}

var count int

func (s *sudoku) iter(starti, startj int) {
	count++
	// if count > 3 {
	// 	return
	// }
	// fmt.Println(starti, startj, s.check())
	if count%20000 == 0 {
		fmt.Println(count)

	}
	if count%20000 == 0 {
		s.printGuess()
	}
	if s.check() {
		return
	}
	ni, nj := nextIdx(starti, startj)
	if ni == 0 && nj == 0 {
		return
	}

	opts := s.opt[starti][startj]
	if len(opts) == 1 {
		s.iter(ni, nj)
		return
	}

	for idx := range opts[1:] {
		s.idxs[starti][startj] = idx + 1
		s.iter(ni, nj)
	}
}

func nextIdx(i, j int) (ii, jj int) {
	if i == 8 && j == 8 {
		return 0, 0
	}
	if j == 8 {
		return i + 1, 0
	}
	return i, j + 1
}

func byte2String(sli []byte) []string {
	ret := make([]string, len(sli))
	for i, v := range sli {
		ret[i] = string(v)
	}
	return ret
}

func getSudokuOptions(board [][]byte, i, j int) []byte {
	exi := map[byte]bool{
		'1': false,
		'2': false,
		'3': false,
		'4': false,
		'5': false,
		'6': false,
		'7': false,
		'8': false,
		'9': false,
	}

	for idx := 0; idx < 9; idx++ {
		exi[board[i][idx]] = true
		exi[board[idx][j]] = true
	}
	for idx := 0; idx < 3; idx++ {
		for jdx := 0; jdx < 3; jdx++ {
			ai := ((i)/3)*3 + idx
			aj := ((j)/3)*3 + jdx
			exi[board[ai][aj]] = true
		}
	}

	ret := []byte{}
	for k, v := range exi {
		if !v {
			ret = append(ret, k)
		}
	}
	return ret
}
