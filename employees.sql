CREATE TABLE sql_practice.employees (
    emp_no      INT64        ,
    birth_date  DATE       ,
    first_name  STRING,
    last_name   STRING,
    gender      STRING,    
    hire_date   DATE       ,
);

CREATE TABLE sql_practice.departments (
    dept_no     STRING    ,
    dept_name   STRING,
);

CREATE TABLE sql_practice.dept_manager (
   emp_no       INT64        ,
   dept_no      STRING    ,
   from_date    DATE       ,
   to_date      DATE       ,
); 

CREATE TABLE sql_practice.dept_emp (
    emp_no      INT64        ,
    dept_no     STRING    ,
    from_date   DATE       ,
    to_date     DATE       ,
);

CREATE TABLE sql_practice.titles (
    emp_no      INT64        ,
    title       STRING,
    from_date   DATE       ,
    to_date     DATE,
) 
; 

CREATE TABLE sql_practice.salaries (
    emp_no      INT64        ,
    salary      INT64        ,
    from_date   DATE       ,
    to_date     DATE       ,
); 