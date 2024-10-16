using Microsoft.AspNetCore.Mvc;
using Proyecto_template.Source.Domain.Filters.Dtos;
using Proyecto_template.Source.Domain.Filters.Entities;
using Proyecto_template.Source.Domain.Application;
using System.Data;
using Microsoft.OpenApi.Any;

namespace Proyecto_template.Source.Domain.Sales.Application.Interfaces
{
    public interface ISales<T,Y>: IServices<T,Y>
    {


        DataSet createDataset(List<object> dbdata);
        string exportDataInFile(DataTable datos);

    }
}
