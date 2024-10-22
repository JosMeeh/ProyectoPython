using Proyecto_template.Source.Domain.Authentication.Dtos;

namespace Proyecto_template.Source.Domain.Authentication.Application.Interfaces
{
    public interface IAuthService<T>
    {
        Task<bool> sendRegistrationRequest(string username, string password, string email);
        Task<T> authenticateUser(string username, string password);
        Task<bool> logoutAsync();
    }
}
