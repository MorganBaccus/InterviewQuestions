using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    /// <summary>
    /// Asks the user to guess a number between a certain range and then guesses that number in the fewest possible guesses
    /// </summary>
    public class NumberGuesser
    {
        #region Public Properties

        /// <summary>
        /// The largest number we ask the user to guess, between 0 and this number
        /// </summary>
        public int MaximumNumber { get; set; }

        /// <summary>
        /// The current number of guesses the computer has had
        /// </summary>
        public int CurrentNumberOfGuesses { get; private set; }

        /// <summary>
        /// The current known min number the user is thinking of
        /// </summary>
        public int CurrentGuessMinimum { get; private set; }

        /// <summary>
        /// The current known max number the user is thinking of
        /// </summary>
        public int CurrentGuessMaximum { get; private set; }

        #endregion

        #region Default Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
        public NumberGuesser() // same name as class
        {
            // Set default max number
            this.MaximumNumber = 100;
        }

        #endregion

        #region Public Methods

        /// <summary>
        /// Asks the user to think of a number between 0 and max num
        /// </summary>
        public void InformUser()
        {
            // Ask the user to think of a number between 0 and max num
            Console.WriteLine($"Think of a number between 0 and { this.MaximumNumber }.");
            Console.ReadLine();
        }

        /// <summary>
        /// Asks the user a series of questions to discover the number they are thinking of
        /// </summary>
        public void DiscoverNumber()
        {
            // Clear variables to their initial values before a discovery
            this.CurrentNumberOfGuesses = 0;
            this.CurrentGuessMinimum = 0;
            this.CurrentGuessMaximum = this.MaximumNumber / 2;

            // While the guess isn't the same as the known max number
            while (this.CurrentGuessMinimum != this.CurrentGuessMaximum)
            {
                // Increase guess amount by 1
                this.CurrentNumberOfGuesses++;

                // Ask the user if their number is between the guess range
                Console.WriteLine($"Is your number between { this.CurrentGuessMinimum } and { this.CurrentGuessMaximum }?");
                string response = Console.ReadLine();

                // If the user confirmed their number is between that range, set a new max num
                if (response?.ToLower().FirstOrDefault() == 'y')
                {
                    this.MaximumNumber = this.CurrentGuessMaximum;

                    // Change the next guess range to be half of the new max range
                    this.CurrentGuessMaximum = this.CurrentGuessMaximum - (this.CurrentGuessMaximum - this.CurrentGuessMinimum) / 2;
                }
                // The number is greater than the guessed max and les than or equal to max
                else
                {
                    // The new min is one above the old max
                    this.CurrentGuessMinimum = this.CurrentGuessMaximum + 1;

                    // Guess the bottom half of the new range
                    int remainingDifference = this.MaximumNumber - this.CurrentGuessMaximum;

                    // Set the guess max to half way between the guess min and max
                    // NOTE: math.Ceiling will round up the remaining difference to 2 if the diff is 3
                    this.CurrentGuessMaximum += (int)Math.Ceiling(remainingDifference / 2f);
                }

                // If we only have 2 numbers left, guess one of them
                if (this.CurrentGuessMinimum + 1 == this.MaximumNumber)
                {
                    // Increase guess amount by 1
                    this.CurrentNumberOfGuesses++;

                    // Ask the user if their number is the lower num
                    Console.WriteLine($"Is your number { this.CurrentGuessMinimum }?");
                    response = Console.ReadLine();

                    // If the user confirmed their number is the lower num...
                    if (response?.ToLower().FirstOrDefault() == 'y')
                    {
                        break;
                    }
                    else
                    {
                        // That means the number is the higher of the two
                        this.CurrentGuessMinimum = this.MaximumNumber;
                        break;
                    }
                }
            }
        }

        /// <summary>
        /// Announces the number the user was thinking and the number of guesses it took
        /// </summary>
        public void AnnounceResults()
        {
            // Tell the user their number
            Console.WriteLine($"** Your number is: { this.CurrentGuessMinimum } **");

            // Tell the user how many guesses it took
            Console.WriteLine($"Guessed in: { this.CurrentNumberOfGuesses } guesses");

            Console.ReadLine();
        }

        #endregion
    }
}