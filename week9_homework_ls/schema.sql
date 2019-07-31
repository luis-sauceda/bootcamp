--- Creating tables
CREATE TABLE employees (
    emp_number int PRIMARY KEY NOT NULL,
    birth_date date   NOT NULL,
    first_name varchar   NOT NULL,
    last_name varchar   NOT NULL,
    gender varchar(1)   NOT NULL,
    hire_date date   NOT NULL
);

CREATE TABLE departments (
    dept_no varchar PRIMARY KEY NOT NULL,
    dept_name varchar   NOT NULL
);

CREATE TABLE dept_emp (
    emp_no int   NOT NULL,
    dept_no varchar   NOT NULL,
    from_date date	NOT NULL,
    to_date date   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_number),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);

CREATE TABLE dept_manager (
    dept_no varchar   NOT NULL,
    emp_no int   NOT NULL,
    from_date date  NOT NULL,
    to_date date   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_number),
	FOREIGN KEY (dept_no) REFERENCES departments(dept_no)
);
drop table salaries;
CREATE TABLE salaries (
    emp_no int PRIMARY KEY NOT NULL,
    salary money   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_number)
);

CREATE TABLE titles (
    emp_no int NOT NULL,
    title varchar   NOT NULL,
    from_date date   NOT NULL,
    to_date date   NOT NULL,
	FOREIGN KEY (emp_no) REFERENCES employees(emp_number)
);

--- Analysis
---1) employee details
select em.emp_number, em.first_name, em.last_name, em.gender, sal.salary
from employees as em
inner join salaries as sal on
em.emp_number=sal.emp_no;
	
--2) employes hired in 1986
select * 
from employees
where hire_date >= '1986-01-01' and hire_date <= '1986-12-31'

-- 3) Manager of each department
select man.dept_no, dep.dept_name, man.emp_no, emp.last_name, emp.first_name, man.from_date, man.to_date
from dept_manager as man
inner join departments as dep on man.dept_no = dep.dept_no
inner join employees as emp on man.emp_no = emp.emp_number;

-- 4) Department of each employee
select emp.emp_number, emp.last_name, emp.first_name, dep.dept_name
from employees as emp
inner join dept_emp as dm on emp.emp_number = dm.emp_no
inner join departments as dep on dm.dept_no = dep.dept_no;

-- 5) List employees named "Hercules" and last name starts with "B"
select * 
from employees
where
	first_name='Hercules' and last_name like 'B%'
	
-- 6) Employees in sales department
select emp.emp_number, emp.last_name, emp.first_name, dep.dept_name
from employees as emp
inner join dept_emp as dm on emp.emp_number = dm.emp_no
inner join departments as dep on dm.dept_no = dep.dept_no
where dep.dept_name = 'Sales';

-- 7) Employees in sales and development department
select emp.emp_number, emp.last_name, emp.first_name, dep.dept_name
from employees as emp
inner join dept_emp as dm on emp.emp_number = dm.emp_no
inner join departments as dep on dm.dept_no = dep.dept_no
where dep.dept_name = 'Sales' or dep.dept_name = 'Development';

-- 8 employee last names frecuency
select last_name, count(last_name) as LN_count
from employees
group by last_name
order by LN_count desc;

-- 9 Average salary per title
select tit.title, avg(sal.salary::numeric)
from titles as tit
inner join salaries as sal on tit.emp_no = sal.emp_no
group by tit.title;