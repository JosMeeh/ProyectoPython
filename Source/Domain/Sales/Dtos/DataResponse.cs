using Microsoft.AspNetCore.Mvc;
using Proyecto_template.Source.Domain.Authentication.Entities;
using Proyecto_template.Source.Domain.Filters.Entities;
using System.Data;

namespace Proyecto_template.Source.Domain.Sales.Dtos
{
    public class DataResponse
    {
        public int Response_code { get; set; }
        public object Data { get; set; } 

        public DataResponse(int response_code, object data)
        {
            Response_code = response_code;
            Data = data;

        }

    }
}
