import java.util.Scanner;
import java.util.Random;

class BettingTableTest {
	int House = 1000 ;
	int Player = 200 ;
	public void intro() {
		System.out.println("Hello, and welcome to the Betting Table! This is a test for practicing good betting strategy. The odds are 50/50 and the winnings are always 100%. You are only betting against the house. The house has one thousand coins and you have two hundred. Good luck to you and have fun!") ;
	}
	public void gaMe() {	
		while (Player > 0) {
			Scanner user_input = new Scanner(System.in) ; 
			System.out.print("[Please place your bet: ]") ;
			int bet = user_input.nextInt() ;
			if (bet == 0) {
				System.out.println("Thanks for playing!") ;
				break ;
			}
			else if ((bet > 0) && (bet <= Player)) {
				Random chance = new Random();
				boolean winOrLose = chance.nextBoolean();
				House = House - bet ;
				Player = Player - bet ;
				int Pot = bet * 2 ;
				System.out.println("The house has bet " + bet + " coins and now has " + House + " coins.") ;
				System.out.println("The Player has bet " + bet + " coins and now has " + Player + " coins.") ;
				System.out.println("The Pot now has " + Pot + " coins.") ;
				if (winOrLose == true) {
					Player = Player + Pot ;
					System.out.println("YOU WIN! Your now have " + Player + " coins.") ;
				}
				else if (winOrLose == false) {
					House = House + Pot ;
					System.out.println("YOU LOST. You now have " + Player + " coins.") ;
				}
			}
			else {
				System.out.println("Please try a different number.") ;
			}
		}
	}
	public void ending() {
		System.out.println("The game has ended.") ;
	}
	public static void main(String[] args) {
		BettingTableTest test = new BettingTableTest() ;
		test.intro() ;
		test.gaMe() ;
		test.ending() ;
	}
}