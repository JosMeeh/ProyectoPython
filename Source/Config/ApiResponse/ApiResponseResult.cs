using Microsoft.AspNetCore.Mvc;

namespace Proyecto_template.Source.Config.ApiResponse
{
    public class ApiResponseResult<T> : IActionResult
    {
        private readonly ApiResponse<T> _response;
        public ApiResponseResult(ApiResponse<T> response)
        {
            _response = response;
        }
        public async Task ExecuteResultAsync(ActionContext context)
        {
            var objectResult = new ObjectResult(_response)
            {
                StatusCode = _response.StatusCode
            };
            await objectResult.ExecuteResultAsync(context);
        }
    }
}
