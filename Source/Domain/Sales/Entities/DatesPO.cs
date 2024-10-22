namespace Proyecto_template.Source.Domain.Sales.Entities
{
    public class DatesPO
    {
        public string Start_date { get; set; }
        public string End_date {get; set; }


        public DatesPO(string start_date, string end_date)
        {
            Start_date = start_date;
            End_date = end_date;

        }


    }
}
