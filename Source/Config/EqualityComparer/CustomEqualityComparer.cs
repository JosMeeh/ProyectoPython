namespace Proyecto_template.Source.Config.EqualityComparer
{
    public class CustomEqualityComparer : IEqualityComparer<object>
    {
        public bool Equals(object x, object y)
        {
            return x.GetHashCode() == y.GetHashCode();
        }

        public int GetHashCode(object obj)
        {
            return obj.GetHashCode();
        }
    }
}
