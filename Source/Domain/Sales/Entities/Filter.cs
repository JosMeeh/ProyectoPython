namespace Proyecto_template.Source.Domain.Filters.Entities
{
    public class Filter
    {
        public FilterPO Filter_data { get; set; }
       

        public Filter(FilterPO filter_data)
        {
            Filter_data = filter_data;
        }

       
    }
}
