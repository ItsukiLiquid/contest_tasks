CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  if N <= 0 then return;
  end if;
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    select (select distinct Employee.Salary from Employee order by Salary desc limit 1 offset N - 1)
  );
END;
$$ LANGUAGE plpgsql;