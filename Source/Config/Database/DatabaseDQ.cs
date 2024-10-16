using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Proyecto_template.Models;
using Proyecto_template.Source.Domain.Filters.Dtos;
using System.Text; // Para tareas asíncronas

namespace Proyecto_template.Source.Config.Database
{
    public class DatabaseDQ //Dynamic Query
    {
        DmVentasContext _context = new DmVentasContext();
        //TENEMOS LA MISION DE OPTIMIZAR ESTE CODIGO      
        public async Task<JsonResult> ExecuteNewQuery([FromBody] FilterRequest filterRequest)
        {
            var sqlBuilder = new StringBuilder();

            // Almacenar las columnas seleccionadas
            var selectedColumns = new List<string>();
            var conditionsByTable = new Dictionary<string, List<string>>(); // Para almacenar condiciones por tabla
            var fechaConditions = new List<string>(); // Para almacenar condiciones específicas de Tabla_Fechas
            // Primero, recorremos los filtros para construir la parte SELECT
            foreach (var tableFilter in filterRequest.Filters)
            {
                switch (tableFilter.Table_name)
                {
                    case "Clientes":
                        // Agregar columnas seleccionadas de Clientes
                        foreach (var column in tableFilter.Colunm_select)
                        {
                            selectedColumns.Add($"c.{column.Trim()}"); // Prefijo 'c.' para Clientes
                        }
                        break;

                    case "Localidad":
                        // Agregar columnas seleccionadas de Localidad
                        foreach (var column in tableFilter.Colunm_select)
                        {
                            selectedColumns.Add($"l.{column.Trim()}"); // Prefijo 'l.' para Localidad
                        }
                        break;
                    case "Tabla_Fechas":
                        // Agregar columnas seleccionadas de Localidad
                        foreach (var column in tableFilter.Colunm_select)
                        {
                            selectedColumns.Add($"f.{column.Trim()}"); // Prefijo 'l.' para Localidad
                        }
                        break;

                        // Agrega más casos para otras tablas según sea necesario.
                }

                // Recolectar condiciones por tabla
                foreach (var filter in tableFilter.Filter_values)
                {
                    string condition = $"{tableFilter.Table_name}.{filter.Column_name.Trim()}";

                    switch (filter.Operator.ToLower())
                    {
                        case "equal":
                            condition += $" = '{filter.Value}'";
                            break;
                        case "greater_than":  // Operador mayor que
                            condition += $" >= '{filter.Value}'";
                            break;
                        case "less_than":  // Operador menor que
                            condition += $" <= '{filter.Value}'";
                            break;
                        default:
                            continue; // Ignorar operadores no soportados
                    }

                    if (tableFilter.Table_name == "Tabla_Fechas")
                    {
                        fechaConditions.Add(condition); // Agregar a las condiciones de Tabla_Fechas
                    }
                    else
                    {
                        if (!conditionsByTable.ContainsKey(tableFilter.Table_name))
                        {
                            conditionsByTable[tableFilter.Table_name] = new List<string>();
                        }
                        conditionsByTable[tableFilter.Table_name].Add(condition);
                    }
                }
            }

            // Comenzar la consulta SELECT
            sqlBuilder.Append("SELECT "); // Seleccionar todas las columnas de Fact_Ventas

            // Agregar las columnas seleccionadas
            if (selectedColumns.Count > 0)
            {
                sqlBuilder.Append(string.Join(", ", selectedColumns));
            }
            sqlBuilder.Append(",fv.*");
            // Comenzar desde la tabla principal
            sqlBuilder.Append(" FROM Fact_Ventas fv ");

            // Agregar los JOINs necesarios
            sqlBuilder.Append("JOIN Clientes c ON fv.cliente = c.Codigo_Cliente ");
            sqlBuilder.Append("JOIN Localidad l ON fv.locvta = l.loc ");
            sqlBuilder.Append("JOIN Tabla_Fechas f ON fv.IdFecha = f.IdFecha ");  // Ajusta la condición del JOIN según sea necesario
            // Construir la cláusula WHERE si hay filtros
            if (conditionsByTable.Count > 0 || fechaConditions.Count > 0)
            {
                sqlBuilder.Append("WHERE ");
                var allConditions = new List<string>();

                foreach (var table in conditionsByTable)
                {
                    var conditionsList = table.Value;
                    if (conditionsList.Count > 0)
                    {
                        allConditions.Add($"({string.Join(" OR ", conditionsList)})"); // Agrupar condiciones en paréntesis con OR
                    }
                }

                if (fechaConditions.Count > 0)
                {
                    allConditions.Add($"({string.Join(" AND ", fechaConditions)})"); // Combinar condiciones de Tabla_Fechas con AND
                }

                sqlBuilder.Append(string.Join(" AND ", allConditions)); // Combinar condiciones de diferentes tablas con AND
            }

            // Asegurarse de que se use el prefijo correcto en el WHERE
            var whereClause = sqlBuilder.ToString();

            whereClause = whereClause.Replace("Clientes.", "c.");
            whereClause = whereClause.Replace("Localidad.", "l.");
            whereClause = whereClause.Replace("Tabla_Fechas.", "f.");
            Console.WriteLine(whereClause); // Para depuración

            var results = await ExecuteRawSqlQuery(whereClause);

            return new JsonResult(results);
        }
        public async Task<List<Dictionary<string, object>>> ExecuteRawSqlQuery(string sqlQuery)
        {
            using var context = new DmVentasContext();

            var results = new List<Dictionary<string, object>>();

            // Obtener la conexión de la base de datos
            var connection = context.Database.GetDbConnection();

            // Abrir la conexión
            await connection.OpenAsync();

            using (var command = connection.CreateCommand())
            {
                command.CommandText = sqlQuery;

                using (var reader = await command.ExecuteReaderAsync())
                {
                    // Leer los resultados
                    while (await reader.ReadAsync())
                    {
                        var row = new Dictionary<string, object>();

                        for (int i = 0; i < reader.FieldCount; i++)
                        {
                            row[reader.GetName(i)] = reader.GetValue(i);
                        }

                        results.Add(row);
                    }
                }
            }

            return results;
        }
    }
}
