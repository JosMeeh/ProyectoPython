using Microsoft.AspNetCore.Mvc;
using Proyecto_template.Source.Domain.Filters.Dtos;
using Proyecto_template.Source.Domain.Sales.Application;
using Proyecto_template.Source.Config.ApiResponse;
using Proyecto_template.Source.Config;
using Azure;
using Proyecto_template.Source.Domain.Authentication.Entities;



namespace Proyecto_template.Source.Domain.Sales.Controller
{
    [ApiController]
    [Route("[controller]")]
    public class SalesController : ControllerBase
    {
       SalesService _salesService = new SalesService();
        
        [HttpPost("/Data")]
        public async Task<IActionResult> getDynamicData([FromBody] FilterRequest queryRequest)
        {
            var result = await _salesService.execute(queryRequest);
            ApiResponse<object> response;
            switch (result.Response_code)
            {
                case 200:
                    response = new ApiResponse<object>(200, "Query executed", data: result.Data); break; // OK                             
                default:
                    response = new ApiResponse<object>(400, "Error during execution", data: null); break; // Bad Request
            }
            return new ApiResponseResult<object>(response);
        }

        [HttpGet("/Clients")]
        public async Task<IActionResult> getDataClients()
        {
            var result = await _salesService.getClients();
            ApiResponse<object> response;
            switch (result.Response_code)
            {
                case 200:
                    response = new ApiResponse<object>(200, "Query executed", data: result.Data); break; // OK                             
                default:
                    response = new ApiResponse<object>(400, "Error during execution", data: null); break; // Bad Request
            }
            return new ApiResponseResult<object>(response);
        }

    }  
}


