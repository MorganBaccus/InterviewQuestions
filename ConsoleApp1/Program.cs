using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Create a new instance of our number guesser class
            var numberGuesser = new NumberGuesser();

            // Change the default max to 200
            //numberGuesser.MaximumNumber = 200;

            // Asks the user to think of a number
            numberGuesser.InformUser();

            // Discover the number the user is thinking of
            numberGuesser.DiscoverNumber();

            // Announce results
            numberGuesser.AnnounceResults();
        }
    }
}
