//Versão tarefa1 monolítica

import java.util.Scanner;

public class SistemaAcademico {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i =0; i <5; i++) {
            System.out.println ("Nome do aluno: ");
            String nome = sc.nextLine();

            double[] notas = new double[3];
            for (int j =0; j < 3; j++) {
                System.out.println("Nota" + (j+1) + ":");
                notas[j] = sc.nextDouble();
            }
            sc.nextLine();

            double media = (notas[0] + notas[1] + notas[2]) /3;

            String situacao;
            if (media >= 7.0)      situacao = "Aprovado!";
            else if (media >=5.0)  situacao = "Recuperação";
            else                    situacao = "Reprovado";


            System.out.println("Aluno: " + nome  +
                " | Média: " + String.format("%.1f", media) +
                " | Situação: " + situacao);
        }
        sc.close();
    }
    
}













