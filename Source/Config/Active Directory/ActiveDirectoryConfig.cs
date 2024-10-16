using Proyecto_template.Source.Domain.Authentication.Entities;
using System.Diagnostics.Eventing.Reader;
using System.DirectoryServices.AccountManagement;
namespace Proyecto_template.Source.Config.Active_Directory
{
    public class ActiveDirectoryConfig
    {
        private readonly string _domain= "sa.kof.ccf";
        private readonly string _container = "DC=sa,DC=kof,DC=ccf";
        public async Task<bool> AuthenticateUser(string username, string password)
        {
            try
            {
                using (var context = new PrincipalContext(ContextType.Domain, _domain, _container))
                {
                    return context.ValidateCredentials(username, password);
                }
            }
            catch (Exception ex)
            {
                // Manejar o registrar la excepción
                Console.WriteLine($"Error de autenticación: {ex.Message}");
                return false;
            }
        }
        public async Task<User> GetUser(string username)
        {
            try
            {
                using (var context = new PrincipalContext(ContextType.Domain, _domain, _container))
                {
                    var UserPrincipale = UserPrincipal.FindByIdentity(context, IdentityType.SamAccountName, username);
                    string groups = "";
                    if (UserPrincipale != null)
                    {
                        var userGroups = UserPrincipale.GetGroups();
                        if (userGroups.Any())
                        {
                            groups = string.Join(",", userGroups.Select(g => g.Name));
                        }
                        return new User(UserPrincipale.SamAccountName, UserPrincipale.EmailAddress, groups, UserPrincipale.Name);
                    }
                    else return null;
                  }
            }
            catch (Exception ex)
            {              
                Console.WriteLine($"Error al obtener usuario: {ex.Message}");
                return null;
            }
        }


    }
}
