.PHONY: run python qt

run: hello
	./hello
	
qt: kettle_form.py
	python interface.py

hello: hello.c
	gcc $< -o $@ -D TEST

python: hello.c hello_wrap.c
	gcc hello.c hello_wrap.c -o _euler.so -fPIC --shared -I/usr/include/python3.6m -lpython3.6m


hello_wrap.c: hello.i
	swig -python -py3 $<

kettle_form.py: ui/KettleForm.ui
	pyuic5 -x -o $@ $<
	