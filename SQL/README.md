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
Group by Gender
```
3) Write a query to fetch the second highest salaried employer
```
SELECT  Name, Salary from Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee) ORDER BY Salary DESC LIMIT 1;
```
4)Write a query to fetch the employ details who did not assigned with any students.
```
```

5)Write a query to fetch the student who passed in all three subjects.

```
```

6)Write a query to fetch the top employee details where all of his students passed in the subjects.

```
```
