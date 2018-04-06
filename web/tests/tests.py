# Nose tests
from hello.hello import HelloView
from hello.database import init, User, Recipe, SESSION


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


class TestDatabase:
    def setUp(self):
        init()

    def test_init(self):
        assert True

    def test_create_users(self):
        petrov = User("Petrov")
        petrov.setpasswd("12345")
        SESSION.add(petrov)
        SESSION.commit()
        assert True

    def test_create_user_and_recipes(self):
        petrov = User("Petrov")
        petrov.setpasswd("12345")
        pancakes = Recipe(petrov, "Pancakes")
        pancakes.totalTime = 45
        SESSION.add(petrov)
        SESSION.add(pancakes)
        SESSION.commit()

        u = SESSION.query(User).filter_by(name="Petrov").first()

        print(u)

        assert u == petrov
