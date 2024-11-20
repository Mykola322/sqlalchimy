from app.db.base import create_db, Session
from app.db.models import Pizza, Student, Group

create_db()


with Session() as session:
    name = "Маргарита"
    ingradients = "Сир, моцарела, кепуч, гриби"
    price = 25.5
    pizza = Pizza(name=name, ingradients=ingradients, price=price)
    session.add(pizza)

    group_1 = Group(name="1-а")
    session.add(group_1)

    group_2 = Group(name="1-В")
    session.add(group_2)

    group_3 = Group(name="10-а")
    session.add(group_3)

    student_1 = Student(name="Олександр", group_id=1)
    session.add(student_1)

    student_2 = Student(name="Мекола", group=group_3)
    session.add(student_2)

session.commit()