// tarefa 3 - passagem de parametros

public class PassagemPorValor {

    public static void alterarNumero(int x) {
        System.out.println("  [método] antes:  " + x);
        x = x * 2;
        System.out.println("  [método] depois: " + x);
    }

    public static void main(String[] args) {
        int numero = 10;
        System.out.println("[main] antes da chamada:  " + numero);
        alterarNumero(numero);
        System.out.println("[main] depois da chamada: " + numero);
    }
}








