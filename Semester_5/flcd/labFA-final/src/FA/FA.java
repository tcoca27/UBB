package FA;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicReference;

public class FA {

    private List<String> Q;

    private String initialState;

    private List<String> finalStates;

    private List<String> alphabet;

    private Map<List<String>, List<String>> transitions;

    private List<String> sequence;

    public FA(String path, String sequencePath) {
        Q = new ArrayList<>();
        initialState = "";
        finalStates = new ArrayList<>();
        alphabet = new ArrayList<>();
        transitions = new HashMap<>();
        readFile(path);
        sequence = readSequence(sequencePath);
    }

    private List<String> readSequence(String sequencePath) {
        List<String> sequence = new ArrayList<>();
        try {
            File file = new File(sequencePath);
            BufferedReader br = new BufferedReader(new FileReader(file));
            String[] tokens = br.readLine().split(" ");
            for (String token : tokens) {
                sequence.add(token.trim());
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return sequence;
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
                for (int j = 0; j < tokens.length; j++) {
                    if (j == 0) statePair.add(tokens[j].trim());
                    else if (j == tokens.length - 1) statePair.add(tokens[j].trim());
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
        String[] tokens = readLine.split(" ");
        for (String token : tokens) {
            alphabet.add(token.trim());
        }
    }

    private void readFinalStates(String readLine) {
        String[] tokens = readLine.split(" ");
        for (String token : tokens) {
            finalStates.add(token.trim());
        }
    }

    private void readInitial(String readLine) {
        initialState = readLine.trim();
    }

    private void readQ(String readLine) {
        String[] tokens = readLine.split(" ");
        for (String token : tokens) {
            Q.add(token.trim());
        }
    }

    public void printFA() {
        Scanner console = new Scanner(System.in);
        boolean print = true;
        while (print) {
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
                case 6:
                    if (!isDfa()) System.out.println("Not a DFA\n");
                    else System.out.println(computeSequence());
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
                        "5. Print Initial State \n" +
                        "6. Verify sequence \n"
        );
    }

    private boolean isDfa() {
        AtomicBoolean res = new AtomicBoolean(true);
        Map<String, Set<String>> dfa = new HashMap<>();
        transitions.forEach((k, v) -> {
            v.forEach(val -> {
                if (dfa.getOrDefault(k.get(0), new HashSet<String>()).contains(val)) {
                    res.set(false);
                } else {
                    Set<String> result = dfa.getOrDefault(k.get(0), new HashSet<String>());
                    result.add(val);
                    dfa.put(k.get(0), result);
                }
            });
        });
        return res.get();
    }

    private boolean computeSequence() {
        AtomicReference<String> currentState = new AtomicReference<>();
        currentState.setOpaque(initialState);
        sequence.forEach(tr -> {
            AtomicReference<String> current = new AtomicReference<>();
            transitions.forEach((k, v) -> {
                if (k.get(0).equals(currentState.get()) && v.contains(tr)) {
                    current.set(k.get(1));
                }
            });
            if(current.get() != null) currentState.set(current.get());
        });
        return finalStates.contains(currentState.get());
    }
}
