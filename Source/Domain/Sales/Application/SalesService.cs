using Microsoft.AspNetCore.Mvc;
using Proyecto_template.Source.Domain.Application;
using Proyecto_template.Source.Domain.Filters.Dtos;
using Proyecto_template.Source.Domain.Sales.Application.Interfaces;
using Proyecto_template.Source.Domain.Sales.Dtos;
using System.Data;
namespace Proyecto_template.Source.Domain.Sales.Application
{
    public class SalesService : ISales<DataResponse, FilterRequest>
    {
        SalesRepository SalesRepository = new SalesRepository();

   
         public async Task<DataResponse> execute(FilterRequest queryRequest)
        {
      
            try
            {
                var results = await SalesRepository.ExecuteDynamicQueryinDB(queryRequest);
                if (results == null) { return new DataResponse(response_code: 400, null); }
                return new DataResponse(response_code: 200, results.Value);
            }
            catch(Exception ex) {
                return new DataResponse(response_code: 500, null);
            }           
        }

        public async Task<DataResponse> getClients()
        {
            try
            {
                var results = await SalesRepository.getClientFilter();
                if (results == null) { return new DataResponse(response_code: 400, null); }
                Console.WriteLine(results.Value);
                return new DataResponse(response_code: 200, results.Value);
            }
            catch (Exception ex)
            {
                return new DataResponse(response_code: 500, null);
            }
        }
    
    public DataSet createDataset(List<object> dataset_data) 
        {
            DataSet dataSet = new DataSet();
            DataTable dt = new DataTable("Resultados");
            dataSet.Tables.Add(new DataTable());
            HashSet<string> columnNames = new HashSet<string>(); //Avoid columns duplicates
            foreach (var item in dataset_data) {
                var properties = item.GetType().GetProperties();
                foreach (var property in properties) { 
                    if (columnNames.Add(property.Name)){
                        dt.Columns.Add(property.Name,property.PropertyType);
                    }
                }
             DataRow dataRow = dt.NewRow();
             foreach (var property in properties) {
                    dataRow[property.Name] = property.GetValue(item,null)?? DBNull.Value;
                 }
             dt.Rows.Add(dataRow);
            }
           dataSet.Tables.Add(dt);
            return dataSet;
        }

        public string exportDataInFile(DataTable datos)
        {
            throw new NotImplementedException();
        }

        
    }
}
