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
,c5.descripcion r5
,cd5.negociacion n5
,cd5.tamano t5
,c6.descripcion r6
,cd6.negociacion n6
,cd6.tamano t6
,c7.descripcion r7
,cd7.negociacion n7
,cd7.tamano t7
,c8.descripcion r8
,cd8.negociacion n8
,cd8.tamano t8
,c9.descripcion r9
,cd9.negociacion n9
,cd9.tamano t9
,c10.descripcion r10
,cd10.negociacion n10
,cd10.tamano t10
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
left join cbpo_popular_wiser.codigos c5
on t.codigo05 = c5.codigo 
and t.unidad = c5.unidad
left join cbpo_popular_wiser.codigos_dual cd5
on t.codigo05 = cd5.id
and t.unidad = cd5.unidad
left join cbpo_popular_wiser.codigos c6
on t.codigo06 = c6.codigo 
and t.unidad = c6.unidad
left join cbpo_popular_wiser.codigos_dual cd6
on t.codigo06 = cd6.id
and t.unidad = cd6.unidad
left join cbpo_popular_wiser.codigos c7
on t.codigo07 = c7.codigo 
and t.unidad = c7.unidad
left join cbpo_popular_wiser.codigos_dual cd7
on t.codigo07 = cd7.id
and t.unidad = cd7.unidad
left join cbpo_popular_wiser.codigos c8
on t.codigo08 = c8.codigo 
and t.unidad = c8.unidad
left join cbpo_popular_wiser.codigos_dual cd8
on t.codigo08 = cd8.id
and t.unidad = cd8.unidad
left join cbpo_popular_wiser.codigos c9
on t.codigo09 = c9.codigo 
and t.unidad = c9.unidad
left join cbpo_popular_wiser.codigos_dual cd9
on t.codigo09 = cd9.id
and t.unidad = cd9.unidad
left join cbpo_popular_wiser.codigos c10
on t.codigo10 = c10.codigo 
and t.unidad = c10.unidad
left join cbpo_popular_wiser.codigos_dual cd10
on t.codigo10 = cd10.id
and t.unidad = cd6.unidad
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
--where g.deudor_id = '11000321206'
where usuario_id = '{0}'
and usuario_id not in ('VDAD_AGENTE', 'VDAD', 'SMS_BACK', 'EMAIL_BACK')
and g.gestion_fecha::date = current_date
order by g.gestion_fecha desc;