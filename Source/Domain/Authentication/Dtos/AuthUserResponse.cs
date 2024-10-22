using Proyecto_template.Source.Domain.Authentication.Entities;

namespace Proyecto_template.Source.Domain.Authentication.Dtos
{
    public class AuthUserResponse
    {

        public int Response_code { get; set; }
        public User User { get; set; }
        public AuthUserResponse(int response_code, User user)
        {
            Response_code = response_code;
            User = user;
        
        }
    }
}
