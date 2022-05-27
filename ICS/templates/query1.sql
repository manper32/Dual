-- realizar lectura de ultima gestion de asesor en esquema popular
-- para posterior procesamiento con dual

select distinct
g.deudor_id
,g.gestion_fecha
,c.descripcion r1
,cd.negociacion n1
,cd.tamano t1
,c2.descripcion r2
,cd2.negociacion n2
,cd2.tamano t2
,c3.descripcion r3
,cd3.negociacion n3
,cd3.tamano t3
,c4.descripcion r4
,cd4.negociacion n4
,cd4.tamano t4
,g.telefono
,g.descripcion
,ig.indicador
,co.valor
,co.fecha_pago
,t2.telefono phone
,d.direccion address
,d.ciudad city
,cor.correo email
from cbpo_popular_wiser.gestiones g
left join cbpo_popular_wiser.tipificaciones t
on g.id_tipificacion = t.id
left join cbpo_popular_wiser.codigos c 
on t.codigo01 = c.codigo
and t.unidad = c.unidad
left join cbpo_popular_wiser.codigos_dual cd 
on t.codigo01 = cd.id
and t.unidad = cd.unidad
left join cbpo_popular_wiser.codigos c2
on t.codigo02 = c2.codigo
and t.unidad = c2.unidad
left join cbpo_popular_wiser.codigos_dual cd2
on t.codigo02 = cd2.id
and t.unidad = cd2.unidad
left join cbpo_popular_wiser.codigos c3
on t.codigo03 = c3.codigo
and t.unidad = c3.unidad
left join cbpo_popular_wiser.codigos_dual cd3
on t.codigo03 = cd3.id
and t.unidad = cd3.unidad
left join cbpo_popular_wiser.codigos c4
on t.codigo04 = c4.codigo 
and t.unidad = c4.unidad
left join cbpo_popular_wiser.codigos_dual cd4
on t.codigo04 = cd4.id
and t.unidad = cd4.unidad
left join public.indicadores_general ig
on t.indicador = ig.id
left join cbpo_popular_wiser.compromiso co
on g.gestion_id = co.gestion_id
left join cbpo_popular_wiser.telefonos t2 
on g.gestion_id = t2.gestion_id
left join cbpo_popular_wiser.direcciones d 
on g.gestion_id = d.gestion_id
left join cbpo_popular_wiser.correos cor 
on g.gestion_id = cor.gestion_id
--where g.deudor_id = '{0}'
where usuario_id = '{0}'
and usuario_id not in ('VDAD_AGENTE', 'VDAD', 'SMS_BACK', 'EMAIL_BACK')
and g.gestion_fecha::date = current_date
order by g.gestion_fecha desc;