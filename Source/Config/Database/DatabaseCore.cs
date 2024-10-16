using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Proyecto_template.Models;
using Proyecto_template.Source.Domain.Filters.Dtos;
using Proyecto_template.Source.Domain.Filters.Entities;
using Proyecto_template.Source.Domain.Sales.Dtos;
using System.Dynamic;
using System.Linq.Expressions;
using System.Reflection.Emit;
using System.Reflection;

namespace Proyecto_template.Source.Config.Database
{
    public class DatabaseCore //Here you can find basic methods for database 
    {
        private DmVentasContext _context = new DmVentasContext();

        public async Task<IEnumerable<T>> getFromDB<T>() where T : class
        {
            var data = await _context.Set<T>().ToListAsync();
            return data;
        }

        public async Task<JsonResult> GetFromDBWithParams<T>(string[] query) where T : class, new()
        {
            // Obtener todos los datos de la tabla T
            var data = await _context.Set<T>().ToListAsync();
           // Proyectar los resultados en un formato dinámico
            var result = data.Select(item =>
            {
                var selectedProperties = new Dictionary<string, object>();

                foreach (var prop in query)
                {
                    var propertyInfo = typeof(T).GetProperty(prop);
                    if (propertyInfo != null)
                    {
                        selectedProperties[prop] = propertyInfo.GetValue(item);
                    }
                }
                return selectedProperties;
            });
            return new JsonResult(result.ToList());
        }
    }
}
