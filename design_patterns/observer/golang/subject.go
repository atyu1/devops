// A.k.a. publisher
package main

type subject interface {
	register(Observer observer)
	deregister(Observer observer)
	notifyAll()
}