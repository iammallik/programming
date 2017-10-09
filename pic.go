package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
  var arr [][]byte

	for i:=0; i<dy; i++{
	var arr1 []byte
		for j:=0; j<dx; j++{
			if i<j {arr1 =append(arr1, byte (i+j) )
			}else{ arr1 =append(arr1, byte (j-i) )}
		}
		arr  = append(arr, arr1);
	}
	
	return arr
}

func main() {
	pic.Show(Pic)
}
