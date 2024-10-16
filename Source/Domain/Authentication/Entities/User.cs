using Proyecto_template.Models;
using System.ComponentModel.DataAnnotations;

namespace Proyecto_template.Source.Domain.Authentication.Entities
{
    public class User
    {

        public string UserName { get; set; }
        public string FullName { get; set; }

        public string Email { get; set; }

        public string Group { get; set; }
        public User(string userName, string email, string group, string fullName)
        {
            UserName = userName;
            Email = email;
            Group = group;
            FullName = fullName;
        }

    }
}

