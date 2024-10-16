using Proyecto_template.Source.Domain.Filters.Dtos;

namespace Proyecto_template.Source.Domain.Sales.Entities.Interface
{
    public interface ISalesRepository<T> where T : class
    {
        Task<T> ExecuteDynamicQueryinDB(FilterRequest queryRequest);


    }
}
