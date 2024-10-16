using Microsoft.AspNetCore.Mvc;
using Proyecto_template.Source.Domain.Authentication.Application;
using Proyecto_template.Source.Domain.Authentication.Dtos;
using Proyecto_template.Source.Config.ApiResponse;
using Proyecto_template.Source.Domain.Authentication.Entities;
using Proyecto_template.Source.Domain.Filters.Dtos;
using Proyecto_template.Models;
using Proyecto_template.Source.Domain.Filters.Entities;
using Microsoft.EntityFrameworkCore;
using Proyecto_template.Source.Domain.Sales.Application;
using System.Text;
using System.ComponentModel;
using System.Runtime.ConstrainedExecution;

namespace Proyecto_template.Source.Domain.Authentication.Controller
{
    [ApiController]
    [Route("[Controller]")]
    public class AuthController: ControllerBase
    {
        AuthService authService = new AuthService();
        [HttpPost("/Authentication")]
        public async Task<IActionResult> autheticateAccess([FromBody] UserRequest Auth_user)
        {                      
            var auth = await authService.authenticateUser(Auth_user.UserName, Auth_user.Password);
            ApiResponse<User> response;
            switch (auth.Response_code)
            {
                case 200:
                    response = new ApiResponse<User>(200, "Ok", data: auth.User); break; // OK
                case 401:
                    response = new ApiResponse<User>(401, "UnAuthorized", data: auth.User); break;// Unauthorized
                case 403:
                    response = new ApiResponse<User>(403, "Forbidden", data: auth.User); break; // Forbidden    
                case 404:
                    response = new ApiResponse<User>(404, "Not Found", data: null); break; // Not Found                   
                default:
                    response = new ApiResponse<User>(400, "Bad Request", data: null); break; // Bad Request
            }
            return new ApiResponseResult<User>(response);
        }
         
    }



}

