using Microsoft.AspNetCore.Mvc;
using Proyecto_template.Models;
using Proyecto_template.Source.Config.Database;
using Proyecto_template.Source.Domain.Filters.Dtos;
using Proyecto_template.Source.Domain.Sales.Dtos;
using Proyecto_template.Source.Domain.Sales.Entities.Interface;

namespace Proyecto_template.Source.Domain.Sales.Application
{
    public class SalesRepository : ISalesRepository<JsonResult>
    {
        private readonly DatabaseCore databaseConfig = new DatabaseCore();
        private readonly DatabaseDQ _databaseDQ = new DatabaseDQ();

        public async Task<JsonResult> ExecuteDynamicQueryinDB(FilterRequest queryRequest)
        {
            try
            {
                return await _databaseDQ.ExecuteNewQuery(queryRequest);
            }
            catch (Exception ex)
            {
                return null;
            } 
        }
        public async Task<JsonResult> getClientFilter()
        {
            return await databaseConfig.GetFromDBWithParams<Cliente>(["CodigoCliente","NombreCliente"]); ;
        }
    }
}
