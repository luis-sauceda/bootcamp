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
