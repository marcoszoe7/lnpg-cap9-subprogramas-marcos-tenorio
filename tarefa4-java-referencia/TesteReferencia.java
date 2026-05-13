// Tarefa 4 — Objetos e referência em Java

public class TesteReferencia {

    static class Produto {
        String nome;
        double preco;

        Produto(String nome, double preco) {
            this.nome  = nome;
            this.preco = preco;
        }
    }

    public static void aplicarDesconto(Produto p) {
        System.out.println("  [método] antes:  R$ " + p.preco);
        p.preco = p.preco * 0.9;
        System.out.println("  [método] depois: R$ " + p.preco);
    }

    public static void main(String[] args) {
        Produto prod = new Produto("Notebook", 3000.0);
        System.out.println("[main] antes:  R$ " + prod.preco);
        aplicarDesconto(prod);
        System.out.println("[main] depois: R$ " + prod.preco);
    }
}


















