

class CenterForTeachingAndLearning:
    def __init__(self):
        pass

    def collectInfo(self):
        pass

    def displayInfo(self):
        pass

    def RequestFromStudents(self):
        pass

    # imagine some type of data collection from students
    def RunASurvey(self):
        # selects  number of students to give out information
        # selects those students in a pseudorandom fashion
        pass


class Singleton2(CenterForTeachingAndLearning):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


