.PHONY: run python

run: hello
	./hello

hello: hello.c
	gcc $< -o $@ -D TEST

python: hello.c hello_wrap.c
	gcc hello.c hello_wrap.c -o _euler.so -fPIC --shared -I/usr/include/python3.6m -lpython3.6m


hello_wrap.c: hello.i
	swig -python -py3 $<
