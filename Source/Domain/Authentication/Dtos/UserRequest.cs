namespace Proyecto_template.Source.Domain.Authentication.Dtos
{
    public class UserRequest
    {
    
        public string UserName { get; set; }
        public string Password { get; set; }
        public UserRequest(string userName, string password)
        {
            UserName = userName;
            Password = password;
        }
    
    }
}
