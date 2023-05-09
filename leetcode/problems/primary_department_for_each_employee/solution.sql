/* Write your PL/SQL query statement below */

select employee_id, department_id from (select employee_id, department_id, primary_flag, row_number() over (partition by employee_id order by primary_flag desc) rk from employee)
where rk = 1