with open("C:\\Users\\User\\Desktop\\contest_tasks\\leetcode\\PostgreSQL\\175_combine_two_tables.sql", "w") as f:
    f.write("select person.firstName, Person.lastName, Address.city, Address.state \n")
    f.write("from Person \n")
    f.write("left join Address on Person.personId = Address.personId;")
print("SQL query written to 175_combine_two_tables.sql # 2026-07-16")