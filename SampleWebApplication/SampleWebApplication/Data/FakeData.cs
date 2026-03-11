using SampleWebApplication.Models;

namespace SampleWebApplication.Data
{
    public class FakeData
    {
        public static List<Person> people = new List<Person>()
        {
        new Person
            
        {
            Id = 1,Name="samet",LastName="bozkuş",Place="Göre"
        },
        new Person
        {
            Id=2,Name="hasan",LastName="yıldırım",Place="izmir"
        },
        new Person
        {
            Id=3,Name="yusuf",LastName="kılıç",Place="antep"

        },
        new Person
        {
            Id=3,Name="nejat",LastName="işler",Place="aydın"
        },
        new Person
        {
            Id=4,Name="eşref",LastName="tek",Place="istanbul"

        },
        new Person
        {
            Id=5,Name="nisan",LastName="güzel",Place="kayseri"
        }

        };
     }
}