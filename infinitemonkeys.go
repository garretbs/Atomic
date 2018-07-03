package main

import "fmt"
import "time"
import "math/rand"

const keyboard = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxys0123456789,.;!? "

func main(){
	rand.Seed(time.Now().UTC().UnixNano())
	c := make(chan bool)
	numThreads := 4
	for i := 0;i<numThreads;i++{
		go monkey(c)
	}
	
	for i := 0;i<numThreads;i++{
		<- c
	}
	//time.Sleep(3000)
}

func monkey(c chan bool){
	for i := 0;i<10;i++{
		fmt.Println(randomString(50))
	}
	c <- true
} 

func randomString(length int) string{
	result := make([]byte, length)
	
	for i := 0;i<length;i++{
		result[i] = keyboard[rand.Int() % len(keyboard)]
	}
	return string(result);
}