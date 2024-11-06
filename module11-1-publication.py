ITALIC = "\033[3m"
RESET = "\033[0m"

class Publication:
    def __init__(self,name):
        self.name = name
        pass

class Book(Publication):
    def __init__(self, name,author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
        pass

    def print_information(self):
        print(f"{ITALIC}{self.name}{RESET},author {self.author},{self.page_count} pages")

class Magazine(Publication):
    def __init__(self, name,chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
        pass

    def print_information(self):
        print(f"{ITALIC}{self.name}{RESET},{self.chief_editor}")

publication1 = Magazine("Donald Duck","Aki Hyyppä")
publication2 = Book("Compartment No.6","Rosa Liksom",192)

publication1.print_information()
publication2.print_information()