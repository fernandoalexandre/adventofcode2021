package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func btou(b bool) int64 {
	if b {
		return 1
	}
	return 0
}

func part1(model_num []int64) bool {
	var x int64 = 0
	var z int64 = 0
	var w int64 = 0

	z = ((157326 + model_num[2] + 2) * 26) + model_num[3] + 7

	w = model_num[4]
	x = (z % 26) - 10
	z = z / 26
	if x != w {
		z = (z * 26) + w + 13
	}

	z = (z * 26) + model_num[5] + 6

	w = model_num[6]
	x = (z % 26) - 14
	z = z / 26
	if x != w {
		z = (z * 26) + w + 10
	}

	z = (z * 26) + model_num[7] + 11

	w = model_num[8]
	x = (z % 26) - 4
	z = z / 26 // 11,881,376
	if x != w {
		z = (z * 26) + w + 6
	}

	w = model_num[9]
	x = (z % 26) - 3
	z = z / 26 // has to be 456976
	if x != w {
		z = (z * 26) + w + 5
	}

	z = (z * 26) + model_num[10] + 11

	w = model_num[11]
	x = (z % 26) - 3
	z = z / 26 // has to be 17576
	if x != w {
		z = (z * 26) + w + 4
	}

	w = model_num[12]
	x = (z % 26) - 9
	z = z / 26 // has to be 676
	if x != w {
		z = (z * 26) + w + 4
	}

	w = model_num[13]
	x = (z % 26) - 12
	z = z / 26 // Has to be 26
	if x != w {
		z = (z * 26) + w + 6
	}

	return z == 0
}

func part1_routine(digit int64) {
	for a := int64(1); a < 10; a++ {
		for b := int64(1); b < 10; b++ {
			for c := int64(1); c < 10; c++ {
				for d := int64(1); d < 10; d++ {
					for e := int64(1); e < 10; e++ {
						for f := int64(1); f < 10; f++ {
							for g := int64(1); g < 10; g++ {
								for h := int64(1); h < 10; h++ {
									for i := int64(1); i < 10; i++ {
										for j := int64(1); j < 10; j++ {
											for k := int64(1); k < 10; k++ {
												model := []int64{9, 9, digit, a, b, c, d, e, f, g, h, i, j, k}
												if part1(model) {
													fmt.Printf("Found model = %v", model)
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}
	wg.Done()
}

func part1_routine_launch() {
	for a := int64(1); a < 10; a++ {
		wg.Add(1)
		go part1_routine(a)
	}
	wg.Wait()
}

func solve_3_to_5_digits() {
	var a int64
	for i := int64(1); i < int64(10); i++ {
		for j := int64(1); j < int64(10); j++ {
			a = (((((157328 + i) * 26) + j + 7) / 26) % 26) - 10
			if a >= 1 && a < 10 {
				fmt.Printf("(%v,%v) = %v | ", i, j, a)
			}
		}
	}
}

func main() {
	fmt.Println("Part 1")
	solve_3_to_5_digits()
	part1_routine_launch()
}
