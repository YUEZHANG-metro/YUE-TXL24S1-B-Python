class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}"

class Member(Person):
    def __init__(self, name, age, gender,membership_id):
        super().__init__(self,name,age,gender)
        self.membership_id = membership_id

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, {self.gender}, with {self.membership_id}"

class Author(Person):
    def __init__(self, name, age, gender, books_written):
        Person.__init__(self,name,age,gender)
        self.books = []
        self.books.append(books_written)

    def get_books(self,books_written):
        self.books.append(books_written)
        return f"books written: {self.books}"

class AuthorMember(Member, Author):
    def __init__(self, name, age, gender, books_written, membership_id):
        Member.__init__(self,name,age,gender,membership_id)
        Author.__init__(self,name,age,gender,books_written)

    def introduce(self):
        return f"I am {self.name} {self.age} years old, {self.gender}, with {self.membership_id}, wrote {self.books}"

author_member_list =[]
am1 = AuthorMember("John", "25", "Male", "<how to feed a cat>", "M-01")
am1.get_books("<Leave it alone>")
author_member_list.append(am1)

am2 = AuthorMember("Lucy","40","Female","<Happy dog Happy life", "M-02")
author_member_list.append(am2)

for am in author_member_list:
    print(AuthorMember.introduce(am))