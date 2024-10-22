using Microsoft.EntityFrameworkCore;
using Proyecto_template.Models;
using Proyecto_template.Source.Config.Active_Directory;
using Proyecto_template.Source.Domain.Authentication.Application.Interfaces;
using Proyecto_template.Source.Domain.Authentication.Dtos;
using Proyecto_template.Source.Domain.Authentication.Entities;

namespace Proyecto_template.Source.Domain.Authentication.Application
{
    public class AuthService : IAuthService<AuthUserResponse>
    {
        AuthRepository repository = new AuthRepository();
        public async Task<AuthUserResponse> authenticateUser(string username, string password)
        {
            IEnumerable<GrupoAutorizado> authorizegroups = await repository.authorizeGroup();
            User user_in_ad =  await repository.getUserInADAsync(username);
            if (user_in_ad != null)
            {
                string[] userGroups = user_in_ad.Group.Split(',');
                bool isAuthenticated = await repository.verifyAccess(user_in_ad.UserName, password);
                if (isAuthenticated)
                {
                    foreach (var groups in authorizegroups)
                    {
                        if (userGroups.Contains(groups.Grupo)){
                            return new AuthUserResponse(200, user_in_ad); ///USER AUTHENTICATE WITH PERMISSIONS TO ACCESS
                        }
                        return new AuthUserResponse(403, user_in_ad); //USER AUTHENTICATE WITHOUT PERMISSIONS TO ACCESS
                    }              
                }
                else return new AuthUserResponse(401, user_in_ad); //UNAUTHORIZE USER, CREDENTIAL TYPE ERROR
            }
            else return new AuthUserResponse(404,null); //USER NOT FOUND
            return new AuthUserResponse(400, null); //UNPROCESSABLE REQUEST
        }

       

        //METODO DE PRUEBA FINAL, NO SERA INCLUIDO HASTA CULMINAR EL PRINCIPAL
        public Task<bool> logoutAsync()
        {
            throw new NotImplementedException();
        }        
        //METODO DE PRUEBA FINAL, NO SERA INCLUIDO HASTA CULMINAR EL PRINCIPAL
        public Task<bool> sendRegistrationRequest(string username, string password, string email)
        {
            //GU - KOF - USUARIOAD
            //GU - KOF - USUARIOAD
            //VEOFC - SISTEMAS
            //VEOFC - SISTEMAS@kof.com.mx 



            throw new NotImplementedException();
        }
    }
}
