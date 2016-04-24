import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Collections;
import java.util.Random;

public class Cards {
	public ArrayList<String> createDeck() {
		ArrayList<String> faces = new ArrayList<String>() ;
		faces.add("2");
		faces.add("3");
		faces.add("4");
		faces.add("5");
		faces.add("6");
		faces.add("7");
		faces.add("8");
		faces.add("9");
		faces.add("Ten");
		faces.add("Jack");
		faces.add("Queen");
		faces.add("King");
		faces.add("Ace");
		ArrayList<String> suits = new ArrayList<String>() ;
		suits.add("Hearts");
		suits.add("Diamonds");
		suits.add("Clovers");
		suits.add("Spades");
		ArrayList<String> cards = new ArrayList<String>() ;
		for (int i = 0; i < faces.size(); i++) {
			String face = faces.get(i) ;
			for (int x = 0; x < suits.size(); x++) {
				String suit = suits.get(x) ;
				String card = face + " of " + suit ;
				cards.add(card) ;
			}
		}
		int cardSize = cards.size() ;
		return (cards) ;
	}
	public void shuffle(ArrayList<String> deck) {
		long seed = System.nanoTime() ; 
		Collections.shuffle(deck, new Random(seed)) ;
		return (deck) ;
	}
	public void Blackjack() {
		
	}
	public static void main(String []args) {
		Cards test = new Cards() ;
		test.createDeck() ;
		ArrayList deck = new ArrayList() ; 
		test.shuffle(test.createDeck()) ;
	}
}