package FA;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class FA {

    private List<String> Q;

    private String initialState;

    private List<String> finalStates;

    private List<String> alphabet;

    private Map<List<String>, List<String>> transitions;

    public FA(String path) {
        Q= new ArrayList<>();
        initialState = "";
        finalStates = new ArrayList<>();
        alphabet = new ArrayList<>();
        transitions = new HashMap<>();
        readFile(path);
    }

    private void readFile(String path) {
        try {
            File file = new File(path);
            BufferedReader br = new BufferedReader(new FileReader(file));
            String str;
            readQ(br.readLine());
            readInitial(br.readLine());
            readFinalStates(br.readLine());
            readAlphabet(br.readLine());
            while ((str = br.readLine()) != null) {
                String[] tokens = str.split(" ");
                List<String> statePair = new ArrayList<>();
                List<String> alph = new ArrayList<>();
                for(int j=0; j< tokens.length; j++) {
                    if (j==0) statePair.add(tokens[j].trim());
                    else if(j==tokens.length-1 )statePair.add(tokens[j].trim());
                    else {
                        alph.add(tokens[j].trim());
                    }
                }
                transitions.put(statePair, alph);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void readAlphabet(String readLine) {
        String[] tokens = readLine.split( " ");
        for(String token : tokens) {
            alphabet.add(token.trim());
        }
    }

    private void readFinalStates(String readLine) {
        String[] tokens = readLine.split( " ");
        for(String token : tokens) {
            finalStates.add(token.trim());
        }
    }

    private void readInitial(String readLine) {
        initialState = readLine.trim();
    }

    private void readQ(String readLine) {
        String[] tokens = readLine.split( " ");
        for(String token : tokens) {
            Q.add(token.trim());
        }
    }

    public void printFA() {
        Scanner console = new Scanner(System.in);
        boolean print = true;
        while(print) {
            printMenu();
            System.out.print("Enter option ");
            int option = console.nextInt();
            switch (option) {
                case 1:
                    System.out.println(Q.toString());
                    break;
                case 2:
                    System.out.println(alphabet.toString());
                    break;
                case 3:
                    System.out.println(transitions.toString());
                    break;
                case 4:
                    System.out.println(finalStates.toString());
                    break;
                case 5:
                    System.out.println(initialState.toString());
                    break;
                default:
                    print = false;
                    break;
            }
        }
    }

    private void printMenu() {
        System.out.println(
                "0. Exit \n" +
                "1. Print states \n" +
                        "2. Print Alphabet \n" +
                        "3. Print Transitions \n" +
                        "4. Print Final States \n" +
                        "5. Print Initial State \n"
        );
    }
}
