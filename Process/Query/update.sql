-- query para actualizar segun el usuario la ip de la maquina correspondiente
update public.dual_users
set ip = '{1}'
where id = {0};