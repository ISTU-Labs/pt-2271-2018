.PHONY: run compile


compile:
	gcc euler.c -o euler


run: compile
	./euler
