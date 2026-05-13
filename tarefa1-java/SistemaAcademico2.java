// Versão tarefa1 modularizada
import java.util.Scanner;


public class SistemaAcademico2 {
    static Scanner sc = new Scanner(System.in);

    public static String lerAluno(){
        System.out.println("Nome do aluno: ");
        return sc.nextLine();
    }

    public static double[] lerNotas() {
        double[] notas = new double[3];
        for (int j = 0; j <3; j++) {
          System.out.print("Nota " + (j+1) + ": ");
            notas[j] = sc.nextDouble();
        }
        sc.nextLine();
        return notas;
    }

    public static double calcularMedia(double[] notas) {
        return (notas[0] + notas[1] + notas[2]) / 3;

    }

    public static String determinarSituacao(double media){
        if (media >= 7.0)  return "Aprovado!";
        else if (media >= 5.0) return "Recueração";
        else                    return "Reprovado";

    }

    public static void imprimirRelatorio(String nome,double media, String situacao) {
        System.out.println("Aluno: " + nome +
        " | Média: " + String.format("%.1f", media) +
        " | Situação: " + situacao);
    }
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            String nome    = lerAluno();
            double[] notas = lerNotas();
            double media   = calcularMedia(notas);
            String sit     = determinarSituacao(media);
            imprimirRelatorio(nome, media, sit);
        }
    }



}
