using Proyecto_template.Models;
using Proyecto_template.Source.Domain.Authentication.Entities;
using System.Collections.Generic;
using System.Threading.Tasks;

public interface IAuthRepository<T> where T : class
{
    Task<IEnumerable<T>> authorizeGroup();
    Task<User> getUserInADAsync(string username);
    Task<bool> verifyAccess(string username, string password);
}