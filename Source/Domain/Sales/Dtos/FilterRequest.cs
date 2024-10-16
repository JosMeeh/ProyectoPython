using Proyecto_template.Source.Domain.Authentication.Entities;
using Proyecto_template.Source.Domain.Filters.Entities;
using Proyecto_template.Source.Domain.Sales.Entities;
using System.Text.Json.Serialization;

namespace Proyecto_template.Source.Domain.Filters.Dtos
{
    public class FilterRequest
    {
        [JsonPropertyName("Filters")]
        public List<FilterPO> Filters { get; set; }
        public FilterRequest(List<FilterPO> filters)
        {
            Filters = filters;
        }

    }
}
