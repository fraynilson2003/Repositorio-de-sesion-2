import java.util.Scanner;
class AreaTriangulo{
static Scanner teclado=new Scanner (System.in);
public static void main(String [] arg){
  //Definir Variables y otros
  System.out.println("Hola Mundo");
  int b, h, area;
  //Datos de entrada
  System.out.println("Ingrese la Base:");
  b=teclado.nextInt();
  System.out.println("Ingrese la Altura:");
  h=teclado.nextInt();
  //Proceso
  area=(b*h)/2;
  //Datos de salida
  System.out.println("Area de un Triangulo es:"+area);
  System.out.println("Salio profe");
}
}




