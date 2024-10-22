using Microsoft.AspNetCore.Mvc;

namespace Proyecto_template.Source.Domain.Application
{
    public interface IServices<T,Y>
    {
        Task<T> execute(Y Param);
    
    }
}
