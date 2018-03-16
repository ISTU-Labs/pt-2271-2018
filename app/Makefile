.PHONY: run python qt

run: euler
	./euler

qt: kettle_form.py euler.py _euler.so
	python interface.py

hello: euler.c
	gcc $< -o $@ -D TEST

_euler.so: euler.c euler_wrap.c
	gcc euler.c euler_wrap.c -o _euler.so -fPIC --shared -I/usr/include/python3.6m -lpython3.6m


euler_wrap.c euler.py: euler.i
	swig -python -py3 $<

kettle_form.py: ui/KettleForm.ui
	pyuic5 -x -o $@ $<
