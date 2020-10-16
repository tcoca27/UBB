import SymbolTbl.SymbolTbl;

public class Main {

    public static void main(String[] args) {

        SymbolTbl symbolTbl = new SymbolTbl();

        symbolTbl.add("asd");
        symbolTbl.add("sda");
        symbolTbl.add("opt");

        System.out.println(symbolTbl.getId("asd"));
        System.out.println(symbolTbl.getId("sda"));
        System.out.println(symbolTbl.getId("opt"));
    }
}
