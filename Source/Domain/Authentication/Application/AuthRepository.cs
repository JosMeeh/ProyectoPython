using Proyecto_template.Models;
using Proyecto_template.Source.Config.Active_Directory;
using Proyecto_template.Source.Config.Database;
using Proyecto_template.Source.Domain.Authentication.Entities;

namespace Proyecto_template.Source.Domain.Authentication.Application
{
    public class AuthRepository: IAuthRepository<GrupoAutorizado> 
    {
        private readonly DatabaseCore databaseConfig = new DatabaseCore();
        private readonly ActiveDirectoryConfig _adService = new ActiveDirectoryConfig();

        public async Task<IEnumerable<GrupoAutorizado>> authorizeGroup()
        {
            return await databaseConfig.getFromDB<GrupoAutorizado>(); ;
        }
        public async Task<User> getUserInADAsync(string username)
        {
            return await _adService.GetUser(username);
        }
        public async Task<bool> verifyAccess(string username, string password)
        {
            return await _adService.AuthenticateUser(username, password);
        }

    }
}
