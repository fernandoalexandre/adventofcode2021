package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func btou(b bool) int32 {
	if b {
		return 1
	}
	return 0
}

func part1(model_num []int32) bool {
	var x int32 = 0
	var z int32 = 0
	var w int32 = 0

	// w = model_num[0]
	// z = 224
	// w = model_num[1]
	// z = 6051
	w = model_num[2]
	z = 157326 + w + 2
	w = model_num[3]
	z = z * 26
	z = z + w + 7
	w = model_num[4]
	x = z % 26
	z = z / 26
	x = x - 10
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 13) * x)
	w = model_num[5]
	z = z * 26
	z = z + w + 6
	w = model_num[6]
	x = z % 26
	z = z / 26
	x = x - 14
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 10) * x)
	w = model_num[7]
	z = z * 26
	z = z + w + 11
	w = model_num[8]
	x = (z % 26) - 4
	z = z / 26
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 6) * x)
	w = model_num[9]
	x = (z % 26) - 3
	z = z / 26
	x = x + -3
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 5) * x)
	w = model_num[10]
	z = z * 26
	z = z + w + 11
	w = model_num[11]
	x = (z % 26) - 3
	z = z / 26
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 4) * x)
	w = model_num[12]
	x = (z % 26) - 9
	z = z / 26
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 4) * x)
	w = model_num[13]
	x = (z % 26) - 12
	z = z / 26
	x = btou(x != w)
	z = z * ((25 * x) + 1)
	z = z + ((w + 6) * x)

	return z == 0
}

func part1_routine(digit int32) {
	for a := int32(1); a < 10; a++ {
		for b := int32(1); b < 10; b++ {
			for c := int32(1); c < 10; c++ {
				for d := int32(1); d < 10; d++ {
					for e := int32(1); e < 10; e++ {
						for f := int32(1); f < 10; f++ {
							for g := int32(1); g < 10; g++ {
								for h := int32(1); h < 10; h++ {
									for i := int32(1); i < 10; i++ {
										for j := int32(1); j < 10; j++ {
											for k := int32(1); k < 10; k++ {
												model := []int32{9, 9, digit, a, b, c, d, e, f, g, h, i, j, k}
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
	for a := int32(1); a < 10; a++ {
		wg.Add(1)
		go part1_routine(a)
	}
	wg.Wait()
}

func main() {
	fmt.Println("Part 1")
	part1_routine_launch()
}
