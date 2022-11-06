## SQL

1) Write a query to fetch Employee name whose grade greater than 200

```
SELECT NAME FROM Employees
WHERE Grade > 200;
```

2) Wite a query to fetch the department name where only male staff available.

```
SELECT Department 
(SELECT Gender  FROM Employees WHERE Gender="M")
FROM Employees
```
3) Write a query to fetch the second highest salaried employer
```
SELECT  Name, Salary from Employee WHERE Salary < (SELECT MAX(Salary) FROM Employees) ORDER BY Salary DESC LIMIT 1;
```
4)Write a query to fetch the employ details who did not assigned with any students.
```
SELECT * from Employees.Name, Employees.Department, Employees.Gradem Employees.Salary,Employees.Gender, Student_id, Class_Teacher_Employee_Id 
FROM Employee, Student 
WHERE Student_id NOT IN Class_Teacher_Employee_Id
```

5)Write a query to fetch the student who passed in all three subjects.

```
SELECT Student_Id 
(SELECT Subject1 FROM Student WHERE Subject1="P")
(SELECT Subject2 FROM Student WHERE Subject2="P")
(SELECT Subject3 FROM Student WHERE Subject3="P")
FROM Student
```

6)Write a query to fetch the top employee details where all of his students passed in the subjects.

```
Select * from Employees
WHERE (SELECT Student_id( SELECT Subject1, Subject2, Subject3 FROM Student WHERE Subject1, Subject2, Subject3="P") FROM Student); 
```
