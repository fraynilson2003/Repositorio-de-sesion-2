import java.util.Scanner;
class EstCondicional{
  static Scanner teclado=new Scanner(System.in); static void ejercicio01(){
  }
  static void ejercicio02(){
    //Definir variables y otros
    System.out.println("Ejemplo estructura Condicional 02 en Java"); int cantidadX=0;
    double montoP=0;
    //Datos de Entrada
    System.out.println("Ingrese la cantidad de personas:")cantidadX=teclado.nextInt();
    //Proceso
    if(cantidadX<=200){
      montoP=cantidadX*95;
    }else if(cantidadX>200 && cantidadX<=300){
      montoP=cantidadX*85;
    }else{
      montoP=cantidadX*75;
    }
    //Datos de salida
    System.out.println("El monto a pagar es:"+montoP);
  }
  public static void main(String[] arg){
    //ejercicio01();
    ejercicio02();
  }
  }
