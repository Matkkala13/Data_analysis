-- ============================================================
-- C25 · Proyecto Integrador: Reporte de ventas por país
-- Curso: SQL con PostgreSQL — TiendaLatam
-- ============================================================

-- ============================================================
-- PASO 1: Explorar los datos disponibles
-- ============================================================
SELECT COUNT(*) AS total_pedidos    FROM pedidos;
SELECT COUNT(*) AS total_clientes   FROM clientes;
SELECT COUNT(*) AS total_productos  FROM productos;
SELECT COUNT(*) AS total_detalle    FROM detalle_pedidos;

-- ============================================================
-- PASO 2: Construir el reporte de ventas por país
-- ============================================================

SELECT
    pa.nombrepais                               AS pais,
    COUNT(DISTINCT p.pedidoid)             AS total_pedidos,
    COUNT(DISTINCT p.clienteid)            AS clientes_unicos,
    SUM(dp.cantidad * dp.preciounitario)       AS monto_total,
    AVG(dp.cantidad * dp.preciounitario)       AS ticket_promedio
FROM pedidos p
INNER JOIN sucursales s        ON p.sucursalid  = s.sucursalid
INNER JOIN paises pa           ON s.paisid      = pa.paisid
INNER JOIN detalle_pedidos dp  ON p.pedidoid    = dp.pedidoid
GROUP BY pa.paisid, pa.nombrepais
ORDER BY monto_total DESC;

-- ============================================================
-- PASO 3: Agregar formato a los números
-- ============================================================

SELECT
    pa.nombrepais                                           AS pais,
    COUNT(DISTINCT p.pedidoid)                         AS total_pedidos,
    COUNT(DISTINCT p.clienteid)                        AS clientes_unicos,
    TO_CHAR(SUM(dp.cantidad * dp.preciounitario),
            'FM$999,999,999.00')                        AS monto_total,
    TO_CHAR(AVG(dp.cantidad * dp.preciounitario),
            'FM$999,999.00')                            AS ticket_promedio
FROM pedidos p
JOIN sucursales s        ON p.sucursalid  = s.sucursalid
JOIN paises pa           ON s.paisid      = pa.paisid
JOIN detalle_pedidos dp  ON p.pedidoid    = dp.pedidoid
GROUP BY pa.paisid, pa.nombrepais
ORDER BY SUM(dp.cantidad * dp.preciounitario) DESC;

-- ============================================================
-- VARIANTE 1: Reporte por mes (top 12 meses)
-- ============================================================

SELECT
    TO_CHAR(p.fecha, 'YYYY-MM') AS periodo,
    COUNT(DISTINCT p.pedido_id)           AS pedidos,
    SUM(dp.cantidad * dp.precio_unit)     AS monto_total
FROM pedidos p
JOIN detalle_pedidos dp ON p.pedido_id = dp.pedido_id
GROUP BY TO_CHAR(p.fecha, 'YYYY-MM')
ORDER BY periodo DESC
LIMIT 12;

-- ============================================================
-- VARIANTE 2: Top 10 productos más vendidos
-- ============================================================

SELECT
    pr.nombre                           AS producto,
    ca.nombre                           AS categoria,
    SUM(dp.cantidad)                    AS unidades_vendidas,
    SUM(dp.cantidad * dp.precio_unit)   AS ingreso_total
FROM detalle_pedidos dp
JOIN productos pr  ON dp.producto_id = pr.producto_id
JOIN categorias ca ON pr.categoria_id = ca.categoria_id
GROUP BY pr.producto_id, pr.nombre, ca.nombre
ORDER BY ingreso_total DESC
LIMIT 10;

-- ============================================================
-- VARIANTE 3: Reporte por categoría con HAVING
-- ============================================================

SELECT
    ca.nombre                           AS categoria,
    COUNT(DISTINCT p.pedido_id)         AS pedidos,
    SUM(dp.cantidad)                    AS unidades,
    SUM(dp.cantidad * dp.precio_unit)   AS monto_total
FROM detalle_pedidos dp
JOIN productos pr  ON dp.producto_id = pr.producto_id
JOIN categorias ca ON pr.categoria_id = ca.categoria_id
JOIN pedidos p     ON dp.pedido_id    = p.pedido_id
GROUP BY ca.categoria_id, ca.nombre
HAVING SUM(dp.cantidad * dp.precio_unit) > 10000
ORDER BY monto_total DESC;

-- ============================================================
-- CONSULTA FINAL: Dashboard completo de TiendaLatam
-- ============================================================

SELECT
    'Países activos'    AS indicador, COUNT(DISTINCT pais_id)::TEXT    AS valor FROM sucursales
UNION ALL
SELECT 'Sucursales',    COUNT(*)::TEXT FROM sucursales
UNION ALL
SELECT 'Empleados',     COUNT(*)::TEXT FROM empleados
UNION ALL
SELECT 'Clientes activos', COUNT(*)::TEXT FROM clientes WHERE activo = TRUE
UNION ALL
SELECT 'Productos',     COUNT(*)::TEXT FROM productos
UNION ALL
SELECT 'Pedidos totales', COUNT(*)::TEXT FROM pedidos
UNION ALL
SELECT 'Líneas de detalle', COUNT(*)::TEXT FROM detalle_pedidos;
