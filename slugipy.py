class Slugipy:
    def __init__(self, text, lower=None, separator='-'):
        self.text = text
        self.lower = lower
        self.separator = separator

    def slug(self):
        self.validate(self.text)
        if self.lower:
            self.text = self.to_lower(self.text)
        value = self.separate(self.text)
        return value

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('value must be a string')
        return True

    def separate(self, value):
        value = str(value).split(' ')
        value = f'{self.separator}'.join(value)
        return value

    def to_lower(self, value):
        return value.lower()


s = Slugipy('Hello everybody', lower=True)
print(s.slug())
