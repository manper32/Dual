-- query para comprobar existencia del registro
select id, ip
from public.dual_users
where id = {0};