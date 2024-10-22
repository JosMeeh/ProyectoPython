using System.Text.Json.Serialization;

namespace Proyecto_template.Source.Domain.Sales.Entities
{
    public class WhereRequest
    {
        public string Column_name { get; set; }
       
        public object Value { get; set; }
        public string Operator { get; set; }

        public WhereRequest()
        {
            // Inicializa las propiedades si es necesario
        }

        public WhereRequest(string column_name, object value, string operatore)
        {
            Column_name = column_name;
            Value = value;
            Operator = operatore;
        }
    }
}
