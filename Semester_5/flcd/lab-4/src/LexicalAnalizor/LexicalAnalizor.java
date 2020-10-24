package LexicalAnalizor;

import SymbolTbl.SymbolTbl;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.regex.Pattern;

public class LexicalAnalizor {

    public static final List<String> separators = Collections.unmodifiableList(Arrays.asList("(", ")", "[", "]", "{", "}", ";", ",", " ", "\n", "\t"));
    public static final List<String> operators = Collections.unmodifiableList(Arrays.asList("+", "-", "*", "/", "=", "<", "<=", "==", "!=", ">=", ">", "++", "!", "%"));
    public static final List<String> reservedWords = Collections.unmodifiableList(Arrays.asList("intreg", "adevar", "caracter", "cuvant", "citeste", "printeaza", "std::in", "Adevarat", "Fals", "daca", "daca nu", "eventual", "raporteaza", "in timp ce", "nu"));

    private SymbolTbl symbolTblId;
    private SymbolTbl symbolTblCt;
    private Map<String, List<Integer>> PIF;
    private Map<String, Integer> errors;
    private int errorPos;
    private String codeFile;

    public LexicalAnalizor(String codeFile) {
        this.symbolTblId = new SymbolTbl();
        this.symbolTblCt = new SymbolTbl();
        PIF = new HashMap<>();
        this.errorPos = -1;
        this.codeFile = codeFile;
        errors = new HashMap<>();
    }


    public String parseCode() {
        String code = "";
        try {
            File file = new File(codeFile);
            BufferedReader br = new BufferedReader(new FileReader(file));
            String str;
            while ((str = br.readLine()) != null) {
                code += str;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return code;
    }

    public List<String> detectTokens() {
        String code = parseCode();
        String tokenChar = "";
        String tokenOp = "";
        String lastToken = "";
        List<String> tokens = new ArrayList<String>();
        int i = 0;
        while (i < code.length()) {
            String ch = Character.toString(code.charAt(i));
            while (!isSeparator(ch) && !isOperator(ch)) {
                tokenChar += ch;
                i++;
                if (i < code.length()) {
                    ch = Character.toString(code.charAt(i));
                } else break;
            }
            if (tokenChar.length() > 0) {
                tokenChar = tokenChar.trim();
                tokens.add(tokenChar);
                lastToken = tokenChar;
                tokenChar = "";
            }
            while (isSeparator(ch)) {
                tokens.add(ch);
                i++;
                if (i < code.length()) {
                    ch = Character.toString(code.charAt(i));
                } else break;
            }
            while (isOperator(ch)) {
                tokenOp += ch;
                i++;
                if (i < code.length()) {
                    ch = Character.toString(code.charAt(i));
                } else break;
            }
            if (tokenOp.length() > 0) {
                if(tokenOp.equals("-") && lastToken.equals("=")) {
                    while (isDigit(ch)) {
                        tokenOp += ch;
                        i++;
                        if (i < code.length()) {
                            ch = Character.toString(code.charAt(i));
                        } else break;
                    }
                }
                tokenOp = tokenOp.trim();
                tokens.add(tokenOp);
                lastToken = tokenOp;
                tokenOp = "";
            }
        }
        tokens = removeSpaces(tokens);
        return tokens;
    }

    private boolean isDigit(String ch) {
        Pattern pattern = Pattern.compile("[0-9]");
        return (pattern.matcher(ch).matches());
    }

    private List<String> removeSpaces(List<String> tokens) {
        List<String> output = new ArrayList<String>();
        Pattern pattern = Pattern.compile("\\s+");
        for (int i = 0; i < tokens.size(); i++) {
            if (!pattern.matcher(tokens.get(i)).matches() && !tokens.get(i).equals("")) {
                output.add(tokens.get(i));
            }
        }
        return output;
    }

    public boolean isSeparator(String ch) {
        return separators.contains(ch);
    }

    public boolean isOperator(String ch) {
        return operators.contains(ch);
    }

    public boolean isReservedWord(String ch) {
        return reservedWords.contains(ch);
    }

    public boolean isReservedWordCombined(List<String> list) {
        String content = combine(list);
        return reservedWords.contains(content);
    }

    public String combine(List<String> list) {
        String content = "";
        for (String str : list) {
            if (list.indexOf(str) != list.size() - 1) content += str + " ";
            else content += str;
        }
        return content;
    }


    public boolean isIdentifier(String token) {
        Pattern pattern = Pattern.compile("[A-Za-z_][A-Za-z0-9_]*");
        return (pattern.matcher(token).matches());
    }

    public boolean isConstant(String ch) {
        return (isCharacter(ch) || isInteger(ch) || ch.equals("Adevarat") || ch.equals("Fals"));
    }

    public boolean isInteger(String ch) {
        Pattern pattern = Pattern.compile("[-]?\\d+");
        return (pattern.matcher(ch).matches());
    }

    public boolean isCharacter(String ch) {
        Pattern pattern = Pattern.compile("^'[a-zA-Z0-9]'$");
        return (pattern.matcher(ch).matches());
    }

    public void addToST() {
        List<String> tokens = detectTokens();
        for (int i = 0; i < tokens.size(); i++) {
            if (isReservedWord(tokens.get(i)) || isOperator(tokens.get(i)) || isSeparator(tokens.get(i))) continue;
            if (i < tokens.size() - 2) {
                List<String> reserved = new ArrayList<>();
                reserved.add(tokens.get(i));
                reserved.add(tokens.get(i + 1));
                if (isReservedWordCombined(reserved)) {
                    i += reserved.size()-1;
                }
                reserved.add(tokens.get(i + 2));
                if (isReservedWordCombined(reserved)) {
                    i += reserved.size()-1;
                }
            }
            if (isIdentifier(tokens.get(i))) {
                if (symbolTblId.getId(tokens.get(i)) == null) {
                    symbolTblId.add(tokens.get(i));
                }
            } else if (isConstant(tokens.get(i))) {
                if (symbolTblCt.getId(tokens.get(i)) == null) {
                    symbolTblCt.add(tokens.get(i));
                }
            }
        }
    }

    public void showSTs() {
        addToST();
        System.out.println("CT: " + symbolTblCt);
        System.out.println("ID: " + symbolTblId);
    }

    public void addToPIF() {
        int nrLines = 1;
        this.errors = new HashMap<>();
        List<String> tokens = detectTokens();
        List<Integer> emptyPos = new ArrayList<>();
        List<Integer> pos = new ArrayList<>();
        emptyPos.add(-1);
        emptyPos.add(-1);
        for (int i = 0; i < tokens.size(); i++) {
            if (isReservedWord(tokens.get(i)) || isOperator(tokens.get(i)) || isSeparator(tokens.get(i))) {
                if(lineEnder(tokens.get(i)))nrLines++;
                PIF.put(tokens.get(i), emptyPos);
            }
            else {
                if (i < tokens.size() - 2) {
                    List<String> reserved = new ArrayList<>();
                    reserved.add(tokens.get(i));
                    reserved.add(tokens.get(i + 1));
                    if (isReservedWordCombined(reserved)) {
                        PIF.put(combine(reserved), emptyPos);
                        i=i+reserved.size()-1;
                    }
                    reserved.add(tokens.get(i + 2));
                    if (isReservedWordCombined(reserved)) {
                        PIF.put(combine(reserved), emptyPos);
                        i=i+reserved.size()-1;
                        continue;
                    }
                }
                if (isIdentifier(tokens.get(i))) {
                    pos = symbolTblId.getId(tokens.get(i));
                    PIF.put(tokens.get(i), pos);
                } else if (isConstant(tokens.get(i))) {
                    pos = symbolTblCt.getId(tokens.get(i));
                    PIF.put(tokens.get(i), pos);
                }
                else {
                    if(!errors.containsKey(tokens.get(i))) errors.put(tokens.get(i),nrLines);
                }
            }
        }
        System.out.println(PIF.toString());
        System.out.println(errors);
    }

    private boolean lineEnder(String token) {
        return (token.equals(";") || token.equals("{") || token.equals("}"));
    }
}
