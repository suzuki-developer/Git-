// 所属パッケージ名
package Chapter_06.calapp.main;

// インポート（FQCNの省略）
import Chapter_06.calapp.logics.CalcLogic;

public class Calc {
    public static void main(String[] args) {
        int a = 10;
        int b = 2;
        
        // -----------------------------------
        // CalcLogicクラス内のメソッドを呼び出す
        // -----------------------------------        
        // FQCN = <1行目に書いてある所属パッケージ名>.<メソッド名>
        int total = Chapter_06.calapp.logics.CalcLogic.tasu(a, b);

        // インポート（FQCNの省略）した場合
        int delta = CalcLogic.hiku(a, b);
        System.out.println("足すと" + total + "引くと" + delta);
    }
}

