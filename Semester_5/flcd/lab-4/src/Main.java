import LexicalAnalizor.LexicalAnalizor;

import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {

        LexicalAnalizor lex = new LexicalAnalizor("p1.txt");
        lex.showSTs();
        lex.addToPIF();

        LexicalAnalizor lex2 = new LexicalAnalizor("p2.txt");
        lex2.showSTs();
        lex2.addToPIF();

        LexicalAnalizor lex3 = new LexicalAnalizor("p3.txt");
        lex3.showSTs();
        lex3.addToPIF();

        LexicalAnalizor lexerr = new LexicalAnalizor("perror.txt");
        lexerr.showSTs();
        lexerr.addToPIF();


    }
}
