package main

import (
	"syscall"
	"time"
)

const (
	MOUSEEVENTF_MOVE       = 0x0001 // mouse move
	MOUSEEVENTF_LEFTDOWN   = 0x0002 // left button down
	MOUSEEVENTF_LEFTUP     = 0x0004 // left button up
	MOUSEEVENTF_RIGHTDOWN  = 0x0008 // right button down
	MOUSEEVENTF_RIGHTUP    = 0x0010 // right button up
	MOUSEEVENTF_MIDDLEDOWN = 0x0020 // middle button down
	MOUSEEVENTF_MIDDLEUP   = 0x0040 // middle button up
	MOUSEEVENTF_WHEEL      = 0x0800 // wheel button rolled
	MOUSEEVENTF_ABSOLUTE   = 0x8000 // absolute move
	SM_CXSCREEN            = 0
	SM_CYSCREEN            = 1
)

// var (
// 	moduser32 = syscall.NewLazyDLL("user32.dll")
// 	procKeyBd = moduser32.NewProc("keybd_event")
// 	procMouse = moduser32.NewProc("mouse_event")
// )

// func main() {
// 	var dx, dy int = 5, -5

// 	for true {
// 		dx *= -1
// 		dy *= -1
// 		procMouse.Call(uintptr(MOUSEEVENTF_MOVE), uintptr(dx), uintptr(dy), 0, 0)
// 		time.Sleep(2 * time.Second) // 2s
// 	}
// }

func main() {
	var user32, _ = syscall.LoadLibrary("user32.dll")
	defer syscall.FreeLibrary(user32)
	var mouse_event, _ = syscall.GetProcAddress(user32, "mouse_event")

	var num_of_args uintptr = 4
	var dx, dy int = 5, -5
	for true {
		dx *= -1
		dy *= -1
		syscall.Syscall6(uintptr(mouse_event), num_of_args, uintptr(MOUSEEVENTF_MOVE), uintptr(dx), uintptr(dy), 0, 0, 0)
		time.Sleep(2 * time.Second)
	}
}
