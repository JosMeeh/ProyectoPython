using Proyecto_template.Source.Domain.Authentication.Entities;
using Proyecto_template.Source.Domain.Sales.Entities;

namespace Proyecto_template.Source.Domain.Filters.Entities
{
    public class FilterPO
    {

        public List<string> Colunm_select { get; set; }
        public string Table_name /*Tabla_Estados*/{ get; set; }
        public List<WhereRequest> Filter_values { get; set; }

        public FilterPO(List<string> colunm_select, string table_name, List<WhereRequest> filter_values)
        {
            Colunm_select = colunm_select;  
            Table_name = table_name;
            Filter_values = filter_values;

        }

    }
}
