# Nose tests
from hello.hello import HelloView


class TestTests(object):
    """Class for testing testing system.

    """

    def test_testing(self):
        assert True

    def test_csv_loading(self):
        testnames = ['Camilla',
                     'Ezekiel',
                     'Grace',
                     'Griffith',
                     'Neve']
        helloview = HelloView()
        data = helloview.data
        count = 5
        collection = []
        while count:
            v = next(data)
            collection.append(v)
            count -= 1

        names = [c[0] for c in collection]
        names.sort()
        # print(repr(names))

        assert names == testnames

    def test_emp_by_nuber(self):
        personname = "Griffith"

        view = HelloView(number=5)

        assert view.emp.name == personname
